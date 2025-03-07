.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_7seg:

5.2 Zahlen auf einer 7-Segment-Anzeige darstellen
===========================================================

In dieser Lektion lernen wir, wie man eine **7-Segment-Anzeige** mit dem Raspberry Pi Pico 2 und einem **74HC595-Schieberegister** verwendet, um Zahlen darzustellen. Die 7-Segment-Anzeige ist eine häufig verwendete elektronische Komponente, die beispielsweise in Digitaluhren, Taschenrechnern und Haushaltsgeräten zur Anzeige numerischer Informationen eingesetzt wird.

Durch die Kombination des 74HC595-Schieberegisters mit der 7-Segment-Anzeige können wir alle Segmente mit nur wenigen GPIO-Pins des Pico steuern und dadurch wertvolle I/O-Ressourcen für andere Komponenten sparen.

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

**Funktionsweise der 7-Segment-Anzeige**

Eine 7-Segment-Anzeige besteht aus sieben LEDs (Segmente), die in einer Acht-Form angeordnet sind, um Ziffern von 0 bis 9 darzustellen. Zusätzlich gibt es eine achte LED für den Dezimalpunkt. Jedes Segment ist von **a** bis **g** beschriftet, der Dezimalpunkt als **dp**.

Hier ist die Segmentbeschriftung:

|img_7seg_cathode|

Bei einer **gemeinsamen Kathoden-7-Segment-Anzeige** sind alle Kathoden (negative Anschlüsse) der LEDs gemeinsam an Masse angeschlossen.



**Schaltplan**

|sch_74hc_7seg|

Die Verdrahtung folgt im Wesentlichen dem Prinzip von :ref:`py_74hc_led`, mit dem Unterschied, dass Q0-Q7 mit den Pins a ~ g der 7-Segment-Anzeige verbunden sind.

.. list-table:: Verdrahtung
    :widths: 15 25
    :header-rows: 1

    *   - 74HC595
        - LED-Segmentanzeige
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

Wir werden ein Programm schreiben, das die 7-Segment-Anzeige steuert, indem serielle Daten an das 74HC595-Schieberegister gesendet werden. Die Anzeige wird die Zahlen 0 bis 9 in einer Schleife anzeigen.

.. note::

   * Sie können die Datei ``5.2_number_display.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/5.2_number_display`` öffnen.
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: arduino

    // Pins für das 74HC595 definieren
    const int DS = 0;    // GPIO 0 -> DS (Pin 14)
    const int SHCP = 1;  // GPIO 1 -> SHCP (Pin 11)
    const int STCP = 2;  // GPIO 2 -> STCP (Pin 12)

    // Hexadezimale Codes für die Zahlen 0-9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige
    const byte numArray[] = {
      0x3F, // 0: 00111111
      0x06, // 1: 00000110
      0x5B, // 2: 01011011
      0x4F, // 3: 01001111
      0x66, // 4: 01100110
      0x6D, // 5: 01101101
      0x7D, // 6: 01111101
      0x07, // 7: 00000111
      0x7F, // 8: 01111111
      0x6F  // 9: 01101111
    };

    void setup() {
      // Initialisieren der Steuerpins als Ausgänge
      pinMode(DS, OUTPUT);
      pinMode(SHCP, OUTPUT);
      pinMode(STCP, OUTPUT);
    }

    void loop() {
      // Zahlen 0-9 durchlaufen
      for (int num = 0; num < 10; num++) {
        // STCP auf LOW setzen, um Daten vorzubereiten
        digitalWrite(STCP, LOW);

        // Daten in das Schieberegister schieben
        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

        // STCP auf HIGH setzen, um die Daten zu übernehmen
        digitalWrite(STCP, HIGH);

        delay(1000); // Eine Sekunde warten, bevor die nächste Zahl angezeigt wird
      }

      // Nach der Anzeige von 0-9 alle Segmente ausschalten
      digitalWrite(STCP, LOW);
      shiftOut(DS, SHCP, MSBFIRST, 0x00);
      digitalWrite(STCP, HIGH);
      delay(1000);
    }

Nach dem Hochladen des Codes sollte die Anzeige die Zahlen 0 bis 9 in einer Schleife durchlaufen, wobei jede Zahl für eine Sekunde angezeigt wird. 
Nach der 9 sollten alle Segmente für eine Sekunde ausgeschaltet werden, bevor die Sequenz erneut beginnt.

**Verständnis des Codes**

#. Definition der Steuerpins:

   * ``DS (Data Serial Input)``: Empfängt serielle Daten, die in das Register übertragen werden.
   * ``SHCP (Shift Register Clock Input)``: Steuert das Schieben von Daten in das Register.
   * ``STCP (Storage Register Clock Input)``: Steuert das Übernehmen der Daten vom Schieberegister zu den Ausgangspins.

   .. code-block:: arduino

        const int DS = 0;    // GPIO 0 -> DS (Pin 14)
        const int SHCP = 2;  // GPIO 2 -> SHCP (Pin 11)
        const int STCP = 1;  // GPIO 1 -> STCP (Pin 12)

#. Erstellung von Datenmustern:

   * ``numArray``: Ein Array, das die hexadezimalen Codes zur Anzeige der Zahlen 0–9 auf einer gemeinsamen Kathoden-7-Segment-Anzeige enthält.
   * Jede hexadezimale Zahl entspricht den Segmenten, die zur Darstellung einer bestimmten Zahl aktiviert werden müssen.

   .. code-block:: arduino

        const byte numArray[] = {
          0x3F, // 0: 00111111
          0x06, // 1: 00000110
          0x5B, // 2: 01011011
          0x4F, // 3: 01001111
          0x66, // 4: 01100110
          0x6D, // 5: 01101101
          0x7D, // 6: 01111101
          0x07, // 7: 00000111
          0x7F, // 8: 01111111
          0x6F  // 9: 01101111
        };

   Wenn die 7-Segment-Anzeige die Zahl „1“ darstellen soll, müssen die Segmente b und c eingeschaltet werden, während a, d, e, f, g und dp ausgeschaltet bleiben.

   |img_1_segment|

   Dafür muss die Binärzahl „00000110“ geschrieben werden. Zur besseren Lesbarkeit verwenden wir die hexadezimale Darstellung „0x06“.

