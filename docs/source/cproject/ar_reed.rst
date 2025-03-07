.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihre Kenntnisse über Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_reed:

2.9 Den Magnetismus fühlen
===============================

In dieser Lektion werden wir untersuchen, wie man einen **Reedschalter** mit dem Raspberry Pi Pico 2 verwendet, um das Vorhandensein eines Magnetfelds zu erkennen. Ein Reedschalter ist ein einfacher elektrischer Schalter, der mit einem Magnetfeld betrieben wird. Nähert sich ein Magnet dem Schalter, schließen sich seine internen Kontakte und vervollständigen den Stromkreis.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_reed`
        - 1
        - 


**Verständnis des Reedschalters**

Ein Reedschalter besteht aus zwei dünnen Metallzungen, die in einer Glasampulle versiegelt sind. Diese Zungen sind aus ferromagnetischem Material gefertigt und leicht voneinander entfernt positioniert. In Abwesenheit eines Magnetfelds sind die Zungen getrennt und der Schalter ist **offen**. Nähert sich ein Magnet dem Schalter, werden die Zungen magnetisiert, ziehen sich an und schließen den Stromkreis.

* **Kein Magnet in der Nähe**: Schalter ist **offen**; der Stromkreis ist unvollständig.
* **Magnet in der Nähe**: Schalter ist **geschlossen**; der Stromkreis ist vollständig.

|img_reed_sche|

**Schaltplan**

|sch_reed|

Standardmäßig ist GP14 niedrig; er wird hoch, wenn der Magnet in der Nähe des Reedschalters ist.

Der Zweck des 10K-Widerstands ist es, den GP14 auf einem konstanten niedrigen Niveau zu halten, wenn kein Magnet in der Nähe ist.

* **Kein Magnet in der Nähe**:

  * Der Reedschalter ist **offen**.
  * **GP14** ist durch den Pull-down-Widerstand mit **GND** verbunden.
  * Der GPIO-Pin liest **LOW** (0).

* **Magnet in der Nähe**:

  * Der Reedschalter ist **geschlossen**.
  * **GP14** ist durch den Reedschalter mit **3.3V** verbunden.
  * Der GPIO-Pin liest **HIGH** (1).

**Verdrahtungsdiagramm**

|wiring_reed|


**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.9_feel_the_magnetism.ino`` aus ``newton-lab-kit/arduino/2.9_feel_the_magnetism`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino


   const int reedPin = 14;    // GPIO pin connected to the reed switch
   int reedState = 0;

   void setup() {
     Serial.begin(115200);       // Initialize Serial Monitor at 115200 baud
     pinMode(reedPin, INPUT);    // Set the reed pin as input
   }

   void loop() {
     reedState = digitalRead(reedPin);  // Read the state of the reed switch

     if (reedState == HIGH) {
       Serial.println("Magnet Detected!");
     } else {
       Serial.println("No Magnet.");
     }
     delay(500);  // Delay to avoid flooding the Serial Monitor
   }

Wenn der Code läuft und die serielle Überwachung geöffnet ist:

* **Kein Magnet in der Nähe**: Die serielle Überwachung zeigt "Kein Magnet."
* **Magnet in der Nähe**: Bringen Sie einen Magnet in die Nähe des Reedschalters. Die serielle Überwachung zeigt "Magnet erkannt!"

**Verständnis des Codes**

#. Serielle Kommunikation initialisieren:

   Startet die serielle Kommunikation mit einer Baudrate von 115200. Dies ermöglicht es uns, Nachrichten auf der seriellen Überwachung anzuzeigen.

   .. code-block:: Arduino

        Serial.begin(115200);

#. Den Reedschalter-Pin einrichten:
 
   Konfiguriert reedPin (GP14) als Eingang, um den Zustand des Reedschalters zu lesen.

   .. code-block:: Arduino

        pinMode(reedPin, INPUT);

#. Den Zustand des Reedschalters lesen:

   Liest den aktuellen Zustand des Reedschalters. Er wird HIGH, wenn der Magnet in der Nähe ist (Schalter geschlossen) und LOW, wenn kein Magnet in der Nähe ist (Schalter offen).

   .. code-block:: Arduino

        reedState = digitalRead(reedPin);

#. Auf Magnetpräsenz reagieren:

   Gibt eine Nachricht aus, je nachdem, ob ein Magnet in der Nähe des Reedschalters ist.

   .. code-block:: Arduino

        if (reedState == HIGH) {
          Serial.println("Magnet Detected!");
        } else {
          Serial.println("No Magnet.");
        }


