.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_temp:

2.13 Thermometer
===========================

In dieser Lektion lernen wir, wie man einen **Thermistor** mit dem Raspberry Pi Pico 2 zur Temperaturmessung verwendet. Ein Thermistor ist ein Typ von Widerstand, dessen Widerstandswert sich signifikant mit der Temperatur ändert. Speziell werden wir einen NTC-Thermistor verwenden, dessen Widerstand mit steigender Temperatur abnimmt.

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Verständnis des Thermistors**

Ein NTC-Thermistor ist ein temperatursensitiver Widerstand. Sein Widerstand verringert sich, wenn die Temperatur steigt. Indem wir ihn in einen Spannungsteiler einbauen, können wir die Spannung über ihm messen, die sich mit der Temperatur ändert. Mit dem Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 können wir diese Spannung messen und die entsprechende Temperatur berechnen.

**Schaltplan**

|sch_temp|

In diesem Schaltkreis bilden ein 10K-Widerstand und ein NTC-Thermistor einen Spannungsteiler, wobei GP28 die Spannung über dem Thermistor misst. Der 10K-Widerstand bietet auch Schutz, indem er den Strom begrenzt.

* **Hohe Temperatur**: Der Widerstand des Thermistors verringert sich, wodurch auch seine Spannung und der GP28-Wert sinken. Bei sehr hohen Temperaturen nähert sich der Widerstand null, und GP28 liest nahezu 0.
* **Niedrige Temperatur**: Der Widerstand des Thermistors steigt, ebenso seine Spannung und der GP28-Wert. Bei extremer Kälte wird der Widerstand fast unendlich, und GP28 liest nahezu 1023.

Der 10K-Widerstand stellt sicher, dass 3,3V und GND nicht direkt verbunden sind, was einen Kurzschluss verhindert.

**Verdrahtungsplan**

|wiring_temp|



