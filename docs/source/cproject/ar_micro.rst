.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_micro:

2.8 Sanft Drücken
==========================

In dieser Lektion lernen wir, wie man einen **Mikroschalter** (auch bekannt als Grenztaster) mit dem Raspberry Pi Pico 2 verwendet, um zu erkennen, wann er gedrückt oder losgelassen wird. Mikroschalter werden häufig in Geräten wie Mikrowellentürschaltern, Druckerabdeckungen oder als Endschalter in 3D-Druckern verwendet, da sie zuverlässig sind und häufige Betätigungen aushalten.

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Verständnis des Mikroschalters**

Ein Mikroschalter hat typischerweise drei Pins:

|img_micro_switch|

- **Common (C)**: Der mittlere Pin.
- **Normally Open (NO)**: Verbunden mit dem Common-Pin, wenn der Schalter **gedrückt** ist.
- **Normally Closed (NC)**: Verbunden mit dem Common-Pin, wenn der Schalter **nicht gedrückt** ist.

Durch entsprechendes Verbinden des Schalters können wir erkennen, wann er gedrückt wird, indem wir das Spannungsniveau an einem GPIO-Pin lesen.

**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 niedrig und beim Drücken hoch.

Der Zweck des 10K-Widerstands ist es, GP14 während des Drückens niedrig zu halten.

Wenn Sie einen mechanischen Schalter drücken, können die Kontakte prellen, was zu mehreren schnellen Übergängen zwischen offenen und geschlossenen Zuständen führt. Der zwischen GP14 und GND angeschlossene Kondensator hilft, dieses Rauschen zu filtern.

* **Schalter nicht gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NC**-Pin verbunden, der mit **GND** verbunden ist.
  * **GP14** liest **LOW** (0V).

* **Schalter gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NO**-Pin verbunden, der mit **3.3V** verbunden ist.
  * **GP14** liest **HIGH** (3.3V).

**Verdrahtungsplan**

|wiring_limit_sw|


**Schreiben des Codes**

Wir werden ein einfaches Programm schreiben, das erkennt, wann der Mikroschalter gedrückt wird, und eine Nachricht auf dem Seriellen Monitor ausgibt.

