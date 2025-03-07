.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_rfid:

6.5 Schnittstelle zu RFID
===========================================

In dieser Lektion erkunden wir, wie man die **Radio Frequency Identification (RFID)** Technologie mit dem Raspberry Pi Pico 2 verwendet. RFID ermöglicht eine drahtlose Kommunikation zwischen einem Lesegerät und Tags, die zur Identifikation, Authentifizierung und Datenspeicherung verwendet werden können.

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten. 

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Sie können sie auch einzeln über die unten stehenden Links kaufen.

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
        - Micro USB Kabel
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

**Verständnis von RFID**

RFID-Technologie nutzt elektromagnetische Felder, um automatisch Tags zu identifizieren und zu verfolgen, die an Objekten angebracht sind. Die Tags enthalten elektronisch gespeicherte Informationen, die aus der Ferne gelesen werden können, ohne dass eine direkte Sichtverbindung erforderlich ist.

* **RFID-Lesegerät (MFRC522):** Ein Gerät, das Radiowellen aussendet, um mit RFID-Tags zu kommunizieren.
* **RFID-Tag:** Ein kleines Objekt, wie eine Karte oder ein Schlüsselanhänger, das einen Mikrochip und eine Antenne enthält. Es kann passiv (ohne Batterie) oder aktiv (mit Batterie) sein.

**Schaltplan**

|sch_rfid|

**Verdrahtungsdiagramm**

|wiring_rfid|


**Schreiben des Codes**

Wir werden zwei Programme schreiben, die den MFRC522 RFID-Leser initialisieren, auf RFID-Tags warten und deren eindeutige Kennungen (UIDs) lesen.

.. note::

   * Die ``MFRC522`` Bibliothek wird hier verwendet, Sie können sie über den **Library Manager** installieren.

      .. image:: img/lib_mfrc522.png


1. Informationen auf RFID-Tags schreiben:

   .. note::
   
      * Sie können die Datei ``6.5_rfid_read.ino`` aus ``newton-lab-kit/arduino/6.5_rfid_read`` öffnen. 
      * Oder kopieren Sie diesen Code in **Arduino IDE**.
      * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".
   
   .. code-block:: arduino
   
       #include <SPI.h>
       #include <MFRC522.h>
   
       // Define the connection pins for the RFID module
       #define SS_PIN 17    // SDA pin connected to GPIO 17 (SPI SS)
       #define RST_PIN 9    // RST pin connected to GPIO 9
   
       MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance
   
       void setup() {
         // Initialize serial communication
         Serial.begin(115200);
         while (!Serial); // Wait for serial port to connect
   
         // Initialize SPI bus
         SPI.begin();
   
         // Initialize RFID reader
         mfrc522.PCD_Init();
         Serial.println("RFID Writer Initialized!");
   
       }
   
       void loop() {
         // Check if data is available in the serial buffer
         if (Serial.available() > 0) {
           String data = Serial.readStringUntil('#'); // Read until '#' is received
           data.trim(); // Remove any trailing whitespace
   
           // Wait for a new RFID card
           Serial.println("Place your RFID tag near the reader...");
           if ( ! mfrc522.PICC_IsNewCardPresent()) {
             return;
           }
   
           // Select one of the cards
           if ( ! mfrc522.PICC_ReadCardSerial()) {
             return;
           }
   
           // Authenticate using key A
           MFRC522::MIFARE_Key key;
           for (byte i = 0; i < 6; i++) {
             key.keyByte[i] = 0xFF;
           }
   
           byte block = 4; // Example block to write to
           byte sector = mfrc522.PICC_GetUid()->uidByte[0] % 32; // Calculate sector
   
           MFRC522::StatusCode status;
           status = mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, block, &key, &(mfrc522.uid));
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Authentication failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           // Prepare data to write (16 bytes)
           byte buffer[18];
           data.getBytes(buffer, sizeof(buffer));
           buffer[16] = 0x00; // Padding
           buffer[17] = 0x00; // Padding
   
           // Write data to the block
           status = mfrc522.MIFARE_Write(block, buffer, 16);
           if (status != MFRC522::STATUS_OK) {
             Serial.print("Write failed: ");
             Serial.println(mfrc522.GetStatusCodeName(status));
             return;
           }
   
           Serial.println("Data written successfully!");
         }
       }

   Nach dem Hochladen des Codes passiert Folgendes:
   
   * Im seriellen Monitor sehen Sie:
   
     .. code-block::

        RFID Reader Initialized!
        Place your RFID tag near the reader...
   
   * Geben Sie die Daten ein, die Sie auf das RFID-Tag schreiben möchten, und beenden Sie mit dem Zeichen ``#``. Zum Beispiel:
   
     .. code-block::
   
        Hello World#
   
   * Legen Sie das RFID-Tag in die Nähe des Lesers. Beobachten Sie die Bestätigungsnachricht im seriellen Monitor:
   
     .. code-block::
       
        Data written successfully!