**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.13_thermometer.ino`` aus ``newton-lab-kit/arduino/2.13_thermometer`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

    // Define the pins
    const int thermistorPin = 28;  // Thermistor connected to GP28 (ADC2)

    // Constants for the thermistor and calculations
    const float BETA = 3950;       // Beta value of the thermistor (provided by manufacturer)
    const float SERIES_RESISTOR = 10000; // 10KΩ resistor
    const float NOMINAL_RESISTANCE = 10000; // Resistance at 25°C (provided by manufacturer)
    const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

    void setup() {
      Serial.begin(115200);  // Initialize Serial Monitor
    }

    void loop() {
      // Read the analog value from the thermistor
      int adcValue = analogRead(thermistorPin);
      // Convert the ADC value to voltage
      float voltage = adcValue * (3.3 / 1023.0);
      // Calculate the resistance of the thermistor
      float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);
      // Calculate the temperature in Kelvin using the Beta formula
      float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
      // Convert Kelvin to Celsius
      float temperatureC = temperatureK - 273.15;
      // Convert Celsius to Fahrenheit
      float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

      // Print the temperature readings
      Serial.print("Temperature: ");
      Serial.print(temperatureC);
      Serial.print(" °C, ");
      Serial.print(temperatureF);
      Serial.println(" °F");

      delay(1000);  // Wait a second before the next reading
    }

Wenn der Code läuft und der serielle Monitor offen ist:

* Sie sollten die Temperaturwerte in Celsius und Fahrenheit sehen.
* Halten Sie den Thermistor sanft zwischen Ihren Fingern. Die Temperaturanzeige sollte steigen, da der Thermistor erwärmt wird.
* Pusten Sie kalte Luft über den Thermistor oder platzieren Sie ein kaltes Objekt in der Nähe. Die Temperaturanzeige sollte sinken.

**Verständnis des Codes**

#. Definition der Pins und Konstanten:

   Weist den GPIO-Pin zu, der für das Auslesen des Thermistors verwendet wird.

   .. code-block:: arduino

        const int thermistorPin = 28;  // Thermistor connected to GP28 (ADC2)

#. Konstanten für Berechnungen:

   Diese Konstanten werden in den Berechnungen zur Bestimmung der Temperatur verwendet.

   .. code-block:: arduino

        const float BETA = 3950;       // Beta value of the thermistor
        const float SERIES_RESISTOR = 10000; // 10KΩ resistor
        const float NOMINAL_RESISTANCE = 10000; // Resistance at 25°C
        const float NOMINAL_TEMPERATURE = 25.0; // 25°C in Celsius

#. Auslesen des Analogwerts:

   Liest die analoge Spannung am thermistorPin und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: arduino

        int adcValue = analogRead(thermistorPin);

#. Berechnung der Spannung:

   Wandelt den ADC-Wert in die tatsächliche Spannung um.

   .. code-block:: arduino

        float voltage = adcValue * (3.3 / 1023.0);

#. Berechnung des Thermistorwiderstands:

   Verwendet die Formel des Spannungsteilers, um den Widerstand des Thermistors zu berechnen.

   .. code-block:: arduino

        float resistance = (voltage * SERIES_RESISTOR) / (3.3-voltage);

#. Berechnung der Temperatur:

   .. code-block:: arduino

        float temperatureK = 1 / ( (1 / (NOMINAL_TEMPERATURE + 273.15)) + (1 / BETA) * log(resistance / NOMINAL_RESISTANCE) );
        float temperatureC = temperatureK - 273.15;
        float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;

#. Ausgabe der Temperatur:

   Gibt die Temperatur in Celsius und Fahrenheit auf dem seriellen Monitor aus.

   .. code-block:: arduino

        Serial.print("Temperature: ");
        Serial.print(temperatureC);
        Serial.print(" °C, ");
        Serial.print(temperatureF);
        Serial.println(" °F");

#. Verzögerung:

   Wartet eine Sekunde, bevor die nächste Messung durchgeführt wird.

   .. code-block:: arduino

        delay(1000);

**Verständnis der Temperaturberechnung**

* Steinhart-Hart-Gleichung:

Die Steinhart-Hart-Gleichung liefert ein Modell des Widerstands des Thermistors als Funktion der Temperatur:

|temp_format|

* ``T`` ist die Temperatur des Thermistors in Kelvin.
* ``T0`` ist eine Referenztemperatur, üblicherweise bei 25°C (was in Kelvin 273.15 + 25 ist).
* ``B`` ist der Beta-Parameter des Materials, der Beta-Koeffizient des NTC-Thermistors, der in diesem Kit verwendet wird, ist 3950.
* ``R`` ist der gemessene Widerstand.
* ``R0`` ist der Widerstand bei der Referenztemperatur T0, der Widerstand des NTC-Thermistors in diesem Kit bei 25°C beträgt 10 Kilohm.

**Hinweis zur Genauigkeit**

* Thermistoren sind nichtlineare Geräte, und die Beta-Gleichung liefert eine Annäherung.
* Für genauere Temperaturmessungen über einen größeren Bereich kann die Steinhart-Hart-Gleichung verwendet werden.
* Eine Kalibrierung kann für präzise Anwendungen notwendig sein.

**Weitere Erkundungen**

* Temperaturanzeige auf einem LCD:

  Verbinden Sie ein LCD-Display, um die Temperaturwerte ohne Computer anzuzeigen.

* Datenprotokollierung:

  Erfassen Sie Temperaturwerte über einen Zeitraum, um Umweltveränderungen zu überwachen.

* Temperaturgesteuerte Geräte:

  Verwenden Sie die Temperaturwerte, um einen Ventilator oder Heizgerät zu steuern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Thermistor mit dem Raspberry Pi Pico zur Temperaturmessung verwendet. Durch das Erstellen eines Spannungsteilers und die Verwendung der Beta-Gleichung konnten Sie analoge Werte auslesen, den Widerstand berechnen und die Temperatur in Celsius und Fahrenheit bestimmen.

