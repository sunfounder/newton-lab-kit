.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Verkauf aufkommende Probleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ar_lcd:

3.4 Flüssigkristallanzeige (LCD1602)
=====================================

In dieser Lektion lernen wir, wie man ein **1602 LCD** mit dem Raspberry Pi Pico 2 verwendet, um Text anzuzeigen. Das LCD1602 ist eine zeichenbasierte Flüssigkristallanzeige, die 16 Zeichen auf 2 Zeilen darstellen kann, ideal für Projekte, die Informationen wie Nachrichten, Sensorwerte oder Statusaktualisierungen anzeigen müssen.

Die direkte Verbindung eines LCD mit einem Mikrocontroller benötigt typischerweise viele GPIO-Pins, was die Funktionalität Ihres Projekts einschränken kann. Um dieses Problem zu lösen, können wir ein LCD1602-Modul verwenden, das eine **I2C-Schnittstelle** hat. Das I2C-Protokoll verwendet nur zwei Datenleitungen (SDA und SCL), was es Ihnen ermöglicht, das LCD mit nur zwei GPIO-Pins zu steuern und andere Pins für zusätzliche Sensoren oder Geräte frei zu machen.

**Verständnis von I2C auf dem Raspberry Pi Pico 2**

Der Raspberry Pi Pico 2 unterstützt I2C-Kommunikation über mehrere GPIO-Pins und bietet Flexibilität für Ihre Projekte. Er verfügt über zwei I2C-Busse, I2C0 und I2C1, und jeder kann mehreren Pin-Sets zugeordnet werden.

Hier ist eine Übersicht der I2C-fähigen Pins am Pico 2:

|pin_i2c|

Sie können jedes passende Paar von SDA- und SCL-Pins für I2C0 oder I2C1 wählen. Diese Flexibilität ermöglicht es Ihnen, Pin-Konflikte mit anderen Peripheriegeräten in Ihrem Projekt zu vermeiden.

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ITEMS IN THIS KIT
        - LINK
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd_ar|

**Verdrahtungsplan**

|wiring_lcd_ar|

**Schreiben des Codes**

