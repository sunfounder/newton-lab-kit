.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_ultrasonic:

6.1 Messung von Entfernungen mit einem Ultraschallsensor
==========================================================

In dieser Lektion lernen wir, wie man einen **Ultraschallsensormodul** mit dem Raspberry Pi Pico 2 verwendet, um die Entfernung zu einem Objekt zu messen. Ultraschallsensoren werden häufig in Robotik und Automatisierungssystemen zur Objekterkennung und Entfernungsmessung eingesetzt.

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Verständnis des Ultraschallsensors**

Der Ultraschallsensor funktioniert, indem er einen kurzen Ultraschallimpuls vom **Trig**-Pin aussendet und das Echo am **Echo**-Pin hört. Indem die Zeit gemessen wird, die das Echo zur Rückkehr benötigt, können wir die Entfernung zu einem Objekt unter Verwendung der Schallgeschwindigkeit berechnen.

|ultrasonic_prin|

* **Triggerimpuls**: Ein 10-Mikrosekunden-Hochimpuls am Trig-Pin startet die Messung.
* **Ultraschallburst**: Der Sensor sendet einen 8-Zyklen-Ultraschallburst bei 40 kHz aus.
* **Echoempfang**: Der Echo-Pin wird hochgeschaltet und bleibt hoch, bis das Echo zurückempfangen wird.
* **Zeitmessung**: Durch Messung der Zeit, die der Echo-Pin hoch bleibt, können wir die Entfernung berechnen.

**Schaltplan**

|sch_ultrasonic|

**Verdrahtungsplan**

|wiring_ultrasonic|

**Schreiben des Codes**

Wir werden ein Programm schreiben, das den Ultraschallsensor auslöst, die Echozeit misst und die Entfernung zu einem Objekt berechnet. Die Entfernung wird auf dem Seriellen Monitor ausgegeben.

