.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_74hc_led:

5.1 Verwendung des 74HC595-Schieberegisters
===========================================================

In dieser Lektion lernen wir, wie man das **74HC595-Schieberegister** verwendet, um mehrere LEDs mit nur wenigen GPIO-Pins des Raspberry Pi Pico 2 zu steuern. Der **74HC595** ist ein integrierter Schaltkreis (IC), der serielle Eingaben in parallele Ausgaben umwandelt. Dadurch können mehrere digitale Ausgänge gesteuert werden, ohne viele GPIO-Pins zu belegen – eine äußerst nützliche Funktion, wenn nur wenige Pins zur Verfügung stehen.

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
        - 8 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|



**Funktionsweise des 74HC595-Schieberegisters**

Der **74HC595** ist ein **8-Bit-Serien-Eingang, Parallel-Ausgang**-Schieberegister mit Ausgangslatch. Es ermöglicht die serielle Eingabe von Daten und deren parallele Ausgabe, wodurch sich 8 Ausgänge mit nur 3 GPIO-Pins des Pico steuern lassen.

**Wichtige Pins des 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serielle Dateneingabe
* **SHCP (Pin 11)**: Takt für das Schieberegister
* **STCP (Pin 12)**: Takt für das Speicherregister (Latch-Pin)
* **OE (Pin 13)**: Ausgangsaktivierung (aktiv niedrig, mit GND verbinden)
* **MR (Pin 10)**: Master-Reset (aktiv niedrig, mit 3,3V verbinden)
* **Q0-Q7 (Pins 15, 1-7)**: Parallele Ausgänge
* **VCC (Pin 16)**: Mit 3,3V verbinden
* **GND (Pin 8)**: Mit GND verbinden

**Schaltplan**

|sch_74hc_led|

**Verdrahtungsdiagramm**

|wiring_74hc_led|

**Code schreiben**

Nun schreiben wir ein MicroPython-Programm, um LEDs über das 74HC595-Schieberegister zu steuern.

.. note::

    * Öffnen Sie die Datei ``5.1_microchip_74hc595.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.

    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 



.. code-block:: python

    import machine
    import utime

    # Definition der Pins für das 74HC595
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serielle Dateneingabe (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Speicherregister-Takt (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Schieberegister-Takt (SHCP)

    # Funktion zum Senden von Daten an das 74HC595
    def shift_out(data):
        for bit in range(8):
            # Höchstwertiges Bit extrahieren und zuerst senden
            bit_val = (data & 0x80) >> 7
            SDI.value(bit_val)
            # Takt für das Schieberegister setzen
            SRCLK.high()
            utime.sleep_us(1)
            SRCLK.low()
            utime.sleep_us(1)
            # Daten um 1 Bit nach links verschieben
            data = data << 1
        # Takt für das Speicherregister setzen (Latching)
        RCLK.high()
        utime.sleep_us(1)
        RCLK.low()
        utime.sleep_us(1)

    # Hauptschleife zur Demonstration verschiedener Muster
    while True:
        # LEDs nacheinander von Q0 bis Q7 einschalten
        for i in range(8):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # LEDs nacheinander von Q7 bis Q0 einschalten
        for i in range(7, -1, -1):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # Erzeugung eines Balkeneffekts
        for i in range(9):
            data = (1 << i) - 1
            shift_out(data)
            utime.sleep(0.2)
        # Alle LEDs ausschalten
        shift_out(0x00)
        utime.sleep(0.5)

Wenn Sie den Code ausführen, erzeugen die an das 74HC595-Schieberegister angeschlossenen LEDs dynamische Lichtmuster:

* **Erste Sequenz**: Die LEDs leuchten nacheinander von links nach rechts auf. Jede LED wird der Reihe nach eingeschaltet, wodurch der Effekt eines wandernden Lichts über die Reihe entsteht.
* **Zweite Sequenz**: Die LEDs leuchten nacheinander von rechts nach links auf, wodurch die Bewegung in die entgegengesetzte Richtung verläuft.
* **Dritte Sequenz**: Die LEDs erzeugen einen wachsenden Balkeneffekt, bei dem sich die LEDs von links nach rechts kumulativ einschalten, bis alle LEDs leuchten.
* **Letzter Schritt**: Alle LEDs schalten sich kurz aus, bevor die gesamte Sequenz erneut beginnt.

Dies führt zu einer beeindruckenden Lichtanzeige mit sich hin- und herbewegenden Lichtern und einem wachsenden Balkeneffekt, der sich kontinuierlich wiederholt.

**Den Code verstehen**

#. **Module importieren:**

   * ``machine``: Ermöglicht den Zugriff auf GPIO-Pins.
   * ``utime``: Enthält zeitbezogene Funktionen.

#. Steuerpins definieren:

   Die GPIO-Pins, die mit dem 74HC595 verbunden sind, werden festgelegt.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)   # Dateneingang
      RCLK = machine.Pin(1, machine.Pin.OUT)  # Latch-Takt
      SRCLK = machine.Pin(2, machine.Pin.OUT) # Schieberegister-Takt

#. Funktion shift_out definieren:

   * Diese Funktion sendet 8 Bit Daten an das Schieberegister.
   * Sie sendet das höchstwertige Bit (MSB) zuerst.
   * Der Schieberegister-Takt (SRCLK) wird gepulst, um jedes Bit einzulesen.
   * Nachdem alle Bits übertragen wurden, wird der Register-Takt (RCLK) gepulst, um die Daten an die Ausgänge zu übertragen.

   .. code-block:: python

      def shift_out(data):
          for bit in range(8):
              bit_val = (data & 0x80) >> 7
              SDI.value(bit_val)
              SRCLK.high()
              utime.sleep_us(1)
              SRCLK.low()
              utime.sleep_us(1)
              data = data << 1
          RCLK.high()
          utime.sleep_us(1)
          RCLK.low()
          utime.sleep_us(1)

#. Hauptschleife:

   * Jede LED leuchtet nacheinander von Q0 bis Q7 auf.

   .. code-block:: python

      for i in range(8):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)


   * Jede LED leuchtet nacheinander von Q7 bis Q0 auf.

   .. code-block:: python

      for i in range(7, -1, -1):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)

   * LEDs schalten sich schrittweise ein, um einen wachsenden Balken von Q0 bis Q7 zu erzeugen.

   .. code-block:: python

      for i in range(9):
          data = (1 << i) - 1
          shift_out(data)
          utime.sleep(0.2)

   * Sendet 0x00, um alle LEDs auszuschalten.

   .. code-block:: python

     shift_out(0x00)
     utime.sleep(0.5)

**Weitere Experimente**

* Benutzerdefinierte Muster erstellen:  
  Ändern Sie die gesendeten Daten, um verschiedene LED-Muster zu erzeugen. Beispiel: Blinken alternierender LEDs:

  .. code-block:: python

    shift_out(0b10101010)

* Mehr LEDs steuern:
  Mehrere 74HC595-Chips hintereinanderschalten, um zusätzliche Ausgänge zu steuern. Verbinden Sie den Q7' (Pin 9) des ersten Chips mit DS (Pin 14) des zweiten Chips.

* Integration mit Sensoren:  
  Nutzen Sie Eingaben von Sensoren oder Tasten, um die LED-Muster dynamisch zu verändern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie das 74HC595-Schieberegister verwenden, um die Ausgangsmöglichkeiten Ihres Raspberry Pi Pico 2 zu erweitern. Diese Technik ist besonders nützlich für Projekte, bei denen viele Ausgänge mit einer begrenzten Anzahl von GPIO-Pins gesteuert werden müssen.
