.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Werbegeschenke**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pot:

2.11 Den Knopf drehen
=======================

In dieser Lektion werden wir lernen, wie man analoge Eingänge mit dem Raspberry Pi Pico 2 liest, indem man den eingebauten Analog-Digital-Wandler (ADC) verwendet, und wie man diesen Eingang nutzt, um die Helligkeit einer LED über Pulsweitenmodulation (PWM) zu steuern. Konkret werden wir einen Potentiometer – einen variablen Widerstand – als analogen Eingabegerät verwenden. Durch das Drehen des Potentiometerknopfes passen wir die vom Pico gelesene Spannung an, die wir dann nutzen, um die Helligkeit der LED zu steuern.


**Analoge Eingänge verstehen**

Bisher haben wir mit digitalen Eingängen und Ausgängen gearbeitet, die entweder EIN (hohe Spannung) oder AUS (niedrige Spannung) sind. Viele Signale in der realen Welt sind jedoch analog, d.h. sie können kontinuierlich über einen Bereich von Werten variieren. Beispiele hierfür sind Lichtintensität, Temperatur und Schallpegel.

Der Raspberry Pi Pico 2 verfügt über einen eingebauten ADC, der es ihm ermöglicht, analoge Spannungen zu lesen und in digitale Werte umzuwandeln, die im Code verarbeitet werden können.

Die Umwandlung der analogen Spannung vom Potentiometer in einen digitalen Wert erfolgt nach der Formel:

.. code-block::

  Digitaler Wert = (Analoge Spannung / 3,3V) * 1023


**ADC-Pins des Pico**

|pin_adc|

Der Pico verfügt über drei GPIO-Pins, die für analoge Eingänge verwendet werden können:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

Zusätzlich gibt es einen vierten ADC-Kanal, der intern mit einem Temperatursensor (ADC4) verbunden ist, den wir in späteren Lektionen erkunden werden.

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
        - :ref:`cpn_resistor`
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schaltplan**

|sch_pot|

**Verdrahtungsplan**

|wiring_pot|


**Schreiben des Codes**


