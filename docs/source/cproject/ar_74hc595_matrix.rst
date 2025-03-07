.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_788bs:

5.4 Grafiken auf einer 8x8-LED-Matrix anzeigen
===================================================================

In dieser Lektion lernen wir, wie man eine **8x8-LED-Matrix** mit dem Raspberry Pi Pico 2 und zwei **74HC595-Schieberegistern** steuert. Wir werden Muster und einfache Grafiken anzeigen, indem wir einzelne LEDs auf der Matrix steuern.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

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

Alternativ können die Komponenten auch einzeln über die untenstehenden Links erworben werden.


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

Eine 8x8-LED-Matrix besteht aus 64 LEDs, die in 8 Reihen und 8 Spalten angeordnet sind. Jede LED kann einzeln gesteuert werden, indem eine Spannung über die zugehörige Zeile und Spalte angelegt wird. Durch die Steuerung des Stroms zwischen den Reihen und Spalten können wir verschiedene Muster und Zeichen anzeigen.

In diesem Aufbau verwenden wir zwei 74HC595-Schieberegister, um die Zeilen und Spalten der LED-Matrix zu steuern. Dadurch können wir die Anzahl der benötigten GPIO-Pins des Raspberry Pi Pico 2 minimieren.

**Schaltplan**

|sch_ledmatrix|

Die 8x8-LED-Matrix wird von zwei **74HC595**-Schieberegistern gesteuert: eines kontrolliert die Reihen, das andere die Spalten. Beide Schieberegister teilen sich die GPIO-Pins **GP18**, **GP19** und **GP20** des Pico, wodurch die Anzahl der belegten I/O-Pins reduziert wird.

Der Pico sendet jeweils eine 16-Bit-Binärzahl aus. Die ersten 8 Bits steuern das Schieberegister für die Reihen, die letzten 8 Bits das Schieberegister für die Spalten. Dies ermöglicht die Darstellung bestimmter Muster auf der LED-Matrix.

**Q7' (Pin 9)**: Dieser serielle Ausgang des ersten 74HC595 ist mit dem **DS (Pin 14)** des zweiten 74HC595 verbunden, wodurch mehrere Schieberegister in Reihe geschaltet werden können.

**Verdrahtungsdiagramm**

Der Aufbau der Schaltung kann komplex sein, daher gehen wir schrittweise vor.

**Schritt 1:** Setzen Sie den Pico, die LED-Matrix und die beiden 74HC595-Chips auf 
das Breadboard. Verbinden Sie die 3,3V- und GND-Pins des Pico mit der Stromversorgung 
des Breadboards. Anschließend verbinden Sie Pin 16 und Pin 10 der beiden 
74HC595-Chips mit VCC und Pin 13 sowie Pin 8 mit GND.

.. note::
   In der Fritzing-Abbildung oben befindet sich die beschriftete Seite unten.

|wiring_ledmatrix_4|

**Schritt 2:** Verbinden Sie Pin 11 der beiden 74HC595-Chips miteinander und dann 
mit GP20. Anschließend Pin 12 der beiden Chips mit GP19, dann Pin 14 des linken 
74HC595 mit GP18, und schließlich Pin 9 mit Pin 14 des zweiten 74HC595.

|wiring_ledmatrix_3|

**Schritt 3:** Das rechte 74HC595 steuert die Spalten der LED-Matrix. Die Q0-Q7-Pins 
des 74HC595 sind mit den Pins der LED-Matrix gemäß folgender Tabelle verbunden:

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Schritt 4:** Verbinden Sie nun die Reihen der LED-Punktmatrix. Das linke 74HC595 
steuert die Reihen der LED-Matrix. Die folgende Tabelle zeigt die Zuordnung. Hier 
sehen wir, dass Q0-Q7 des linken 74HC595 den Pins 9, 14, 8, 12, 1, 7, 2 und 5 zugeordnet sind.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|


**Code schreiben**

