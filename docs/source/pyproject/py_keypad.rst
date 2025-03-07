.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_keypad:

4.2 Nutzung eines 4x4-Tastenfelds
=================================================

In dieser Lektion lernen wir, wie man ein **4x4 Matrix-Tastenfeld** mit dem Raspberry Pi Pico 2 verwendet, um zu erkennen, welche Tasten gedrückt werden. Matrix-Tastenfelder werden häufig in Geräten wie Taschenrechnern, Telefonen, Verkaufsautomaten und Sicherheitssystemen für die numerische Eingabe verwendet.

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

Sie können sie auch einzeln über die untenstehenden Links kaufen.


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
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Verständnis des 4x4-Tastenfelds**

Ein 4x4-Tastenfeld besteht aus:

* **16 Tasten**, angeordnet in 4 Reihen und 4 Spalten.
* **8 Pins**: 4 verbunden mit den Reihen und 4 mit den Spalten.

Wenn Sie eine Taste drücken, wird eine bestimmte Reihe und Spalte verbunden, was uns erlaubt, die Taste anhand der Reihen- und Spaltennummern zu identifizieren.

So sind die Tasten angeordnet:

|img_keypad|

**Schaltplan**

|sch_keypad|

4 Pull-Down-Widerstände sind mit jeder der Spalten des Matrix-Tastenfelds verbunden, sodass G6 bis G9 ein stabiles niedriges Niveau erhalten, wenn die Tasten nicht gedrückt sind.

Die Reihen des Tastenfelds (G2 bis G5) sind so programmiert, dass sie hoch gehen; wenn einer von G6 bis G9 hoch gelesen wird, wissen wir, welche Taste gedrückt ist.

Beispielsweise, wenn G6 hoch gelesen wird, dann wird die Zahlentaste 1 gedrückt; dies liegt daran, dass die Steuerpins der Zahlentaste 1 G2 und G6 sind, wenn Zahlentaste 1 gedrückt wird, werden G2 und G6 miteinander verbunden und G6 ist ebenfalls hoch.

**Verdrahtungsdiagramm**

|wiring_keypad|

**Code schreiben**

Lassen Sie uns ein MicroPython-Programm schreiben, um zu lesen, welche Taste gedrückt wird.

.. note::

    * Öffnen Sie die Datei ``4.2_4x4_keypad.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import time

    # Definieren Sie die Zeichen auf dem Tastenfeld
    keys = [
        ['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']
    ]

    # Definieren Sie die GPIO-Pins, die mit den Reihen und Spalten verbunden sind
    row_pins = [2, 3, 4, 5]   # GP2-GP5
    col_pins = [6, 7, 8, 9]   # GP6-GP9

    # Initialisieren Sie die Reihenpins als Ausgänge
    rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

    # Initialisieren Sie die Spaltenpins als Eingänge mit Pull-Down-Widerständen
    cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

    def scan_keypad():
        for i, row in enumerate(rows):
            # Setzen Sie alle Reihen auf niedrig
            for r in rows:
                r.value(0)
            # Setzen Sie die aktuelle Reihe auf hoch
            row.value(1)
            # Überprüfen Sie die Spalten auf ein hohes Signal
            for j, col in enumerate(cols):
                if col.value() == 1:
                    # Taste erkannt
                    return keys[i][j]
        return None

    last_key = None

    while True:
        key = scan_keypad()
        if key != last_key:
            if key is not None:
                print("Key pressed:", key)
            last_key = key
        time.sleep(0.1)

**Verständnis des Codes**

#. Definieren Sie Tastencharaktere

   Diese 2D-Liste repräsentiert das Layout des Tastenfelds, passend zur physischen Anordnung.

   .. code-block:: python

        keys = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ]


#. Initialisieren Sie die Pins:

   .. code-block:: python

        row_pins = [2, 3, 4, 5]   # GPIO-Pins für Reihen
        col_pins = [6, 7, 8, 9]   # GPIO-Pins für Spalten

        # Initialisieren Sie Reihen als Ausgänge
        rows = [machine.Pin(pin_num, machine.Pin.OUT) for pin_num in row_pins]

        # Initialisieren Sie Spalten als Eingänge mit Pull-Down-Widerständen
        cols = [machine.Pin(pin_num, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin_num in col_pins]

#. Definieren Sie die Tastenfeld-Scanfunktion:

    Die Funktion scannt jede Reihe, indem sie sie hoch setzt und prüft, ob eine Spalte hoch liest, was auf einen Tastendruck in dieser Reihe und Spalte hinweist.

   .. code-block:: python

        def scan_keypad():
            for i, row in enumerate(rows):
                # Setzen Sie alle Reihen auf niedrig
                for r in rows:
                    r.value(0)
                # Setzen Sie die aktuelle Reihe auf hoch
                row.value(1)
                # Überprüfen Sie die Spalten auf einen Tastendruck
                for j, col in enumerate(cols):
                    if col.value() == 1:
                        # Taste wird gedrückt
                        return keys[i][j]
            return None

#. Hauptschleife zum Erkennen von Tastendrücken

   * Die Schleife scannt kontinuierlich nach Tastendrücken.
   * Sie prüft, ob der aktuelle Schlüssel sich vom letzten unterscheidet, um mehrfache Erkennungen desselben Tastendrucks zu verhindern (Entprellung).
   * Druckt die Taste, wenn ein neuer Tastendruck erkannt wird.

   .. code-block:: python

        last_key = None

        while True:
            key = scan_keypad()
            if key != last_key:
                if key is not None:
                    print("Key pressed:", key)
                last_key = key
            time.sleep(0.1)

Nachdem Sie das Programm ausgeführt haben, drücken Sie verschiedene Tasten auf dem Tastenfeld. Der entsprechende Tastencharakter sollte in der Thonny Shell ausgegeben werden.

**Tipps zur Fehlerbehebung**

* Keine Ausgabe beim Drücken von Tasten:

  * Stellen Sie sicher, dass alle Verbindungen korrekt sind.
  * Überprüfen Sie, ob die Pull-Down-Widerstände richtig zwischen den Spaltenpins und GND angeschlossen sind.

* Falsche Taste erkannt:

  * Überprüfen Sie das Tastenarray, um sicherzustellen, dass es mit dem Layout Ihres Tastenfelds übereinstimmt.
  * Stellen Sie sicher, dass die Reihen- und Spaltenpins im Code mit den physischen Verbindungen übereinstimmen.

* Mehrere Tasten erkannt:

  Mechanische Tastenfelder können manchmal Ghosting (falsche Tastendrücke) erkennen, wenn mehrere Tasten gleichzeitig gedrückt werden. Vermeiden Sie es in diesem einfachen Setup, mehrere Tasten gleichzeitig zu drücken.

**Weiterführende Experimente**

* **Implementieren Sie ein einfaches Passwortschloss**: Speichern Sie eine Sequenz von Tastendrücken und vergleichen Sie diese mit einem voreingestellten Passwort.
* **Fügen Sie ein LCD-Display hinzu**: Zeigen Sie die gedrückten Tasten auf einem LCD-Bildschirm an.
* **Erstellen Sie einen Taschenrechner**: Verwenden Sie das Tastenfeld, um Zahlen einzugeben und grundlegende Rechenoperationen durchzuführen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man ein 4x4 Matrix-Tastenfeld mit dem Raspberry Pi Pico 2 verbindet und programmiert. Sie können jetzt Tastendrücke erkennen und diese nutzen, um mit Ihren Projekten zu interagieren, was Möglichkeiten für die Erstellung interaktiver Geräte wie Schlösser, Taschenrechner und Steuerungsschnittstellen eröffnet.
