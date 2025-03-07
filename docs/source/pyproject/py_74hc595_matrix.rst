.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_788bs:

5.4 Grafiken auf einer 8x8-LED-Matrix anzeigen
===================================================================

In dieser Lektion lernen wir, wie man eine **8x8-LED-Matrix** mit dem Raspberry Pi Pico 2 und zwei **74HC595-Schieberegistern** steuert. Wir werden Muster und einfache Grafiken anzeigen, indem wir einzelne LEDs der Matrix gezielt ansteuern.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE KOMPONENTEN
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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Funktionsweise der 8x8-LED-Matrix**

Eine 8x8-LED-Matrix besteht aus 64 LEDs, die in 8 Reihen und 8 Spalten angeordnet sind. Jede LED kann individuell gesteuert werden, indem eine Spannung zwischen der entsprechenden Reihe und Spalte angelegt wird. Durch gezielte Steuerung der Reihen- und Spaltenströme können Zeichen oder Muster angezeigt werden.

In diesem Aufbau verwenden wir zwei 74HC595-Schieberegister, um die Reihen und Spalten der LED-Matrix zu steuern. Dies ermöglicht eine effiziente Erweiterung der digitalen Ausgänge des Raspberry Pi Pico 2, während nur wenige GPIO-Pins benötigt werden.

**Schaltplan**

|sch_ledmatrix|

Die 8x8-LED-Matrix wird durch zwei **74HC595-Schieberegister** gesteuert: eines für die Reihen, das andere für die Spalten. Diese beiden Chips teilen sich die GPIO-Pins **GP18**, **GP19** und **GP20** des Pico und sparen so wertvolle I/O-Ports.

Der Pico sendet ein 16-Bit-Binärmuster: Die ersten 8 Bits steuern die Reihen, die letzten 8 Bits steuern die Spalten. Dadurch lassen sich gezielt Muster auf der LED-Matrix darstellen.

**Q7' (Pin 9)**: Dieser serielle Ausgang des ersten 74HC595 wird mit **DS (Pin 14)** des zweiten 74HC595 verbunden, um eine Kaskadierung mehrerer Schieberegister zu ermöglichen.

**Verdrahtungsdiagramm** 

Der Aufbau der Schaltung kann komplex sein, daher gehen wir schrittweise vor.

**Schritt 1:** Setzen Sie zuerst den Pico, die 8x8-LED-Matrix und zwei 74HC595-Schieberegister in das Breadboard ein. Verbinden Sie 3,3V und GND des Pico mit den seitlichen Stromschienen des Boards. Anschließend schließen Sie Pin 16 und Pin 10 der beiden 74HC595 an VCC an und verbinden Pin 13 sowie Pin 8 mit GND.

.. note::
   Im obigen Fritzing-Bild befindet sich die Seite mit der Beschriftung unten.

|wiring_ledmatrix_4|

**Schritt 2:** Verbinden Sie Pin 11 der beiden 74HC595 miteinander und dann mit GP20. Danach verbinden Sie Pin 12 beider Chips mit GP19. Anschließend verbinden Sie Pin 14 des linken 74HC595 mit GP18 und Pin 9 mit Pin 14 des zweiten 74HC595.

|wiring_ledmatrix_3|

**Schritt 3:** Das rechte 74HC595 steuert die Spalten der LED-Matrix. Die Zuordnung der Pins ist in der folgenden Tabelle dargestellt. Q0-Q7 des 74HC595 sind mit den Pins 13, 3, 4, 10, 6, 11, 15 und 16 der LED-Matrix verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED-Matrix**     | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Schritt 4:** Nun werden die Reihen der LED-Matrix angeschlossen. Das linke 74HC595 steuert die Reihen. Die Zuordnung der Pins ist in der folgenden Tabelle dargestellt. Q0-Q7 des linken 74HC595 sind mit den Pins 9, 14, 8, 12, 1, 7, 2 und 5 der LED-Matrix verbunden.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED-Matrix**     | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|

**Code schreiben**

Nun schreiben wir ein MicroPython-Programm, um ein Muster auf der LED-Matrix darzustellen.

