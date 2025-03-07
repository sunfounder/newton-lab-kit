.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_mpu6050:

6.3 Daten aus dem MPU-6050 auslesen
=======================================

In dieser Lektion erforschen wir, wie man den **MPU-6050 6-Achsen-Bewegungssensor** mit dem Raspberry Pi Pico 2 verwendet. Der MPU-6050 kombiniert ein 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungsmesser und stellt rohe Sensordaten über das I2C-Kommunikationsprotokoll bereit.

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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Verständnis des MPU-6050 Sensors**

Der **MPU-6050**-Sensor wird häufig in Projekten eingesetzt, die Bewegungserfassung und Orientierungsdetektion erfordern, wie z. B. Drohnen, Robotik und Gaming-Geräte.

* **Beschleunigungsmesser**: Misst Beschleunigungskräfte entlang der X-, Y- und Z-Achsen. Dies umfasst die Gravitationsbeschleunigung, wodurch Sie die Neigung oder Orientierung des Sensors bestimmen können.
* **Gyroskop**: Misst die Rotationsgeschwindigkeit um die X-, Y- und Z-Achsen und liefert Informationen darüber, wie schnell der Sensor sich dreht.

**Schaltplan**

|sch_mpu6050_ar|


**Verdrahtungsplan**

|wiring_mpu6050_ar|

**Schreiben des Codes**

Wir werden ein Programm schreiben, das den MPU-6050 Sensor initialisiert, Beschleunigungs- und Gyroskopdaten liest und die Werte auf dem Seriellen Monitor ausgibt.