2. Lesen von RFID-Tags:

   .. note::
   
      * Sie können die Datei ``6.5_rfid_read.ino`` aus ``newton-lab-kit/arduino/6.5_rfid_read`` öffnen. 
      * Oder kopieren Sie diesen Code in **Arduino IDE**.
      * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".
   
   .. code-block:: arduino

        #include <SPI.h>
        #include <MFRC522.h>

        // Define the connection pins for the RFID module
        #define SS_PIN 17    // SDA pin connected to GPIO 17 (SPI SS)
        #define RST_PIN 9    // RST pin connected to GPIO 9

        MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

        void setup() {
          // Initialize serial communication
          Serial.begin(115200);
          while (!Serial); // Wait for serial port to connect

          // Initialize SPI bus
          SPI.begin();

          // Initialize RFID reader
          mfrc522.PCD_Init();
          Serial.println("RFID Reader Initialized!");
        }

        void loop() {
          // Look for new RFID cards
          if ( ! mfrc522.PICC_IsNewCardPresent()) {
            return;
          }

          // Select one of the cards
          if ( ! mfrc522.PICC_ReadCardSerial()) {
            return;
          }

          // Read the UID of the card
          Serial.print("UID tag :");
          String content= "";
          byte letter;
          for (byte i = 0; i < mfrc522.uid.size; i++) {
             content.concat(String(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " "));
             content.concat(String(mfrc522.uid.uidByte[i], HEX));
          }
          Serial.println(content);

          // Print the associated user data
          if (userData.length() > 0) {
            Serial.print("Associated Data: ");
            Serial.println(userData);
          } else {
            Serial.println("No data associated with this UID.");
          }
        }

   Nach dem Hochladen des Codes passiert Folgendes:
   
   * Im seriellen Monitor sehen Sie:
   
     .. code-block::
   
        RFID Reader Initialized!
   
   * Legen Sie ein RFID-Tag (z. B. einen Schlüsselanhänger oder eine Karte) in die Nähe des MFRC522 RFID-Moduls. Der serielle Monitor sollte sowohl die UID als auch die auf dem Tag gespeicherten Daten anzeigen:
   
     .. code-block::
   
        UID tag : 04 A3 1B 7C 3E
        Data on tag: HelloWorld

**Fehlersuche**

* Keine Anzeige von Lesungen:

  * Überprüfen Sie alle Verdrahtungsverbindungen, insbesondere die SPI-Leitungen (SCK, MOSI, MISO, SS).
  * Stellen Sie sicher, dass das RFID-Modul mit Strom versorgt wird (VCC- und GND-Verbindungen).
  * Überprüfen Sie, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Lesungen:

  * Stellen Sie sicher, dass die RFID-Tags mit dem MFRC522-Modul kompatibel sind.
  * Verwenden Sie einen anderen RFID-Tag, um tagspezifische Probleme auszuschließen.

* Schreibfehler:

  * Stellen Sie sicher, dass das RFID-Tag nicht gesperrt oder schreibgeschützt ist.
  * Überprüfen Sie, ob der Authentifizierungsschlüssel mit dem Schlüssel des Tags übereinstimmt.
  * Überprüfen Sie, ob der Datenpuffer korrekt formatiert ist und 16 Bytes nicht überschreitet.

* Signalstörungen:

  * Vermeiden Sie es, das RFID-Modul in der Nähe anderer elektronischer Geräte zu platzieren, die Störungen verursachen könnten.
  * Stellen Sie sicher, dass keine physischen Hindernisse die Kommunikation zwischen dem RFID-Tag und dem Lesegerät blockieren.

**Weitere Erkundungen**

* Zugangskontrollsysteme: 

  Implementieren Sie Türschlossmechanismen, die durch RFID-Tags gesteuert werden.

* Bestandsverwaltung: 

  Verfolgen und verwalten Sie Bestandsartikel mithilfe von RFID-Tags für automatisiertes Zählen und Überwachen.

* RFID-basierte Authentifizierung:
  Erstellen Sie sichere Authentifizierungssysteme für Benutzeranmeldungen oder Gerätezugriff.

* Kombination mit anderen Sensoren:

  Integrieren Sie RFID mit anderen Sensoren wie Temperatur- oder Bewegungssensoren für umfassende Überwachungssysteme.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man ein RFID-System mit dem MFRC522 RFID-Modul und dem Raspberry Pi Pico interfaced. Durch die Nutzung des SPI-Kommunikationsprotokolls und der MFRC522-Bibliothek können Sie mühelos Daten auf RFID-Tags lesen und schreiben, was eine breite Palette von Anwendungen wie Zugangskontrollsysteme, Bestandsverwaltung und interaktive Projekte ermöglicht.