.. note::

    * Öffnen Sie ``5.4_8x8_pixel_graphics.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import time

    # Definition der Pins für die 74HC595-Schieberegister
    sdi = machine.Pin(18, machine.Pin.OUT)   # Serielle Dateneingabe
    rclk = machine.Pin(19, machine.Pin.OUT)  # Speicherregister-Takt (RCLK)
    srclk = machine.Pin(20, machine.Pin.OUT) # Schieberegister-Takt (SRCLK)

    # Muster für den Buchstaben "X"
    glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

    def hc595_in(dat):
        """
        Sendet 8 Bit Daten an das 74HC595-Schieberegister.
        """
        for bit in range(7, -1, -1):
            srclk.low()
            sdi.value((dat >> bit) & 1)
            srclk.high()
            time.sleep_us(1)

    def hc595_out():
        """
        Latcht die Daten vom Schieberegister ins Speicherregister.
        """
        rclk.high()
        rclk.low()

    while True:
        for i in range(8):
            hc595_in(glyph[i])       # Send the column data for the current row
            hc595_in(1 << i)         # Activate the current row
            hc595_out()              # Update the display
            time.sleep_ms(1)         # Delay for visual persistence       



Wenn Sie diesen Code ausführen, zeigt die 8x8-LED-Matrix ein "X"-Muster an, wobei die LEDs aufleuchten, um die Form des Buchstabens "X" über die gesamte Matrix zu bilden.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Bietet Zugriff auf hardwarebezogene Funktionen, z. B. zur Steuerung von GPIO-Pins.
   * ``time``: Wird verwendet, um Verzögerungen für die Zeitsteuerung hinzuzufügen.

#. Pins definieren:

   * ``sdi``: Sendet serielle Daten an das Schieberegister.
   * ``rclk``: Latcht die verschobenen Daten an die Ausgangspins.
   * ``srclk``: Verschiebt die Daten bei jeder steigenden Flanke in das Register.

#. Das Muster für "X" definieren:

   * Jedes Element repräsentiert eine Reihe in der LED-Matrix.
   * Die Hexadezimalwerte geben an, welche LEDs in jeder Reihe leuchten (0) oder ausgeschaltet bleiben (1).
   * Dieses Muster erzeugt eine symmetrische "X"-Form in der Matrix.

   .. code-block:: python
    
        glyph = [0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E]