.. note::

   * Sie können die Datei ``5.4_8x8_pixel_graphics.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/5.4_8x8_pixel_graphics`` öffnen.
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: arduino

    const int STcp = 19;  // Pin connected to ST_CP (latch pin) of 74HC595
    const int SHcp = 20;  // Pin connected to SH_CP (clock pin) of 74HC595
    const int DS = 18;    // Pin connected to DS (data pin) of 74HC595

    // Data array representing the 'X' shape on an 8x8 LED matrix
    byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};

    void setup() {
      // Set pins as outputs
      pinMode(STcp, OUTPUT);
      pinMode(SHcp, OUTPUT);
      pinMode(DS, OUTPUT);
    }

    void loop()
    {
      for(int num = 0; num <8; num++)
      {
        digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
        shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
        shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
        //return the latch pin high to signal chip that it 
        //no longer needs to listen for information
        digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
      }
    }



Nach dem Hochladen des Codes sollte die LED-Matrix ein 'X'-Muster anzeigen, indem die entsprechenden LEDs aktiviert werden. 
Falls das Muster nicht sichtbar ist, versuchen Sie, die Timing-Einstellungen anzupassen oder überprüfen Sie die Verdrahtung.

**Verständnis des Codes**

#. Pin-Definitionen:

   * ``STcp (ST_CP)``: Dient zum Übernehmen der verschobenen Daten in das Ausgangsregister bei einer steigenden Flanke.
   * ``SHcp (SH_CP)``: Verschiebt Daten bei jeder steigenden Flanke in das Register.
   * ``DS``: Serielle Dateneingabe für das Schieberegister.

   .. code-block:: arduino

      const int STcp = 19;  // Latch-Pin (ST_CP) des 74HC595
      const int SHcp = 20;  // Takt-Pin (SH_CP) des 74HC595
      const int DS = 18;    // Daten-Pin (DS) des 74HC595

#. Datenarray (``datArray``):

   * Jedes Element repräsentiert eine Zeile der LED-Matrix.
   * Die Hexadezimalwerte bestimmen, welche LEDs in der jeweiligen Zeile ein- (0) oder ausgeschaltet (1) sind.
   * Dieses Muster bildet eine symmetrische 'X'-Form auf der Matrix.

   .. code-block:: arduino

      byte datArray[] = {0x7E, 0xBD, 0xDB, 0xE7, 0xE7, 0xDB, 0xBD, 0x7E};
  

#. Setup-Funktion:

   Initialisiert die Steuerpins als Ausgänge zur Kommunikation mit den Schieberegistern.

   .. code-block:: arduino

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

#. Loop-Funktion:

   * ``num`` läuft von 0 bis 7 und repräsentiert jede Zeile der LED-Matrix.
   * ``0x80>>num`` aktiviert jeweils eine Zeile.
   * ``shiftOut()`` sendet die Spalten- und Zeilendaten an die Schieberegister, beginnend mit dem höchstwertigen Bit (``MSBFIRST``).
   * Die Daten werden durch Umschalten des ``STcp``-Pins übernommen.

   .. code-block:: arduino

      void loop()
      {
        for(int num = 0; num <8; num++)
        {
          digitalWrite(STcp,LOW); //ground ST_CP and hold low for as long as you are transmitting
          shiftOut(DS,SHcp,MSBFIRST,datArray[num]);
          shiftOut(DS,SHcp,MSBFIRST,0x80>>num);    
          //return the latch pin high to signal chip that it 
          //no longer needs to listen for information
          digitalWrite(STcp,HIGH); //pull the ST_CPST_CP to save the data
        }
      }

**Fehlersuche**

* Keine LEDs leuchten auf:

  * Überprüfen Sie alle Stromanschlüsse.
  * Stellen Sie sicher, dass die Schieberegister ordnungsgemäß mit dem Pico verbunden sind.
  
* Falsche Muster:

  * Überprüfen Sie das Datenarray auf Fehler.
  * Stellen Sie sicher, dass Reihen und Spalten korrekt mit den Schieberegistern verdrahtet sind.