.. note::

   * Sie können die Datei ``2.11_turn_the_knob.ino`` aus ``newton-lab-kit/arduino/2.11_turn_the_knob`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

   // Define the pins
   const int potPin = 28;   // Potentiometer connected to GP28 (ADC2)
   const int ledPin = 15;   // LED connected to GP15 (PWM capable)

   void setup() {
     // Initialize serial communication for debugging
     Serial.begin(115200);
     // Set up the LED pin as output
     pinMode(ledPin, OUTPUT);
   }

   void loop() {
     // Read the analog value from the potentiometer (0-1023)
     int sensorValue = analogRead(potPin);
     // Print the sensor value for debugging
     Serial.println(sensorValue);

     // Map the sensor value to a PWM value (0-255)
     int brightness = map(sensorValue, 0, 1023, 0, 255);
     // Set the brightness of the LED
     analogWrite(ledPin, brightness);

     // Small delay for stability
     delay(10);
   }

Wenn der Code ausgeführt wird und der serielle Monitor geöffnet ist:

* Wenn Sie den Knopf des Potentiometers drehen, sollte die Helligkeit der LED von schwach bis hell reibungslos wechseln.
* Sie sollten die analogen Werte sehen, die gedruckt werden und von etwa 0 bis 1023 variieren, wenn Sie das Potentiometer einstellen.

**Verständnis des Codes**

#. Definition der Pins:

   Weist die GPIO-Pins, die für das Potentiometer und die LED verwendet werden, zu.

   .. code-block:: Arduino

        const int potPin = 28;   // Potentiometer connected to GP28 (ADC2)
        const int ledPin = 15;   // LED connected to GP15 (PWM capable)

#. Serielle Kommunikation initialisieren:

   Startet die serielle Kommunikation, sodass Sie Nachrichten auf den seriellen Monitor drucken können.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Den analogen Wert lesen:

   Liest die analoge Spannung an potPin (GP28) und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: Arduino

        int sensorValue = analogRead(potPin);

#. Den Sensorwert drucken:

   Gibt den aktuellen Sensorwert zum Debugging im seriellen Monitor aus.

   .. code-block:: Arduino

        Serial.println(sensorValue);

#. Den Sensorwert abbilden:

   Konvertiert den Sensorwert (0-1023) in einen Helligkeitswert, der für die PWM-Ausgabe geeignet ist (0-255).

   .. code-block:: Arduino

        int brightness = map(sensorValue, 0, 1023, 0, 255);

#. Die Helligkeit der LED einstellen:

   Passt die Helligkeit der LED an, indem der PWM-Tastgrad an ledPin (GP15) eingestellt wird.

   .. code-block:: Arduino

        analogWrite(ledPin, brightness);

#. Eine kleine Verzögerung hinzufügen:

   Eine kurze Verzögerung, um die Ablesungen zu stabilisieren und zu verhindern, dass die Schleife zu schnell läuft.

   .. code-block:: Arduino

        delay(10);

**Weiterführende Explorationen**

* **Spannung anzeigen**: Modifizieren Sie den Code, um die tatsächlich gelesene Spannung vom Potentiometer zu berechnen und anzuzeigen.

  .. code-block:: Arduino

        // Define the pins
        const int potPin = 28;  // Potentiometer connected to GP28 (ADC2)
        const int ledPin = 15;  // LED connected to GP15 (PWM capable)
        
        void setup() {
          // Initialize serial communication for debugging
          Serial.begin(115200);
          // Set up the LED pin as output
          pinMode(ledPin, OUTPUT);
        }
        
        void loop() {
          // Read the analog value from the potentiometer (0-1023)
          int sensorValue = analogRead(potPin);
        
          // Print the sensor value for debugging
          Serial.println(sensorValue);
        
          // Calculate and display the actual voltage
          float voltage = sensorValue * (3.3 / 1023.0);
          Serial.print("Voltage: ");
          Serial.print(voltage);
          Serial.println(" V");
        
          // Map the sensor value to a PWM value (0-255)
          int brightness = map(sensorValue, 0, 1023, 0, 255);
          // Set the brightness of the LED
          analogWrite(ledPin, brightness);
        
          // Small delay for stability
          delay(10);
        }

* **Mehrere LEDs steuern**: Verwenden Sie mehrere Potentiometer, um verschiedene LEDs oder Farben in einer RGB-LED zu steuern.
* **Verwendung mit anderen Sensoren**: Ersetzen Sie das Potentiometer durch einen anderen analogen Sensor, wie einen lichtabhängigen Widerstand (LDR), um die LED basierend auf dem Umgebungslicht zu steuern.


**Erklärung der Konzepte**

* Analog-Digital-Wandlung (ADC):

  * Der ADC des Pico wandelt die analoge Spannung vom Potentiometer in einen digitalen Wert um.
  * Der Spannungsbereich von 0V bis 3,3V wird in einen numerischen Wert zwischen 0 und 1023 umgewandelt.

* Pulsweitenmodulation (PWM):

  * PWM ist eine Technik, die verwendet wird, um eine analoge Spannung zu simulieren, indem ein digitaler Pin schnell zwischen HOCH und NIEDRIG geschaltet wird.
  * Durch die Anpassung des Anteils der Zeit, in der das Signal HOCH ist (Tastgrad), können wir Geräte wie LEDs und Motoren steuern.

* Werte abbilden:

  * Die Funktion ``map()`` skaliert einen Bereich von Werten auf einen anderen.
  * In diesem Fall mappen wir den Bereich des Potentiometers von 0-1023 auf den PWM-Bereich von 0-255.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man analoge Eingänge von einem Potentiometer mit dem ADC des Raspberry Pi Pico liest und diesen Eingang verwendet, um die Helligkeit einer LED über PWM zu steuern. Diese grundlegende Fähigkeit ermöglicht es Ihnen, mit einer Vielzahl von analogen Sensoren zu arbeiten und Ausgänge proportional zu steuern.


