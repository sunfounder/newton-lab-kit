.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_7seg:

5.2 Zahlen anzeigen
===========================================================

In dieser Lektion lernen wir, wie man ein **7-Segment-Display** verwendet, um Zahlen mit dem Raspberry Pi Pico 2 und einem **74HC595-Schieberegister** darzustellen. Das 7-Segment-Display ist eine häufig verwendete elektronische Komponente in digitalen Uhren, Taschenrechnern und Haushaltsgeräten zur Anzeige numerischer Informationen.

Durch die Kombination des 74HC595-Schieberegisters mit dem 7-Segment-Display können wir alle Segmente mit nur wenigen GPIO-Pins des Pico steuern und so wertvolle I/O-Ressourcen für andere Komponenten sparen.

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
        - :ref:`cpn_resistor`
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_7_segment`
        - 1
        - |link_7segment_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|

**Funktionsweise des 7-Segment-Displays**

Ein 7-Segment-Display besteht aus 7 LEDs (Segmenten), die in einer Acht-Form angeordnet sind, um Ziffern von 0 bis 9 darzustellen. Zusätzlich gibt es eine achte LED für den Dezimalpunkt. Jedes Segment ist von **a** bis **g** beschriftet, und der Dezimalpunkt wird als **dp** gekennzeichnet.

Hier ist die Segmentbeschriftung:

|img_7seg_cathode|

In einem **gemeinsamen Kathoden**-7-Segment-Display sind alle Kathoden (negative Anschlüsse) der LEDs miteinander verbunden und an eine gemeinsame Masse angeschlossen.



**Schaltplan**

|sch_74hc_7seg|

Das Verdrahtungsprinzip ist im Wesentlichen dasselbe wie bei :ref:`py_74hc_led`, der einzige Unterschied besteht darin, dass Q0-Q7 mit den a ~ g Pins des 7-Segment-Displays verbunden sind.

.. list-table:: Wiring
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - LED-Segment-Display
    *   - Q0
        - a
    *   - Q1
        - b
    *   - Q2
        - c
    *   - Q3
        - d
    *   - Q4
        - e
    *   - Q5
        - f
    *   - Q6
        - g
    *   - Q7
        - dp

**Verdrahtungsdiagramm**


|wiring_74hc_7seg|



**Code schreiben**

Nun schreiben wir ein MicroPython-Programm, um die Ziffern 0 bis 9 auf dem 7-Segment-Display anzuzeigen.

.. note::

    * Öffnen Sie ``5.2_number_display.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # Definieren der Binärcodes für jede Ziffer (0-9)
    SEGMENT_CODES = [
        0x3F,  # 0
        0x06,  # 1
        0x5B,  # 2
        0x4F,  # 3
        0x66,  # 4
        0x6D,  # 5
        0x7D,  # 6
        0x07,  # 7
        0x7F,  # 8
        0x6F   # 9
    ]

    # Initialisieren der Steuerpins für 74HC595
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serieller Dateneingang (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Register-Takt (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Schieberegister-Takt (SHCP)

    # Funktion zum Senden von Daten an 74HC595
    def shift_out(data):
        RCLK.low()
        for bit in range(7, -1, -1):
            SRCLK.low()
            bit_val = (data >> bit) & 0x01
            SDI.value(bit_val)
            SRCLK.high()
        RCLK.high()

    # Hauptschleife zum Anzeigen der Zahlen 0-9
    while True:
        for num in range(10):
            shift_out(SEGMENT_CODES[num])
            utime.sleep(0.5)

Wenn Sie diesen Code ausführen, zeigt das 7-Segment-Display nacheinander die Ziffern 0 bis 9 an und wechselt alle 0,5 Sekunden. Dadurch entsteht ein zyklischer Zählereffekt, bei dem sich die Zahlen der Reihe nach erhöhen und nach der 9 wieder bei 0 beginnen.

**Erklärung des Codes**

#. **Module importieren:**

   * ``machine``: Ermöglicht den Zugriff auf GPIO-Pins und Hardwarefunktionen.
   * ``utime``: Enthält Zeitfunktionen für Verzögerungen.

#. Segmentcodes definieren: 

   Jeder Eintrag entspricht den Segmenten, die aktiviert werden müssen, um eine Ziffer darzustellen. Die Werte sind zur besseren Lesbarkeit im Hexadezimalformat angegeben.
   
   .. code-block:: python

      SEGMENT_CODES = [
          0x3F,  # 0
          0x06,  # 1
          0x5B,  # 2
          0x4F,  # 3
          0x66,  # 4
          0x6D,  # 5
          0x7D,  # 6
          0x07,  # 7
          0x7F,  # 8
          0x6F   # 9
      ]

   Angenommen, das 7-Segment-Display soll die Zahl "1" anzeigen. Dafür müssen die Segmente b und c auf HIGH gesetzt werden, während a, d, e, f, g und dp auf LOW bleiben.

   |img_1_segment|

   Das bedeutet, dass das Binärmuster "00000110" geschrieben werden muss. Zur besseren Lesbarkeit verwenden wir die hexadezimale Darstellung "0x06".


#. Steuerpins initialisieren:

   Weist die GPIO-Pins des Pico zur Steuerung des 74HC595-Schieberegisters zu.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)
      RCLK = machine.Pin(1, machine.Pin.OUT)
      SRCLK = machine.Pin(2, machine.Pin.OUT)


#. Die Funktion ``shift_out`` definieren:

   * Sendet 8 Bit an das 74HC595-Schieberegister.
   * Überträgt die Daten beginnend mit dem höchstwertigen Bit (MSB).
   * Pulsiert die Schieberegister- und Register-Taktleitungen entsprechend.

   .. code-block:: python

        def shift_out(data):
            RCLK.low()
            for bit in range(7, -1, -1):
                SRCLK.low()
                bit_val = (data >> bit) & 0x01
                SDI.value(bit_val)
                SRCLK.high()
            RCLK.high()

#. Hauptschleife zur Anzeige der Zahlen:

   * Durchläuft die Zahlen 0 bis 9.
   * Ruft shift_out mit dem entsprechenden Segmentcode auf.
   * Fügt eine Verzögerung von 0,5 Sekunden zwischen den Zahlen hinzu.

   .. code-block:: python

        while True:
            for num in range(10):
                shift_out(SEGMENT_CODES[num])
                utime.sleep(0.5)


**Verständnis der Segmentcodes**

Jeder Segmentcode entspricht den zu beleuchtenden Segmenten für eine bestimmte Ziffer. Hier ist die Zuordnung der Segmente zu den einzelnen Ziffern:

* **0**: Segments a, b, c, d, e, f (code 0x3F)
* **1**: Segments b, c (code 0x06)
* **2**: Segments a, b, g, e, d (code 0x5B)
* **3**: Segments a, b, c, d, g (code 0x4F)
* **4**: Segments b, c, f, g (code 0x66)
* **5**: Segments a, c, d, f, g (code 0x6D)
* **6**: Segments a, c, d, e, f, g (code 0x7D)
* **7**: Segments a, b, c (code 0x07)
* **8**: Segments a, b, c, d, e, f, g (code 0x7F)
* **9**: Segments a, b, c, d, f, g (code 0x6F)

**Weitere Experimente**

* Hexadezimale Zeichen anzeigen:

  Erweitern Sie die ``SEGMENT_CODES``-Liste um die Buchstaben A-F für die hexadezimale Darstellung. Zum Beispiel hat der Buchstabe 'A' den Segmentcode 0x77.

* Einen Zähler erstellen:

  Ändern Sie den Code so, dass ein Zähler hoch- oder herunterzählt. Verwenden Sie Tasten, um die angezeigte Zahl zu erhöhen oder zu verringern.

* Mehrere Anzeigen steuern:

  Nutzen Sie zusätzliche 74HC595-Schieberegister, um mehrere 7-Segment-Anzeigen zu steuern. Implementieren Sie Multiplexing, um mehrere Anzeigen mit minimalem GPIO-Aufwand zu verwalten.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie ein 7-Segment-Display mit einem 74HC595-Schieberegister verwenden, um Zahlen mit dem Raspberry Pi Pico 2 darzustellen. Durch das Verständnis der Steuerung der einzelnen Segmente über Binärcodes und die Nutzung des Schieberegisters können Sie effizient mehrere Ausgaben mit einer begrenzten Anzahl an GPIO-Pins verwalten.
