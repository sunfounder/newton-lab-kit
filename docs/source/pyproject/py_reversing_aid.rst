.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook!  
    Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_reversing_aid:

7.10 Bau eines Einparkassistenten
====================================

In diesem Projekt bauen wir ein **Einparkhilfe-System** mit dem Raspberry Pi Pico 2, einem Ultraschallsensor, einer LED und einem Buzzer.  
Das System simuliert reale Parksensoren, indem es den Abstand zu einem Hindernis misst und akustische sowie visuelle Signale ausgibt.  
Je näher das Objekt kommt, desto schneller blinkt die LED und desto häufiger ertönt der Buzzer.  
Du kannst diese Schaltung an ein ferngesteuertes Auto anbringen, um das Einparken in eine Garage nachzustellen.

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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 2 (1KΩ, 220Ω)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        -
    *   - 8
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 9
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Funktionsweise der Komponenten**

* **Ultraschallsensor (HC-SR04):** Misst den Abstand zu einem Objekt, indem er Ultraschallwellen aussendet und die Zeit misst, bis das Echo zurückkehrt.
* **Buzzer:** Gibt akustische Signale aus, die mit abnehmender Distanz schneller ertönen.
* **LED:** Blinkt mit zunehmender Frequenz, je näher das Hindernis kommt.

**Schaltplan**

|sch_reversing_aid|

**Verdrahtungsdiagramm**

|wiring_reversing_aid| 

**Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* Die Distanz mit dem Ultraschallsensor misst.
* Die Frequenz des Buzzers und die Blinkgeschwindigkeit der LED basierend auf der Entfernung anpasst.
* Kontinuierliches Feedback liefert, wenn sich das Objekt bewegt.

.. note::

    * Öffne die Datei ``7.10_reversing_aid.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf „Run“ oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Pins definieren
    trigger = machine.Pin(17, machine.Pin.OUT)
    echo = machine.Pin(16, machine.Pin.IN)
    buzzer = machine.Pin(15, machine.Pin.OUT)
    led = machine.Pin(14, machine.Pin.OUT)

    # Funktion zur Distanzmessung
    def measure_distance():
        # Ensure trigger is low
        trigger.low()
        utime.sleep_us(2)
        # Send 10us pulse to trigger
        trigger.high()
        utime.sleep_us(10)
        trigger.low()

        # Measure the duration of the echo pulse
        while echo.value() == 0:
            signaloff = utime.ticks_us()
        while echo.value() == 1:
            signalon = utime.ticks_us()

        timepassed = utime.ticks_diff(signalon, signaloff)
        distance = (timepassed * 0.0343) / 2  # Umrechnung in cm
        return distance

    # Funktion zur Steuerung von Buzzer und LED
    def alert(interval):
        buzzer.high()
        led.high()
        utime.sleep(0.1)
        buzzer.low()
        led.low()
        utime.sleep(interval)

    # Hauptschleife
    try:
        while True:
            dist = measure_distance()
            print("Distance: {:.2f} cm".format(dist))
            if dist < 0:
                print("Out of range")
                utime.sleep(1)
            elif dist <= 10:
                alert(0.2)  # Sehr nah, schnelles Signal
            elif dist <= 20:
                alert(0.5)  # Nah, mittleres Signal
            elif dist <= 50:
                alert(1)    # Weiter entfernt, langsames Signal
            else:
                alert(2)    # Weit weg, sehr seltenes Signal
    except KeyboardInterrupt:
        print("Measurement stopped by User")

Wenn das Skript läuft, platziere ein Objekt in verschiedenen Abständen zum Ultraschallsensor.  
Beobachte, wie sich die Tonfrequenz des Buzzers und die Blinkgeschwindigkeit der LED verändern.  
Die Konsole zeigt die gemessene Entfernung an.

**Den Code verstehen**

#. Distanzmessung:
   * Die Funktion ``measure_distance()`` sendet einen 10-Mikrosekunden-Puls an den TRIG-Pin. 
   * Anschließend misst sie die Zeit, bis der ECHO-Pin auf HIGH geht und dann wieder auf LOW wechselt.
   * Die Entfernung wird basierend auf der Zeit berechnet, die der Ultraschallimpuls für die Rückkehr benötigt.

   .. code-block:: python

        def measure_distance():
            # Sicherstellen, dass der Trigger auf LOW ist
            trigger.low()
            utime.sleep_us(2)
            # Sende einen 10us-Puls an den Trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Messe die Dauer des Echo-Impulses
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Umrechnung in cm
            return distance


#. Warnfunktion:

   * Die Funktion ``alert(interval)`` aktiviert den Buzzer und die LED für 0,1 Sekunden und schaltet sie dann wieder aus.
   * Der Parameter interval steuert die Pause zwischen den Warnsignalen abhängig von der gemessenen Entfernung.

   .. code-block:: python

        def measure_distance(): 
            # Sicherstellen, dass der Trigger auf LOW ist
            trigger.low()
            utime.sleep_us(2)
            # Sende einen 10µs-Puls an den Trigger
            trigger.high()
            utime.sleep_us(10)
            trigger.low()

            # Messe die Dauer des Echo-Pulses
            while echo.value() == 0:
                signaloff = utime.ticks_us()
            while echo.value() == 1:
                signalon = utime.ticks_us()

            timepassed = utime.ticks_diff(signalon, signaloff)
            distance = (timepassed * 0.0343) / 2  # Umrechnung in cm
            return distance

#. Hauptschleife:

   * Misst kontinuierlich die Entfernung.
   * Passt die Frequenz der Warnsignale entsprechend den vordefinierten Abstandsschwellen an.

   .. code-block:: python

        try:
            while True:
                dist = measure_distance()
                print("Distance: {:.2f} cm".format(dist))
                if dist < 0:
                    print("Out of range")
                    utime.sleep(1)
                elif dist <= 10:
                    alert(0.2)  # Sehr nah, schnelles Warnsignal
                elif dist <= 20:
                    alert(0.5)  # Nah, mittleres Warnsignal
                elif dist <= 50:
                    alert(1)    # Weiter entfernt, langsames Warnsignal
                else:
                    alert(2)    # Sehr weit entfernt, seltenes Warnsignal
        except KeyboardInterrupt:
            print("Measurement stopped by User")
        
**Sicherheitsaspekte**

* Spannungsebenen:

  * Achte darauf, dass der ECHO-Pin des Ultraschallsensors 5V ausgeben kann.
  * Verwende einen Spannungsteiler oder Pegelwandler, um die GPIO-Pins des Pico zu schützen.

* Stromversorgung:

  Stelle sicher, dass die Stromquelle die Stromaufnahme aller Komponenten bewältigen kann.

**Weitere Experimente**

* Visuelle Anzeige:

  Ergänze ein LCD- oder OLED-Display zur grafischen Darstellung der Entfernung.

* Mehrere Sensoren:

  Verwende zusätzliche Ultraschallsensoren, um mehrere Richtungen abzudecken.

* Erweiterte Warnsignale:

  Implementiere unterschiedliche Töne oder Signalmuster für verschiedene Entfernungen.

**Fazit**

Du hast erfolgreich ein Einparkhilfe-System mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt zeigt, wie Sensoren genutzt werden können, um Echtzeit-Feedback bereitzustellen – ein grundlegendes Konzept in Robotik und Automatisierung.
