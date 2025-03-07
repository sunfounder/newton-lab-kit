.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_mpr121:

4.3 Elektroden-Tastatur mit MPR121
========================================================

In dieser Lektion lernen wir, wie man den **MPR121 kapazitiven Berührungssensor** verwendet, um eine berührungsempfindliche Tastatur mit dem Raspberry Pi Pico 2 zu erstellen. Der MPR121 ermöglicht es Ihnen, Berührungseingaben auf bis zu 12 Elektroden zu erkennen, die mit leitfähigen Materialien wie Drähten, Folie oder sogar Früchten wie Bananen verbunden werden können!

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
        - :ref:`cpn_mpr121`
        - 1
        - 

**Verständnis des MPR121-Sensors**

Der **MPR121** ist ein kapazitiver Berührungssensor-Controller, der über die I2C-Schnittstelle kommuniziert. Er kann bis zu 12 Berührungseingaben verarbeiten, was ihn ideal für interaktive Projekte mit mehreren Berührungspunkten macht.

Der MPR121-Sensor erkennt Veränderungen in der Kapazität seiner Elektroden. Wenn Sie eine Elektrode berühren, ändert sich die Kapazität, und der Sensor registriert eine Berührung. Diese Information wird über I2C an den Raspberry Pi Pico 2 übermittelt.

**Schaltplan**

|sch_mpr121_ar|


**Verdrahtungsplan**

|wiring_mpr121_ar|

* Verbinden Sie Drähte oder leitfähige Materialien mit den Elektrodenpins (markiert als **E0** bis **E11**) am MPR121.
* Sie können die anderen Enden der Drähte mit leitfähigen Objekten wie Früchten, Aluminiumfolieformen oder Touchpads verbinden.


**Schreiben des Codes**


