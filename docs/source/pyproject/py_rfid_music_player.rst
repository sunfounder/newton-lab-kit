.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_music_player:

7.8 Bau eines RFID-Musikspielers
========================================================

In diesem Projekt erstellen wir einen **RFID-Musikspieler** mit dem Raspberry Pi Pico 2, einem MFRC522-RFID-Lesegerät, einem passiven Buzzer und WS2812-RGB-LEDs.  
Durch das Speichern von Musiknoten auf RFID-Tags können wir diese auslesen, eine Melodie abspielen und gleichzeitig Lichteffekte anzeigen.  
Dieses Projekt kombiniert RFID-Technologie mit Musikgenerierung und ermöglicht das Speichern sowie Teilen von Melodien auf RFID-Karten oder Schlüsselanhängern.

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
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_mfrc522`
        - 1
        - |link_rfid_buy|
    *   - 9
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Funktionsweise der Komponenten**

* **MFRC522-RFID-Lesegerät:** Ein kostengünstiger RFID-Reader, der über SPI kommuniziert und RFID-Tags mit einer Frequenz von 13,56 MHz lesen und beschreiben kann.
* **RFID-Tags/Schlüsselanhänger:** Passive Speicherchips, auf denen kleine Datenmengen gespeichert werden können. Hier werden Musiknoten gespeichert.
* **Passiver Buzzer:** Ein elektronisches Bauteil, das Töne erzeugt, wenn es mit einem PWM-Signal angesteuert wird. Er wird genutzt, um Musiknoten zu spielen.
* **WS2812-RGB-LEDs:** Auch bekannt als NeoPixels, können diese LEDs verschiedene Farben anzeigen und über eine einzige Datenleitung individuell gesteuert werden.

**Schaltplan**

|sch_music_player|

**Verdrahtungsdiagramm**

|wiring_rfid_music_player| 

**Code schreiben**

Wir schreiben zwei Skripte:

* ``6.5_rfid_write.py``: Zum Speichern von Musiknoten auf dem RFID-Tag.
* ``7.8_rfid_music_player.py``: Zum Lesen der gespeicherten Noten und Abspielen der Melodie.

.. note:: 

    Die Bibliotheken im Ordner ``mfrc522`` müssen auf den Pico hochgeladen sein. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

#. Öffne die Datei ``6.5_rfid_write.py`` aus ``newton-lab-kit/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run“ oder drücke F5.

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
                pass

        write_to_tag()

#. Nach dem Start gib ``EEFGGFEDCCDEEDD EEFGGFEDCCDEDCC`` in die Konsole ein und halte den RFID-Tag an das Lesegerät. Dies speichert die Noten der „Ode an die Freude“. Nach erfolgreicher Speicherung wird die Meldung „Daten erfolgreich geschrieben!“ angezeigt.

#. Öffne die Datei ``7.8_rfid_music_player.py`` aus ``newton-lab-kit/micropython`` oder kopiere diesen Code in Thonny, dann klicke auf „Run“ oder drücke F5.

   .. code-block:: python

        from mfrc522 import SimpleMFRC522 
        import machine
        import time
        from ws2812 import WS2812
        import urandom

        # WS2812-LED-Setup
        # Initialisierung eines WS2812-LED-Streifens mit 8 LEDs an Pin 0
        ws = WS2812(machine.Pin(0), 8)

        # MFRC522-RFID-Leser-Setup
        # Initialisierung des RFID-Lesers über SPI mit den spezifischen Pins
        reader = SimpleMFRC522(spi_id=0, sck=18, miso=16, mosi=19, cs=17, rst=9)

        # Frequenzen der Buzzer-Noten (in Hertz)
        NOTE_C4 = 262
        NOTE_D4 = 294
        NOTE_E4 = 330
        NOTE_F4 = 349
        NOTE_G4 = 392
        NOTE_A4 = 440
        NOTE_B4 = 494
        NOTE_C5 = 523

        # Initialisierung des PWM-Signals für den Buzzer an Pin 15
        buzzer = machine.PWM(machine.Pin(15))

        # Liste der Notenfrequenzen, die den Musiknoten entsprechen
        note = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5]

        # Funktion zum Abspielen eines Tons auf dem Buzzer mit einer bestimmten Frequenz und Dauer
        def tone(pin, frequency, duration):
         pin.freq(frequency)  # Setze die Buzzer-Frequenz
         pin.duty_u16(30000)  # Setze den Duty-Cycle auf ca. 50 %
         time.sleep_ms(duration)  # Spiele den Ton für die angegebene Dauer
         pin.duty_u16(0)  # Stoppe den Ton, indem der Duty-Cycle auf 0 gesetzt wird

        # Funktion zum Beleuchten einer WS2812-LED an einem bestimmten Index mit einer zufälligen Farbe
        def lumi(index):
         for i in range(8):
             ws[i] = 0x000000  # Schalte alle LEDs aus
         ws[index] = int(urandom.uniform(0, 0xFFFFFF))  # Setze eine zufällige Farbe für die LED am angegebenen Index
         ws.write()  # Schreibe die Farbdaten an die WS2812-LEDs

        # Musiknoten-Text in Indizes umwandeln und entsprechende Noten abspielen
        words = ["C", "D", "E", "F", "G", "A", "B", "N"]  # Zuordnung von Musiknoten zu Zeichen
        def take_text(text):
         string = text.replace(' ', '').upper()  # Entferne Leerzeichen und konvertiere den Text in Großbuchstaben
         while len(string) > 0:
             index = words.index(string[0])  # Bestimme den Index der ersten Note im String
             tone(buzzer, note[index], 250)  # Spiele die entsprechende Note für 250 ms auf dem Buzzer
             lumi(index)  # Leuchte die LED entsprechend der Note auf
             string = string[1:]  # Gehe zum nächsten Zeichen im String über

        # Funktion zum Lesen von RFID-Karten und Abspielen der gespeicherten Noten
        def read():
         print("Reading...Please place the card...")
         id, text = reader.read()  # RFID-Karte auslesen (ID und gespeicherter Text)
         print("ID: %s\nText: %s" % (id, text))  # ID und gespeicherten Text ausgeben
         take_text(text)  # Spiele die gespeicherten Noten aus dem auf der Karte gespeicherten Text

        # Lese eine RFID-Karte und spiele die entsprechende Melodie ab
        read()



#. Nach dem Start wird in der Konsole die Meldung angezeigt: „Halte den Tag an das Lesegerät...“.

   Halte den RFID-Tag an das Lesegerät:
   
   * Der Pico liest die Daten vom RFID-Tag aus.
   * Die Konsole zeigt die Tag-ID und den gespeicherten Text an.
   * Der Buzzer spielt die der gespeicherten Melodie entsprechenden Noten ab.
   * Die WS2812-LEDs leuchten synchron zur Musik mit Lichteffekten auf.

**Den Code verstehen**

* RFID-Interaktion:

  * Die Klasse ``SimpleMFRC522`` vereinfacht das Lesen und Schreiben von RFID-Tags.
  * **Daten schreiben**: In ``write_to_tag()`` werden Benutzereingaben auf den RFID-Tag geschrieben.
  * **Daten lesen**: In ``read_and_play()`` werden Daten vom RFID-Tag ausgelesen, sobald er sich in der Nähe des Lesegeräts befindet.

* Musik-Wiedergabe:

  * **Noten-Wörterbuch**: Ordnet Zeichenfolgen von ``note`` den entsprechenden Frequenzen zu.
  * **Noten-Analyse**: Der Text vom RFID-Tag wird bereinigt und Zeichen für Zeichen durchlaufen.
  * **Noten abspielen**: Für jedes Zeichen wird die entsprechende Frequenz auf dem Buzzer wiedergegeben.

* LED-Effekte:

  * **WS2812-Steuerung**: Das ``ws``-Objekt steuert die RGB-LEDs.
  * **LEDs leuchten auf**: Für jede gespielte Note wird eine zufällige Farbe einer LED zugewiesen.

* Timing:

  * **Notendauer**: Jede Note wird 300 Millisekunden lang gespielt.
  * **Pause zwischen den Noten**: Eine kurze Pause von 100 Millisekunden sorgt für saubere Trennung der Noten.

**Weitere Experimente**

* Erstelle eigene Melodien:

  * Speichere unterschiedliche Notenfolgen auf RFID-Tags.
  * Verwende die Noten C, D, E, F, G, A, B und N (für Pause).
  * Tausche deine RFID-Musikkarten mit Freunden.

* Tonumfang erweitern:

  * Definiere zusätzliche Frequenzen, um weitere Oktaven hinzuzufügen.
  * Aktualisiere das Noten-Dictionary entsprechend.

* Visuelle Verbesserungen:

  * Modifiziere die lumi()-Funktion, um verschiedene LED-Muster zu erzeugen.
  * Synchronisiere die LED-Effekte genauer mit der Musik.

* Mehrere RFID-Tags für verschiedene Lieder:

  * Speichere unterschiedliche Melodien auf mehreren RFID-Tags.
  * Erstelle eine kleine RFID-Musikbibliothek.

**Einschränkungen verstehen**

* Datenspeicherung auf RFID-Tags:

  * RFID-Tags haben eine begrenzte Speicherkapazität (meist bis zu 48 Zeichen für den MFRC522).
  * Halte deine Musiksequenzen kurz und effizient.

* Audioqualität:

  * Passive Buzzer erzeugen einfache Töne.
  * Für eine bessere Klangqualität könnte ein aktiver Lautsprecher mit DAC-Ausgang verwendet werden.

* Kompatibilität der RFID-Tags:

  Stelle sicher, dass deine RFID-Tags mit dem MFRC522-Lesegerät kompatibel sind.

**Fazit**

Du hast erfolgreich einen RFID-Musikspieler mit dem Raspberry Pi Pico 2 gebaut!  
Dieses Projekt kombiniert RFID-Technologie, Musikgenerierung und LED-Steuerung, um ein interaktives und unterhaltsames Erlebnis zu schaffen.  
Durch das Speichern von Melodien auf RFID-Tags kannst du einfach verschiedene Lieder abrufen und teilen.
