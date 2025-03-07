.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_water:

2.14 Wasserstandserkennung
==============================

In dieser Lektion werden wir lernen, wie man einen **Wassersensor** mit dem Raspberry Pi Pico 2 verwendet, um das Vorhandensein von Wasser oder den Wasserstand zu erkennen. Dieser Sensor wird häufig in Projekten zur Erkennung von Regenfall, Überwachung des Wasserstands und Warnung bei Flüssigkeitsleckagen verwendet.

**Funktionsweise des Wassersensors**

Der Wassersensor verfügt über eine Reihe von freiliegenden parallelen Drahtbahnen, die Wassertröpfchen erkennen oder das Volumen von Wasser messen. Sobald Wasser mit diesen Bahnen in Kontakt kommt, gibt der Sensor ein analoges Signal aus. Je mehr Wasser mit dem Sensor in Kontakt kommt, desto höher ist der Ausgabewert, der vom Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 gelesen werden kann.

|img_water_sensor|

* Tauchen Sie den Sensor nicht vollständig ins Wasser ein. Nur der Bereich mit den freiliegenden Bahnen sollte mit Wasser in Kontakt kommen.
* Die Verwendung des Sensors in feuchter Umgebung bei Betrieb kann zu schnellerer Korrosion der Sonde führen, daher wird empfohlen, den Sensor nur bei der Messung einzuschalten.

**Was Sie benötigen**

Für dieses Projekt benötigen wir folgende Komponenten.

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

Sie können diese auch einzeln über die unten stehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - ANZAHL
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
        - :ref:`cpn_water_level`
        - 1
        - 


**Schaltplan**

|sch_water|


**Verdrahtungsplan**


|wiring_water|


**Code schreiben**

.. note::

   * Sie können die Datei ``2.14_feel_the_water_level.ino`` aus ``newton-lab-kit/arduino/2.14_feel_the_water_level`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

   const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);  // Initialize Serial Monitor
   }

   void loop() {
     // Read the analog value from the water sensor
     int sensorValue = analogRead(waterSensorPin);
     // Print the sensor value to the Serial Monitor
     Serial.print("Water Sensor Value: ");
     Serial.println(sensorValue);
     delay(500);  // Wait half a second before reading again
   }

Nach dem Hochladen des Codes öffnen Sie den Seriellen Monitor, und Sie sollten eine Reihe von Zahlen sehen, die die analogen Werte vom Wassersensor darstellen.

* Die Sensorwerte sollten niedrig sein (nahe 0), wenn der Sensor trocken ist.
* Tauchen Sie den Sensor vorsichtig ins Wasser, beginnend von unten. Wenn mehr von den Bahnen des Sensors untergetaucht sind, sollten die Sensorwerte steigen.

**Verständnis des Codes**

#. Definieren des Sensorpins:

   Weist ``waterSensorPin`` GPIO 28 zu, der mit dem analogen Eingang verbunden ist.

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)


#. Initialisieren der seriellen Kommunikation:

   Startet die serielle Kommunikation, die das Ausgeben von Nachrichten auf dem Seriellen Monitor ermöglicht.

   .. code-block:: arduino

      Serial.begin(115200);

#. Lesen des analogen Werts:

   Liest die analoge Spannung am ``waterSensorPin`` und gibt einen Wert zwischen 0 und 1023 zurück (für 10-Bit-ADC).

   .. code-block:: arduino

      int sensorValue = analogRead(waterSensorPin);

#. Ausgabe des Sensorwerts:

   Gibt den Sensorwert auf dem Seriellen Monitor aus.

   .. code-block:: arduino

      Serial.print("Water Sensor Value: ");
      Serial.println(sensorValue);

#. Hinzufügen einer Verzögerung:

   Wartet 500 Millisekunden vor der nächsten Messung.

   .. code-block:: arduino

      delay(500);


**Den Wassersensor als digitalen Sensor verwenden**

Sie können das analoge Eingabemodul als digitalen Sensor nutzen, indem Sie einen Schwellenwert festlegen.

* Bestimmen Sie den Schwellenwert:

  * Lesen Sie den Sensorwert, wenn der Sensor trocken ist.
  * Verwenden Sie diesen Wert als Basiswert (z.B. wenn der trockene Wert bei etwa 100 liegt).

* Ändern Sie den Code:

   .. code-block:: arduino

      const int waterSensorPin = 28;  // Water sensor connected to GP28 (ADC2)
      const int threshold = 500;      // Set a threshold value

      void setup() {
        Serial.begin(115200);  // Initialize Serial Monitor
      }

      void loop() {
        // Read the analog value from the water sensor
        int sensorValue = analogRead(waterSensorPin);

        // Check if the sensor value exceeds the threshold
        if (sensorValue > threshold) {
          Serial.println("Water Detected!");
        } else {
          Serial.println("No Water Detected.");
        }
        delay(500);  // Wait half a second before reading again
      }

Platzieren Sie den Sensor in der Nähe eines potenziellen Leckagebereichs.
Wenn Wasser mit dem Sensor in Kontakt kommt, sollte im Seriellen Monitor "Wasser erkannt!" angezeigt werden.

**Sicherheitsvorkehrungen**

* Kurzschlüsse vermeiden:

  * Stellen Sie sicher, dass die Verbindungen sicher sind und dass der Sensor nicht über die freiliegenden Bahnen hinaus untergetaucht ist.
  * Lassen Sie nicht zu, dass Wasser den Pico oder andere elektronische Komponenten berührt.

* Korrosionsschutz:

  * Lassen Sie den Sensor nicht eingeschaltet, während er für längere Zeit untergetaucht ist.
  * Trocknen Sie den Sensor nach dem Gebrauch gründlich ab, um Korrosion zu verhindern.

**Weitere Erkundungen**

* Wasserstandsalarm:

  Fügen Sie einen Summer oder eine LED hinzu, um zu alarmieren, wenn Wasser erkannt wird.

* Automatisierte Pumpensteuerung:

  Verwenden Sie den Sensor, um eine Pumpe zu steuern, die je nach Wasserstand ein- oder ausgeschaltet wird.

* Datenaufzeichnung:

  Zeichnen Sie Wasserstandsänderungen über die Zeit zur Analyse auf.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Wassersensor mit dem Raspberry Pi Pico verwendet, um die Anwesenheit von Wasser zu erkennen oder den Wasserstand zu messen. Durch das Lesen der analogen Werte des Sensors können Sie Veränderungen des Wasserstands überwachen und entsprechend in Ihren Projekten reagieren.

