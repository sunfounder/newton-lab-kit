.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_4dig:

5.3 Erstellen eines Zeitzählers mit einer 4-stelligen 7-Segment-Anzeige
===========================================================================

In dieser Lektion lernen wir, wie man eine **4-stellige 7-Segment-Anzeige** mit dem Raspberry Pi Pico 2 verwendet, um einen einfachen Zeitmesser zu erstellen. Das Display zählt jede Sekunde hoch und zeigt die verstrichene Zeit in Sekunden an.

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Ein komplettes Kit ist besonders praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Sie können die Teile auch einzeln über die unten stehenden Links kaufen.


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
        - 4 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Verständnis der 4-stelligen 7-Segment-Anzeige**

Eine 4-stellige 7-Segment-Anzeige besteht aus vier einzelnen 7-Segment-Anzeigen, die in einem Modul kombiniert sind. Jede Ziffer teilt sich die gleichen Segmentsteuerleitungen (**a** bis **g** und **dp**), aber jede Ziffer hat ihre eigene **gemeinsame Kathodensteuerung**. Dadurch kann gesteuert werden, welche Ziffer zu einem bestimmten Zeitpunkt aktiv ist.

Um verschiedene Zahlen auf jeder Ziffer anzuzeigen, verwenden wir eine Technik namens **Multiplexing**. Dabei wird schnell zwischen den Ziffern umgeschaltet, sodass jede Ziffer nacheinander aktualisiert wird. Durch die Trägheit des menschlichen Auges erscheint es so, als wären alle Ziffern gleichzeitig sichtbar.

|4digit_control_pins|

**Schaltplan**

|sch_4dig|

Die Verdrahtungslogik ist im Grunde dieselbe wie bei :ref:`py_74hc_led`, mit dem Unterschied, dass Q0-Q7 mit den Pins a ~ g der 4-stelligen 7-Segment-Anzeige verbunden sind.

Die Pins G10 ~ G13 steuern, welche der 7-Segment-Anzeigen aktiv ist.

**Verdrahtungsdiagramm**

|wiring_4dig|

* **Segmentverbindungen (über 220 Ω Widerstände):**

  * **Q0** → Segment **a**
  * **Q1** → Segment **b**
  * **Q2** → Segment **c**
  * **Q3** → Segment **d**
  * **Q4** → Segment **e**
  * **Q5** → Segment **f**
  * **Q6** → Segment **g**
  * **Q7** → Segment **dp** (Dezimalpunkt)

* **Gemeinsame Kathodenanschlüsse (Ziffernauswahl-Pins):**

  * **Ziffer 1 (linke Ziffer):** Verbinden mit **GP10** am Pico
  * **Ziffer 2:** Verbinden mit **GP11**
  * **Ziffer 3:** Verbinden mit **GP12**
  * **Ziffer 4 (rechte Ziffer):** Verbinden mit **GP13**

**Code schreiben**

