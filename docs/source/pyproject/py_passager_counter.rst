.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dein Wissen über Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_passage_counter:

7.4 Bau eines Passagierzählers
=======================================================

In dieser Lektion erstellen wir einen **Passagierzähler** mit einem Raspberry Pi Pico 2, einem PIR (Passiv-Infrarot) Bewegungssensor und einer 4-stelligen 7-Segment-Anzeige. Dieses Gerät zählt, wie oft Bewegungen vom PIR-Sensor erkannt werden und zeigt die Anzahl auf der 7-Segment-Anzeige an. Dies simuliert, wie solche Zähler an öffentlichen Orten verwendet werden, um den Fußgängerverkehr zu überwachen.

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

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


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
        - Micro USB-Kabel
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
        - 4(220Ω)
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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|

**Verständnis der Komponenten**

* **PIR-Bewegungssensor**: Erkennt Bewegungen, indem er die von Objekten in seinem Sichtfeld ausgehende Infrarotstrahlung misst. Bei erkannter Bewegung gibt er ein HOCH-Signal aus.
* **4-stellige 7-Segment-Anzeige**: Ermöglicht uns, Zahlen von 0000 bis 9999 anzuzeigen. Wir verwenden Schieberegister, um die Anzeige mit weniger GPIO-Pins zu steuern.
* **74HC595 Schieberegister**: Ein 8-Bit seriell-ein, parallel-aus Schieberegister mit Ausgangsverriegelung. Es ermöglicht uns, mehrere Ausgänge mit nur wenigen GPIO-Pins zu steuern.

**Schaltplan**

|sch_passager_counter| 

* Dieser Schaltkreis basiert auf dem :ref:`py_74hc_4dig` mit der Ergänzung eines PIR-Moduls.
* Der PIR sendet ein etwa 2,8 Sekunden langes Hochsignal, wenn jemand vorbeigeht.
* Das PIR-Modul hat zwei Potentiometer: eines zur Einstellung der Empfindlichkeit, das andere zur Einstellung der Erkennungsdistanz. Um das PIR-Modul besser zu nutzen, solltest du beide gegen den Uhrzeigersinn bis zum Anschlag drehen.

    |img_PIR_TTE|

**Verdrahtungsplan**

|wiring_passager_counter| 

**Den Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* Bewegungen mit dem PIR-Sensor erkennt.
* Den Zähler jedes Mal erhöht, wenn eine Bewegung erkannt wird.
* Die aktuelle Zählung auf der 4-stelligen 7-Segment-Anzeige aktualisiert.
* Multiplexing verwendet, um die Anzeige zu steuern.

.. note::

    * Öffne die Datei ``7.4_passager_counter.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der korrekte Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    from machine import Pin
    import utime

    # Definiere den PIR-Sensor-Pin
    pir_sensor = Pin(16, Pin.IN)

    # Initialisiere den Zähler
    count = 0

    # Definiere die Binärcodes für jede Ziffer (0-9)
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # Initialisiere die Steuerpins für 74HC595
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # Initialisiere die Ziffernauswahlpins (gemeinsame Kathoden)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
        machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
        machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
        machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
    ]

    # Funktion, um Daten an 74HC595 zu senden
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

    # Funktion, um eine Zahl auf der 4-stelligen Anzeige anzuzeigen
    def display_number(number):
        # Einzelne Ziffern extrahieren
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # Jede Ziffer schnell anzeigen
        for i in range(4):
            display_digit(i, digits[i])

    # Unterbrechungsbehandler für den PIR-Sensor
    def pir_handler(pin):
        global count
        count += 1
        if count > 9999:
            count = 0

    # Unterbrechung für den PIR-Sensor einrichten
    pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

    # Hauptloop
    while True:
        # Anzeige kontinuierlich aktualisieren
        display_number(count)

Wenn der Code läuft, sollte die 7-Segment-Anzeige initialisieren und 0000 anzeigen.
Bewege dich vor den PIR-Sensor.
Die angezeigte Zählung sollte jedes Mal um eins erhöht werden, wenn eine Bewegung erkannt wird.
Wenn die Zählung 9999 erreicht, wird sie auf 0000 zurückgesetzt.

**Verständnis des Codes**

#. Imports und Pin-Definitionen:

   * ``machine.Pin``: Zur Steuerung der GPIO-Pins.
   * ``utime``: Für Zeitfunktionen.
   * Definiere SDI, SRCLK und RCLK Pins zur Steuerung des Schieberegisters.
   * Definiere ``pir_sensor`` am GP16 als Eingangspin für den PIR-Sensor.

#. Segmentcodes:

   * ``SEGMENT_CODES``: Eine Liste mit den Binärcodes zur Anzeige der Ziffern 0-9 auf einer 7-Segment-Anzeige. Jedes Byte repräsentiert, welche Segmente beleuchtet sein sollten.

   .. code-block:: python

        # 7-Segment-Anzeige Segmentcodes für die Ziffern 0-9 (gemeinsame Kathode)
        SEGMENT_CODES = [
            0x3F,  # 0
            0x06,  # 1
            0x5B,  # 2
            0x4F,  # 3
            0x66,  # 4
            0x6D,  # 5
            0x7D,  # 6
            0x07,  # 7
            0x7F,  # 8
            0x6F   # 9
        ]

