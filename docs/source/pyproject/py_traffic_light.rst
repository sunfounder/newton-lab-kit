.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Python & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Python und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_traffic_light:

7.6 Bau eines Ampelsteuerungssystems
==============================================================

In diesem Projekt erstellen wir eine **Ampelsteuerung** mit dem Raspberry Pi Pico 2, drei LEDs (rot, gelb, grün) und einer 4-stelligen 7-Segment-Anzeige. Dieses System simuliert eine echte Ampelschaltung und zeigt die verbleibende Zeit für jedes Licht auf der Anzeige an.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Ein komplettes Kit ist besonders praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten auch einzeln über die folgenden Links erworben werden.


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
        - 7 (220Ω)
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
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|

**Funktionsweise der Komponenten**

* **LEDs**: Stellen die Ampellichter dar. Sie werden in einer festgelegten Reihenfolge geschaltet.
* **4-stellige 7-Segment-Anzeige**: Zeigt den Countdown-Timer für jede Lichtphase an.
* **74HC595 Schieberegister**: Ermöglicht die Steuerung mehrerer Ausgänge (Segmente und Ziffern der Anzeige) mit weniger GPIO-Pins des Pico.


**Schaltplan**

|sch_traffic_light|


* Diese Schaltung basiert auf der :ref:`py_74hc_4dig` mit der zusätzlichen Integration von 3 LEDs.
* Die drei LEDs (Rot, Gelb, Grün) sind mit GP7 bis GP9 verbunden.

**Verdrahtungsdiagramm**

|wiring_traffic_light| 

**Code schreiben**

Das MicroPython-Skript wird:

* Die Ampelsequenz steuern.
* Die verbleibende Zeit auf der 7-Segment-Anzeige darstellen.
* Schieberegister zur Steuerung der Anzeige nutzen.

.. note::

    * Öffne ``7.6_traffic_light.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    from machine import Timer

    # Initialisierung der LED-Pins
    led_pins = [7, 8, 9]  # Grün, Gelb, Rot an GP7, GP8, GP9
    leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

    # Dauer für jede Ampelphase [Grün, Gelb, Rot]
    light_time = [30, 5, 30]  # [Grün, Gelb, Rot]

    # Binärcodes für Ziffern (0-9)
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

    # Pins für das 74HC595 Schieberegister
    SDI = machine.Pin(18, machine.Pin.OUT)  
    RCLK = machine.Pin(19, machine.Pin.OUT)  
    SRCLK = machine.Pin(20, machine.Pin.OUT) 

    # Pins zur Steuerung der 4-stelligen Anzeige
    digit_pins = [
        machine.Pin(10, machine.Pin.OUT),  
        machine.Pin(11, machine.Pin.OUT),  
        machine.Pin(12, machine.Pin.OUT),  
        machine.Pin(13, machine.Pin.OUT)   
    ]

    # Function to send data to 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Function to display a digit at a specific position
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

    # Function to display a number on the 4-digit display
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

    # Function to update the LEDs based on the current state
    def update_leds(state):
        # States: 0 = Green, 1 = Yellow, 2 = Red
        for i in range(3):
            leds[i].value(0)
        leds[state].value(1)

    # Timer variables
    counter = light_time[0]  # Start with green light duration
    current_state = 0  # 0 = Green, 1 = Yellow, 2 = Red

    # Timer interrupt callback to update the traffic light state and counter
    def timer_callback(t):
        global counter, current_state
        counter -= 1
        if counter <= 0:
            current_state = (current_state + 1) % 3  # Cycle through the states
            counter = light_time[current_state]  # Reset counter for the new state
            update_leds(current_state)

    # Initialize the timer
    timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

    # Initial LED state
    update_leds(current_state)

    # Main loop
    try:
        while True:
            display_number(counter)
    except KeyboardInterrupt:
        timer.deinit()
        print("Program stopped.")


Wenn der Code ausgeführt wird, leuchtet zuerst die grüne LED auf, und die Anzeige startet einen Countdown von 30 Sekunden.  
Nach 30 Sekunden schaltet die gelbe LED ein, während die Anzeige von 5 herunterzählt.  
Anschließend leuchtet die rote LED auf, und die Anzeige zählt erneut 30 Sekunden herunter.  
Dieser Zyklus wiederholt sich kontinuierlich.

