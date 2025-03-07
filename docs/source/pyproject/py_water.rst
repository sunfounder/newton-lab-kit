.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_water:

2.14 Wasserstandserkennung
=============================

In dieser Lektion lernen wir, wie man einen **Wassersensor** mit dem Raspberry Pi Pico 2 verwendet, um das Vorhandensein von Wasser zu erkennen oder den Wasserstand zu messen. Dieser Sensor wird häufig in Projekten zur Niederschlagserkennung, Wasserstandsüberwachung und Flüssigkeitsleckagen eingesetzt.

**Funktionsweise des Wassersensors**

Der Wassersensor verfügt über eine Reihe offener, paralleler Leiterbahnen, die Wassertröpfchen erkennen oder das Wasservolumen messen. Sobald Wasser mit diesen Leiterbahnen in Kontakt kommt, gibt der Sensor ein analoges Signal aus. Je mehr Wasser den Sensor berührt, desto höher ist der ausgegebene Wert, der vom Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 ausgelesen werden kann.

|img_water_sensor|

* Tauche den Sensor nicht vollständig ins Wasser ein. Nur der Bereich mit den offenen Leiterbahnen sollte mit Wasser in Berührung kommen.
* Die Nutzung des Sensors in feuchten Umgebungen kann zu schnellerer Korrosion der Sonde führen. Es wird daher empfohlen, den Sensor nur während der Messung mit Strom zu versorgen.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Es ist praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

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
        - :ref:`cpn_water_level`
        - 1
        - 


**Schaltplan**

|sch_water|


**Verdrahtungsdiagramm**


|wiring_water|

**Code schreiben**


Wir schreiben ein einfaches MicroPython-Programm, um den analogen Wert des Wassersensors auszulesen und ihn auf der Konsole anzuzeigen. Je weiter der Sensor ins Wasser eingetaucht wird, desto höher wird der ausgelesene Wert von GP28.

.. note::

    * Öffne ``2.14_feel_the_water_level.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny und klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Initialisiere ADC auf GP28
    sensor = machine.ADC(28)

    while True:
        # Lese den analogen Wert des Sensors aus
        value = sensor.read_u16()
        print("Water level reading:", value)
        utime.sleep(0.2)  # Verzögerung zur Vermeidung einer überfluteten Konsole


Wenn der Code ausgeführt wird, tauche den Wassersensor langsam ins Wasser und beobachte die auf der Konsole angezeigten Werte. Je mehr Wasser der Sensor erkennt, desto höher wird der ausgegebene Wert.

**Erweiterung: Nutzung des Sensors zur Leckerkennung**

Der Wassersensor kann auch zur Erkennung von Flüssigkeitsleckagen verwendet werden, indem er als digitaler Sensor fungiert:

#. Bestimmung des Basiswerts:

   * Nimm zuerst eine Messung mit dem Wassersensor in einer komplett trockenen Umgebung vor. Dieser Wert dient als Schwellenwert.
   * Falls der Sensor später einen höheren Wert als diesen Basiswert ausgibt, deutet dies auf den Kontakt mit Wasser hin, was auf eine mögliche Leckage hindeutet.

#. Code zur Leckerkennung:

   In diesem Beispiel prüfen wir, ob der gemessene Wert den festgelegten Schwellenwert überschreitet.

   .. code-block:: python

      import machine
      import utime
  
      # Initialisiere ADC auf GP28
      sensor = machine.ADC(28)
  
      # Setze einen Schwellenwert basierend auf den Messwerten im Trockenzustand (bei Bedarf anpassen)
      threshold = 30000
  
      while True:
          # Lese den analogen Wert des Sensors aus
          value = sensor.read_u16()
          
          # Prüfe, ob der Wert den Schwellenwert überschreitet, was auf Wasser hinweist
          if value > threshold:
              print("Liquid leakage detected!")
          
          utime.sleep(0.2)  # Verzögerung zur besseren Lesbarkeit
    

   Das Programm überprüft, ob der Sensorwert den festgelegten Schwellenwert übersteigt. Falls ja, gibt es eine Meldung aus, die auf Wasser oder eine Leckage hinweist.

**Anwendungsfälle**

* **Leckage-Erkennung**: Platziere den Sensor in der Nähe von Wasserleitungen, um Lecks frühzeitig zu erkennen.
* **Wasserstandsmessung**: Verwende den Sensor in Tanks oder Behältern, um den Wasserstand zu überwachen und bei Bedarf Alarme oder Aktionen auszulösen.
* **Regenmessung**: Installiere den Sensor im Freien (mit geeignetem Schutz), um Regenfälle zu detektieren.

**Fazit**

Der Wassersensor ist ein einfaches, aber effektives Werkzeug zur Messung von Wasserständen oder zur Erkennung von Flüssigkeitsleckagen. In Kombination mit dem Raspberry Pi Pico 2 lassen sich vielseitige und nützliche Wassererkennungssysteme für verschiedene Anwendungen realisieren.
