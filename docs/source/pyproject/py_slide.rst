.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_slide:

2.7 Umschalten nach Links und Rechts
========================================

In dieser Lektion lernen wir, wie man einen **Schiebeschalter** mit dem Raspberry Pi Pico 2 verwendet, um seine Position (links oder rechts) zu erkennen und entsprechende Aktionen auszuführen.  
Ein Schiebeschalter ist ein einfaches mechanisches Bauteil, das je nach Stellung den gemeinsamen Mittelkontakt mit einem der beiden äußeren Pins verbindet.

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
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Funktionsweise des Schiebeschalters**

|img_slide|

Ein Schiebeschalter hat drei Pins:

- **Pin 1**: Wird verbunden, wenn der Schalter in eine Richtung geschoben wird (z. B. links).
- **Pin 2**: Gemeinsamer Mittelkontakt.
- **Pin 3**: Wird verbunden, wenn der Schalter in die andere Richtung geschoben wird (z. B. rechts).

Durch das Messen der Spannung am Mittelpin kann die Position des Schalters bestimmt werden.

**Schaltplan**

|sch_slide|

GP14 erhält je nach Stellung des Schalters ein anderes Signal.

Der 10KΩ-Widerstand hält GP14 während des Umschaltens auf LOW, wenn sich der Schalter weder ganz links noch ganz rechts befindet.

Beim Umschalten kann es zu schnellen, unregelmäßigen Signalen („Prellen“) kommen.  
Der zwischen GP14 und GND geschaltete Kondensator reduziert diese Schwankungen und sorgt für ein stabileres Signal.

* Schalter nach rechts geschoben:

  * Pin 2 (GP14) wird über Pin 1 mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HIGH** (1).

* Schalter nach links geschoben:
  * Pin 2 (GP14) wird über Pin 3 mit **GND** verbunden.
  * Der GPIO-Pin liest **LOW** (0).

* Schalter in Mittelstellung:
  * Pin 2 (GP14) ist weder mit **3.3V** noch mit **GND** verbunden.
  * Der Pull-Down-Widerstand hält den GPIO-Pin auf **LOW** (0).
  * Der Kondensator reduziert Störsignale durch mechanische Bewegung.

**Verdrahtung**

|wiring_slide|  



**Code schreiben**

Wir schreiben ein MicroPython-Programm, das die Position des Schiebeschalters erkennt und eine entsprechende Meldung ausgibt.

.. note::

  * Öffne ``2.7_slide_switch.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.


  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

  import machine
  import utime

  # Initialisierung von GP14 als Eingang
  slide_switch = machine.Pin(14, machine.Pin.IN)

  while True:
      switch_state = slide_switch.value()
      if switch_state == 1:
          print("Switch is toggled to the LEFT!")
      else:
          print("Switch is toggled to the RIGHT!")
      utime.sleep(0.5)

Wenn der Code läuft, zeigt die Konsole folgende Meldungen an:

* **Schalter nach rechts geschoben** → „Schalter ist nach RECHTS geschoben!“
* **Schalter nach links geschoben** → „Schalter ist nach LINKS geschoben!“

**Den Code verstehen**

#. Module importieren:

   * ``import machine``: Zugriff auf Hardware-Funktionen.
   * ``import utime``: Nutzung von Zeitfunktionen.

#. Schiebeschalter-Pin initialisieren:

   * ``slide_switch = machine.Pin(14, machine.Pin.IN)``: Setzt GP14 als Eingabepin.

#. Hauptschleife:

   * ``while True``: Endlosschleife zur kontinuierlichen Überprüfung des Schalters.
   * ``switch_state = slide_switch.value()``: Liest den aktuellen Zustand des Schalters.
   * ``if switch_state == 1``: Falls der GPIO-Pin HIGH ist (Schalter nach links geschoben).
   * ``print("Switch is toggled to the RIGHT!")``: Gibt eine Meldung aus.
   * ``else``: Falls der GPIO-Pin LOW ist (Schalter nach rechts oder in Mittelstellung).
   * ``print("Switch is toggled to the LEFT!")``: Gibt eine Meldung aus.
   * ``utime.sleep(0.5)``: Fügt eine kurze Verzögerung zur Entprellung ein.


**Alternative: Interner Pull-Down-Widerstand**

Der Raspberry Pi Pico 2 ermöglicht die Aktivierung interner Pull-Down-Widerstände, wodurch der externe Widerstand überflüssig wird.

* Schaltung anpassen:

  Entferne den externen 10KΩ-Widerstand und den 0.1µF-Kondensator.

* Angepasster Code:

  .. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingang mit internem Pull-Down-Widerstand
    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        switch_state = slide_switch.value()
        if switch_state == 1:
            print("Switch is toggled to the LEFT!")
        else:
            print("Switch is toggled to the RIGHT!")
        utime.sleep(0.5)
  
**Praktische Anwendungen**

* **Modus-Umschaltung**: Der Schalter kann zur Auswahl zwischen verschiedenen Betriebsmodi verwendet werden.
* **Energieverwaltung**: Steuere die Stromversorgung für bestimmte Schaltungsteile.
* **Benutzereingabe**: Einfache Steuerung für interaktive Projekte.

**Erweiterungen**

* LED-Anzeige hinzufügen:

  Verbinde eine LED mit einem GPIO-Pin (z. B. GP15) und passe den Code so an, dass die LED je nach Schalterstellung leuchtet.

  .. code-block:: python

    import machine
    import utime

    slide_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if slide_switch.value() == 1:
            led.value(1)  # LED einschalten
        else:
            led.value(0)  # LED ausschalten
        utime.sleep(0.1)

* Mittlere Position erkennen: 

  Um zu erkennen, wenn sich der Schalter in der Mittelstellung befindet (weder links noch rechts), muss die Verdrahtung sowie der Code angepasst werden, um alle drei Zustände auszulesen.

**Fazit**

Die Verwendung eines Schiebeschalters mit dem Raspberry Pi Pico 2 ermöglicht es dir, physische Eingabesteuerungen in deine Projekte zu integrieren.  
Indem du lernst, den Zustand des Schalters korrekt auszulesen und mögliche Probleme wie das Prellen zu berücksichtigen, kannst du interaktive und benutzerfreundliche Anwendungen entwickeln.
