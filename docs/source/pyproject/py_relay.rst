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

.. _py_relay:

2.16 Steuerung eines anderen Stromkreises mit einem Relais
==============================================================

In dieser Lektion lernen wir, wie man mit einem **Relais** und dem Raspberry Pi Pico 2 einen anderen Stromkreis steuert.  
Ein Relais fungiert als Schalter, der von einem Niederspannungskreis (wie dem Pico) gesteuert wird, um einen Hochspannungskreis zu schalten.  
Zum Beispiel kannst du mit einem Relais eine Lampe oder ein anderes Gerät ein- und ausschalten, wodurch sich elektrische Haushaltsgeräte automatisieren lassen.

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
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 7
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|

**Schaltplan**

|sch_relay_1|

* Relais-Aktivierung:

  * Die Relaisspule wird über den Transistor aktiviert, wenn der Pico an GP15 ein **hohes Signal** (3,3V) ausgibt.
  * Der Transistor ermöglicht den Stromfluss durch das Relais und schaltet den internen Schalter.
  * Beim Umschalten gibt das Relais ein hörbares "Klick" von sich, das anzeigt, dass der Laststromkreis gesteuert wird.

* Freilaufdiode:

  * Die Diode wird parallel zur Relaisspule platziert, um den Transistor vor Spannungsspitzen zu schützen, die beim Abschalten des Relais entstehen.

**Verdrahtungsdiagramm**

|wiring_relay_1|

**Code schreiben**

Das folgende Skript steuert das Relais und schaltet den angeschlossenen Stromkreis alle zwei Sekunden ein und aus.

.. note::

    * Öffne die Datei ``2.16_control_another_circuit.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialisierung des Relais an GP15
    relay = machine.Pin(15, machine.Pin.OUT)

    while True:
        relay.value(1)  # Relais einschalten
        utime.sleep(2)  # 2 Sekunden warten
        relay.value(0)  # Relais ausschalten
        utime.sleep(2)  # 2 Sekunden warten

Wenn der Code ausgeführt wird, solltest du alle zwei Sekunden ein "Klick"-Geräusch vom Relais hören, das anzeigt, dass der Stromkreis ein- und ausgeschaltet wird.

**Weitere Experimente**

* **Timer setzen**: Ändere den Code so, dass das Relais für 10 Minuten eingeschaltet bleibt und sich dann automatisch ausschaltet.
* **Steuerung von Haushaltsgeräten**: Mit entsprechender Vorsicht kannst du Hochspannungsgeräte an das Relais anschließen, um Automatisierungsaufgaben wie das Ein- und Ausschalten von Lampen oder Ventilatoren zu realisieren.

  * Der Schaltkreis könnte folgendermaßen aussehen: Um die sichere Steuerung eines externen Stromkreises zu demonstrieren, fügen wir eine externe 5V-Stromversorgung (über ein Breadboard-Netzteil) hinzu, um eine LED zu betreiben. Dies simuliert, wie du mit einem Relais Hochspannungsgeräte (z. B. Haushaltsgeräte) steuern kannst. So kannst du den Schaltkreis anpassen:

    |sch_relay_2|
  
    |wiring_relay_2|

  * Code zur Steuerung des Relais:

    .. code-block:: python

        import machine
        import utime

        # Initialisierung des Relais an GP15
        relay = machine.Pin(15, machine.Pin.OUT)

        while True:
            relay.value(1)  # Relais einschalten
            utime.sleep(2)  # 2 Sekunden warten
            relay.value(0)  # Relais ausschalten
            utime.sleep(2)  # 2 Sekunden warten

    Wenn das Relais aktiviert wird (GP15 gibt HIGH aus), verbinden sich die "Normally Open" (NO) und "Common" (C) Pins des Relais. Dadurch kann der externe 5V-Strom durch die LED fließen und sie leuchtet auf – das simuliert, wie ein Relais ein externes Gerät steuern kann.

    Wenn das Relais deaktiviert wird (GP15 gibt LOW aus), trennen sich die NO- und C-Pins wieder, der externe Stromfluss wird unterbrochen und die LED erlischt.

**Sicherheitsüberlegungen bei der Steuerung realer Haushaltsgeräte**

Dieses Beispiel verwendet eine LED und eine 5V-Stromquelle zur Demonstration der Relaissteuerung. Falls du Hochspannungsgeräte steuern möchtest, beachte folgende Sicherheitsrichtlinien:

* **Passende Spannungswerte**: Verwende ein Relais mit einer für dein Gerät geeigneten Spannungs- und Stromstärke.
* **Isolation**: Stelle sicher, dass der Niederspannungskreis (Pico) und der Hochspannungskreis des Geräts elektrisch voneinander getrennt sind.
* **Sicherungsschutz**: Verwende Sicherungen oder Schutzschalter gegen Kurzschlüsse oder Überlastungen.
* **Fachkundige Beratung**: Beim Arbeiten mit Hochspannung immer professionelle Unterstützung einholen, um sichere Bedienung zu gewährleisten.

Dieses Projekt kann als Grundlage für Heimautomatisierung dienen, z. B. zur Steuerung von Lampen, Ventilatoren oder anderen Geräten, basierend auf Timern oder Sensoren, die mit dem Raspberry Pi Pico 2 verbunden sind.

**Verwendung des NC-Terminals**

* Wenn du deinen gesteuerten Stromkreis zwischen COM und NC anschließt:

  * Der Stromkreis ist geschlossen (EIN), wenn das Relais nicht aktiviert ist.
  * Der Stromkreis ist geöffnet (AUS), wenn das Relais aktiviert ist.
  * Beispiel: Steuerung eines externen Geräts.
  * Warnung: Versuche nicht, Hochspannungsgeräte ohne ausreichendes Wissen und entsprechende Sicherheitsmaßnahmen zu steuern.

* Falls du einen kleinen Gleichstrommotor oder ein anderes Gerät steuern möchtest:

  * Ersetze die LED durch das Gerät, das du steuern möchtest.
  * Stelle sicher, dass die Spannungs- und Stromanforderungen des Geräts kompatibel sind.
  * Verwende eine geeignete Stromversorgung für das Gerät.
  * Schließe das Gerät in Reihe mit den COM- und NO- (oder NC-)Anschlüssen des Relais.

**Fazit**

Durch die Verwendung eines Relais zur Steuerung eines externen Stromkreises hast du gelernt, wie man Geräte ein- und ausschaltet, von LEDs bis hin zu Hochspannungsgeräten. Dies eröffnet Möglichkeiten für automatisierte Steuerungssysteme, die per Code gesteuert werden – eine wichtige Grundlage für Heimautomatisierung und viele weitere Projekte.