.. note::

    * Sie können die Datei ``6.3_6axis_motion_tracking.ino`` aus ``newton-lab-kit/arduino/6.3_6axis_motion_tracking`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".
    * Die Bibliothek ``Adafruit MPU6050`` wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_mpu6050.png

.. code-block:: arduino

    #include <Adafruit_MPU6050.h>
    #include <Wire.h>

    // Create an MPU6050 object
    Adafruit_MPU6050 mpu;

    void setup(void) {
      // Initialize Serial Communication
      Serial.begin(115200);

      Serial.println("Adafruit MPU6050 test!");

      // Try to initialize the MPU6050
      if (!mpu.begin()) {
        Serial.println("Failed to find MPU6050 chip");
        while (1) {
          delay(10);
        }
      }
      Serial.println("MPU6050 Found!");

      // Set accelerometer range
      mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
      Serial.print("Accelerometer range set to: ");
      switch (mpu.getAccelerometerRange()) {
        case MPU6050_RANGE_2_G:
          Serial.println("+-2G");
          break;
        case MPU6050_RANGE_4_G:
          Serial.println("+-4G");
          break;
        case MPU6050_RANGE_8_G:
          Serial.println("+-8G");
          break;
        case MPU6050_RANGE_16_G:
          Serial.println("+-16G");
          break;
      }

      // Set gyroscope range
      mpu.setGyroRange(MPU6050_RANGE_500_DEG);
      Serial.print("Gyro range set to: ");
      switch (mpu.getGyroRange()) {
        case MPU6050_RANGE_250_DEG:
          Serial.println("+-250 deg/s");
          break;
        case MPU6050_RANGE_500_DEG:
          Serial.println("+-500 deg/s");
          break;
        case MPU6050_RANGE_1000_DEG:
          Serial.println("+-1000 deg/s");
          break;
        case MPU6050_RANGE_2000_DEG:
          Serial.println("+-2000 deg/s");
          break;
      }

      // Set filter bandwidth
      mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
      Serial.print("Filter bandwidth set to: ");
      switch (mpu.getFilterBandwidth()) {
        case MPU6050_BAND_260_HZ:
          Serial.println("260 Hz");
          break;
        case MPU6050_BAND_184_HZ:
          Serial.println("184 Hz");
          break;
        case MPU6050_BAND_94_HZ:
          Serial.println("94 Hz");
          break;
        case MPU6050_BAND_44_HZ:
          Serial.println("44 Hz");
          break;
        case MPU6050_BAND_21_HZ:
          Serial.println("21 Hz");
          break;
        case MPU6050_BAND_10_HZ:
          Serial.println("10 Hz");
          break;
        case MPU6050_BAND_5_HZ:
          Serial.println("5 Hz");
          break;
      }

      Serial.println("");
      delay(100);
    }

    void loop() {
      // Get new sensor events with the readings
      sensors_event_t a, g, temp;
      mpu.getEvent(&a, &g, &temp);

      // Print acceleration values
      Serial.print("Acceleration X: ");
      Serial.print(a.acceleration.x);
      Serial.print(" m/s^2, Y: ");
      Serial.print(a.acceleration.y);
      Serial.print(" m/s^2, Z: ");
      Serial.print(a.acceleration.z);
      Serial.println(" m/s^2");

      // Print gyroscope values
      Serial.print("Rotation X: ");
      Serial.print(g.gyro.x);
      Serial.print(" rad/s, Y: ");
      Serial.print(g.gyro.y);
      Serial.print(" rad/s, Z: ");
      Serial.print(g.gyro.z);
      Serial.println(" rad/s");

      delay(500); // Adjust delay as needed
    }

Nach dem Hochladen des Codes sollte der Serielle Monitor kontinuierlich die Beschleunigungs- und Rotationswerte anzeigen.

.. code-block::

    Adafruit MPU6050 test!
    MPU6050 Found!
    Accelerometer range set to: +-8G
    Gyro range set to: +-500 deg/s
    Filter bandwidth set to: 21 Hz

    Acceleration X: 0.00 m/s^2, Y: 0.00 m/s^2, Z: 9.81 m/s^2
    Rotation X: 0.02 rad/s, Y: -0.01 rad/s, Z: 0.00 rad/s
    Acceleration X: 0.10 m/s^2, Y: 0.05 m/s^2, Z: 9.76 m/s^2
    Rotation X: 0.15 rad/s, Y: -0.05 rad/s, Z: 0.02 rad/s

Drehen oder bewegen Sie vorsichtig das MPU-6050-Sensormodul.
Beobachten Sie die Veränderungen in den Beschleunigungs- und Rotationswerten, die den Bewegungen entsprechen.

**Verständnis des Codes**

#. Einbinden von Bibliotheken und Definieren von Konstanten:


   * ``Adafruit_MPU6050.h``: Bindet die MPU6050-Bibliothek für eine einfachere Schnittstellensteuerung ein.
   * ``Wire.h``: Bindet die I2C-Kommunikationsbibliothek ein.
   * ``mpu``: Erstellt ein MPU6050-Objekt zur Interaktion mit dem Sensor.

#. Setup-Funktion:

   * MPU6050-Initialisierung: 
   
     Versucht, den MPU6050-Sensor zu initialisieren. Bei einem Misserfolg wird eine Fehlermeldung ausgegeben und das Programm wird angehalten.
   
     .. code-block:: arduino
   
         Serial.println("Adafruit MPU6050 test!");
   
         // Try to initialize the MPU6050
         if (!mpu.begin()) {
           Serial.println("Failed to find MPU6050 chip");
           while (1) {
             delay(10);
           }
         }
         Serial.println("MPU6050 Found!");

   * Beschleunigungsmesserbereich: 
   
     Stellt den Beschleunigungsmesserbereich auf ±8G ein und gibt den aktuellen Bereich aus.
   
     .. code-block:: arduino
   
         mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
         Serial.print("Accelerometer range set to: ");
         switch (mpu.getAccelerometerRange()) {
           case MPU6050_RANGE_2_G:
             Serial.println("+-2G");
             break;
            ...
           case MPU6050_RANGE_16_G:
             Serial.println("+-16G");
             break;
         }
   
   * Gyroskopbereich: 
   
     Stellt den Gyroskopbereich auf ±500 Grad pro Sekunde ein und gibt den aktuellen Bereich aus.
   
     .. code-block:: arduino
   
         mpu.setGyroRange(MPU6050_RANGE_500_DEG);
         Serial.print("Gyro range set to: ");
         switch (mpu.getGyroRange()) {
           case MPU6050_RANGE_250_DEG:
             Serial.println("+-250 deg/s");
             break;
            ...
           case MPU6050_RANGE_2000_DEG:
             Serial.println("+-2000 deg/s");
             break;
         }
   
   * Filterbandbreite einstellen: 
   
     Stellt die Filterbandbreite auf 21 Hz ein, um Rauschen zu reduzieren, und gibt die aktuelle Einstellung aus.
   
     .. code-block:: arduino
   
         mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
         Serial.print("Filter bandwidth set to: ");
         switch (mpu.getFilterBandwidth()) {
           case MPU6050_BAND_260_HZ:
             Serial.println("260 Hz");
             break;
            ...
           case MPU6050_BAND_5_HZ:
             Serial.println("5 Hz");
             break;
         }

#. Loop-Funktion:

   * Sensordaten lesen:
   
     * ``sensors_event_t a, g, temp;``: Erstellt Ereignisobjekte, um Beschleunigungs-, Gyroskop- und Temperaturdaten zu speichern.
     * ``mpu.getEvent(&a, &g, &temp);``: Ruft die neuesten Sensordaten ab.
   
     .. code-block:: arduino
   
         sensors_event_t a, g, temp;
         mpu.getEvent(&a, &g, &temp);
   
   * Sensordaten ausgeben:
   
     * **Beschleunigung**: Gibt Beschleunigungswerte entlang der X-, Y- und Z-Achsen in Metern pro Sekunde zum Quadrat (m/s²) aus.
     * **Rotation**: Gibt Gyroskopwerte (Rotationsgeschwindigkeit) um die X-, Y- und Z-Achsen in Radiant pro Sekunde (rad/s) aus.
   
     .. code-block:: Arduino
   
       // Print acceleration values
       Serial.print("Acceleration X: ");
       Serial.print(a.acceleration.x);
       ...
       Serial.print(g.gyro.y);
       Serial.print(" rad/s, Z: ");
       Serial.print(g.gyro.z);
       Serial.println(" rad/s");

**Fehlerbehebung**

* Keine Anzeigen:


  * Überprüfen Sie alle Verkabelungen, insbesondere die I2C-Leitungen (SCL und SDA).
  * Stellen Sie sicher, dass der MPU6050-Sensor mit Strom versorgt wird (VCC- und GND-Verbindungen).
  * Überprüfen Sie, ob die richtigen GPIO-Pins im Code definiert sind.

* Falsche Messwerte:

  * Stellen Sie sicher, dass der MPU6050-Sensor richtig im Steckbrett sitzt.
  * Überprüfen Sie, ob die Bereichs- und Filtereinstellungen des Sensors der gewünschten Anwendung entsprechen.
  * Überprüfen Sie auf lose Verbindungen oder Kurzschlüsse in der Verkabelung.

* Sensorinterferenzen:

  * Platzieren Sie den Sensor nicht in der Nähe anderer elektronischer Geräte, die Störungen verursachen könnten.
  * Stellen Sie sicher, dass keine physischen Hindernisse die Bewegung des Sensors blockieren.

**Weitere Erkundungen**

* Kombination mit anderen Sensoren:

  Integrieren Sie den MPU6050 mit GPS-Modulen, Magnetometern oder anderen Sensoren, um umfassende Tracking-Systeme zu erstellen.

* Bau eines bewegungsbasierten Spielcontrollers:

  Verwenden Sie den MPU6050, um Bewegungen und Orientierungen zu erkennen, was die Erstellung von bewegungsgesteuerten Spielgeräten ermöglicht.

* Erstellung eines selbstbalancierenden Roboters:

  Nutzen Sie die Daten des Beschleunigungsmessers und Gyroskops, um Balance und Stabilität in Roboteranwendungen zu gewährleisten.

* Implementierung von Sensor-Fusion-Algorithmen:

  Kombinieren Sie Beschleunigungs- und Gyroskopdaten, um Orientierungswinkel mit Algorithmen wie dem Kalman-Filter oder dem Komplementärfilter zu berechnen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man den MPU6050 6-Achsen-Bewegungssensor mit dem Raspberry Pi Pico verwendet. Durch die Nutzung der Adafruit MPU6050-Bibliothek können Sie einfach Beschleunigungs- und Gyroskopdaten abrufen und interpretieren, was eine Vielzahl von Bewegungs- und Orientierungsanwendungen ermöglicht. Die optionale LED-Anzeige bietet eine einfache Möglichkeit, visuelles Feedback basierend auf den Sensordaten zu geben und die Interaktivität Ihrer Projekte zu erhöhen.