**Den Code verstehen**

#. Importe und Initialisierung:

   * ``machine``: Ermöglicht den Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Bietet Zeitfunktionen.
   * ``Timer``: Wird zur Erstellung von Hardware-Timern verwendet.

#. Initialisierung der LEDs:

   Definiert die GPIO-Pins für die rote, gelbe und grüne LED und setzt sie als Ausgänge.

   .. code-block:: python

        led_pins = [7, 8, 9]  # Grün, Gelb, Rot an GP7, GP8, GP9
        leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

#. Ampelzeiten definieren:

   Legt die Dauer (in Sekunden) für jede Ampelphase fest.

   .. code-block:: python

        light_time = [30, 5, 30]  # [Grün, Gelb, Rot]

#. Anzeige-Funktionen:

   * ``display_digit(digit)``: Aktiviert eine bestimmte Ziffer auf der Anzeige.
   * ``shift_out(data)``: Sendet Daten an das Schieberegister.
   * ``display_number(num)``: Zerlegt die Zahl in einzelne Ziffern und zeigt sie per Multiplexing an.

#. ``update_leds(state)`` Funktion:

   * Aktualisiert den Status der LEDs entsprechend der aktuellen Ampelphase.
   * Schaltet alle LEDs aus und aktiviert die LED, die zur aktuellen Phase gehört.

   .. code-block:: python

        def update_leds(state):
            # Zustände: 0 = Grün, 1 = Gelb, 2 = Rot
            for i in range(3):
                leds[i].value(0)
            leds[state].value(1)

#. ``timer_callback(t)`` Funktion:

   * Interrupt-Funktion für den Timer.
   * Verringert den Countdown-Wert jede Sekunde um eins.
   * Wenn der Countdown abläuft, wechselt die Ampel zur nächsten Phase und der Timer wird zurückgesetzt.

   .. code-block:: python

        def timer_callback(t):
            global counter, current_state
            counter -= 1
            if counter <= 0:
                current_state = (current_state + 1) % 3  # Wechsle zur nächsten Phase
                counter = light_time[current_state]  # Setze den Timer für die neue Phase zurück
                update_leds(current_state)

#. Hauptprogramm:

   * Initialisierung der Variablen: Setzt den Startzustand auf Grün und initialisiert den Countdown.

     .. code-block:: python

        counter = light_time[0]  # Start mit Grün
        current_state = 0  # 0 = Grün, 1 = Gelb, 2 = Rot

   * Timer initialisieren: Erstellt einen periodischen Timer, der alle 1000 Millisekunden (1 Sekunde) timer_callback aufruft.


     .. code-block:: python

        timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

   * Setze die anfängliche LED-Anzeige: Stellt sicher, dass die richtige LED beim Start leuchtet.

     .. code-block:: python

        update_leds(current_state)

   * Hauptschleife: Zeigt kontinuierlich den Countdown an. Falls eine Tastenkombination wie Strg+C gedrückt wird, wird der Timer deaktiviert und das Programm beendet.


     .. code-block:: python

        try:
            while True:
                display_number(counter)
        except KeyboardInterrupt:
            timer.deinit()
            print("Program stopped.")


**Erweiterungsmöglichkeiten**

* Zeitintervalle anpassen:

  Ändere die Werte in ``light_time``, um die Dauer der einzelnen Ampelphasen anzupassen.

* Fußgängerampel hinzufügen:

  Integriere Taster und zusätzliche LEDs zur Simulation eines Fußgängerübergangs.

* Anzeige verbessern:

  Implementiere eine blinkende LED, wenn die verbleibende Zeit einer Phase fast abgelaufen ist.

* Realistischere Ampelschaltung erstellen:

  Integriere komplexere Sequenzen wie Abbiegesignale oder mehrere Verkehrswege.

**Fazit**

Du hast erfolgreich eine Ampelsteuerung mit dem Raspberry Pi Pico 2 erstellt!  
Dieses Projekt zeigt, wie Mikrocontroller zur Steuerung von Hardware-Komponenten wie LEDs und Anzeigen genutzt werden können, und demonstriert die Verwendung von Timern und Interrupts für Echtzeitanwendungen.

Erweitere das Projekt nach Belieben, indem du neue Funktionen hinzufügst oder es in ein größeres System integrierst!
