.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_dht11:

6.2 Temperatur und Luftfeuchtigkeit mit dem DHT11 messen
========================================================

In dieser Lektion lernen wir, wie man den **DHT11-Temperatur- und Luftfeuchtigkeitssensor** mit dem Raspberry Pi Pico 2 verwendet. Der DHT11 ist ein kostengünstiger digitaler Sensor, der die Umgebungstemperatur und Luftfeuchtigkeit misst und kalibrierte digitale Werte liefert.

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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|


**Funktionsweise des DHT11-Sensors**

Der **DHT11** verwendet einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die Umgebungsluft zu messen. Er gibt ein digitales Signal über den Datenpin aus und ist relativ einfach zu verwenden, erfordert jedoch eine präzise Timing-Steuerung.

* Temperaturbereich: 0–50 °C mit einer Genauigkeit von ±2 °C
* Luftfeuchtigkeitsbereich: 20–80 % relative Luftfeuchtigkeit (RH) mit einer Genauigkeit von ±5 %
* Abtastrate: 1 Hz (eine Messung pro Sekunde)

**Schaltplan**

|sch_dht11|

**Verdrahtungsdiagramm**

|wiring_dht11|

**Code schreiben**

Wir schreiben ein Programm, das Temperatur- und Luftfeuchtigkeitsdaten vom DHT11-Sensor liest und die Werte im Seriellen Monitor anzeigt.

.. note::

    * Sie können die Datei ``6.2_dht11.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/6.2_dht11`` öffnen. 
    * Oder diesen Code in die **Arduino IDE** kopieren.
    * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.
    * Die ``DHT sensor library`` wird hier verwendet und kann über den **Bibliotheksverwalter** installiert werden.

      .. image:: img/lib_dht.png


.. code-block:: arduino

    #include <DHT.h>

    // Define the connection pins
    #define DHTPIN 16       // GPIO 16 -> Data pin of DHT11
    #define DHTTYPE DHT11    // Define the sensor type

    // Create a DHT object
    DHT dht(DHTPIN, DHTTYPE);

    unsigned long previousMillis = 0; // Stores the last time the display was updated
    const long interval = 2000;        // Interval at which to read sensor (milliseconds)

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
      Serial.println(F("DHT11 Sensor Test!"));
    
      // Initialize the DHT sensor
      dht.begin();
   
    }

    void loop() {
      unsigned long currentMillis = millis();

      // Update the sensor reading every 'interval' milliseconds
      if (currentMillis - previousMillis >= interval) {
        previousMillis = currentMillis;

        // Read humidity and temperature
        float humidity = dht.readHumidity();
        float temperatureC = dht.readTemperature();
        float temperatureF = dht.readTemperature(true);

        // Check if any reads failed
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }

        // Calculate heat index
        float heatIndexC = dht.computeHeatIndex(temperatureC, humidity, false);
        float heatIndexF = dht.computeHeatIndex(temperatureF, humidity);

        // Print the results to the Serial Monitor
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));
      }
    }

Nach dem Hochladen des Codes sollten die Temperatur- und Luftfeuchtigkeitswerte alle zwei Sekunden im Seriellen Monitor angezeigt werden.

.. code-block::

    DHT11 Sensor Test!
    Humidity: 45.00%  Temperature: 25.00°C 77.00°F  Heat index: 25.00°C 77.00°F
    Humidity: 46.00%  Temperature: 25.50°C 78.00°F  Heat index: 25.50°C 78.00°F
    Humidity: 47.00%  Temperature: 26.00°C 79.00°F  Heat index: 26.00°C 79.00°F

* **Luftfeuchtigkeit**: Setzen Sie den Sensor unterschiedlichen Luftfeuchtigkeitsniveaus aus, um Veränderungen in den Messwerten zu beobachten. 
* **Temperatur**: Variieren Sie die Temperatur in der Umgebung des Sensors, um die Messungen zu überprüfen.

**Verständnis des Codes**

#. Einbinden von Bibliotheken und Definieren von Konstanten:

   * ``DHT.h``: Beinhaltet die DHT-Sensorbibliothek zur einfachen Nutzung des Sensors.
   * ``DHTPIN``: Definiert den GPIO-Pin, der mit dem Daten-Pin des DHT11 verbunden ist.
   * ``DHTTYPE``: Legt den verwendeten Sensortyp fest (in diesem Fall DHT11).

   .. code-block:: arduino

        #include <DHT.h>
        #define DHTPIN 16       // GPIO 16 -> Daten-Pin des DHT11
        #define DHTTYPE DHT11    // Sensortyp definieren

#. Erstellen des ``DHT``-Objekts:

   Initialisiert ein ``DHT``-Objekt mit dem definierten Daten-Pin und Sensortyp.

   .. code-block:: arduino

        DHT dht(DHTPIN, DHTTYPE);

