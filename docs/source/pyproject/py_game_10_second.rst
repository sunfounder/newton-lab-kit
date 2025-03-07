.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_10_second:

7.5 Erstellen eines „10-Sekunden“-Spiels
======================================================

In diesem spannenden Projekt werden wir ein unterhaltsames Spiel namens **"10 Sekunden"** mit dem Raspberry Pi Pico 2, einem Neigungsschalter und einer 4-stelligen 7-Segment-Anzeige bauen. Das Ziel des Spiels ist es, einen Zauberstab (simuliert durch den am Stab befestigten Neigungsschalter) zu schütteln, um einen Timer zu starten, und ihn dann erneut zu schütteln, um den Timer möglichst genau bei **10,00 Sekunden** zu stoppen. Es ist eine großartige Möglichkeit, deine Zeitgefühl-Fähigkeiten zu testen und Freunde herauszufordern, wer der wahre Zeitzauberer ist!

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_resistor`
        - 5(4-220Ω, 1-10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_tilt`
        - 1
        - 

**Verständnis der Komponenten**

* **Neigungsschalter**: Ein Sensor, der Orientierung oder Bewegung erkennt. Wenn geneigt, schließt oder unterbricht er einen Stromkreis, was es uns ermöglicht, Schütteln oder Bewegung zu erkennen.
* **4-stellige 7-Segment-Anzeige**: Zeigt Zahlen von 0000 bis 9999 an. Wir verwenden Schieberegister, um die Anzeige mit weniger GPIO-Pins zu steuern.
* **74HC595 Schieberegister**: 8-Bit-Serien-in, Parallel-out-Schieberegister, das es uns ermöglicht, mehrere Ausgänge mit nur wenigen GPIO-Pins zu steuern.


**Schaltplan**

|sch_10_second|


* Dieser Schaltkreis basiert auf :ref:`py_74hc_4dig` mit der Ergänzung eines Neigungsschalters.
* GP16 ist hoch, wenn der Neigungsschalter aufrecht steht; niedrig, wenn geneigt.

**Verdrahtungsplan**

|wiring_game_10_second| 

**Code schreiben**

Wir werden ein MicroPython-Skript schreiben, das:

* Das Schütteln mit dem Neigungsschalter erkennt.
* Einen Timer basierend auf dem Neigungsschalter startet und stoppt.
* Die verstrichene Zeit auf der 4-stelligen 7-Segment-Anzeige anzeigt.
* Multiplexing und Schieberegister verwendet, um die Anzeige zu steuern.