#. Zählerinitialisierung:

   * ``count``: Eine globale Variable, die die Anzahl der erkannten Bewegungen zählt.

#. Definiere die Funktion ``shift_out``:

   * Sendet 8 Bits Daten an das 74HC595.
   * Verschiebt die Daten beginnend beim signifikantesten Bit (MSB).
   * Impulsiert die Schiebe- und Registeruhren entsprechend.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Definiere die Funktion ``display_digit``:

   * Schaltet alle Ziffern aus.
   * Sendet den Segmentcode für die Ziffer.
   * Aktiviert die spezifizierte Ziffer, indem deren Pin auf niedrig gesetzt wird.
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

#. Definiere die Funktion ``display_number``:

   * Extrahiert jede Ziffer aus der Zahl.
   * Ruft ``display_digit`` schnell für jede Ziffer auf, um den Multiplexing-Effekt zu erzeugen.

   .. code-block:: python

        def display_number(number):
            # Einzelne Ziffern extrahieren
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # Jede Ziffer schnell anzeigen
            for i in range(4):
                display_digit(i, digits[i])

#. PIR-Unterbrechungsfunktion:

   * ``pir_handler``: Diese Funktion wird automatisch aufgerufen, wenn der PIR-Sensor eine Bewegung erkennt.
   * Erhöht die Variable count.
   * Setzt den Zähler auf 0 zurück, wenn er 9999 überschreitet.

   .. code-block:: python

        def pir_handler(pin):
            global count
            count += 1
            if count > 9999:
                count = 0

#. PIR-Sensor-Unterbrechungseinrichtung:

   ``pir_sensor.irq``: Richtet eine Unterbrechung ein, um ``pir_handler`` bei einem steigenden Signals des PIR-Sensors (d.h. bei erkannter Bewegung) aufzurufen.

   .. code-block:: python

        pir_sensor.irq(trigger=Pin.IRQ_RISING, handler=pir_handler)

#. Hauptloop:

   Ruft kontinuierlich ``display_number(count)`` auf, um die Anzeige mit der aktuellen Zählung zu aktualisieren.

   .. code-block:: python

        while True:
            display_number(count)

**Troubleshooting**

* Anzeigeprobleme:

  * Wenn das Display die Zahlen nicht korrekt anzeigt, überprüfen Sie die Segmentcodes und die Verdrahtungsanschlüsse.
  * Stellen Sie sicher, dass das Schieberegister korrekt angeschlossen ist und die Daten in der richtigen Reihenfolge verschoben werden.

* Empfindlichkeit des PIR-Sensors:

  * Der PIR-Sensor kann über einstellbare Potentiometer für Empfindlichkeit und Verzögerung verfügen.
  * Justieren Sie diese, um die Bewegungserkennung für Ihre Umgebung zu optimieren.
  * Beachten Sie, dass der PIR-Sensor nach der Erkennung einer Bewegung eine kurze Verzögerung haben kann, bevor erneut Bewegungen erkannt werden können.

* Zählgenauigkeit:

  * In Umgebungen mit viel Bewegung kann der Zähler schnell ansteigen.
  * Überlegen Sie, ob Sie eine Logik zum Entprellen des PIR-Sensors hinzufügen oder die Zählfrequenz begrenzen sollten.

**Extensions and Enhancements**

* Reset-Taste:

  Fügen Sie einen Druckknopf hinzu, der mit einem weiteren GPIO-Pin verbunden ist, um den Zähler auf null zurückzusetzen, wenn er gedrückt wird.

* Bidirektionales Zählen:

  Verwenden Sie zwei strategisch platzierte PIR-Sensoren, um die Bewegungsrichtung (Eintritt oder Austritt) zu erkennen und den Zähler entsprechend zu erhöhen oder zu verringern.

* Datenaufzeichnung:

  Erweitern Sie das Programm, um die Zählungen über die Zeit aufzuzeichnen, indem Sie Daten auf dem Pico speichern oder an einen Computer zur Analyse senden.

* Anzeigeverbesserungen:

  Verwenden Sie ein LCD-Display, um zusätzliche Informationen wie Zeitstempel, Gesamtzahlen oder Nachrichten anzuzeigen.

* Netzwerkverbindung:

  Verbinden Sie den Pico mit einem Netzwerk (unter Verwendung von Wi-Fi-Modulen wie ESP8266), um Daten an einen Server oder einen Cloud-Dienst für die Fernüberwachung zu senden.

**Conclusion**

In dieser Lektion haben Sie gelernt, wie Sie einen praktischen Passagierzähler mit dem Raspberry Pi Pico 2, einem PIR-Bewegungssensor und einem 4-stelligen 7-Segment-Display erstellen. Dieses Projekt zeigt, wie Mikrocontroller mit Sensoren und Ausgabegeräten interagieren können, um Daten in Echtzeit zu erfassen und anzuzeigen.

Experimentieren Sie ruhig mit dem Code und der Hardware, um neue Funktionen hinzuzufügen oder die Funktionalität zu verbessern. Dieses Projekt kann als Grundlage für komplexere Systeme dienen, die Datenanalyse, Fernüberwachung oder die Integration mit anderen Sensoren und Geräten umfassen.