#. Funktion ``hc595_in(dat)``:

   * Diese Funktion sendet 8 Bit Daten (``dat``) seriell an das Schieberegister.
   * Sie iteriert vom höchstwertigen Bit zum niedrigstwertigen Bit.
   * Der Pin ``srclk`` wird getoggelt, um jedes Bit in das Register zu verschieben.
   * Der ``sdi``-Pin setzt die Datenleitung je nach aktuellem Bit auf HIGH oder LOW.
   

   .. code-block:: python
    
        def hc595_in(dat):
            """
            Shifts 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()
                sdi.value((dat >> bit) & 1)  # Daten Bit für Bit ausgeben
                srclk.high()
                time.sleep_us(1)  # Kurze Verzögerung für korrekte Übertragung


#. Funktion ``hc595_out()``:

   * Diese Funktion latcht die verschobenen Daten vom Schieberegister in das Ausgangsregister.
   * Eine steigende Flanke am ``rclk``-Pin überträgt die Daten an die Ausgangspins und aktualisiert die LEDs.

   .. code-block:: python
    
        def hc595_out():

            rclk.high()
            rclk.low()

#. **Hauptschleife:**

   * Die Schleife aktualisiert kontinuierlich die Anzeige, um ein stabiles "X"-Muster zu erzeugen.
   * Die ``for``-Schleife iteriert über jeden Zeilenindex von 0 bis 7.
   * ``hc595_in(1 << i)`` aktiviert eine Reihe nach der anderen, indem jeweils ein Bit auf HIGH gesetzt wird.
   * ``hc595_in(glyph[i])`` sendet die Spaltendaten für die aktuelle Zeile und bestimmt, welche LEDs in dieser Zeile leuchten.
   * ``hc595_out()`` latcht die Daten und aktualisiert die LED-Matrix.
   * ``time.sleep_ms(1)`` sorgt für eine kurze Verzögerung, damit jede Zeile lang genug angezeigt wird, um vom menschlichen Auge wahrgenommen zu werden.
   * Dieses schnelle Scannen erzeugt die Illusion, dass das gesamte "X" gleichzeitig angezeigt wird.

   .. code-block:: python
    
        while True:
            for i in range(8):
                hc595_in(glyph[i])       # Spaltendaten für die aktuelle Reihe senden
                hc595_in(1 << i)         # Aktuelle Reihe aktivieren
                hc595_out()              # Anzeige aktualisieren
                time.sleep_ms(1)         # Verzögerung für visuelle Beständigkeit


**Weitere Experimente**

* Muster ändern 
  Ersetzen Sie die glyph-Liste durch die folgenden Arrays, um verschiedene Grafiken anzuzeigen. Ersetzen Sie glyph in Ihrem Code durch ``pattern_heart`` oder ``pattern_smile``, um andere Muster zu sehen.


  .. code-block:: python

        # Herzform
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]

        # Smiley-Gesicht
        pattern_smile = [
            0b11000011,  # Reihe 0
            0b10111101,  # Reihe 1
            0b01011010,  # Reihe 2
            0b01111110,  # Reihe 3
            0b01011010,  # Reihe 4
            0b01100110,  # Reihe 5
            0b10111101,  # Reihe 6
            0b11000011   # Reihe 7
        ]

* Animationen erstellen 
 
  Erstellen Sie mehrere Muster und lassen Sie sie in einer Schleife durchlaufen, um Animationen zu erzeugen.

  .. code-block:: python

        import machine
        import time
        
        # Pins für 74HC595 definieren
        sdi = machine.Pin(18, machine.Pin.OUT)   # Serielle Dateneingabe
        rclk = machine.Pin(19, machine.Pin.OUT)  # Speicherregister-Takt
        srclk = machine.Pin(20, machine.Pin.OUT) # Schieberegister-Takt
        
        # Herzform
        pattern_heart = [
            0b11111111,
            0b10011001,
            0b00000000,
            0b00000000,
            0b00000000,
            0b10000001,
            0b11000011,
            0b11100111
        ]
        
        # Smiley-Gesicht
        pattern_smile = [
            0b11000011,  # Reihe 0
            0b10111101,  # Reihe 1
            0b01011010,  # Reihe 2
            0b01111110,  # Reihe 3
            0b01011010,  # Reihe 4
            0b01100110,  # Reihe 5
            0b10111101,  # Reihe 6
            0b11000011   # Reihe 7
        ]
        
        def hc595_in(dat):
            """
            Shift 8 bits of data into the 74HC595 shift register.
            """
            for bit in range(7, -1, -1):
                srclk.low()                            # Prepare to shift data
                sdi.value((dat >> bit) & 1)            # Set data bit
                srclk.high()                           # Shift data bit into register
                time.sleep_us(1)                       # Short delay for timing

        def hc595_out():
            """
            Latch the shifted data to the output pins of the 74HC595.
            """
            rclk.high()                               # Latch data (rising edge)
            rclk.low()                                # Prepare for next data

        def display_pattern(pattern):
            """
            Display a given 8x8 pattern on the LED matrix.
            """
            for _ in range(500):                      # Display the pattern for a certain duration
                for i in range(8):
                    hc595_in(pattern[i])              # Send column data for current row
                    hc595_in(1 << i)                  # Activate current row
                    hc595_out()                       # Update the output
                    time.sleep_ms(1)                  # Short delay for persistence

        while True:
            display_pattern(pattern_heart)            # Display the heart shape
            display_pattern(pattern_smile)            # Display the smiley face

* Eigene Muster entwerfen  

  Jedes Byte repräsentiert eine Zeile, Bits mit Wert 0 schalten die LED in dieser Spalte ein. Erstellen Sie individuelle Muster, indem Sie Ihre eigene Musterliste definieren.


**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie eine 8x8-LED-Matrix mit dem Raspberry Pi Pico 2 und zwei 74HC595-Schieberegistern steuern. Durch das Verständnis der Bit-Manipulation und den Einsatz von Schieberegistern können Sie Muster und Grafiken auf der LED-Matrix anzeigen.