#. Setup-Funktion:

   * **Serielle Kommunikation**: Startet die serielle Kommunikation zur Debugging- und Datenanzeige.
   * **DHT-Sensorinitialisierung**: Bereitet den DHT11-Sensor auf die Datenerfassung vor.

   .. code-block:: arduino

        void setup() {
          // Initialize serial communication at 115200 baud
          Serial.begin(115200);
          Serial.println(F("DHT11 Sensor Test!"));

          // Initialize the DHT sensor
          dht.begin();
        }

#. Loop-Funktion:

   * Zeitsteuerung mit ``millis()``: 
   
     Verwendet eine nicht blockierende Zeitsteuerung, um den Sensor alle 2 Sekunden (Intervall = 2000 Millisekunden) auszulesen.
   
     .. code-block:: arduino
   
        if (currentMillis - previousMillis >= interval) {
          previousMillis = currentMillis;
          ...
        }
   
   * Sensorwerte auslesen:
   
     * ``dht.readHumidity()``: Liest die aktuelle Luftfeuchtigkeit aus.
     * ``dht.readTemperature()``: Liest die aktuelle Temperatur in Grad Celsius aus.
     * ``dht.readTemperature(true)``: Liest die aktuelle Temperatur in Grad Fahrenheit aus.
   
   * Fehlerbehandlung:
   
     Prüft, ob einer der Messwerte fehlschlägt (gibt NaN zurück) und gibt ggf. eine Fehlermeldung aus.
   
     .. code-block:: arduino
   
        if (isnan(humidity) || isnan(temperatureC) || isnan(temperatureF)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
   
   * Berechnung des Hitzeindex:
   
     * ``dht.computeHeatIndex(temperatureC, humidity, false)``: Berechnet den Hitzeindex in Grad Celsius.
     * ``dht.computeHeatIndex(temperatureF, humidity)``: Berechnet den Hitzeindex in Grad Fahrenheit.
   
   * Ausgabe der Messwerte:
   
     Gibt Luftfeuchtigkeit, Temperatur (Celsius und Fahrenheit) sowie den Hitzeindex im Seriellen Monitor aus.
   
     .. code-block:: arduino
   
        Serial.print(F("Humidity: "));
        Serial.print(humidity);
        Serial.print(F("%  Temperature: "));
        Serial.print(temperatureC);
        Serial.print(F("°C "));
        Serial.print(temperatureF);
        Serial.print(F("°F  Heat index: "));
        Serial.print(heatIndexC);
        Serial.print(F("°C "));
        Serial.print(heatIndexF);
        Serial.println(F("°F"));

**Fehlersuche**

* Keine Messwerte angezeigt:

  * Überprüfen Sie alle Kabelverbindungen.
  * Stellen Sie sicher, dass der DHT11-Sensor mit Strom versorgt wird.
  * Prüfen Sie, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Messwerte:

  * Stellen Sie sicher, dass der DHT11-Sensor nicht beschädigt ist.
  * Prüfen Sie im Datenblatt des Sensors die korrekten Timing- und Signal-Anforderungen.

* Sensorstörungen:

  * Platzieren Sie den Sensor nicht in der Nähe von elektronischen Geräten, die Störungen verursachen könnten.
  * Achten Sie darauf, dass keine Hindernisse die Messung des Sensors beeinträchtigen.

**Weitere Experimente**

* Integration mit Displays:

  Schließen Sie ein LCD- oder OLED-Display an, um die Temperatur- und Luftfeuchtigkeitswerte anzuzeigen, ohne den Seriellen Monitor zu verwenden.

* Warnsysteme erstellen:

  Implementieren Sie einen Summer oder ein Benachrichtigungssystem, das aktiviert wird, wenn Temperatur oder Luftfeuchtigkeit bestimmte Schwellenwerte überschreiten.

* Kombination mit anderen Sensoren:

  Kombinieren Sie den DHT11 mit Bewegungsmeldern, Lichtsensoren oder anderen Umwelt-Sensoren, um ein umfassendes Überwachungssystem zu erstellen.

* Bau einer Wetterstation:

  Erweitern Sie das Projekt durch zusätzliche Sensoren wie barometrische Drucksensoren, Regenmesser und Windgeschwindigkeitssensoren, um eine vollständige Wetterstation zu realisieren.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie den DHT11-Temperatur- und Luftfeuchtigkeitssensor mit dem Raspberry Pi Pico verwenden, um Umgebungswerte zu messen und anzuzeigen. Durch die Nutzung der DHT-Bibliothek können Umweltdaten leicht in Ihre Projekte integriert werden. Eine optionale LED-Anzeige kann als visuelles Feedback dienen, um die Interaktivität Ihres Systems zu verbessern.