.. code-block:: python

    from machine import Pin
    import utime

    # Steuerpins für 74HC595 initialisieren
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # 7-Segment-Anzeigecodes für die Ziffern 0-9 (Gemeinsame Kathode)
    SEGMENT_CODES = [0x3F,  # 0
                    0x06,  # 1
                    0x5B,  # 2
                    0x4F,  # 3
                    0x66,  # 4
                    0x6D,  # 5
                    0x7D,  # 6
                    0x07,  # 7
                    0x7F,  # 8
                    0x6F]  # 9

    # Zifferauswahl-Pins initialisieren (Gemeinsame Kathoden)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
        machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
        machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
        machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
    ]


    # Neigungsschalter initialisieren
    tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

    # Variablen für die Zeitmessung
    start_time = 0
    elapsed_time = 0
    counting = False

    # Funktion, um Daten an die Schieberegister auszugeben
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Funktion, um eine Ziffer an einer bestimmten Position anzuzeigen
    def display_digit(position, digit):
        # Alle Ziffern ausschalten
        for dp in digit_pins:
            dp.high()
        # Segmentdaten senden
        shift_out(SEGMENT_CODES[digit])
        # Die ausgewählte Ziffer aktivieren (gemeinsame Kathode ist aktiv niedrig)
        digit_pins[position].low()
        # Kleine Verzögerung, um die Ziffer sichtbar zu machen
        utime.sleep_ms(5)
        # Die Ziffer ausschalten
        digit_pins[position].high()

    # Funktion, um die verstrichene Zeit anzuzeigen
    def display_time(time_ms):
        # Zeit in Hundertstelsekunden umrechnen (Hundertstel einer Sekunde)
        centiseconds = int(time_ms / 10)
        # Auf 9999 begrenzen, um auf das Display zu passen
        if centiseconds > 9999:
            centiseconds = 9999

        # Einzelne Ziffern extrahieren
        digits = [
            (centiseconds // 1000) % 10,
            (centiseconds // 100) % 10,
            (centiseconds // 10) % 10,
            centiseconds % 10
        ]
        # Jede Ziffer schnell anzeigen
        for i in range(4):
            display_digit(i, digits[i])

    # Interrupt-Handler für den Neigungsschalter
    def tilt_handler(pin):
        global counting, start_time, elapsed_time
        if not counting:
            # Beginne mit der Zeitmessung
            counting = True
            start_time = utime.ticks_ms()
        else:
            # Beende die Zeitmessung
            counting = False
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

    # Interrupt für den Neigungsschalter einrichten
    tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

    # Hauptloop
    while True:
        if counting:
            # Verstrichene Zeit berechnen
            current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            display_time(current_time)
        else:
            # Die endgültige Zeit anzeigen
            display_time(elapsed_time)



Wenn der Code läuft, sollte das 4-stellige 7-Segment-Display initialisieren und 00.00 anzeigen.

* Timer starten:

  * Schütteln Sie den Zauberstab oder neigen Sie den Neigungsschalter, um den Interrupt auszulösen.
  * Der Timer beginnt ab 00.00 zu zählen.

* Timer stoppen:

  * Schütteln Sie den Zauberstab oder neigen Sie den Schalter erneut.
  * Der Timer stoppt und zeigt die Endzeit an.

* Ziel:

  * Versuchen Sie, den Timer so nah wie möglich an 10,00 Sekunden zu stoppen.
  * Fordern Sie Freunde heraus, um zu sehen, wer am nächsten kommt!


**Verständnis des Codes**

#. Importe und Pin-Definitionen:

   * ``machine.Pin``: Zur Steuerung von GPIO-Pins.
   * ``utime``: Für Timing-Funktionen.
   * Definieren Sie SDI, SRCLK und RCLK-Pins zur Steuerung der Schieberegister.
   * Initialisieren Sie den Neigungsschalter auf GP16 mit einem Pull-Down-Widerstand.

#. Segment- und Zifferncodes:

   * ``SEGMENT_CODES``: Eine Liste mit den Binärcodes zur Anzeige der Ziffern 0-9 auf einem 7-Segment-Display.
   * ``digit_pins``: Codes zur Auswahl jeder Ziffer des Displays. Aktiv LOW für Displays mit gemeinsamer Kathode.

   .. code-block:: python

        # 7-Segment-Anzeigecodes für die Ziffern 0-9 (gemeinsame Kathode)
        SEGMENT_CODES = [0x3F,  # 0
                        0x06,  # 1
                        0x5B,  # 2
                        0x4F,  # 3
                        0x66,  # 4
                        0x6D,  # 5
                        0x7D,  # 6
                        0x07,  # 7
                        0x7F,  # 8
                        0x6F]  # 9

        # Initialisierung der Auswahlpins für Ziffern (gemeinsame Kathoden)
        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
            machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
            machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
            machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
        ]

#. Variablen für die Zeitmessung:

   * ``start_time``: Speichert den Zeitpunkt, zu dem der Timer startet.
   * ``elapsed_time``: Speichert die gesamte verstrichene Zeit, wenn der Timer stoppt.
   * ``counting``: Ein boolescher Indikator, der anzeigt, ob der Timer läuft.

#. Definition der Funktion ``shift_out``:

   * Sendet 8 Bit Daten an den 74HC595.
   * Schiebt die Daten beginnend vom signifikantesten Bit (MSB).
   * Steuert die Schiebe- und Registeruhren entsprechend.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Definition der Funktion ``display_digit``:

   * Schaltet alle Ziffern aus.
   * Sendet den Segmentcode für die Ziffer.
   * Aktiviert die angegebene Ziffer durch Setzen ihres Pins auf LOW.
   * Fügt eine kleine Verzögerung hinzu, um die Ziffer sichtbar zu machen.
   * Schaltet die Ziffer nach der Anzeige aus.

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()

#. Funktion ``display_time``:

   * Wandelt die verstrichene Zeit von Millisekunden in Hundertstelsekunden um.
   * Teilt die Zeit in einzelne Ziffern auf.
   * Nutzt Multiplexing, um jede Ziffer schnell anzuzeigen.

   .. code-block:: python

        def display_time(time_ms):
            # Zeit in Hundertstelsekunden umrechnen
            centiseconds = int(time_ms / 10)
            # Begrenzung auf 9999, um auf das Display zu passen
            if centiseconds > 9999:
                centiseconds = 9999

            # Einzelne Ziffern extrahieren
            digits = [
                (centiseconds // 1000) % 10,
                (centiseconds // 100) % 10,
                (centiseconds // 10) % 10,
                centiseconds % 10
            ]
            # Jede Ziffer schnell anzeigen
            for i in range(4):
                display_digit(i, digits[i])

#. Funktion ``tilt_handler``:

   * Wird durch den Interrupt des Neigungsschalters ausgelöst.
   * Wechselt den Zustand des Zählens.
   * Zeichnet ``start_time`` auf, wenn das Zählen beginnt.
   * Berechnet ``elapsed_time``, wenn das Zählen stoppt.

   .. code-block:: python

        def tilt_handler(pin):
            global counting, start_time, elapsed_time
            if not counting:
                # Beginne mit dem Zählen
                counting = True
                start_time = utime.ticks_ms()
            else:
                # Stoppe das Zählen
                counting = False
                elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

#. Hauptschleife:

   * Wenn ``counting`` „True“ ist, wird die Anzeige kontinuierlich mit der aktuellen verstrichenen Zeit aktualisiert.
   * Wenn ``counting`` „False“ ist, wird die endgültige ``elapsed_time`` angezeigt.

   .. code-block:: python

        while True:
            if counting:
                # Verstrichene Zeit berechnen
                current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
                display_time(current_time)
            else:
                # Endzeit anzeigen
                display_time(elapsed_time)

**Fehlerbehebung**

* Anzeigeprobleme:

  * Wenn das Display die Zahlen nicht korrekt anzeigt, überprüfen Sie die Segment- und Zifferncodes sowie die Verdrahtungsverbindungen.
  * Stellen Sie sicher, dass das Schieberegister richtig angeschlossen ist und dass die Daten in der richtigen Reihenfolge ausgegeben werden.

* Empfindlichkeit des Neigungsschalters:

  * Wenn der Neigungsschalter zu empfindlich oder nicht empfindlich genug ist, erwägen Sie, seine Ausrichtung anzupassen oder ihn durch einen anderen Typ zu ersetzen.
  * Stellen Sie sicher, dass der Pull-Down-Widerstand korrekt angeschlossen ist, um Fehlauslösungen zu vermeiden.

* Zeitgenauigkeit:

  * Der Timer basiert auf der Systemuhr, die recht genau ist, aber leichte Abweichungen aufweisen kann.
  * Für eine verbesserte Genauigkeit verwenden Sie ein externes Echtzeituhrmodul (RTC).

**Erweiterungen und Verbesserungen**

* Visuelle Effekte:

  * Fügen Sie LEDs hinzu, die aufleuchten oder die Farbe ändern, wenn der Timer stoppt.
  * Verwenden Sie einen Summer, um akustisches Feedback beim Starten und Stoppen des Timers zu geben.

* Highscore-Verfolgung:

  * Modifizieren Sie den Code, um die beste (nahe 10,00 Sekunden) erreichte Zeit zu speichern.
  * Zeigen Sie eine Glückwunschmeldung oder Animation für neue Highscores an.

* Mehrspielermodus:

  * Ermöglichen Sie mehreren Spielern, sich abzuwechseln und die Zeiten jedes Spielers zu speichern.
  * Zeigen Sie die Spielernummern und deren jeweilige Zeiten an.

* Schwierigkeitsstufen:

  * Führen Sie verschiedene Zielzeiten ein (z. B. 5,00 Sekunden, 15,00 Sekunden), um die Herausforderung zu erhöhen.
  * Randomisieren Sie die Zielzeit und zeigen Sie sie zu Beginn jeder Runde an.

* Alternative Eingabemethoden:

  * Ersetzen Sie den Neigungsschalter durch einen Knopf oder einen anderen Sensor zum Starten und Stoppen des Timers.
  * Verwenden Sie einen Bewegungssensor, um spezifische Gesten zu erkennen.

**Fazit**

Sie haben erfolgreich ein „10-Sekunden“-Spiel mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt kombiniert Sensorik, Timing-Funktionen und Anzeigesteuerung, um ein interaktives und unterhaltsames Spiel zu schaffen. Es ist ein ausgezeichnetes Beispiel dafür, wie Mikrocontroller verwendet werden können, um spaßige und fesselnde Erlebnisse zu schaffen.

Fühlen Sie sich frei, dieses Projekt nach Ihren Wünschen anzupassen und weiterzuentwickeln. Ob Sie neue Funktionen hinzufügen, das Design verbessern oder zusätzliche Komponenten integrieren, die Möglichkeiten sind grenzenlos.
