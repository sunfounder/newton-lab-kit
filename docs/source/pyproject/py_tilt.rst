.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_tilt:

2.6 Neigungssensor nutzen
===========================

In dieser Lektion lernen wir, wie man einen Neigungsschalter mit dem Raspberry Pi Pico 2 verwendet, um Änderungen in der Ausrichtung zu erkennen. Ein Neigungsschalter ist ein einfaches Bauteil, das erkennen kann, ob es aufrecht oder geneigt ist. Er wird häufig für Bewegungsmelder, Orientierungssensoren oder als Auslöser basierend auf der Position eingesetzt.

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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_tilt|

* **Aufrecht (Schalter geschlossen)**:

  * Der Neigungsschalter verbindet **3.3V** direkt mit **GP14**.
  * Die GPIO-Pin liest **HIGH** (1).

* **Geneigt (Schalter offen)**:

  * Der Neigungsschalter trennt **3.3V** von **GP14**.
  * Der Pull-Down-Widerstand zieht **GP14** auf **GND**.
  * Die GPIO-Pin liest **LOW** (0).

**Verdrahtung**

|wiring_tilt|

**Code schreiben**

Wir schreiben ein einfaches MicroPython-Programm, das den Zustand des Neigungsschalters erkennt und eine Meldung ausgibt, wenn der Schalter gekippt wird.

.. note::

    * Öffne ``2.6_tilt_switch.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingabepin
    tilt_switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if tilt_switch.value() == 0:
            print("Tilt detected!")
            utime.sleep(1)  # Verzögerung zur Vermeidung mehrfacher Erkennungen

Wenn der Code läuft, beobachte folgendes Verhalten:

* Wenn der Neigungsschalter aufrecht steht, wird keine Meldung ausgegeben.
* Wenn das Steckbrett oder der Schalter geneigt wird, erscheint die Meldung "Neigung erkannt!" in der Konsole.

**Den Code verstehen**

#. Module importieren:

   * ``import machine``: Ermöglicht den Zugriff auf Hardwarekomponenten.
   * ``import utime``: Erlaubt die Nutzung zeitbezogener Funktionen.

#. Den Neigungsschalter initialisieren:

   * ``tilt_switch = machine.Pin(14, machine.Pin.IN)``: Setzt GP14 als Eingabepin.

#. Hauptschleife:

   * ``while True``: Erstellt eine Endlosschleife zur kontinuierlichen Überprüfung des Neigungsschalters.
   * ``if tilt_switch.value() == 0``: Prüft, ob der GPIO-Pin LOW (0) liest, was bedeutet, dass der Schalter geneigt ist.
   * ``print("Neigung erkannt!")``: Gibt eine Meldung aus, wenn die Neigung erkannt wird.
   * ``utime.sleep(1)``: Fügt eine 1-Sekunden-Verzögerung hinzu, um Mehrfacherkennungen zu vermeiden.

**Alternative Verdrahtung: Interner Pull-Down-Widerstand**

Der Raspberry Pi Pico 2 erlaubt die Aktivierung interner Pull-Up- oder Pull-Down-Widerstände, wodurch kein externer Widerstand benötigt wird.

.. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingabepin mit internem Pull-Down-Widerstand
    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            utime.sleep(1)

Durch Aktivieren des internen Pull-Down-Widerstands (``machine.Pin.PULL_DOWN``) wird der GPIO-Pin standardmäßig auf LOW gesetzt, wenn keine Spannung anliegt.  
Wenn der Neigungsschalter aufrecht (geschlossen) ist, verbindet er 3.3V mit GP14, wodurch der Pin HIGH (1) liest.

**Praktische Anwendungen**

* **Orientierungserkennung**: Bestimme, ob ein Gerät aufrecht oder geneigt ist.
* **Bewegungsgesteuerte Ereignisse**: Aktiviere Alarme, Benachrichtigungen oder Aktionen bei Bewegung.
* **Interaktive Projekte**: Nutze den Neigungsschalter als Steuerung für Spiele oder interaktive Installationen.

**Weitere Experimente**

* LED als Indikator hinzufügen:

Verbinde eine LED mit einem anderen GPIO-Pin (z. B. GP15) und passe den Code an, um die LED zu aktivieren, wenn eine Neigung erkannt wird.

.. code-block:: python

    import machine
    import utime

    tilt_switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if tilt_switch.value() == 1:
            print("Tilt detected!")
            led.value(1)  # Schalte die LED ein
            utime.sleep(1)
        else:
            led.value(0)  # Schalte die LED aus

* Mit anderen Sensoren kombinieren:

  Kombiniere den Neigungsschalter mit anderen Sensoren wie Tastern oder Lichtsensoren für komplexere Interaktionen.

**Fazit**

Durch den Einsatz eines Neigungsschalters in deinen Raspberry Pi Pico 2-Projekten kannst du eine neue Dimension der Interaktivität durch Positions- und Bewegungserkennung hinzufügen.  
Das Verständnis, wie digitale Eingaben von Sensoren wie dem Neigungsschalter verarbeitet werden, erweitert deine Möglichkeiten zur Entwicklung dynamischer und reaktionsfähiger Elektronikprojekte.
