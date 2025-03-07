.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook!  
    Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_pump:


3.6 Steuerung einer Wasserpumpe
==================================

In dieser Lektion lernen wir, wie eine **kleine Wasserpumpe** mithilfe des Raspberry Pi Pico 2 und eines **L293D-Motortreibers** gesteuert wird. Eine kleine Kreiselpumpe kann in Projekten wie automatischen Bewässerungssystemen für Pflanzen oder Miniatur-Wasserfontänen eingesetzt werden. Die Steuerung der Pumpe funktioniert nach den gleichen Prinzipien wie die Steuerung eines Gleichstrommotors.

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 7
        - 9V-Batterie
        - 1
        -  
    *   - 8
        - :ref:`cpn_pump`
        - 1
        -  

**Wichtige Hinweise vor dem Start**

* **Pumpen-Setup**: Schließe den Schlauch an den Pumpenausgang an und tauche die Pumpe in Wasser, bevor sie eingeschaltet wird.
* **Trockenlauf vermeiden**: Die Pumpe sollte stets in Wasser eingetaucht sein. Ein Trockenlauf kann den Motor überhitzen und beschädigen.
* **Verstopfungen vermeiden**: Falls die Pumpe zur Bewässerung von Pflanzen eingesetzt wird, sollte das Wasser frei von Schmutzpartikeln sein.
* **Pumpe entlüften**: Falls kein Wasser fließt, befindet sich möglicherweise Luft im Schlauch. Lasse Wasser durch die Pumpe laufen, um Luftblasen zu entfernen.

**Schaltplan**

|sch_pump|

Der L293D ist ein Motortreiber-Chip. EN ist mit 5V verbunden, um den L293D zu aktivieren. 1A und 2A sind die Eingänge und mit GP15 bzw. GP14 verbunden; 1Y und 2Y sind die Ausgänge und steuern die beiden Anschlüsse der Pumpe.

Y (Ausgang) entspricht A (Eingang), sodass sich die Drehrichtung der Pumpe ändern lässt, wenn GP15 und GP14 verschiedene Pegel erhalten.


**Verdrahtung**

|wiring_pump|

In dieser Schaltung ist der Taster mit dem **RUN**-Pin des Pico verbunden. Grund dafür ist, dass die Pumpe einen hohen Strom benötigt, was dazu führen kann, dass der Pico die Verbindung zum Computer verliert. Der Taster muss gedrückt werden, damit der **RUN**-Pin des Pico auf LOW gesetzt wird und ein Reset erfolgt.


**Code schreiben**

Das folgende MicroPython-Programm startet die Pumpe, sodass sie nach dem Start kontinuierlich läuft.

.. note::

    * Öffne ``3.6_pumping.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny und klicke auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Steuerpins für den L293D definieren
    pump_in1 = machine.Pin(14, machine.Pin.OUT)
    pump_in2 = machine.Pin(15, machine.Pin.OUT)

    # Pumpe starten (IN1 HIGH, IN2 LOW)
    pump_in1.high()
    pump_in2.low()

    # Die Pumpe dauerhaft laufen lassen
    while True:
        utime.sleep(1)

Sobald das Programm läuft, sollte die Pumpe starten und Wasser durch den Schlauch befördern.

**Code verstehen**

#. Module importieren:

   * ``machine``: Zugriff auf Hardwarefunktionen.
   * ``utime``: Zeitbezogene Funktionen für Verzögerungen.

#. Steuerpins initialisieren:

   ``pump_in1`` und ``pump_in2`` steuern die Pumpe über den L293D.

   .. code-block:: python

      pump_in1 = machine.Pin(14, machine.Pin.OUT)
      pump_in2 = machine.Pin(15, machine.Pin.OUT)

#. Pumpe starten:

   Durch HIGH an IN1 und LOW an IN2 wird die Pumpe eingeschaltet.

   .. code-block:: python

      pump_in1.high()
      pump_in2.low()

#. Pumpe dauerhaft laufen lassen:

   Eine Endlosschleife hält das Programm aktiv.

   .. code-block:: python

      while True:
          utime.sleep(1)


**Fehlersuche**

* Pumpe startet nicht:

  * Überprüfe alle Verbindungen.
  * Stelle sicher, dass das Netzteil auf 5V eingestellt und eingeschaltet ist.
  * Stelle sicher, dass die Pumpe im Wasser eingetaucht ist.

* Pico reagiert nicht mehr:

  * Falls der Pico die Verbindung verliert oder das Programm stoppt, kann ein Reset erforderlich sein.
  * Verwende die Reset-Schaltung, indem du den RUN-Pin kurzzeitig mit GND verbindest.

* Pumpe läuft weiter nach dem Stoppen des Skripts:
  * Die letzte GPIO-Pin-Konfiguration bleibt auch nach Beendigung des Skripts bestehen.
  * Führe einen Reset durch, indem du RUN mit GND verbindest.

  |wiring_run_reset|

**Sicherheitsmaßnahmen**

* Elektrische Sicherheit:

  * Sei vorsichtig beim Arbeiten mit Wasser und Elektronik.
  * Halte den Pico und andere elektronische Komponenten von Wasser fern, um Schäden oder Verletzungen zu vermeiden.

* Pflege der Pumpe:

  * Die Pumpe darf nicht trocken laufen.
  * Falls das Wasser Partikel enthält, sollte die Pumpe regelmäßig gereinigt werden.

**Fazit**

In dieser Lektion hast du gelernt, wie eine kleine Wasserpumpe mit dem Raspberry Pi Pico 2 und einem L293D-Motortreiber gesteuert werden kann. Diese Technik kann als Grundlage für Projekte wie automatische Bewässerungssysteme oder Miniatur-Wasserbrunnen dienen.