.. note::

   * Sie können die Datei ``5.3_time_counter.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/5.3_time_counter`` öffnen.
   * Oder den folgenden Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: arduino

    // Define the connection pins for the shift register
    #define DATA_PIN 18   // DS (Serial Data Input)
    #define LATCH_PIN 19  // STCP (Storage Register Clock)
    #define CLOCK_PIN 20  // SHCP (Shift Register Clock)

    // Define the digit control pins for the 4-digit 7-segment display
    const int digitPins[4] = { 10, 11, 12, 13 };  // DIG1, DIG2, DIG3, DIG4

    // Segment byte maps for numbers 0-9
    const byte digitCodes[10] = {
      // Pgfedcba
      0b00111111,  // 0
      0b00000110,  // 1
      0b01011011,  // 2
      0b01001111,  // 3
      0b01100110,  // 4
      0b01101101,  // 5
      0b01111101,  // 6
      0b00000111,  // 7
      0b01111111,  // 8
      0b01101111   // 9
    };

    unsigned long previousMillis = 0;  // Stores the last time the display was updated
    unsigned int counter = 0;          // Counter value

    void setup() {
      // Initialize the shift register pins
      pinMode(DATA_PIN, OUTPUT);
      pinMode(LATCH_PIN, OUTPUT);
      pinMode(CLOCK_PIN, OUTPUT);

      // Initialize the digit control pins
      for (int i = 0; i < 4; i++) {
        pinMode(digitPins[i], OUTPUT);
        digitalWrite(digitPins[i], HIGH);  // Turn off all digits
      }
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the counter every 1000 milliseconds (1 second)
      if (currentMillis - previousMillis >= 1000) {
        previousMillis = currentMillis;
        counter++;  // Increment the counter
        if (counter > 9999) {
          counter = 0;  // Reset counter after 9999
        }
      }

      // Display the counter value
      displayNumber(counter);
    }

    void displayNumber(int num) {
      // Break the number into digits
      int digits[4];
      digits[0] = num / 1000;        // Thousands
      digits[1] = (num / 100) % 10;  // Hundreds
      digits[2] = (num / 10) % 10;   // Tens
      digits[3] = num % 10;          // Units

      // Display each digit
      for (int i = 0; i < 4; i++) {
        digitalWrite(digitPins[i], LOW);  // Activate digit
        shiftOutDigit(digitCodes[digits[i]]);
        delay(5);                          // Small delay for multiplexing
        digitalWrite(digitPins[i], HIGH);  // Deactivate digit
      }
    }

    void shiftOutDigit(byte data) {
      // Send data to the shift register
      digitalWrite(LATCH_PIN, LOW);
      shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
      digitalWrite(LATCH_PIN, HIGH);
    }

Nach dem Hochladen des Codes sollte die 4-stellige 7-Segment-Anzeige beginnen, von 0000 an hochzuzählen, wobei jede Sekunde um 1 erhöht wird. 
Die Zählung sollte wie folgt fortschreiten: 0000, 0001, 0002, ..., 9999 und dann auf 0000 zurückgesetzt werden.

**Verständnis des Codes**

#. Definition der Steuerpins:

   * ``DATA_PIN (DS)``: Empfängt serielle Daten, die in das 74HC595-Schieberegister übertragen werden.
   * ``LATCH_PIN (STCP)``: Steuert das Übernehmen der Daten vom Schieberegister zu den Ausgangspins.
   * ``CLOCK_PIN (SHCP)``: Steuert das Schieben der Daten in das Schieberegister.

   .. code-block:: arduino

      #define DATA_PIN   18  // DS (Serielle Dateneingabe)
      #define LATCH_PIN  19  // STCP (Speicherregister-Takt)
      #define CLOCK_PIN  20  // SHCP (Schieberegister-Takt)
  
#. Definition der Ziffernsteuerungs-Pins:

   * Die gemeinsame Kathode jeder Ziffer ist mit einem separaten GPIO-Pin verbunden.
   * Das Setzen eines Digit-Pins auf LOW aktiviert die Ziffer, während HIGH sie deaktiviert.

   .. code-block:: arduino

      const int digitPins[4] = {10, 11, 12, 13}; // DIG1, DIG2, DIG3, DIG4
  
#. Erstellen der Segment-Byte-Mapping:

   * Jedes Byte repräsentiert die Segmente, die zum Anzeigen der Zahlen 0 bis 9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige aktiviert werden müssen.
   * Die Bits entsprechen den Segmenten a bis g sowie dp:

   .. code-block:: arduino

      const byte digitCodes[10] = {
        0b00111111, // 0
        0b00000110, // 1
        0b01011011, // 2
        0b01001111, // 3
        0b01100110, // 4
        0b01101101, // 5
        0b01111101, // 6
        0b00000111, // 7
        0b01111111, // 8
        0b01101111  // 9
      };

