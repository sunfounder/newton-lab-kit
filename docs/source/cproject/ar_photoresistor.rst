.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Werbegeschenke**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_photoresistor:

2.12 Das Licht fühlen
=========================

In dieser Lektion lernen wir, wie man einen **Fotowiderstand** (auch bekannt als lichtabhängiger Widerstand oder LDR) mit dem Raspberry Pi Pico 2 verwendet, um die Lichtintensität zu messen. Ein Fotowiderstand ändert seinen Widerstand abhängig von der Menge des empfangenen Lichts: Je heller das Licht, desto geringer der Widerstand. Dies macht ihn ideal für die Erkennung von Veränderungen im Umgebungslicht.

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
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Schaltplan**

|sch_photoresistor|

In diesem Schaltkreis sind ein 10K-Widerstand und ein Fotowiderstand in Reihe geschaltet, was einen Spannungsteiler bildet. GP28 liest die Spannung über dem Fotowiderstand, während der 10K-Widerstand als Schutz dient, indem er den Strom begrenzt.

* **Helles Licht**: Der Widerstand des Fotowiderstands verringert sich, was seine Spannung und den GP28-Wert senkt. Bei starkem Licht nähert sich sein Widerstand null, und GP28 liest nahezu 0. In diesem Fall spielt der 10K-Widerstand eine schützende Rolle, sodass 3.3V und GND nicht miteinander kurzgeschlossen werden.
* **Dunkelheit**: Der Widerstand des Fotowiderstands erhöht sich, was seine Spannung und den GP28-Wert erhöht. Bei völliger Dunkelheit ist sein Widerstand nahezu unendlich (der 10K-Widerstand ist vernachlässigbar), und GP28 liest nahe 1023.

Die Berechnungsformel lautet wie folgt.

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 1023

**Verdrahtungsplan**

|wiring_photoresistor|

**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.12_feel_the_light.ino`` aus ``newton-lab-kit/arduino/2.12_feel_the_light`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port und klicken Sie dann auf "Upload".

.. code-block:: Arduino

   const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
   }

   void loop() {
     // Read the analog value from the photoresistor
     int sensorValue = analogRead(sensorPin);
     // Print the sensor value to the Serial Monitor
     Serial.println(sensorValue);
     delay(500);  // Wait half a second before reading again
   }

Wenn der Code läuft und der serielle Monitor geöffnet ist:

* Beobachten der Sensorwerte:

  Sie sollten eine Reihe von Zahlen sehen, die die analogen Werte vom Fotowiderstand darstellen.

* Interaktion mit dem Fotowiderstand:

  * Leuchten Sie mit einer Taschenlampe oder einer Lampe auf den Fotowiderstand. Die Sensorwerte sollten abnehmen (da der Widerstand mit mehr Licht abnimmt).
  * Bedecken Sie den Fotowiderstand mit Ihrer Hand oder platzieren Sie ihn in einem dunklen Bereich. Die Sensorwerte sollten zunehmen (da der Widerstand mit weniger Licht zunimmt).

**Verständnis des Codes**

#. Definition des Sensorpins:

   Weist sensorPin GPIO 28 zu, der mit dem analogen Eingang verbunden ist.

   .. code-block:: arduino

        const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

#. Initialisieren der seriellen Kommunikation:

   Startet die serielle Kommunikation, um Nachrichten auf den seriellen Monitor zu drucken.

   .. code-block:: arduino

        Serial.begin(115200);

#. Lesen des analogen Werts:

   Liest die analoge Spannung an sensorPin und gibt einen Wert zwischen 0 und 1023 zurück.

   .. code-block:: arduino

        int sensorValue = analogRead(sensorPin);

#. Drucken des Sensorwerts:

   Gibt den Sensorwert auf den seriellen Monitor aus.

   .. code-block:: arduino

        Serial.println(sensorValue);

#. Hinzufügen einer Verzögerung:

   Wartet 500 Millisekunden vor der nächsten Messung.

   .. code-block:: arduino

        delay(500);

**Umrechnung in Spannung**

Wenn Sie den tatsächlich gelesenen Spannungswert sehen möchten, können Sie den Code ändern:

.. code-block:: arduino

   const int sensorPin = 28;   // Photoresistor connected to GP28 (ADC2)

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
   }

    void loop() {
      int sensorValue = analogRead(sensorPin);
      // Convert the analog reading to voltage
      float voltage = sensorValue * (3.3 / 1023.0);
      Serial.print("Sensor Value: ");
      Serial.print(sensorValue);
      Serial.print("  Voltage: ");
      Serial.print(voltage);
      Serial.println(" V");
      delay(500);
    }

**Weitere Erkundungen**

* Steuerung einer LED basierend auf Licht:

  Verwenden Sie den Fotowiderstand, um die Helligkeit einer LED zu steuern oder sie basierend auf den Lichtverhältnissen ein- oder auszuschalten.

* Datenprotokollierung:

  Protokollieren Sie die Lichtintensität über die Zeit, um Veränderungen in der Umgebung zu überwachen.

* Bau eines Nachtlichts:

  Erstellen Sie ein Licht, das sich automatisch einschaltet, wenn es dunkel wird.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Fotowiderstand mit dem Raspberry Pi Pico verwendet, um die Lichtintensität zu messen. Durch das Lesen der analogen Spannung aus einem Spannungsteilerkreis können Sie Veränderungen in den Lichtverhältnissen erkennen und diese Informationen in Ihren Projekten verwenden.



