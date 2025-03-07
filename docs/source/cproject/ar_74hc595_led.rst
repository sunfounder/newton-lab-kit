.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_74hc_led:

5.1 Verwendung des 74HC595-Schieberegisters
===========================================================

In dieser Lektion lernen wir, wie man das **74HC595-Schieberegister** verwendet, um mehrere LEDs mit nur wenigen GPIO-Pins am Raspberry Pi Pico 2 zu steuern. Der 74HC595 ist ein integrierter Schaltkreis (IC), der es ermöglicht, die Anzahl der digitalen Ausgänge durch serielle Eingabe zu erweitern. Dies ist besonders nützlich, wenn viele Ausgänge gesteuert werden müssen, aber nur begrenzte GPIO-Pins zur Verfügung stehen.

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

Das **74HC595** ist ein 8-Bit-Serial-In, Parallel-Out-Schieberegister mit Ausgangsspeicher. Es ermöglicht die Umwandlung von seriellen Daten in parallele Ausgaben und erlaubt somit die Steuerung von bis zu 8 Ausgängen mit nur 3 GPIO-Pins des Pico.

**Wichtige Pins des 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serielle Dateneingabe
* **SHCP (Pin 11)**: Schieberegister-Takteingang
* **STCP (Pin 12)**: Speicheregister-Takteingang (Latch-Pin)
* **OE (Pin 13)**: Ausgangsaktivierung (Low-aktiv, mit GND verbinden)
* **MR (Pin 10)**: Master-Reset (Low-aktiv, mit 3.3V verbinden)
* **Q0-Q7 (Pins 15, 1-7)**: Parallele Ausgänge
* **VCC (Pin 16)**: Mit 3.3V verbinden
* **GND (Pin 8)**: Mit GND verbinden

**Schaltplan**

|sch_74hc_led|

**Verdrahtungsdiagramm**

|wiring_74hc_led|

**Code schreiben**

Wir schreiben ein Programm, das die LEDs steuert, die mit dem 74HC595-Schieberegister verbunden sind. Dabei werden die LEDs nacheinander eingeschaltet.

.. note::

   * Sie können die Datei ``5.1_microchip_74hc595.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/5.1_microchip_74hc595`` öffnen.
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: arduino

  // Pins für das 74HC595 definieren
  const int DS = 0;   // GPIO 0 -> DS (Pin 14)
  const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
  const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

  // Binäre Muster zur LED-Steuerung
  int datArray[] = {
    0b00000000, // Alle LEDs aus
    0b00000001, // LED 0 an
    0b00000011, // LEDs 0 und 1 an
    0b00000111, // LEDs 0, 1 und 2 an
    0b00001111, // LEDs 0, 1, 2 und 3 an
    0b00011111, // LEDs 0 bis 4 an
    0b00111111, // LEDs 0 bis 5 an
    0b01111111, // LEDs 0 bis 6 an
    0b11111111  // Alle LEDs an
  };

  void setup() {
    // Steuerpins als Ausgänge initialisieren
    pinMode(DS, OUTPUT);
    pinMode(SHCP, OUTPUT);
    pinMode(STCP, OUTPUT);
  }

  void loop() {
    // Muster aus datArray durchlaufen
    for (int num = 0; num < 9; num++) {
      // STCP auf LOW setzen, um Daten vorzubereiten
      digitalWrite(STCP, LOW);

      // Daten ins Schieberegister schieben
      shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

      // STCP auf HIGH setzen, um die Daten zu übernehmen
      digitalWrite(STCP, HIGH);

      delay(500); // 500 ms warten, bevor das nächste Muster angezeigt wird
    }

    // Nach der Sequenz alle LEDs ausschalten
    digitalWrite(STCP, LOW);
    shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
    digitalWrite(STCP, HIGH);
    delay(500);
  }

Nach dem Hochladen des Codes sollten die mit dem 74HC595 verbundenen LEDs nacheinander aufleuchten, entsprechend den im ``datArray`` definierten Mustern. 
Sobald alle LEDs eingeschaltet sind, werden sie der Reihe nach wieder ausgeschaltet.

**Verständnis des Codes**

#. Definition der Steuerpins:

   * ``DS (Data Serial Input)``: Empfängt serielle Daten.
   * ``SHCP (Shift Register Clock Input)``: Steuert das Verschieben der Daten in das Register.
   * ``STCP (Storage Register Clock Input)``: Steuert das Übernehmen der Daten zu den Ausgangspins.

   .. code-block:: arduino

      const int DS = 0;   // GPIO 0 -> DS (Pin 14)
      const int SHCP = 1; // GPIO 1 -> SHCP (Pin 11)
      const int STCP = 2; // GPIO 2 -> STCP (Pin 12)