.. note::

   * Sie können die Datei ``6.1_ultrasonic.ino`` aus ``newton-lab-kit/arduino/6.1_ultrasonic`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

    // Define the connection pins
    const int trigPin = 17;  // GPIO 17 -> Trig
    const int echoPin = 16;  // GPIO 16 -> Echo

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
    
      // Initialize the sensor pins
      pinMode(trigPin, OUTPUT);
      pinMode(echoPin, INPUT);
    }

    void loop() {
      long duration;
      float distance;

      // Trigger the sensor by setting Trig HIGH for 10 microseconds
      digitalWrite(trigPin, HIGH);
      delayMicroseconds(10);
      digitalWrite(trigPin, LOW);
    
      // Read the Echo pin, returns the duration in microseconds
      duration = pulseIn(echoPin, HIGH);
    
      // Calculate the distance in centimeters
      distance = duration * 0.034 / 2;
    
      // Print the distance to the Serial Monitor
      Serial.print("Distance: ");
      Serial.print(distance);
      Serial.println(" cm");
    
      delay(500); // Wait for half a second before the next measurement
    }

Nach dem Hochladen des Codes sollte der Serielle Monitor die Entfernungsmessungen in Zentimetern anzeigen.

.. code-block:: 

    Entfernung: 25.3 cm
    Entfernung: 24.8 cm
    Entfernung: 24.5 cm

Platzieren Sie ein Objekt in unterschiedlichen Entfernungen vom Sensor.
Bewegen Sie das Objekt näher und weiter, um Änderungen in den Entfernungsmessungen zu beobachten.

**Verständnis des Codes**

#. Definition der Anschlusspins:

   * ``trigPin``: Sendet den Ultraschallimpuls.
   * ``echoPin``: Empfängt das Echo des Ultraschallimpulses.

   .. code-block:: arduino

        const int trigPin = 17;  // GPIO 17 -> Trig
        const int echoPin = 16;  // GPIO 16 -> Echo

#. Setup-Funktion:

   * **Serielle Kommunikation**: Ermöglicht die Kommunikation zwischen dem Pico und dem Computer für Debugging.
   * **Pinmodi**: Setzt den ``Trig``-Pin als ``OUTPUT`` und den ``Echo``-Pin als ``INPUT``.

   .. code-block:: arduino

        void setup() {
          // Initialize serial communication at 115200 baud
          Serial.begin(115200);

          // Initialize the sensor pins
          pinMode(trigPin, OUTPUT);
          pinMode(echoPin, INPUT);
        }

#. Loop-Funktion:

   * **Sensor auslösen**: Setzt den ``Trig``-Pin für 10 Mikrosekunden auf ``HIGH``, um den Ultraschallimpuls zu senden. Setzt den ``Trig``-Pin auf ``LOW``, um den Impuls zu beenden.

     .. code-block:: arduino

        digitalWrite(trigPin, HIGH);
        delayMicroseconds(10);
        digitalWrite(trigPin, LOW);

   * **Echo lesen**: Misst die Dauer (in Mikrosekunden), die der ``Echo``-Pin auf ``HIGH`` bleibt, was die Zeit für die Rückkehr des Echos anzeigt.

     .. code-block:: arduino

        duration = pulseIn(echoPin, HIGH);

   * **Entfernung berechnen**: Wandelt die Zeit in Entfernung (cm/Mikrosekunde) um. Teilt durch 2, um den Hin- und Rückweg des Impulses zu berücksichtigen.

     .. code-block:: arduino

        distance = duration * 0.034 / 2;

   * **Serienausgabe**: Gibt die berechnete Entfernung auf dem Seriellen Monitor zur Echtzeitüberwachung aus.

     .. code-block:: arduino

        Serial.print("Distance: ");
        Serial.print(distance);
        Serial.println(" cm");

   * **Verzögerung**: Fügt eine Verzögerung von 500 Millisekunden hinzu, um das Überfluten des Seriellen Monitors zu verhindern und Zeit zwischen den Messungen zu lassen.

**Fehlersuche**

* Keine Anzeigen:

  * Stellen Sie sicher, dass die Trig- und Echo-Pins korrekt verbunden sind.
  * Überprüfen Sie, ob der Sensor mit Strom versorgt wird (VCC- und GND-Anschlüsse).
  * Stellen Sie sicher, dass der Serielle Monitor auf die richtige Baudrate eingestellt ist.

* Falsche Messungen:

  * Stellen Sie sicher, dass die Berechnungen im Code korrekt sind.
  * Überprüfen Sie, ob die Schallgeschwindigkeitskonstante (0.034) für Ihre Umgebung geeignet ist (Feuchtigkeit und Temperatur können die Schallgeschwindigkeit beeinflussen).


* Sensorinterferenzen:

  * Stellen Sie sicher, dass keine Hindernisse oder reflektierende Oberflächen vorhanden sind, die die Ultraschallimpulse stören könnten.
  * Platzieren Sie den Sensor nicht in der Nähe anderer Ultraschallgeräte, die falsche Messungen verursachen könnten.


**Weiterführende Untersuchungen**

* Integration mit LEDs oder Displays:

  * Verwenden Sie mehrere LEDs, um einen visuellen Entfernungsindikator zu erstellen.
  * Integrieren Sie ein 7-Segment- oder LCD-Display, um die Entfernung numerisch anzuzeigen.

* Erstellen eines Näherungsalarm-Systems:

  Legen Sie Schwellenwerte fest, um Alarme auszulösen (z. B. Soundalarme, wenn Objekte zu nah kommen).

* Bau eines einfachen hindernisvermeidenden Roboters:

  Verwenden Sie den Ultraschallsensor, um Hindernisse zu erkennen und sie zu umfahren.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Ultraschallsensormodul mit dem Raspberry Pi Pico verwendet, um die Entfernung zu einem Objekt zu messen. Indem Sie Ultraschallimpulse auslösen und die Echozeit messen, können Sie die Entfernung naher Objekte genau bestimmen. Dieses Projekt dient als Grundlage für komplexere Anwendungen in Robotik, Automatisierung und interaktiven Systemen.
