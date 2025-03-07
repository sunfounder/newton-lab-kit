.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse After-Sales-Probleme und technische Herausforderungen mit Hilfe unserer Community und unserem Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bist du bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_photoresistor:

2.12 Fühle das Licht
=====================

In dieser Lektion lernen wir, wie man einen **Fotowiderstand** (auch bekannt als lichtabhängiger Widerstand oder LDR) mit dem Raspberry Pi Pico 2 verwendet, um die Lichtintensität zu messen. Ein Fotowiderstand ändert seinen Widerstand abhängig von der Menge des empfangenen Lichts: je heller das Licht, desto geringer der Widerstand. Dies macht ihn ideal für die Erkennung von Veränderungen im Umgebungslicht.

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

Du kannst sie auch separat über die untenstehenden Links kaufen.


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
        - Micro USB-Kabel
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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Schaltplan**

|sch_photoresistor|


In diesem Schaltkreis sind ein 10K-Widerstand und ein Fotowiderstand in Serie geschaltet, was einen Spannungsteiler bildet. GP28 liest die Spannung über den Fotowiderstand, während der 10K-Widerstand Schutz bietet, indem er den Strom begrenzt.

* **Helles Licht**: Der Widerstand des Fotowiderstands verringert sich, senkt seine Spannung und den GP28-Wert. Bei starkem Licht nähert sich sein Widerstand null, und GP28 liest nahezu 0. In dieser Zeit spielt der 10K-Widerstand eine schützende Rolle, damit 3,3 V und GND nicht zusammen verbunden werden, was zu einem Kurzschluss führen würde.
* **Dunkelheit**: Der Widerstand des Fotowiderstands erhöht sich, hebt seine Spannung und den GP28-Wert. In völliger Dunkelheit ist sein Widerstand nahezu unendlich (der 10K-Widerstand ist vernachlässigbar), und GP28 liest nahezu 65535.

Die Berechnungsformel wird unten gezeigt.

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535


**Verdrahtungsplan**

|wiring_photoresistor|

**Den Code schreiben**

Wir werden ein MicroPython-Programm schreiben, um den analogen Wert vom Fotowiderstand zu lesen und anzuzeigen.

.. note::

  * Öffne die Datei ``2.12_feel_the_light.py`` im Ordner ``newton-lab-kit/micropython`` oder kopiere den untenstehenden Code in Thonny. Dann klicke auf "Aktuelles Skript ausführen" oder drücke **F5**, um es zu starten.
  * Stelle sicher, dass der Interpreter "MicroPython (Raspberry Pi Pico).COMxx" in der unteren rechten Ecke von Thonny ausgewählt ist.
  * Für detaillierte Anweisungen siehe :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Initialisiere ADC auf GP28
    photoresistor = machine.ADC(28)

    while True:
        # Lies den analogen Wert (0-65535)
        light_value = photoresistor.read_u16()
        print("Light value:", light_value)
        utime.sleep(0.5)

Während der Code läuft, beobachte die in der Konsole ausgegebenen Werte.

* Bedecke den Fotowiderstand mit deiner Hand, um Dunkelheit zu simulieren; der Wert sollte zunehmen.
* Leuchte mit einer Lampe oder einer Taschenlampe auf den Fotowiderstand; der Wert sollte abnehmen.

**Verständnis des Codes**

#. Module importieren:

   * ``machine``: Bietet Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Ermöglicht die Nutzung von zeitbezogenen Funktionen wie Schlaf.

#. Initialisiere den ADC-Pin:

   * ``photoresistor = machine.ADC(28)``: Richtet GP28 als analogen Eingang ein, um Spannungspegel zu lesen.

#. Hauptschleife:

   ``while True``: Startet eine unendliche Schleife.
   ``light_value = photoresistor.read_u16()``: Liest den analogen Wert vom Fotowiderstand. Der Wert reicht von 0 (0V) bis 65535 (3.3V).
   ``print("Light value:", light_value)``: Gibt den Lichtwert in der Konsole aus.
   ``utime.sleep(0.5)``: Pausiert die Schleife für 0.5 Sekunden vor der nächsten Messung.


**Weiteres Experimentieren**

* Kalibrierung der Messwerte:

  Ordne die analogen Werte einem Prozentwert oder einer aussagekräftigeren Skala zu.

  .. code-block:: python
  
      import machine
      import utime
  
      photoresistor = machine.ADC(28)
  
      while True:
          light_value = photoresistor.read_u16()
          light_percentage = (light_value / 65535) * 100
          print("Light level: {:.2f}%".format(light_percentage))
          utime.sleep(0.5)

* Steuere eine LED basierend auf der Lichtintensität:

  Nutze den Lichtsensor, um eine LED im Dunkeln einzuschalten und bei hellem Licht auszuschalten.

  .. code-block:: python

    import machine
    import utime

    photoresistor = machine.ADC(28)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        light_value = photoresistor.read_u16()
        if light_value > 50000:
            led.value(1)  # LED im Dunkeln einschalten
        else:
            led.value(0)  # LED bei hellem Licht ausschalten
        utime.sleep(0.5)

* Erstelle einen lichtaktivierten Alarm oder eine Benachrichtigung: Löse eine Aktion aus, wenn sich die Lichtpegel deutlich ändern.

**Schlussfolgerung**

Durch die Verwendung eines Fotowiderstands mit dem Raspberry Pi Pico 2 hast du gelernt, wie man analoge Eingänge liest und auf Änderungen in der Umgebungsbeleuchtung reagiert. Dieses Wissen kann auf verschiedene Projekte angewendet werden, wie automatische Beleuchtungssysteme, lichtfolgende Roboter oder Sicherheitsgeräte, die auf Lichtänderungen reagieren.