.. note::

    * Sie können die Datei ``3.4_liquid_crystal_display.ino`` aus ``newton-lab-kit/arduino/3.4_liquid_crystal_display`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".
    * Die ``LiquidCrystal I2C``-Bibliothek wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_i2c_lcd.png

.. code-block:: arduino

  #include <Wire.h>
  #include <LiquidCrystal_I2C.h>

  // Set the LCD I2C address (usually 0x27 or 0x3F)
  #define LCD_ADDRESS 0x27
  #define LCD_COLUMNS 16
  #define LCD_ROWS    2

  // Initialize the library with the I2C address and dimensions
  LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

  void setup() {
    // Initialize the LCD
    lcd.init();
    lcd.backlight();  // Turn on the backlight

    // Print messages to the LCD
    lcd.setCursor(0, 0);  // Column 0, Row 0
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);  // Column 0, Row 1
    lcd.print("LCD1602 with I2C");
  }

  void loop() {
    // Nothing to do here
  }


Nach dem Hochladen des Codes auf den Raspberry Pi Pico sollte das LCD folgendes anzeigen:

* Auf der ersten Zeile: "Hello, World!"
* Auf der zweiten Zeile: "LCD1602 with I2C"

Wenn nichts auf dem Bildschirm erscheint, versuchen Sie den Kontrast einzustellen, indem Sie das kleine Potentiometer (Knopf) auf der Rückseite des LCD-Moduls drehen, bis der Text sichtbar wird.

**Verständnis des Codes**

#. Einbinden von Bibliotheken:

   * ``Wire.h``: Handhabt die I2C-Kommunikation.
   * ``LiquidCrystal_I2C.h``: Vereinfacht die Interaktion mit dem I2C-LCD.

#. Definition der LCD-Parameter:

   * ``LCD_ADDRESS``: Die I2C-Adresse des LCD-Moduls. Übliche Adressen sind 0x27 oder 0x3F. Wenn Sie unsicher sind, können Sie einen I2C-Scanner-Sketch verwenden, um die Adresse zu finden.

   .. code-block:: arduino

      #define LCD_ADDRESS 0x27
      #define LCD_COLUMNS 16
      #define LCD_ROWS    2

#. Initialisierung des LCD:

   .. code-block:: arduino

      LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

#. In der ``setup()`` Funktion:

   .. code-block:: arduino

      lcd.init();         // Initializes the LCD
      lcd.backlight();    // Turns on the backlight

#. Textanzeige:

   .. code-block:: arduino

      lcd.setCursor(0, 0);  // Sets cursor to column 0, row 0
      lcd.print("Hello, World!");

      lcd.setCursor(0, 1);  // Sets cursor to column 0, row 1
      lcd.print("LCD1602 with I2C");

**Serial Input zur Textanzeige auf dem LCD verwenden**

Wir können das Programm verbessern, indem wir Eingaben vom Serial Monitor lesen und auf dem LCD anzeigen.

* Modifizierter Code:

  .. code-block:: arduino

    #include <Wire.h>
    #include <LiquidCrystal_I2C.h>

    #define LCD_ADDRESS 0x27
    #define LCD_COLUMNS 16
    #define LCD_ROWS    2

    LiquidCrystal_I2C lcd(LCD_ADDRESS, LCD_COLUMNS, LCD_ROWS);

    void setup() {
      lcd.init();
      lcd.backlight();

      Serial.begin(115200);
      lcd.setCursor(0, 0);
      lcd.print("Enter text:");
    }

    void loop() {
      if (Serial.available() > 0) {
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("You typed:");

        String inputText = Serial.readStringUntil('\n');
        lcd.setCursor(0, 1);
        lcd.print(inputText);
      }
    }

  Nach dem Hochladen des Codes, geben Sie eine Nachricht ein und drücken Sie ``Enter``. Die Nachricht wird auf dem LCD angezeigt.

* Erklärung: 

  * Lesen von Serial Input: Überprüft, ob Daten am Serial Port verfügbar sind. Liest den Eingabetext bis zu einem Zeilenumbruch.

   .. code-block:: arduino

      if (Serial.available() > 0) {
        String inputText = Serial.readStringUntil('\n');
        // ...
      }
    

  * Anzeigen von Serial Input auf dem LCD:

    .. code-block:: arduino

      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("You typed:");
      lcd.setCursor(0, 1);
      lcd.print(inputText);

**Fehlerbehebung**

* Keine Anzeige auf dem LCD:

  * Stellen Sie den Kontrastpotentiometer auf der Rückseite des LCD-Moduls ein.
  * Überprüfen Sie die Verdrahtungsverbindungen.
  * Stellen Sie sicher, dass die richtige I2C-Adresse verwendet wird. Sie können Geräte auf dem I2C-Bus scannen. Wenn Ihr I2C LCD1602 korrekt angeschlossen ist, wird die Adresse angezeigt. Die Standardadresse ist normalerweise 0x27, aber in einigen Fällen könnte sie 0x3F sein.
  
  .. code-block:: arduino

      #include <Wire.h>

      void setup() {
          Wire.begin();
          Serial.begin(115200);
          while (!Serial); // Wait for the serial connection to be established
          Serial.println("\nI2C Scanner");
      }

      void loop() {
          byte error, address;
          int nDevices;

          Serial.println("Scanning...");

          nDevices = 0;
          for (address = 1; address < 127; address++) {
              Wire.beginTransmission(address);
              error = Wire.endTransmission();

              if (error == 0) {
                  Serial.print("I2C device found at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);

                  nDevices++;
              }else if (error == 4) {
                  Serial.print("Unknown error at address 0x");
                  if (address < 16) {
                      Serial.print("0");
                  }
                  Serial.println(address, HEX);
              }
          }
          if(nDevices == 0) {
              Serial.println("No I2C devices found\n");
          }else {
              Serial.println("done\n");
          }
          delay(5000); // Wait 5 seconds before scanning again
      }

* Falsche Zeichen angezeigt:

  * Überprüfen Sie auf lose Verbindungen.
  * Stellen Sie sicher, dass das LCD richtig initialisiert ist.

**Weitere Untersuchungen**

* Eigene Zeichen erstellen:

  Erstellen und anzeigen von eigenen Zeichen oder Symbolen auf dem LCD.

* Sensor-Datenanzeige:

  Lesen von Daten von Sensoren (z. B. Temperatur, Luftfeuchtigkeit) und Anzeigen der Messwerte auf dem LCD.

* Mehrere I2C-Geräte:

  Verbinden Sie mehrere I2C-Geräte mit dem Pico und verwalten Sie sie gleichzeitig.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man ein I2C LCD1602-Display mit dem Raspberry Pi Pico verwendet, um Text anzuzeigen. Durch die Nutzung der I2C-Schnittstelle haben wir die Anzahl der benötigten GPIO-Pins minimiert, was komplexere Projekte mit zusätzlichen Sensoren und Peripheriegeräten ermöglicht.