#. Setup-Funktion:

   * Setzt die Pins ``DATA_PIN``, ``LATCH_PIN`` und ``CLOCK_PIN`` als Ausgänge.
   * Setzt alle Ziffernsteuer-Pins auf ``HIGH``, um alle Ziffern beim Start zu deaktivieren.

   .. code-block:: arduino

      void setup() {
        // Initialize the shift register pins
        pinMode(DATA_PIN, OUTPUT);
        pinMode(LATCH_PIN, OUTPUT);
        pinMode(CLOCK_PIN, OUTPUT);

        // Initialize the digit control pins
        for (int i = 0; i < 4; i++) {
          pinMode(digitPins[i], OUTPUT);
          digitalWrite(digitPins[i], HIGH); // Turn off all digits initially
        }
      }

#. Loop-Funktion:

   * Verwendet die ``millis()``-Funktion, um die vergangene Zeit zu verfolgen, ohne das Programm zu blockieren.
   * Erhöht den ``counter`` jede Sekunde und setzt ihn nach 9999 zurück.

   .. code-block:: arduino

      void loop() {
        unsigned long currentMillis = millis();

        // Update the counter every 1000 milliseconds (1 second)
        if (currentMillis - previousMillis >= 1000) {
          previousMillis = currentMillis;
          counter++; // Increment the counter
          if (counter > 9999) {
            counter = 0; // Reset counter after 9999
          }
        }

        // Display the counter value
        displayNumber(counter);
      }

#. Anzeige der Zahl:

   * Zerlegt den ``counter``-Wert in Tausender-, Hunderter-, Zehner- und Einerstellen.
   * Aktiviert jede Ziffer nacheinander, sendet die zugehörigen Segmentdaten und deaktiviert die Ziffer wieder.
   * Das schnelle Umschalten zwischen den Ziffern erzeugt die Illusion, dass alle Ziffern gleichzeitig angezeigt werden.

   .. code-block:: arduino

      void displayNumber(int num) {
        // Break the number into individual digits
        int digits[4];
        digits[0] = num / 1000;         // Thousands
        digits[1] = (num / 100) % 10;   // Hundreds
        digits[2] = (num / 10) % 10;    // Tens
        digits[3] = num % 10;           // Units

        // Display each digit one by one
        for (int i = 0; i < 4; i++) {
          digitalWrite(digitPins[i], LOW); // Activate current digit

          // Shift out the segment data for the current digit
          shiftOutDigit(digitCodes[digits[i]]);

          delay(5);                        // Small delay for multiplexing
          digitalWrite(digitPins[i], HIGH); // Deactivate current digit
        }
      }

#. Segment-Daten an das Schieberegister senden:

   * Überträgt die Segmentdaten an das 74HC595-Schieberegister.
   * ``shiftOut()`` sendet die Daten Bit für Bit, beginnend mit dem höchstwertigen Bit (``MSBFIRST``).
   * Die Daten werden durch Umschalten des ``LATCH_PIN`` an die Ausgangspins übernommen.

   .. code-block:: arduino

      void shiftOutDigit(byte data) {
        // Daten an das Schieberegister senden
        digitalWrite(LATCH_PIN, LOW);
        shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
        digitalWrite(LATCH_PIN, HIGH);
      }
  
**Weitere Experimente**



* Einen Reset-Knopf hinzufügen:

  Einen Taster an den Pico anschließen, um den Zähler beim Drücken zurückzusetzen.

* Unterschiedliche Daten anzeigen: 

  Den Code so modifizieren, dass Sensormesswerte wie Temperatur oder Lichtstärke dargestellt werden.

* Eine Stoppuhr erstellen:

  Start-, Stopp- und Reset-Funktionen implementieren, um das Display als Stoppuhr zu nutzen.

**Fazit**

Dieses Projekt zeigt, wie eine 4-stellige 7-Segment-Anzeige mithilfe eines Schieberegisters und Multiplexing-Techniken gesteuert wird. Durch das effiziente Zeitmanagement mit ``millis()`` wird ein reaktionsschneller und präziser Zeitmesser geschaffen, ohne die Performance der Anzeige zu beeinträchtigen.
