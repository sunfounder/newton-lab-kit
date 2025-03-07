.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_button:

2.5 Den Tastendruck auslesen
===============================

In dieser Lektion lernen wir, wie man mit dem Raspberry Pi Pico 2 eine Taster-Eingabe liest. Bisher haben wir die GPIO-Pins hauptsächlich für Ausgaben verwendet, z. B. zum Einschalten von LEDs. Jetzt nutzen wir einen GPIO-Pin als Eingang, um zu erkennen, wann eine Taste gedrückt wird. Dies ist eine grundlegende Fähigkeit für die Entwicklung interaktiver Projekte.

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
        - :ref:`cpn_resistor`
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|


**Schaltplan**

|sch_button|

Sobald eine Seite des Tasters mit 3.3v und die andere Seite mit GP14 verbunden ist, wird GP14 auf HIGH gesetzt, wenn der Taster gedrückt wird. Wenn der Taster jedoch nicht gedrückt ist, befindet sich GP14 in einem undefinierten Zustand und kann entweder HIGH oder LOW sein. Um sicherzustellen, dass GP14 im nicht gedrückten Zustand stabil auf LOW bleibt, wird ein 10KΩ-Pull-Down-Widerstand zwischen GP14 und GND angeschlossen.

* **Taster nicht gedrückt**: GP14 ist über den Widerstand mit GND verbunden und liest **LOW (0)**.
* **Taster gedrückt**: GP14 ist mit 3,3V verbunden und liest **HIGH (1)**.

**Verdrahtungsdiagramm**

Ein vierpoliger Taster hat eine **H-Form**. Die beiden linken sowie die beiden rechten Pins sind jeweils intern verbunden. Dies bedeutet, dass die Pins erst dann elektrisch miteinander verbunden werden, wenn der Taster gedrückt wird.

|wiring_button|

**Code schreiben**

.. note::

   * Sie können die Datei ``2.5_reading_button_value.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/2.5_reading_button_value`` öffnen. 
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: Arduino

   const int buttonPin = 14;  // GPIO-Pin, der mit dem Taster verbunden ist

   void setup() {
     Serial.begin(115200);       // Serielle Kommunikation mit 115200 Baud starten
     pinMode(buttonPin, INPUT);  // Den Button-Pin als Eingang setzen
   }

   void loop() {
     int buttonState = digitalRead(buttonPin);  // Status des Tasters auslesen

     if (buttonState == HIGH) {
       Serial.println("Taste gedrückt!");
     }
     delay(100);  // Kleine Verzögerung, um mehrfaches Auslesen zu vermeiden
   }


* Nach dem Hochladen des Codes klicken Sie auf das Lupen-Symbol (Serieller Monitor) in der oberen rechten Ecke der Arduino IDE.
* Setzen Sie die Baudrate auf 115200, um mit der Zeile ``Serial.begin(115200);`` übereinzustimmen.
* Jedes Mal, wenn Sie den Taster drücken, sollte die Meldung "Taste gedrückt!" im Seriellen Monitor erscheinen.

.. image:: ../img/serial_monitor.png

**Verständnis des Codes**

#. Initialisieren der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Damit können wir Nachrichten im Seriellen Monitor ausgeben.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Festlegen des Button-Pins:

   Konfiguriert **GP14** als Eingang, um den Status des Tasters zu lesen.

   .. code-block:: Arduino

        pinMode(buttonPin, INPUT);

#. Tasterstatus auslesen:

   Liest den aktuellen Zustand des Tasters. Er ist ``HIGH``, wenn er gedrückt wird, und ``LOW``, wenn nicht.

   .. code-block:: Arduino

        int buttonState = digitalRead(buttonPin);


#. Reaktion auf das Drücken des Tasters:

   Falls der Taster gedrückt wird, gibt das Programm eine Meldung im Seriellen Monitor aus.

   .. code-block:: Arduino

        if (buttonState == HIGH) {
          Serial.println("You pressed the button!");
        }


**Alternative: Pull-Up-Widerstand verwenden**

Sie können den Taster auch mit einem Pull-Up-Widerstand anschließen. In dieser Konfiguration:

* **Taster nicht gedrückt**: GP14 ist über einen Widerstand mit 3.3V verbunden und liest HIGH (1).
* **Taster gedrückt**: GP14 wird direkt mit GND verbunden und liest LOW (0).

**Verkabelung:**

  * Verbinden Sie einen 10KΩ-Widerstand von GP14 zu 3.3V.
  * Verbinden Sie eine Seite des Tasters mit GP14.
  * Verbinden Sie die andere Seite des Tasters mit GND.

**Code-Anpassung:**

  Ändern Sie die Bedingung in der ``if``-Anweisung:

  .. code-block:: Arduino

        if (buttonState == LOW) {
          Serial.println("You pressed the button!");
        }

**Interner Pull-Up-Widerstand des Pico verwenden**

Der Raspberry Pi Pico 2 erlaubt es, einen internen Pull-Up-Widerstand zu aktivieren, sodass kein externer Widerstand benötigt wird.

Vorteile: Einfachere Verdrahtung und Platzersparnis auf dem Breadboard.

* **Taster nicht gedrückt**: GP14 liest HIGH (1) durch den internen Pull-Up-Widerstand.
* **Taster gedrückt**: GP14 wird mit GND verbunden und liest LOW (0).

**Verkabelung:**

  * Entfernen Sie den 10KΩ-Widerstand.

**Code-Anpassung:**

  * Setzen Sie den Button-Pin als INPUT_PULLUP.
  * Ändern Sie die Bedingung in der ``if``-Anweisung.

  .. code-block:: Arduino

     const int buttonPin = 14;  // GPIO pin connected to the button
  
     void setup() {
       Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
       pinMode(buttonPin, INPUT_PULLUP);  // Set the button pin as input with an internal pull-up resistor
     }
  
     void loop() {
       int buttonState = digitalRead(buttonPin);  // Read the state of the button
  
       if (buttonState == LOW) {
         Serial.println("You pressed the button!");
       }
       delay(100);  // Small delay to avoid reading the button too frequently
     }


**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie mit dem Raspberry Pi Pico eine Tastereingabe auslesen. Diese Fähigkeit ermöglicht es Ihnen, interaktive Projekte zu erstellen, bei denen das Programm auf Benutzereingaben reagiert.

**Weitere Experimente**


* **LED steuern**: Ändern Sie den Code, um eine LED beim Drücken des Tasters einzuschalten.
* **Entprellung**: Implementieren Sie eine Entprell-Routine für zuverlässigere Eingaben.
* **Mehrere Taster**: Lesen Sie Eingaben von mehreren Tastern aus, um verschiedene Aktionen auszulösen.