.. note::

    * Sie können die Datei ``4.3_electrode_keyboard.ino`` aus ``newton-lab-kit/arduino/4.3_electrode_keyboard`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".
    * Die ``Adafruit MPR121``-Bibliothek wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_mpr121.png

.. code-block:: arduino

    #include <Wire.h>
    #include <Adafruit_MPR121.h>

    // Create an instance of the MPR121 sensor
    Adafruit_MPR121 cap = Adafruit_MPR121();

    // Array to hold the touch states of each electrode
    bool touchStates[12] = { false };

    // Variables to store current and last touch states
    uint16_t currtouched = 0;
    uint16_t lasttouched = 0;

    void setup() {
      Serial.begin(115200); // Initialize serial communication at 115200 baud
      while (!Serial);    // Wait for Serial Monitor to open

      // Initialize the MPR121 sensor with I2C address 0x5A
      if (!cap.begin(0x5A)) {
        Serial.println("MPR121 not found, check wiring?");
        while (1);
      }
      Serial.println("MPR121 found!");
    }

    void loop() {
      // Get the currently touched pads
      currtouched = cap.touched();

      // Check if there is a change in touch state
      if (currtouched != lasttouched) {
        // Update the last touched state
        lasttouched = currtouched;

        // Iterate through each electrode
        for (int i = 0; i < 12; i++) {
          // Check if the electrode is touched
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

        // Print the touch states as a binary string
        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();
      }

      delay(100); // Small delay to stabilize readings
    }

Nach dem Hochladen des Codes berühren Sie die an den MPR121-Sensor angeschlossenen Elektroden. 

* Beobachten Sie die binäre Ausgabe im seriellen Monitor, die anzeigt, welche Elektroden berührt werden. 
* Zum Beispiel wird das Berühren der ersten und der elften Elektrode ``100000000010`` anzeigen.


**Verständnis des Codes**

#. Einbinden von Bibliotheken:


   * ``Wire.h``: Handhabt die I2C-Kommunikation.
   * ``Adafruit_MPR121.h``: Stellt Funktionen zur Interaktion mit dem MPR121-Sensor bereit.

#. Initialisieren des MPR121-Sensors:

   Erstellt eine Instanz des MPR121-Sensors.

   .. code-block:: arduino

      Adafruit_MPR121 cap = Adafruit_MPR121();

#. Setup-Funktion:

   * Startet die serielle Kommunikation zur Fehlerbehebung.
   * Initialisiert den MPR121-Sensor mit der I2C-Adresse 0x5A.
   * Wenn der Sensor nicht gefunden wird, wird eine Fehlermeldung ausgegeben und das Programm angehalten.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200); // Initialize serial communication
        while (!Serial);    // Wait for Serial Monitor to open

        // Initialize the MPR121 sensor with I2C address 0x5A
        if (!cap.begin(0x5A)) {
          Serial.println("MPR121 not found, check wiring?");
          while (1);
        }
        Serial.println("MPR121 found!");
      }

#. ``loop()``-Funktion: 

   * Ruft den aktuellen Berührungsstatus vom MPR121-Sensor ab. Jedes Bit in der Variablen ``currtouched`` repräsentiert den Berührungsstatus einer Elektrode (1 für berührt, 0 für nicht berührt).

     .. code-block:: arduino
  
        currtouched = cap.touched();

   * Überprüft, ob sich der Berührungsstatus seit der letzten Schleifeniteration geändert hat.

     .. code-block:: arduino

        if (currtouched != lasttouched) {
          // Update touch states
        }

   * Durchläuft jede Elektrode und aktualisiert das Array ``touchStates`` basierend darauf, ob jede Elektrode berührt wird.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          if (currtouched & (1 << i)) {
            touchStates[i] = true;
          } else {
            touchStates[i] = false;
          }
        }

   * Druckt die Berührungsstatus als 12-Bit-binären String auf den seriellen Monitor. Zum Beispiel, wenn die erste und die elfte Elektrode berührt werden, wird 100000000010 gedruckt.

     .. code-block:: arduino

        for (int i = 0; i < 12; i++) {
          Serial.print(touchStates[i] ? "1" : "0");
        }
        Serial.println();

   * Fügt eine kurze Verzögerung hinzu, um die Messungen zu stabilisieren und den seriellen Monitor nicht zu überfluten.

     .. code-block:: arduino

        delay(100);

**Erweiterung der Elektroden**

Sie können Ihr Projekt erweitern, indem Sie die Elektroden mit verschiedenen leitfähigen Materialien verbinden:

* **Früchte**: Befestigen Sie Drähte an Bananen, Äpfeln oder anderen Früchten, um sie zu berührungsempfindlichen Eingaben zu machen.
* **Folienformen**: Schneiden Sie Formen aus Aluminiumfolie aus und befestigen Sie sie an den Elektroden.
* **Leitfähige Farbe**: Zeichnen Sie Muster mit leitfähiger Tinte oder Farbe.

.. note::
    
    Wenn Sie die Elektroden ändern (z.B. unterschiedliche Materialien anschließen), müssen Sie möglicherweise den Sensor zurücksetzen, um die Baseline-Werte neu zu kalibrieren.

**Weitere Erkundungen**

* Interaktive Projekte erstellen:

  Bauen Sie eine berührungsgesteuerte LED-Matrix, bei der jede Elektrode eine einzelne LED steuert.

* Implementierung von Key Debouncing:

  Verbessern Sie die Zuverlässigkeit der Berührungserkennung durch Implementierung von Entprelltechniken, um falsche Berührungen herauszufiltern.

* Kombination mit anderen Sensoren:

  Integrieren Sie den MPR121 mit anderen Sensoren wie Temperatur- oder Lichtsensoren, um komplexere interaktive Systeme zu erstellen.

* Entwicklung eines berührungsbasierten Spielcontrollers:

  Verwenden Sie die Berührungseingaben, um Spielelemente zu steuern, wie z.B. das Bewegen von Charakteren oder das Auswählen von Optionen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man den MPR121 kapazitiven Berührungssensor mit dem Raspberry Pi Pico verwendet, um eine berührungsempfindliche Tastatur zu erstellen. Durch das Erkennen von Berührungseingaben auf mehreren Elektroden können Sie interaktive Schnittstellen für Ihre Projekte erstellen, wie benutzerdefinierte Tastaturen, Bedienfelder oder kreative Eingabegeräte. Das Verständnis, wie man Berührungseingaben liest und verarbeitet, ist eine wertvolle Fähigkeit für die Entwicklung ansprechender und benutzerfreundlicher Elektronikprojekte.
