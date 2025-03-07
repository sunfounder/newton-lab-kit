.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook!  
    Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_pir:

2.10 Menschliche Bewegung erkennen
=====================================

In dieser Lektion lernen wir, wie man einen **Passiven Infrarotsensor (PIR)** mit dem Raspberry Pi Pico 2 verwendet, um Bewegungen von Menschen zu erkennen. PIR-Sensoren werden häufig in Sicherheitssystemen, automatischen Beleuchtungssystemen und anderen Anwendungen zur Bewegungserkennung eingesetzt. Sie erkennen die Infrarotstrahlung, die von warmen Objekten wie Menschen oder Tieren ausgestrahlt wird.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt:  

Ein vollständiges Kit ist hier erhältlich:  

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten einzeln erworben werden: 


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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schaltplan**

|sch_pir|

Sobald der PIR-Sensor eine Bewegung erkennt, wird GP14 HIGH, ansonsten bleibt es LOW.

.. note::

    Der PIR-Sensor verfügt über zwei Potentiometer:

    * **Empfindlichkeitseinstellung**: Bestimmt die Reichweite der Erkennung.
    * **Verzögerungseinstellung**: Bestimmt, wie lange der Ausgang nach einer Bewegungserkennung HIGH bleibt.

    Für erste Tests sollten beide Potentiometer gegen den Uhrzeigersinn auf ihre Minimalwerte gedreht werden. Dadurch wird der Sensor auf maximale Empfindlichkeit und kürzeste Verzögerung eingestellt, sodass sofortige Reaktionen beobachtet werden können.
    

    |img_PIR_TTE|

**Verdrahtung**

|wiring_pir|


**Code schreiben** 

Wir werden ein MicroPython-Programm schreiben, das eine Unterbrechung (Interrupt) nutzt, um Bewegung zu erkennen und eine Meldung auszugeben, sobald eine Bewegung registriert wird.

.. note::

    * Öffne die Datei ``2.10_detect_human_movement.py`` unter ``newton-lab-kit/micropython`` oder kopiere den folgenden Code in Thonny. Klicke dann auf „Run Current Script“ oder drücke F5.
    * Stelle sicher, dass der Interpreter „MicroPython (Raspberry Pi Pico).COMxx“ unten rechts in Thonny ausgewählt ist.

.. code-block:: python

    import machine
    import utime

    # GP14 als Eingang für den PIR-Sensor initialisieren
    pir_sensor = machine.Pin(14, machine.Pin.IN)

    def motion_detected(pin):
        print("Motion detected!")

    # Interrupt für steigende Flanke (LOW → HIGH) setzen
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Hauptschleife bleibt leer, da der Interrupt die Erkennung übernimmt
    while True:
        utime.sleep(1)

Sobald das Programm läuft, können folgende Beobachtungen gemacht werden:

* Bewege dich vor dem PIR-Sensor.
* Sobald eine Bewegung erkannt wird, erscheint die Meldung „Bewegung erkannt!“ in der Konsole.

**Code verstehen**

#. Module importieren:

   * ``import machine``: Zugriff auf Hardware-Funktionen.
   * ``import utime``: Zeitbezogene Funktionen.

#. PIR-Sensor initialisieren:

   * ``pir_sensor = machine.Pin(14, machine.Pin.IN)``: Setzt GP14 als Eingangspin.

#. Interrupt-Handler definieren:

   * ``def motion_detected(pin)``: Funktion, die bei Bewegungserkennung aufgerufen wird.
   * ``print("Motion detected!")``: Gibt eine Meldung in der Konsole aus.

#. Interrupt konfigurieren:

   * ``pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)``: Löst eine Unterbrechung aus, wenn das PIR-Signal von LOW auf HIGH wechselt. Ruft die Funktion ``motion_detected`` auf.

#. Hauptschleife:

   * ``while True``: Endlosschleife.
   * ``utime.sleep(1)``: Die Schleife schläft für eine Sekunde. Die Bewegungserkennung erfolgt ausschließlich über den Interrupt.

**Erweiterung: Dauer der Bewegungserkennung messen**

Der Code kann so modifiziert werden, dass er die Dauer einer erkannten Bewegung misst:

.. code-block:: python

    import machine
    import utime

    pir_sensor = machine.Pin(14, machine.Pin.IN)

    last_trigger_time = utime.ticks_ms()

    def pir_triggered(pin):
        global last_trigger_time
        current_time = utime.ticks_ms()
        duration = utime.ticks_diff(current_time, last_trigger_time)
        last_trigger_time = current_time

        if pir_sensor.value():
            print("Motion detected! Duration since last detection: {} ms".format(duration))
        else:
            print("Motion ended. Duration of motion: {} ms".format(duration))

    # Interrupts für steigende und fallende Flanken setzen
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=pir_triggered)

    while True:
        utime.sleep(1)

* Interrupts für beide Flanken:  
  Die Unterbrechung wird sowohl bei einer steigenden als auch bei einer fallenden Flanke ausgelöst  (``machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING``).

* Zeitmessung:

  * ``utime.ticks_ms()`` gibt die aktuelle Zeit in Millisekunden zurück.
  * Die Dauer wird anhand der Zeitdifferenz zwischen zwei Triggern berechnet.

**Praktische Anwendungen**

* **Sicherheitssysteme**: Einbruchserkennung und Alarmaktivierung.
* **Automatische Beleuchtung**: Licht schaltet sich bei Bewegung ein.
* **Energiesparen**: Geräte werden ausgeschaltet, wenn keine Bewegung erkannt wird.

**Fehlersuche**

* Falsche Auslösungen:

  * PIR-Sensoren reagieren empfindlich auf Wärmequellen.
  * Vermeide direkte Sonneneinstrahlung oder die Nähe zu Heizkörpern.

* Keine Bewegung erkannt:

  * Einige PIR-Sensoren benötigen bis zu 60 Sekunden zur Initialisierung.
  * Die Empfindlichkeitseinstellung des Potentiometers überprüfen.

* Interferenzen vermeiden:

  * Halte den Sensor von elektromagnetischen Störquellen fern.

**Fazit**

Durch die Integration eines PIR-Sensors mit dem Raspberry Pi Pico 2 hast du die Fähigkeit zur Bewegungserkennung in deine Projekte eingebaut. Das Verständnis von Sensor-Eingaben und Interrupts ermöglicht es dir, effiziente und reaktionsschnelle Programme zu entwickeln.
