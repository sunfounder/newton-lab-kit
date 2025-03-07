.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_rfid:

6.5 Verwendung von RFID
===========================================

In dieser Lektion erkunden wir die **Radio Frequency Identification (RFID)**-Technologie mit dem Raspberry Pi Pico 2. RFID ermöglicht die drahtlose Kommunikation zwischen einem Lesegerät und Tags, die für Identifikation, Authentifizierung und Datenspeicherung verwendet werden können.

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
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|

**Grundlagen von RFID**

RFID-Technologie nutzt elektromagnetische Felder, um Tags zu identifizieren und zu verfolgen, die an Objekten befestigt sind. Diese Tags enthalten elektronisch gespeicherte Informationen, die ohne direkte Sichtverbindung ausgelesen werden können.

* **RFID-Lesegerät (MFRC522):** Sendet Radiowellen aus, um mit RFID-Tags zu kommunizieren.
* **RFID-Tag:** Ein kleiner Chip (z. B. in Karten oder Schlüsselanhängern), der eine Antenne enthält. Es gibt passive (ohne Batterie) und aktive (batteriebetriebene) Tags.

**Schaltplan**

|sch_rfid|

**Verdrahtungsdiagramm**

|wiring_rfid|


**Code schreiben**

Wir werden zwei separate Skripte schreiben:

.. note:: 

    Die Bibliotheken im ``mfrc522``-Ordner müssen auf den Pico hochgeladen sein. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

1. Daten auf einen RFID-Tag schreiben: 

   * Die Klasse ``SimpleMFRC522`` aus der ``mfrc522``-Bibliothek vereinfacht die Interaktion mit dem RFID-Lesegerät.
   * Der Leser wird mit den angegebenen SPI-Pins initialisiert.
   * Der Benutzer wird aufgefordert, die zu speichernden Daten einzugeben.
   * Der Benutzer wird angewiesen, den Tag in die Nähe des Lesegeräts zu halten.
   * Die Daten werden mit ``reader.write(data)`` auf den Tag geschrieben.

   .. note:: 

       Öffne die Datei ``6.5_rfid_write.py`` aus ``newton-lab-kit/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run“ oder drücke F5.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522
        from machine import Pin, SPI

        # Initialisierung des RFID-Lesers
        reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

        def write_to_tag():
            try:
                data = input("Enter data to write to the tag: ")
                print("Place your tag near the reader...")
                reader.write(data)
                print("Data written successfully!")
            finally:
                pass  # Falls nötig, Cleanup-Aktionen

        write_to_tag()

   Ablauf des Programms:

   * Das Programm gibt die folgende Aufforderung aus:  
   
     .. code-block:: 

       Enter data to write to the tag:"

   * Du gibst den Text ein, den du auf den RFID-Tag schreiben möchtest, und drückst die Eingabetaste.  
   * Das Programm zeigt dann:

     .. code-block:: 

        Halte den Tag an das Lesegerät...

   * Du hältst den RFID-Tag in die Nähe des Lesegeräts.  
   * Nach erfolgreichem Schreiben der Daten wird folgende Meldung angezeigt:

     .. code-block:: 

       Data written successfully!

2. Daten von einem RFID-Tag lesen:

   * Der Benutzer hält einen Tag an das Lesegerät.
   * Das Programm liest die ID und die gespeicherten Daten mit ``reader.read()``.
   * Die Informationen werden in der Konsole ausgegeben.

   .. note:: 

       Öffne die Datei ``6.5_rfid_read.py`` aus ``newton-lab-kit/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run“ oder drücke F5.

       
   .. code-block:: python

       from mfrc522 import SimpleMFRC522
       from machine import Pin, SPI

       # Initialisierung des RFID-Lesers
       reader = SimpleMFRC522(spi_id=0, sck=18, mosi=19, miso=16, cs=17, rst=9)

       def read_from_tag():
           try:
               print("Place your tag near the reader...")
               id, text = reader.read()
               print("Tag ID: {}".format(id))
               print("Data: {}".format(text.strip()))
           finally:
               pass  # Falls nötig, Cleanup-Aktionen

       read_from_tag()

Nachdem das Programm gestartet wurde, erscheint die Meldung „Halte den Tag an das Lesegerät...“.  
Nun muss ein RFID-Tag in die Nähe des MFRC522-Lesemoduls gehalten werden.  
Das Programm liest dann die gespeicherten Informationen aus und gibt sie in der Konsole aus.  
Die Ausgabe könnte wie folgt aussehen:

.. code-block:: 

       Tag ID: 1234567890
       Data: Your stored message

**Den Code verstehen**

* **RFID Communication**: Das MFRC522-Modul kommuniziert über Funkwellen mit dem RFID-Tag. Befindet sich der Tag in Reichweite, kann das Lesegerät Daten auslesen oder auf den Speicher des Tags schreiben.
* **SPI Interface**: Das Modul kommuniziert mit dem Pico über das SPI-Protokoll, was eine schnelle Datenübertragung ermöglicht.
* **Data Storage**: RFID-Tags verfügen über eine begrenzte Speicherkapazität, die für kleine Datenmengen wie IDs oder kurze Texte geeignet ist.

**Anwendungen**

* **Access Control Systems**: RFID-Tags können als Schlüssel zum Entsperren von Türen oder Geräten verwendet werden.
* **Inventory Management**: Artikel in einem Lager oder Geschäft können mit RFID-Tags versehen und nachverfolgt werden.
* **Attendance Systems**: Die Anwesenheit kann durch das Scannen von RFID-Tags erfasst werden, die einzelnen Personen zugewiesen sind.

**Erweiterungen und Experimente**

* **Multiple Tags**: Speichere unterschiedliche Daten auf mehreren Tags und lese sie aus.
* **Security Measures**: Füge eine grundlegende Authentifizierung hinzu, um unbefugten Zugriff zu verhindern.
* **Data Formatting**: Speichere strukturierte Daten, z. B. im JSON- oder CSV-Format, für komplexere Anwendungen.

**Fazit**

In dieser Lektion hast du gelernt, wie du ein RFID-Lesegerät mit dem Raspberry Pi Pico 2 verbindest, um RFID-Tags auszulesen und zu beschreiben.  
Diese Technologie eröffnet viele Möglichkeiten für Anwendungen in den Bereichen Identifikation, Nachverfolgung und Automatisierung.
