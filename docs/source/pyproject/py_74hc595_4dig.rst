.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_4dig:

5.3 Erstellung eines Zeitmessers mit einem 4-stelligen 7-Segment-Display
===========================================================================

In dieser Lektion lernen wir, wie man ein **4-stelliges 7-Segment-Display** mit dem Raspberry Pi Pico 2 verwendet, um einen einfachen Zeitmesser zu erstellen. Das Display zählt jede Sekunde hoch und zeigt die verstrichene Zeit in Sekunden an.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE KOMPONENTEN
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
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Funktionsweise des 4-stelligen 7-Segment-Displays**

Ein 4-stelliges 7-Segment-Display besteht aus vier einzelnen 7-Segment-Anzeigen, die zu einem einzigen Modul kombiniert sind. Jede Ziffer teilt sich dieselben Segmentsteuerleitungen (**a** bis **g** und **dp**), aber jede Ziffer hat eine eigene **gemeinsame Kathode**, um zu steuern, welche Ziffer aktiv ist.

Um verschiedene Zahlen auf jeder Ziffer mit gemeinsamen Segmentleitungen anzuzeigen, nutzen wir eine Technik namens **Multiplexing**. Dabei werden die Ziffern schnell hintereinander aktualisiert – so schnell, dass es durch die Trägheit des menschlichen Auges scheint, als wären alle gleichzeitig sichtbar.

|4digit_control_pins|

**Schaltplan**

|sch_4dig|

Das Verdrahtungsprinzip ist im Wesentlichen dasselbe wie bei :ref:`py_74hc_led`, der einzige Unterschied besteht darin, dass Q0-Q7 mit den a ~ g Pins des 4-stelligen 7-Segment-Displays verbunden sind.

Die Pins G10 ~ G13 steuern, welche der vier Ziffern aktiviert wird.

**Verdrahtungsdiagramm**

|wiring_4dig|

* **Segmentverbindungen (über 220 Ω Widerstände):**

  * **Q0** → Segment **a**
  * **Q1** → Segment **b**
  * **Q2** → Segment **c**
  * **Q3** → Segment **d**
  * **Q4** → Segment **e**
  * **Q5** → Segment **f**
  * **Q6** → Segment **g**
  * **Q7** → Segment **dp** (Dezimalpunkt)

* **Gemeinsame Kathodenverbindungen (Ziffernsteuerung):**

  * **Ziffer 1 (linke Ziffer):** Verbinden mit **GP10** auf dem Pico
  * **Ziffer 2:** Verbinden mit **GP11**
  * **Ziffer 3:** Verbinden mit **GP12**
  * **Ziffer 4 (rechte Ziffer):** Verbinden mit **GP13**


**Code schreiben**

Nun erstellen wir ein MicroPython-Programm, das jede Sekunde einen Zähler erhöht und diesen auf dem 4-stelligen 7-Segment-Display anzeigt.

