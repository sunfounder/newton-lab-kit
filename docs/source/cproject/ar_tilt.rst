.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_tilt:

2.6 Neige es!
=======================

In dieser Lektion lernen wir, wie man einen Neigungsschalter mit dem Raspberry Pi Pico 2 verwendet, um Änderungen in der Orientierung zu erkennen. Ein Neigungsschalter ist ein einfaches Gerät, das erkennen kann, ob es aufrecht oder geneigt ist, und eignet sich für Anwendungen wie Bewegungserkennung, Orientierungssensorik oder als Auslöser basierend auf der Position.

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
        - :ref:`cpn_tilt`
        - 1
        - 

**Schaltplan**

|sch_tilt|

* **Im aufrechten Zustand (Schalter geschlossen)**:

  * Der Neigungsschalter verbindet **3.3V** direkt mit **GP14**.
  * Der GPIO-Pin liest **HIGH** (1).

* **Im geneigten Zustand (Schalter offen)**:

  * Der Neigungsschalter trennt **3.3V** von **GP14**.
  * Der Pull-Down-Widerstand zieht **GP14** zu **GND**.
  * Der GPIO-Pin liest **LOW** (0).

**Verdrahtung**

|wiring_tilt|


**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.6_tilt_it.ino`` aus ``newton-lab-kit/arduino/2.4_colorful_light`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

   const int tiltPin = 14;  // GPIO pin connected to the tilt switch

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(tiltPin, INPUT);    // Set the tilt pin as input
   }

   void loop() {
     int tiltState = digitalRead(tiltPin);  // Read the state of the tilt switch

     if (tiltState == HIGH) {
       Serial.println("The switch works!");
     }
     delay(100);  // Small delay to avoid flooding the Serial Monitor
   }

Wenn der Code läuft und der serielle Monitor geöffnet ist, neigen Sie das Steckbrett oder den Neigungsschalter.
Jedes Mal, wenn Sie den Schalter in die aufrechte Position neigen, sollte im seriellen Monitor "Der Schalter funktioniert!" erscheinen.

**Verständnis des Codes**

#. Initialisierung der seriellen Kommunikation:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten an den seriellen Monitor zu senden.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Einrichten des Neigungspins:

   Konfiguriert den ``tiltPin`` (GP14) als Eingang, um den Zustand des Neigungsschalters zu lesen.

   .. code-block:: Arduino

        pinMode(tiltPin, INPUT);


#. Zustand des Neigungsschalters lesen:

   Liest den aktuellen Zustand des Neigungsschalters. Er wird „HIGH“ sein, wenn aufrecht und „LOW“, wenn geneigt.

   .. code-block:: Arduino

        int tiltState = digitalRead(tiltPin);

#. Reaktion auf Neigung:

   Wenn der Neigungsschalter aufrecht (geschlossen) ist, wird eine Nachricht an den seriellen Monitor gesendet.

   .. code-block:: Arduino

        if (tiltState == HIGH) {
          Serial.println("The switch works!");
        }

**Weiteres Experimentieren**

* **Steuerung einer LED**: Modifizieren Sie den Code, um eine LED einzuschalten, wenn der Neigungsschalter aufrecht ist, und auszuschalten, wenn er geneigt ist.

  .. code-block:: Arduino

        const int tiltPin = 14;   // GPIO pin connected to the tilt switch
        const int ledPin = 15;    // GPIO pin connected to an LED

        void setup() {
          Serial.begin(115200);
          pinMode(tiltPin, INPUT);
          pinMode(ledPin, OUTPUT);
        }

        void loop() {
          int tiltState = digitalRead(tiltPin);

          if (tiltState == HIGH) {
            Serial.println("The switch works!");
            digitalWrite(ledPin, HIGH);  // Turn on LED
          } else {
            digitalWrite(ledPin, LOW);   // Turn off LED
          }
          delay(100);
        }

* **Empfindlichkeit einstellen**: Einige Neigungsschalter haben unterschiedliche Empfindlichkeitsstufen. Experimentieren Sie, indem Sie die Orientierung anpassen, um zu sehen, bei welchem Winkel der Schalter aktiviert wird.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Neigungsschalter mit dem Raspberry Pi Pico verwendet, um Änderungen in der Orientierung zu erkennen. Diese grundlegende Fähigkeit ermöglicht es Ihnen, Projekte zu erstellen, die auf Bewegung oder Position reagieren, wie Alarmanlagen, automatische Beleuchtung oder interaktive Geräte.
