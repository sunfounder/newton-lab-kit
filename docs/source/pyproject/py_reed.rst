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

.. _py_reed:

2.9 Magnetismus spüren
===============================

In dieser Lektion erforschen wir, wie ein **Reed-Schalter** mit dem Raspberry Pi Pico 2 verwendet wird, um ein Magnetfeld zu erkennen.  
Ein Reed-Schalter ist ein einfacher elektrischer Schalter, der durch ein Magnetfeld aktiviert wird.  
Wenn ein Magnet in die Nähe des Schalters kommt, schließen sich die internen Kontakte und vervollständigen den Stromkreis.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 

**Funktionsweise des Reed-Schalters**

Ein Reed-Schalter besteht aus zwei dünnen Metallzungen, die in einer Glasröhre eingeschlossen sind. Diese Zungen bestehen aus ferromagnetischem Material und sind leicht voneinander getrennt. Ohne Magnetfeld bleiben sie getrennt, und der Schalter ist **offen**. Kommt ein Magnet in die Nähe, magnetisieren sich die Zungen, ziehen sich gegenseitig an und schließen den Stromkreis.

* **Kein Magnet in der Nähe**: Schalter ist **offen**; der Stromkreis ist unterbrochen.
* **Magnet in der Nähe**: Schalter ist **geschlossen**; der Stromkreis ist verbunden.

|img_reed_sche|

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 auf LOW und wird HIGH, wenn sich ein Magnet in der Nähe des Reed-Schalters befindet.

Der 10K-Widerstand dient dazu, GP14 auf einem stabilen niedrigen Pegel zu halten, wenn sich kein Magnet in der Nähe befindet.

* **Kein Magnet in der Nähe**:

  * Der Reed-Schalter ist **offen**.
  * **GP14** ist über den Pull-down-Widerstand mit **GND** verbunden.
  * Der GPIO-Pin liest **LOW** (0).

* **Magnet in der Nähe**:

  * Der Reed-Schalter ist **geschlossen**.
  * **GP14** ist über den Reed-Schalter mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HIGH** (1).

**Verdrahtungsdiagramm**

|wiring_reed|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, das erkennt, wenn sich ein Magnet in der Nähe des Reed-Schalters befindet, und eine entsprechende Nachricht ausgibt.

.. note::

  * Öffne die Datei ``2.9_feel_the_magnetism.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf „Run“ oder drücke F5.
  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialisierung von GP14 als Eingangs-Pin
    reed_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if reed_switch.value() == 1:
            print("Magnet detected!")
            utime.sleep(1)  # Verzögerung, um Mehrfacherkennungen zu vermeiden

Wenn der Code ausgeführt wird, kannst du Folgendes beobachten:

* **Kein Magnet in der Nähe**: Es erscheint keine Meldung.
* **Magnet annähern**: „"Magnet detected!"“ erscheint in der Konsole.
* **Magnet entfernen**: Die Meldung wird nicht mehr angezeigt.

**Verständnis des Codes** 

#. Importiere Module:

   * ``import machine``: Zugriff auf Hardwarefunktionen.
   * ``import utime``: Zeitbezogene Funktionen.

#. Initialisiere den Reed-Schalter-Pin:

   * ``reed_switch = machine.Pin(14, machine.Pin.IN)``: Setzt GP14 als Eingangs-Pin.

#. Hauptschleife:

   * ``while True``: Startet eine Endlosschleife.
   * ``if reed_switch.value() == 1``: Prüft, ob sich ein Magnet in der Nähe befindet (GPIO-Pin liest HIGH).
   * ``print("Magnet detected!")``: Gibt eine Nachricht aus.
   * ``utime.sleep(1)``: Fügt eine Verzögerung hinzu, um wiederholte Meldungen zu vermeiden.

**Verwendung von Interrupts für eine effiziente Erkennung**

Anstatt den Reed-Schalter ständig in einer Schleife abzufragen, können wir einen Interrupt verwenden, um Änderungen des Schalterzustands effizienter zu erkennen.

Die Verwendung von Interrupts verbessert die Effizienz, indem sie die Notwendigkeit der kontinuierlichen Überprüfung des Reed-Schalters eliminiert und sofort die Handler-Funktion aufruft, wenn das Ereignis eintritt.

Modifizierter Code mit Interrupts: Wenn sich ein Magnet dem Reed-Schalter nähert, erscheint „Magnet erkannt!“. Das Hauptprogramm bleibt frei für andere Aufgaben.

.. code-block:: python

    import machine

    # Initialisiere GP14 als Eingangs-Pin mit internem Pull-down-Widerstand
    reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def magnet_detected(pin):
        print("Magnet detected!")

    # Richte einen Interrupt für die steigende Flanke (LOW zu HIGH) ein
    reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)

* ``def magnet_detected(pin)``: Diese Funktion wird automatisch aufgerufen, wenn der Interrupt ausgelöst wird.
    
  * ``print("Magnet detected!")``: Gibt eine Meldung aus, wenn ein Magnet erkannt wird.

* ``reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)``: Konfiguriert einen Interrupt für den Reed-Schalter-Pin.
     
  * ``trigger=machine.Pin.IRQ_RISING``: Der Interrupt wird ausgelöst, wenn der Pin von LOW auf HIGH wechselt.
  * ``handler=magnet_detected``: Gibt die Funktion an, die beim Interrupt ausgelöst wird.

**Praktische Anwendungen**

* **Sicherheitssysteme**: Erkennen, wenn eine Tür oder ein Fenster geöffnet wird.
* **Positionssensoren**: Bestimmen der Position beweglicher Maschinenteile.
* **Näherungserkennung**: Ereignisse auslösen, wenn sich ein magnetisches Objekt nähert.

**Weitere Experimente**

* Steuerung einer LED:

  Schließe eine LED an einen anderen GPIO-Pin (z. B. GP15) mit einem geeigneten Widerstand an.  
  Ändere den Interrupt-Handler so, dass die LED eingeschaltet wird, wenn ein Magnet erkannt wird.
  
  .. code-block:: python
  
      import machine
  
      reed_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      led = machine.Pin(15, machine.Pin.OUT)
  
      def magnet_detected(pin):
          led.value(1)  # LED einschalten
  
      # Interrupt für steigende Flanke setzen
      reed_switch.irq(trigger=machine.Pin.IRQ_RISING, handler=magnet_detected)
  
      # Hauptschleife
      while True:
          # LED ausschalten, wenn kein Magnet in der Nähe ist
          if reed_switch.value() == 0:
              led.value(0)
          machine.sleep(100)
        
* Erkennung der Magnetentfernung:

  Richte einen weiteren Interrupt für die fallende Flanke ein (wenn der Magnet entfernt wird).

  .. code-block:: python

    def magnet_removed(pin):
        print("Magnet removed!")

    reed_switch.irq(trigger=machine.Pin.IRQ_FALLING, handler=magnet_removed)

**Fazit**

Die Verwendung eines Reed-Schalters mit dem Raspberry Pi Pico 2 ermöglicht die Erkennung von Magnetfeldern und eröffnet vielfältige Einsatzmöglichkeiten – von Sicherheitssystemen bis hin zu interaktiven Projekten. Das Verständnis der Verdrahtung und der Nutzung von Interrupts verbessert die Effizienz und Reaktionsfähigkeit deiner Programme.

**Referenzen**

* |link_mpython_irq|