.. note::

    * Öffnen Sie ``5.3_time_counter.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Definieren der Binärcodes für jede Ziffer (0-9)
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

    # Initialisieren der Steuerpins für 74HC595
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serieller Dateneingang (DS)
    RCLK = machine.Pin(19, machine.Pin.OUT)  # Register-Takt (STCP)
    SRCLK = machine.Pin(20, machine.Pin.OUT) # Schieberegister-Takt (SHCP)

    # Initialisieren der Ziffernsteuerpins (gemeinsame Kathoden)
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  # Ziffer 1
        machine.Pin(11, machine.Pin.OUT),  # Ziffer 2
        machine.Pin(12, machine.Pin.OUT),  # Ziffer 3
        machine.Pin(13, machine.Pin.OUT)   # Ziffer 4
    ]

    # Funktion zum Senden von Daten an 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Funktion zum Anzeigen einer Zahl auf einer bestimmten Position
    def display_digit(position, digit):
        # Turn off all digits
        for dp in digit_pins:
            dp.high()
        # Send segment data
        shift_out(SEGMENT_CODES[digit])
        # Activate the selected digit (common cathode is active low)
        digit_pins[position].low()
        # Small delay to allow the digit to be visible
        utime.sleep_ms(5)
        # Turn off the digit
        digit_pins[position].high()

    # Funktion zum Anzeigen einer Zahl auf dem Display
    def display_number(number):
        # Extract individual digits
        digits = [
            (number // 1000) % 10,
            (number // 100) % 10,
            (number // 10) % 10,
            number % 10
        ]
        # Display each digit rapidly
        for i in range(4):
            display_digit(i, digits[i])

    # Hauptschleife
    counter = 0
    last_update = utime.ticks_ms()

    while True:
        # Update the counter every 1000 ms (1 second)
        current_time = utime.ticks_ms()
        if utime.ticks_diff(current_time, last_update) >= 1000:
            counter += 1
            if counter > 9999:
                counter = 0
            last_update = current_time

        # Continuously refresh the display
        display_number(counter)

Wenn Sie diesen Code ausführen, fungiert das 4-stellige 7-Segment-Display als Zähler, der jede Sekunde um 1 erhöht wird. Die Anzeige beginnt bei 0 und zählt bis 9999 hoch, bevor sie wieder auf 0 zurückgesetzt wird und den Zyklus kontinuierlich wiederholt.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Ermöglicht den Zugriff auf GPIO-Pins und Hardwarefunktionen.
   * ``utime``: Enthält Zeitfunktionen für Verzögerungen und Zeitmessungen.

#. Segmentcodes definieren:

   Jeder Eintrag entspricht den Segmenten, die zum Anzeigen einer Ziffer aktiviert werden müssen. Die Werte sind im Hexadezimalformat angegeben.

   .. code-block:: python

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

#. Steuerpins initialisieren:
   
   Weist die GPIO-Pins des Pico zur Steuerung des 74HC595 zu.

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        RCLK = machine.Pin(19, machine.Pin.OUT)
        SRCLK = machine.Pin(20, machine.Pin.OUT)


#. Ziffernsteuerpins initialisieren:

   Steuert, welche Ziffer aktiv ist. Die gemeinsame Kathode ist aktiv niedrig.

   .. code-block:: python

        digit_pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)
        ]

#. Die Funktion ``shift_out`` definieren:

   * Sendet 8 Bits an den 74HC595.
   * Überträgt die Daten beginnend mit dem höchstwertigen Bit (MSB).
   * Pulsiert die Schieberegister- und Register-Taktleitungen entsprechend.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Die Funktion ``display_digit`` definieren:

   * Schaltet alle Ziffern aus.
   * Sendet die Segmentdaten für die gewünschte Ziffer.
   * Aktiviert die ausgewählte Ziffer durch Setzen des Pins auf LOW.
   * Fügt eine kleine Verzögerung hinzu, um die Ziffer sichtbar zu machen.
   * Schaltet die Ziffer danach wieder aus.

   .. code-block:: python

        def display_digit(position, digit):
            for dp in digit_pins:
                dp.high()
            shift_out(SEGMENT_CODES[digit])
            digit_pins[position].low()
            utime.sleep_ms(5)
            digit_pins[position].high()


#. Die Funktion ``display_number`` definieren:

   * Extrahiert jede einzelne Ziffer aus der Zahl.
   * Ruft ``display_digit`` für jede Ziffer auf, um den Multiplexing-Effekt zu erzeugen.

   .. code-block:: python

        def display_number(number):
            # Extrahiere einzelne Ziffern
            digits = [
                (number // 1000) % 10,
                (number // 100) % 10,
                (number // 10) % 10,
                number % 10
            ]
            # Zeigt jede Ziffer schnell nacheinander an
            for i in range(4):
                display_digit(i, digits[i])

#. Hauptschleife:

   * Erhöht den Zähler jede Sekunde.
   * Setzt den Zähler auf 0 zurück, nachdem er 9999 erreicht hat.
   * Ruft kontinuierlich ``display_number`` auf, um die Anzeige zu aktualisieren.

   .. code-block:: python

        counter = 0
        last_update = utime.ticks_ms()

        while True:
            current_time = utime.ticks_ms()
            if utime.ticks_diff(current_time, last_update) >= 1000:
                counter += 1
                if counter > 9999:
                    counter = 0
                last_update = current_time

            display_number(counter)

**Weitere Experimente**

* Einen Reset-Button hinzufügen: 
  Verbinden Sie eine Taste mit dem Pico, um den Zähler zurückzusetzen, wenn er gedrückt wird.

* Andere Daten anzeigen:  
  Ändern Sie den Code so, dass Sensorwerte angezeigt werden, z. B. Temperatur oder Lichtstärke.

* Display-Helligkeit anpassen:  
  Ändern Sie die Verzögerung ``utime.sleep_ms(5)`` in der Funktion ``display_digit``, um zu steuern, wie lange jede Ziffer angezeigt wird – dies beeinflusst die Helligkeit.

* Eine Stoppuhr erstellen:  
  Implementieren Sie Start-, Stopp- und Reset-Funktionen, um das Display als Stoppuhr zu verwenden.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie ein 4-stelliges 7-Segment-Display mit einem 74HC595-Schieberegister verwenden, um einen Zeitmesser mit dem Raspberry Pi Pico 2 zu erstellen. Durch das Verständnis von Multiplexing und effizientem Timing können Sie dynamische Informationen auf mehrstelligen Anzeigen mit minimalen GPIO-Pins anzeigen.
