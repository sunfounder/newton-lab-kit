.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_ultrasonic:

6.1 Entfernungsmessung mit einem Ultraschallsensor
=====================================================

In dieser Lektion lernen wir, wie man ein **Ultraschallsensormodul** mit dem Raspberry Pi Pico 2 verwendet, um die Entfernung zu einem Objekt zu messen. Ultraschallsensoren werden häufig in Robotik- und Automatisierungssystemen zur Objekterkennung und Distanzmessung eingesetzt.

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Funktionsweise des Ultraschallsensors**

Der Ultraschallsensor sendet einen kurzen Ultraschallimpuls über den **Trig**-Pin aus und wartet auf das Echo am **Echo**-Pin. Durch die Messung der Zeit, die das Echo für die Rückkehr benötigt, kann die Entfernung zu einem Objekt anhand der Schallgeschwindigkeit berechnet werden.

|ultrasonic_prin|

* **Triggerimpuls**: Ein 10-Mikrosekunden-High-Puls am Trig-Pin startet die Messung.
* **Ultraschallimpuls**: Der Sensor sendet eine 8-Zyklen-Ultraschallwelle mit 40 kHz aus.
* **Echoempfang**: Der Echo-Pin geht auf HIGH und bleibt so lange aktiv, bis das Echo zurückkehrt.
* **Zeitmessung**: Durch die Dauer des HIGH-Signals am Echo-Pin kann die Entfernung berechnet werden.


**Schaltplan**

|sch_ultrasonic|

**Verdrahtungsdiagramm**

|wiring_ultrasonic|


**Code schreiben**

Nun schreiben wir ein MicroPython-Programm zur Entfernungsmessung mit dem Ultraschallsensor.

.. note::

    * Öffne ``6.1_measuring_distance.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
     

.. code-block:: python

    import machine
    import utime

    # Definiere die Pins für den Sensor
    TRIG = machine.Pin(17, machine.Pin.OUT)
    ECHO = machine.Pin(16, machine.Pin.IN)

    def measure_distance():
        # Stelle sicher, dass der Trigger-Pin LOW ist
        TRIG.low()
        utime.sleep_us(2)
        # Sende einen 10µs-Puls zur Messung
        TRIG.high()
        utime.sleep_us(10)
        TRIG.low()
        
        # Warte auf den Start des Echos
        while ECHO.value() == 0:
            pass
        start_time = utime.ticks_us()
        
        # Warte auf das Ende des Echos
        while ECHO.value() == 1:
            pass
        end_time = utime.ticks_us()
        
        # Berechne die Dauer des Echo-Impulses
        duration = utime.ticks_diff(end_time, start_time)
        
        # Berechne die Entfernung (Schallgeschwindigkeit: 34300 cm/s)
        distance = (duration * 0.0343) / 2
        return distance

    while True:
        dist = measure_distance()
        print("Distance: {:.2f} cm".format(dist))
        utime.sleep(0.5)

Sobald der Code ausgeführt wird, zeigt die Thonny-Shell die gemessenen Entfernungswerte in Zentimetern an. Bewege ein Objekt näher an den Sensor heran oder weiter weg, um die veränderten Messwerte zu beobachten.

**Den Code verstehen**

#. Notwendige Module importieren und die Trigger- und Echo-Pins einrichten:

   .. code-block:: python
   
       import machine
       import utime
   
       TRIG = machine.Pin(17, machine.Pin.OUT)
       ECHO = machine.Pin(16, machine.Pin.IN)


#. Entfernung messen:

   * Sendet einen Triggerimpuls, um die Messung zu starten.
   * Wartet auf das empfangene Echo.
   * Berechnet die Dauer des Echo-Impulses.
   * Ermittelt die Entfernung basierend auf der Schallgeschwindigkeit.

   .. code-block:: python

       def measure_distance():
           # Sicherstellen, dass der Trigger-Pin LOW ist
           TRIG.low()
           utime.sleep_us(2)
           # 10µs-Impuls zur Messung senden
           TRIG.high()
           utime.sleep_us(10)
           TRIG.low()
           
           # Auf den Beginn des Echo-Signals warten
           while ECHO.value() == 0:
               pass
           start_time = utime.ticks_us()
           
           # Warten, bis das Echo endet
           while ECHO.value() == 1:
               pass
           end_time = utime.ticks_us()
           
           # Dauer des Echo-Impulses berechnen
           duration = utime.ticks_diff(end_time, start_time)
           # Entfernung berechnen
           distance = (duration * 0.0343) / 2
           return distance


#. Hauptschleife:

   * Misst kontinuierlich die Entfernung und gibt sie aus.
   * Legt eine halbe Sekunde Pause zwischen den Messungen ein.

   .. code-block:: python
   
       while True:
           dist = measure_distance()
           print("Distance: {:.2f} cm".format(dist))
           utime.sleep(0.5)


**Einschränkungen verstehen**


* Blockierender Code:

  * Die while-Schleifen zum Warten auf das Echo können verhindern, dass andere Codeabschnitte parallel ausgeführt werden.
  * Für fortgeschrittene Anwendungen sollten Interrupts oder asynchrone Programmierung in Betracht gezogen werden, um Blockierungen zu vermeiden.

* Messbereich:

  * Der HC-SR04-Sensor hat typischerweise einen Messbereich von 2 cm bis 400 cm.
  * Objekte, die näher als 2 cm oder weiter als 400 cm entfernt sind, werden möglicherweise nicht genau erkannt.

* Umwelteinflüsse:

  * Temperatur und Luftfeuchtigkeit können die Schallgeschwindigkeit beeinflussen.
  * Für genauere Messungen kann die Schallgeschwindigkeit an die Umgebungsbedingungen angepasst werden.

**Fazit**

Du hast erfolgreich einen Ultraschallsensor genutzt, um mit dem Raspberry Pi Pico 2 Entfernungen zu messen. Diese grundlegende Fähigkeit findet breite Anwendung in der Robotik, Automatisierung und interaktiven Projekten.