#. Setup-Funktion:

   * Setzt die Pins ``DS``, ``SHCP`` und ``STCP`` als Ausgänge zur Steuerung des Schieberegisters.

   .. code-block:: arduino

        void setup() {
          // Initialisieren der Steuerpins als Ausgänge
          pinMode(DS, OUTPUT);
          pinMode(SHCP, OUTPUT);
          pinMode(STCP, OUTPUT);
        }

#. Loop-Funktion: Die ``for``-Schleife durchläuft jedes Muster im ``numArray``-Array.

   * Datenübertragung:

     * ``shiftOut`` sendet die Bytes nacheinander bitweise.
     * ``MSBFIRST`` gibt an, dass das höchstwertige Bit zuerst gesendet wird.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, numArray[num]);

   * Latch-Daten:

     * ``STCP`` wird auf ``LOW`` gesetzt, um das Schieberegister auf neue Daten vorzubereiten.
     * Nach dem Übertragen der Daten wird ``STCP`` auf ``HIGH`` gesetzt, um die neuen Werte in die Ausgabe zu übernehmen und die 7-Segment-Anzeige zu aktualisieren.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * ``delay(500);`` fügt eine halbe Sekunde Pause zwischen den Mustern ein, um sie gut sichtbar zu machen.

   * Ausschalten aller Segmente: Nachdem die Zahlen 0–9 angezeigt wurden, setzt der Code ``0x00``, um alle Segmente auszuschalten. Die Anzeige bleibt eine Sekunde aus, bevor die Schleife erneut startet.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0x00);
        digitalWrite(STCP, HIGH);
        delay(1000);

**Fehlersuche**

* Keine Zahlen werden angezeigt:

  * Überprüfen Sie alle Kabelverbindungen.
  * Stellen Sie sicher, dass der 74HC595 richtig mit Strom versorgt wird.
  * Vergewissern Sie sich, dass die GPIO-Pins des Pico korrekt mit dem Schieberegister verbunden sind.
  * Prüfen Sie, ob die 7-Segment-Anzeige korrekt angeschlossen ist, mit jedem Segment über einen Widerstand.

* Falsche Zahlen werden angezeigt:

  * Kontrollieren Sie die hexadezimalen Codes im numArray.
  * Überprüfen Sie, ob die Ausgänge des Schieberegisters mit den richtigen Segmenten verbunden sind.

* Flackern oder instabile Anzeige:

  * Sicherstellen, dass die Stromversorgung stabil ist.
  * Überprüfen, ob Widerstände korrekt angeschlossen sind, um den Stromfluss zu begrenzen.

**Verständnis der Segment-Codes**

Jeder Segmentcode gibt an, welche Segmente zur Darstellung einer bestimmten Ziffer aktiviert werden müssen:

* **0**: Segmente a, b, c, d, e, f (Code 0x3F)
* **1**: Segmente b, c (Code 0x06)
* **2**: Segmente a, b, g, e, d (Code 0x5B)
* **3**: Segmente a, b, c, d, g (Code 0x4F)
* **4**: Segmente b, c, f, g (Code 0x66)
* **5**: Segmente a, c, d, f, g (Code 0x6D)
* **6**: Segmente a, c, d, e, f, g (Code 0x7D)
* **7**: Segmente a, b, c (Code 0x07)
* **8**: Segmente a, b, c, d, e, f, g (Code 0x7F)
* **9**: Segmente a, b, c, d, f, g (Code 0x6F)

**Weitere Möglichkeiten zur Erweiterung**

* Steuerung mehrerer 7-Segment-Anzeigen:

  Mehrere 74HC595-Schieberegister in Reihe schalten, um mehrere 7-Segment-Anzeigen zu steuern und mehrstellige Zahlen darzustellen.

* LED-Animationen erstellen:

  Dynamische Effekte oder Lauftexte durch Anpassung der an das Schieberegister gesendeten Datenmuster.

* Integration mit Sensoren:

  Eine Kombination der 7-Segment-Anzeige mit Sensoren (z. B. Temperatur- oder Lichtsensoren), um Echtzeitdaten darzustellen.

* Bau einer digitalen Uhr:

  Mehrere 7-Segment-Anzeigen und eine Echtzeit-Uhr (RTC-Modul) verwenden, um eine funktionale digitale Uhr zu bauen.

* Nutzung des Dezimalpunkts und zusätzlicher Indikatoren:

  Den Dezimalpunkt (dp) sowie weitere Indikatoren (z. B. Doppelpunkte für eine Uhr) für komplexere Anzeigen verwenden.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie das 74HC595-Schieberegister mit dem Raspberry Pi Pico zur Steuerung einer 7-Segment-Anzeige nutzen. Durch das Senden serieller Daten an das Schieberegister können Sie mehrere Ausgänge effizient mit nur wenigen GPIO-Pins verwalten. Diese Technik spart nicht nur wertvolle I/O-Ressourcen, sondern eröffnet auch Möglichkeiten zur Erweiterung Ihrer Projekte mit weiteren LEDs, Anzeigen oder anderen Peripheriegeräten.