**Mehr lernen: Unterbrechungen mit dem Reedschalter verwenden**

* **Einführung in Unterbrechungen**

  Stellen Sie sich vor, Sie lesen ein Buch und sind vollkommen in die Geschichte vertieft. Plötzlich tippt Ihnen jemand auf die Schulter, um eine Frage zu stellen. Sie pausieren Ihr Lesen, beantworten die Frage und kehren dann zu Ihrem Buch zurück. Diese Unterbrechung ähnelt der Arbeitsweise von Unterbrechungen in Mikrocontrollern.
  
  Eine Unterbrechung ermöglicht es einem Programm, sofort auf wichtige Ereignisse zu reagieren, den Hauptprogrammfluss zu pausieren und eine spezielle Funktion namens Interrupt Service Routine (ISR) auszuführen. Nach der Behandlung der Unterbrechung setzt das Programm dort fort, wo es unterbrochen wurde.
  
* **Warum Unterbrechungen verwenden?**

  Die Verwendung von Unterbrechungen mit dem Reedschalter ermöglicht es dem Mikrocontroller, sofort zu reagieren, wenn ein Magnet erkannt wird, anstatt den Reedschalter kontinuierlich in der ``loop()``-Funktion zu überprüfen. Dies ist effizienter und kann Strom in batteriebetriebenen Anwendungen sparen.

* **Den Code mit Unterbrechungen schreiben**

  Lassen Sie uns unser Programm modifizieren, um eine Unterbrechung zur Erkennung des Magneten zu verwenden.

  .. code-block:: Arduino

        const int reedPin = 14;            // GPIO pin connected to the reed switch
        volatile bool magnetDetected = false;  // Flag to indicate if the magnet is detected

        void setup() {
          Serial.begin(115200);               // Initialize Serial Monitor
          pinMode(reedPin, INPUT);            // Set the reed pin as input
          attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);  // Attach interrupt on any change
        }

        void loop() {
          if (magnetDetected) {
            Serial.println("Magnet Present!");
          } else {
            Serial.println("Waiting for magnet...");
          }
          delay(1000);                         // Delay to avoid flooding the serial monitor
        }

        void onMagnetChange() {
          // Update the flag based on the current state of the reed pin
          magnetDetected = digitalRead(reedPin) == HIGH;  // If HIGH, magnet is present; if LOW, magnet is absent
        }


  .. code-block:: Arduino

        attachInterrupt(digitalPinToInterrupt(reedPin), onMagnetChange, CHANGE);
    
  * ``digitalPinToInterrupt(reedPin)``: Konvertiert die Pin-Nummer in die entsprechende Unterbrechungsnummer.
  * ``onMagnetChange``: Der Name der ISR-Funktion, die aufgerufen wird, wenn die Unterbrechung auftritt.
  * ``CHANGE``: Die Unterbrechung wird ausgelöst, wenn sich der Pin ändert.


**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Reedschalter mit dem Raspberry Pi Pico verwendet, um das Vorhandensein eines Magnetfelds zu erkennen. Sie haben auch erforscht, wie Unterbrechungen Ihr Programm effizienter machen können, indem sie sofort auf Ereignisse reagieren, ohne den Sensor ständig im Hauptloop zu überprüfen. Das Verständnis der Verwendung von Unterbrechungen ist eine wertvolle Fähigkeit in der eingebetteten Programmierung, die es Ihnen ermöglicht, reaktionsfähigere und effizientere Anwendungen zu erstellen.

**Weitere Erkundungen**

* **Türsensor**: Verwenden Sie den Reedschalter, um einen einfachen Türalarm zu erstellen, der ausgelöst wird, wenn die Tür geöffnet wird.
* **Umdrehungen zählen**: Befestigen Sie einen Magnet an einem rotierenden Objekt und verwenden Sie den Reedschalter, um die Umdrehungen pro Minute (RPM) zu zählen.
* **Sicherheitssysteme**: Integrieren Sie mehrere Reedschalter, um Fenster und Türen in einem Sicherheitssystem zu überwachen.

**Zusätzliche Ressourcen**

* `attachInterrupt() - Arduino Referenz <https://www.arduino.cc/reference/en/language/functions/external-interrupts/attachinterrupt/>`_