.. note::

   * Sie können die Datei ``2.8_press_gently.ino`` aus ``newton-lab-kit/arduino/2.8_press_gently`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

   const int switchPin = 14;   // GPIO pin connected to the micro switch
   int switchState = 0;

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(switchPin, INPUT);  // Set the switch pin as input
   }

   void loop() {
     switchState = digitalRead(switchPin);  // Read the state of the switch

     if (switchState == HIGH) {
       Serial.println("The switch is pressed!");
     } else {
       Serial.println("The switch is not pressed.");
     }
     delay(200);  // Small delay to avoid flooding the Serial Monitor
   }

Wenn der Code ausgeführt wird und der Serielle Monitor geöffnet ist, drücken und lösen Sie den Mikroschalter.
Der Serielle Monitor zeigt "Der Schalter ist gedrückt!" an, wenn Sie den Schalter drücken, und "Der Schalter ist nicht gedrückt.", wenn Sie ihn loslassen.

**Verständnis des Codes**

#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten auf dem Seriellen Monitor auszugeben.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Einrichten des Schalter-Pins:

   Konfiguriert switchPin (GP14) als Eingang, um den Zustand des Schalters zu lesen.

   .. code-block:: Arduino

        pinMode(switchPin, INPUT);

#. Lesen des Schalterzustands:

   Liest den aktuellen Zustand des Schalters. Er ist HIGH, wenn gedrückt, und LOW, wenn nicht gedrückt.

   .. code-block:: Arduino

        switchState = digitalRead(switchPin);

#. Reaktion auf Schalterdruck:

   Gibt eine Nachricht aus, je nachdem, ob der Schalter gedrückt ist oder nicht.

   .. code-block:: Arduino

        if (switchState == HIGH) {
          Serial.println("The switch is pressed!");
        } else {
          Serial.println("The switch is not pressed.");
        }


**Alternative: Verwendung des internen Pull-Up-Widerstands**

Wenn Sie die Schaltung vereinfachen und die Anzahl der Komponenten reduzieren möchten, können Sie den internen Pull-Up-Widerstand des Pico verwenden.

* GP14 ist mit GND verbunden, wenn der Schalter gedrückt ist, also liest er LOW (0).
* GP14 liest HIGH, wenn der Schalter nicht gedrückt ist, aufgrund des internen Pull-Up-Widerstands.

* Schaltungsänderungen:

  Entfernen Sie den externen 10KΩ-Widerstand und den Kondensator.

* Mikroschalterverbindungen:

  * **Common (C) Terminal**: Verbinden Sie mit GP14 auf dem Pico.
  * **Normally Open (NO) Terminal**: Verbinden Sie mit GND auf dem Pico.
  * **Normally Closed (NC) Terminal**: Lassen Sie unverbunden.

* Code-Änderungen:

  .. code-block:: Arduino

        const int switchPin = 14;   // GPIO pin connected to the micro switch
        int switchState = 0;

        void setup() {
          Serial.begin(115200);          // Initialize Serial Monitor at 115200 baud
          pinMode(switchPin, INPUT_PULLUP);  // Enable internal pull-up resistor
        }

        void loop() {
          switchState = digitalRead(switchPin);  // Read the state of the switch

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
          delay(200);  // Small delay to avoid flooding the Serial Monitor
        }

**Entprellen des Schalters**

Mechanische Schalter können aufgrund von prellenden Kontakten Geräusche erzeugen. Um die Zuverlässigkeit Ihrer Messungen zu verbessern, können Sie eine softwareseitige Entprellung implementieren.


.. code-block:: Arduino

    const int switchPin = 14;   // GPIO pin connected to the micro switch
    int switchState = 0;        // Current state of the switch
    int lastSwitchState = HIGH; // Previous state of the switch
    unsigned long lastDebounceTime = 0;  // Time of the last state change
    unsigned long debounceDelay = 50;    // Debounce time in milliseconds

    void setup() {
      Serial.begin(115200);
      pinMode(switchPin, INPUT_PULLUP);
    }

    void loop() {
      int reading = digitalRead(switchPin);

      if (reading != lastSwitchState) {
        lastDebounceTime = millis();
      }

      if ((millis() - lastDebounceTime) > debounceDelay) {
        if (reading != switchState) {
          switchState = reading;

          if (switchState == LOW) {
            Serial.println("The switch is pressed!");
          } else {
            Serial.println("The switch is not pressed.");
          }
        }
      }

      lastSwitchState = reading;
    }

* Überprüft, ob sich die Lesung vom letzten Zustand geändert hat.
* Wenn ja, wird die ``lastDebounceTime`` zurückgesetzt.
* Wenn die Lesung nach Ablauf der Entprellverzögerung stabil bleibt, wird der neue Zustand als gültig angesehen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Mikroschalter mit dem Raspberry Pi Pico verwendet, um zu erkennen, wann er gedrückt oder losgelassen wird. Sie haben auch gesehen, wie man einen Pull-Down-Widerstand in der Schaltung einsetzt, um zuverlässige Messungen zu gewährleisten, und wie man den internen Pull-Up-Widerstand verwendet, um die Schaltung zu vereinfachen. Zusätzlich haben Sie über das Entprellen gelernt, um das Rauschen mechanischer Schalter zu handhaben.

**Weitere Erkundungen**

* **Steuerung einer LED**: Modifizieren Sie den Code, um eine LED einzuschalten, wenn der Schalter gedrückt wird.
* **Mehrere Schalter**: Versuchen Sie, weitere Mikroschalter hinzuzufügen, um verschiedene Eingaben zu erkennen.
* **Erstellen eines Zählers**: Zählen Sie, wie oft der Schalter gedrückt wird, und zeigen Sie es an.