#. Erstellung von Datenmustern:

   * Ein Array ``datArray`` speichert verschiedene Binärmuster zur Steuerung der LEDs.
   * Jedes Bit repräsentiert den Zustand einer LED (1 = an, 0 = aus).

   .. code-block:: arduino

      int datArray[] = {
        0b00000000, // Alle LEDs aus
        0b00000001, // LED 0 an
        0b00000011, // LEDs 0 und 1 an
        0b00000111, // LEDs 0, 1 und 2 an
        0b00001111, // LEDs 0, 1, 2 und 3 an
        0b00011111, // LEDs 0 bis 4 an
        0b00111111, // LEDs 0 bis 5 an
        0b01111111, // LEDs 0 bis 6 an
        0b11111111  // Alle LEDs an
      };
  
#. Setup-Funktion:

   * Setzt die Pins ``DS``, ``SHCP`` und ``STCP`` als Ausgänge zur Steuerung des Schieberegisters.

   .. code-block:: arduino

      void setup() {
        // Initialisieren der Steuerpins als Ausgänge
        pinMode(DS, OUTPUT);
        pinMode(SHCP, OUTPUT);
        pinMode(STCP, OUTPUT);
      }

#. Loop-Funktion: Die ``for``-Schleife durchläuft jedes Muster im ``datArray``-Array.

   * Datenübertragung:

     * ``shiftOut`` sendet die Daten bitweise an das Schieberegister.
     * ``MSBFIRST`` gibt an, dass das höchstwertige Bit zuerst gesendet wird.

     .. code-block:: arduino

        shiftOut(DS, SHCP, MSBFIRST, datArray[num]);

   * Datenübernahme:

     * ``STCP`` wird auf ``LOW`` gesetzt, um das Schieberegister auf neue Daten vorzubereiten.
     * Nach dem Übertragen der Daten wird ``STCP`` auf ``HIGH`` gesetzt, um die neuen Werte zu übernehmen und die LED-Zustände zu aktualisieren.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        // shiftOut(...)
        digitalWrite(STCP, HIGH);

   * Verzögerung:
   
     ``delay(500);`` sorgt für eine halbe Sekunde Pause zwischen den Mustern für eine bessere Sichtbarkeit.

   * Ausschalten der LEDs: 
     
     Nachdem alle Muster durchlaufen wurden, werden alle LEDs ausgeschaltet, indem ``0b00000000`` gesendet wird.

     .. code-block:: arduino

        digitalWrite(STCP, LOW);
        shiftOut(DS, SHCP, MSBFIRST, 0b00000000);
        digitalWrite(STCP, HIGH);
        delay(500);

**Fehlersuche**

* Keine LEDs leuchten auf:

  * Überprüfen Sie alle Kabelverbindungen.
  * Stellen Sie sicher, dass der 74HC595 richtig mit Strom versorgt wird.
  * Vergewissern Sie sich, dass die GPIO-Pins des Pico korrekt mit dem Schieberegister verbunden sind.

* Falsches LED-Verhalten:

  * Kontrollieren Sie die Binärmuster im ``datArray``.
  * Prüfen Sie, ob die Widerstände korrekt platziert sind, um den Strom zu begrenzen.

**Weitere Möglichkeiten zur Erweiterung**

* Steuerung anderer Geräte:

  Verwenden Sie den 74HC595 zur Ansteuerung von Relais, Motoren oder anderen leistungsstarken Geräten.

* Verkettung mehrerer Schieberegister:

  Mehrere 74HC595 hintereinanderschalten, um mit denselben drei GPIO-Pins noch mehr Ausgänge zu steuern.

* Erstellung von LED-Mustern:

  Entwickeln und implementieren Sie komplexere LED-Animationen und Muster durch Anpassung des ``datArray``.

* Integration mit Sensoren:

  Kombinieren Sie das Schieberegister mit verschiedenen Sensoren, um reaktionsschnelle und interaktive Systeme zu entwickeln.

* Aufbau einer LED-Matrix-Anzeige:

  Mehrere Schieberegister verwenden, um eine größere LED-Matrix für Anzeigen oder Beschilderungen zu erstellen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie das 74HC595-Schieberegister mit dem Raspberry Pi Pico nutzen, um mehrere LEDs mit nur drei GPIO-Pins zu steuern. Diese Technik ermöglicht eine Erweiterung der digitalen Ausgänge und eröffnet neue Möglichkeiten für komplexe und interaktive Projekte, ohne dass zusätzliche GPIO-Ressourcen erforderlich sind. Durch das Verständnis der seriellen Datenübertragung und das Speichern von Daten in parallelen Ausgängen können Sie effizient eine Vielzahl von Aktoren, Anzeigen oder anderen Peripheriegeräten in Ihre Elektronikprojekte integrieren.
