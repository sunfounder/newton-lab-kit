.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in Raspberry Pi, Arduino und ESP32 ein mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_irremote:


6.4 Verwendung einer Infrarot-Fernbedienung
==========================================================

In dieser Lektion lernen wir, wie man eine **Infrarot (IR) Fernbedienung** und ein **IR-Empfängermodul** mit dem Raspberry Pi Pico 2 verwendet. Dies ermöglicht es uns, Signale von einer IR-Fernbedienung zu empfangen und zu dekodieren, um unsere Projekte drahtlos zu steuern.

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Verständnis der Infrarot-Kommunikation**

Die Infrarot-Kommunikation beinhaltet die drahtlose Übertragung von Daten mittels Infrarotlicht. Allgemeine Haushaltsgeräte wie Fernseher und DVD-Player verwenden IR-Fernbedienungen zur Bedienung.

* **IR-Sender (Fernbedienung):** Sendet moduliertes Infrarotlicht, wenn eine Taste gedrückt wird.
* **IR-Empfängermodul:** Erkennt das modulierte IR-Licht und wandelt es in elektrische Signale um, die dekodiert werden können.

**Schaltplan**

|sch_irrecv|

**Verdrahtungsplan**

|wiring_irrecv|

**Code schreiben**

Schreiben wir ein MicroPython-Skript, um IR-Signale von der Fernbedienung zu empfangen und zu dekodieren.

.. note::

    * Öffnen Sie die Datei ``6.4_ir_remote_control.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier müssen Sie die Bibliotheken im Ordner ``ir_rx`` verwenden, bitte prüfen Sie, ob sie auf den Pico hochgeladen wurden, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

.. code-block:: python

    import time
    from machine import Pin
    from ir_rx.nec import NEC_8  # Passen Sie dies an das Protokoll Ihrer Fernbedienung an
    from ir_rx.print_error import print_error

    # Initialisieren Sie den IR-Empfänger-Pin
    ir_pin = Pin(17, Pin.IN)

    # Callback-Funktion zur Behandlung der empfangenen Daten
    def ir_callback(data, addr, ctrl):
        if data < 0:  # Wiederholungscode oder Fehler
            pass
        else:
            key = decode_key(data)
            print("Received Key:", key)

    # Funktion zum Dekodieren der empfangenen Daten in Tastendrücke
    def decode_key(data):
        key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Fügen Sie weitere Tastencodes basierend auf Ihrer Fernbedienung hinzu
        }
        return key_codes.get(data, "UNKNOWN")

    # Instanziieren Sie den IR-Empfänger
    ir = NEC_8(ir_pin, ir_callback)
    ir.error_function(print_error)  # Optional: um Fehler auszudrucken

    try:
        while True:
            time.sleep(1)  # Halten Sie den Hauptthread am Leben
    except KeyboardInterrupt:
        ir.close()
        print("Program terminated")

Wenn Sie diesen Code ausführen und Tasten auf Ihrer Infrarot-Fernbedienung drücken, zeigt die Thonny Shell (oder ein anderer serieller Monitor) den Namen der Taste an, die Sie gedrückt haben. Zum Beispiel, wenn Sie die "PLAY"-Taste auf der Fernbedienung drücken, zeigt die Shell "Empfangener Schlüssel: PLAY" an.

**Verständnis des Codes**

#. Import-Module:

   * ``ir_rx.nec.NEC_8``: Der NEC-Protokolldekoder für 8-Bit-Adressen.
   * ``print_error``: Funktion zum Ausdrucken von Fehlermeldungen.

   .. code-block:: python

        import time
        from machine import Pin
        from ir_rx.nec import NEC_8
        from ir_rx.print_error import print_error

#. Initialisieren Sie den IR-Empfänger-Pin:

   .. code-block:: python

        ir_pin = Pin(17, Pin.IN)

#. Definieren Sie die Callback-Funktion:

   Diese Funktion wird automatisch aufgerufen, wenn Daten empfangen werden. Der Datenparameter enthält den Tastencode.

   .. code-block:: python

        def ir_callback(data, addr, ctrl):
            if data < 0:
                pass  # Ignorieren Sie Wiederholungscodes
            else:
                key = decode_key(data)
                print("Received Key:", key)

#. Dekodieren Sie die Funktionstaste:

   Ordnet empfangene Tastencodes menschenlesbaren Beschriftungen zu.

   .. code-block:: python

        def decode_key(data):
            key_codes = {
            0x45: "POWER",
            0x46: "MODE",
            0x47: "MUTE",
            0x44: "PLAY/PAUSE",
            0x40: "BACKWARD",
            0x43: "FORWARD",
            0x07: "EQ",
            0x15: "-",
            0x09: "+",
            0xD: "U/SD",
            0x16: "0",
            0x19: "cycle",
            0xC: "1",
            0x5E: "3",
            0x18: "2",
            0x8: "4",
            0x1C: "5",
            0x5A: "6",
            0x42: "7",
            0x52: "8",
            0x4A: "9",
            0x0: "ERROR",
            # Fügen Sie weitere Tastencodes basierend auf Ihrer Fernbedienung hinzu
            }
            return key_codes.get(data, "UNKNOWN")

#. Instanziieren Sie den IR-Empfänger:

   Richtet den IR-Empfänger mit der Callback-Funktion ein.

   .. code-block:: python

        ir = NEC_8(ir_pin, ir_callback)
        ir.error_function(print_error)


#. Hauptprogrammschleife:

   Hält das Programm am Laufen, um auf IR-Signale zu hören. Behandelt das Programmende anmutig.

   .. code-block:: python

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            ir.close()
            print("Program terminated")

**Anwendungen**

* **Projekte drahtlos steuern**: Verwenden Sie die IR-Fernbedienung, um LEDs, Motoren oder andere Peripheriegeräte zu steuern.
* **Einen universellen Fernbedienungsdecoder bauen**: Erweitern Sie den Code, um mehrere Protokolle oder Fernbedienungen zu handhaben.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen IR-Empfänger mit dem Raspberry Pi Pico 2 verwendet, um Signale von einer Infrarot-Fernbedienung zu dekodieren. Dies ermöglicht es Ihnen, drahtlose Steuerung zu Ihren Projekten hinzuzufügen, die gängige Haushaltsfernbedienungen verwenden.

* `Callback Function - Wikipedia <https://en.wikipedia.org/wiki/Callback_(computer_programming)>`_