* Flackern oder instabile Anzeige:

  * Passen Sie den Verzögerungswert in der Schleife an, um ein Gleichgewicht zwischen Leistung und Anzeigequalität zu finden.
  * Stellen Sie sicher, dass die Stromversorgung stabil ist und ausreicht, um die Anzahl der LEDs zu betreiben.


**Weitere Experimente**

* Ändern des Musters

  Ersetzen Sie das Musterarray durch die folgenden Arrays, um verschiedene Grafiken anzuzeigen. Ersetzen Sie das Muster in Ihrem Code durch ``pattern_heart`` oder ``pattern_smile``, um unterschiedliche Bilder darzustellen.

  .. code-block:: arduino

      // Heart shape pattern
      byte pattern_heart[] = {
        0xFF, // 11111111
        0x99, // 10011001
        0x00, // 00000000
        0x00, // 00000000
        0x00, // 00000000
        0x81, // 10000001
        0xC3, // 11000011
        0xE7  // 11100111
      };

      // Smile face pattern
      byte pattern_smile[] = {
        0xC3, // 11000011
        0xBD, // 10111101
        0x5A, // 01011010
        0x7E, // 01111110
        0x5A, // 01011010
        0x66, // 01100110
        0xBD, // 10111101
        0xC3  // 11000011
      };

* Animation auf der Anzeige

  Erstellen Sie mehrere Muster und wechseln Sie zwischen ihnen, um Animationen zu erzeugen:

  .. code-block:: arduino
        
      const int STcp = 19;  // Pin connected to ST_CP (latch pin) of 74HC595
      const int SHcp = 20;  // Pin connected to SH_CP (clock pin) of 74HC595
      const int DS = 18;    // Pin connected to DS (data pin) of 74HC595

      // Heart shape pattern
      byte pattern_heart[] = { 0xFF, 0x99, 0x00, 0x00, 0x00, 0x81, 0xC3, 0xE7 };

      // Smile face pattern
      byte pattern_smile[] = { 0xC3, 0xBD, 0x5A, 0x7E, 0x5A, 0x66, 0xBD, 0xC3 };

      void setup() {
        // Set pins as outputs
        pinMode(STcp, OUTPUT);
        pinMode(SHcp, OUTPUT);
        pinMode(DS, OUTPUT);
      }

      void latchData() {
        // Latch the shifted data to the output pins of the 74HC595
        digitalWrite(STcp, HIGH);  // Latch data
        digitalWrite(STcp, LOW);   // Prepare for the next data transmission
      }

      void displayPattern(byte pattern[]) {
        for (int repeat = 0; repeat < 500; repeat++) {  // Display the pattern for a certain duration
          for (int row = 0; row < 8; row++) {
            // Begin data transmission
            digitalWrite(STcp, LOW);  // Prepare to shift data

            // Shift out column data (pattern for the current row)
            shiftOut(DS, SHcp, MSBFIRST, pattern[row]);

            // Shift out row data (activating one row at a time)
            shiftOut(DS, SHcp, MSBFIRST, 1 << row);

            // Latch the data to display
            latchData();

            // Short delay for persistence of vision
            delay(1);
          }
        }
      }

      void loop() {
        // Continuously display patterns: heart and smiley face
        displayPattern(pattern_heart);  // Display the heart shape
        displayPattern(pattern_smile);  // Display the smiley face
      }

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie eine 8x8-LED-Matrix mit dem Raspberry Pi Pico und zwei 74HC595-Schieberegistern steuern. Durch den Einsatz von Schieberegistern können Sie mehrere LEDs effizient mit minimaler GPIO-Nutzung verwalten und so komplexere und interaktive Projekte realisieren. Das Verständnis der seriellen Datenübertragung und deren Umwandlung in parallele Ausgänge ermöglicht die Erstellung dynamischer Muster und Grafiken auf der LED-Matrix.

