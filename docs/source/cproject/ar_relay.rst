.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihre Kenntnisse über Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_relay:

2.16 Steuerung eines weiteren Stromkreises mit einem Relais
================================================================

In dieser Lektion lernen wir, wie man mit einem **Relais** und dem Raspberry Pi Pico 2 einen anderen Stromkreis steuert. Ein Relais fungiert wie ein Schalter, der von einem Niederspannungskreis (wie dem Pico) gesteuert wird, um einen Hochspannungskreis zu betreiben. Beispielsweise können Sie mit einem Relais eine Lampe oder ein anderes Gerät einschalten, was die Automatisierung elektrischer Geräte ermöglicht.

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
        - 1 (220Ω), 1 (1KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_diode`
        - 1
        - 
    *   - 8
        - :ref:`cpn_relay`
        - 1
        - |link_relay_buy|
    *   - 9
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 10
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 11
        - 9V Batterie
        - 1
        - 

**Schaltplan**

|sch_relay_1|

* Relaisaktivierung:

  * Die Spule des Relais wird durch den Transistor aktiviert, wenn der Pico ein **hohes Signal** (3,3V) auf GP15 ausgibt.
  * Der Transistor ermöglicht den Stromfluss durch das Relais, wodurch der Schalter im Inneren aktiviert wird.
  * Das Relais macht ein "Klick"-Geräusch beim Schalten, was auf die Steuerung des Laststromkreises hinweist.

* Freilaufdiode:

  * Die Diode wird über die Relaisspule platziert, um den Transistor vor Spannungsspitzen zu schützen, die auftreten, wenn das Relais abgeschaltet wird.

**Verdrahtungsdiagramm**

|wiring_relay_1|


**Schreiben des Codes**


.. note::

   * Sie können die Datei ``2.16_relay.ino`` aus ``newton-lab-kit/arduino/2.16_relay`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

   const int relayPin = 15;  // GPIO pin connected to the transistor base

   void setup() {
     pinMode(relayPin, OUTPUT);
     digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
   }

   void loop() {
     // Turn the relay on
     digitalWrite(relayPin, HIGH);
     Serial.println("Relay ON");
     delay(2000);  // Wait for 2 seconds

     // Turn the relay off
     digitalWrite(relayPin, LOW);
     Serial.println("Relay OFF");
     delay(2000);  // Wait for 2 seconds
   }

Nach dem Hochladen des Codes sollten Sie alle 2 Sekunden ein "Klick"-Geräusch vom Relais hören, wenn es ein- und ausgeschaltet wird.

**Verständnis des Codes**

#. Definition des Relais-Pins:

   Weist ``relayPin`` GPIO 15 zu, das den Transistor und damit das Relais steuert.

   .. code-block:: arduino

        const int relayPin = 15;  // GPIO pin connected to the transistor base

#. Einrichten der Pin-Modi:

   Stellt ``relayPin`` als Ausgang ein. Initialisiert das Relais im AUS-Zustand.

   .. code-block:: arduino

        void setup() {
          pinMode(relayPin, OUTPUT);
          digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
        }

#. Steuerung des Relais:

   * Stellt ``relayPin`` auf ``HIGH``, um den Transistor einzuschalten, was die Relaisspule aktiviert.
   * Wartet 2 Sekunden.
   * Stellt ``relayPin`` auf ``LOW``, um den Transistor auszuschalten, was die Relaisspule deaktiviert.
   * Wartet weitere 2 Sekunden.
   * Wiederholt den Zyklus unendlich.

   .. code-block:: arduino

        // Turn the relay on
        digitalWrite(relayPin, HIGH);
        Serial.println("Relay ON");
        delay(2000);  // Wait for 2 seconds

        // Turn the relay off
        digitalWrite(relayPin, LOW);
        Serial.println("Relay OFF");
        delay(2000);  // Wait for 2 seconds

**Weitere Experimente**

* **Einen Timer setzen**: Modifizieren Sie den Code, um das Relais 10 Minuten lang einzuschalten und dann automatisch auszuschalten.
* **Steuerung von Haushaltsgeräten**: Mit entsprechender Anleitung können Sie Hochspannungsgeräte mit dem Relais für Automatisierungsaufgaben wie das Ein- und Ausschalten von Lichtern oder Ventilatoren verbinden.

  * Der Schaltkreis sollte folgendermaßen aussehen: Um zu demonstrieren, wie man einen externen Stromkreis sicher steuert, fügen wir eine externe 5V-Stromversorgung (über ein Breadboard-Strommodul) hinzu, um eine LED zu betreiben. Dies simuliert, wie Sie mit dem Relais höhere Spannungsgeräte (wie Haushaltsgeräte) steuern könnten. So modifizieren Sie den Schaltkreis:

    |sch_relay_2|
  
    |wiring_relay_2|

  * Code zur Steuerung des Relais:

    .. code-block:: arduino
    
       const int relayPin = 15;  // GPIO pin connected to the transistor base

       void setup() {
         pinMode(relayPin, OUTPUT);
         digitalWrite(relayPin, LOW);  // Ensure the relay is off at startup
       }

       void loop() {
         // Turn the relay on
         digitalWrite(relayPin, HIGH);
         Serial.println("Relay ON");
         delay(2000);  // Wait for 2 seconds

         // Turn the relay off
         digitalWrite(relayPin, LOW);
         Serial.println("Relay OFF");
         delay(2000);  // Wait for 2 seconds
       }

    Wenn das Relais aktiviert wird (GP15 gibt hoch aus), verbinden sich die Normalerweise Offen (NO) und Gemeinsam (C) Pins des Relais, sodass die externe 5V-Stromversorgung durch die LED fließen kann. Die LED leuchtet auf und simuliert, wie ein Relais ein externes Gerät steuern kann.

    Wenn das Relais deaktiviert wird (GP15 gibt niedrig aus), trennt sich der Normalerweise Offen (NO) Pin vom Gemeinsam (C) Pin, die externe Stromversorgung wird unterbrochen und die LED schaltet sich aus.


**Sicherheitsüberlegungen für die Steuerung echter Geräte**

Dieses Beispiel verwendet eine LED und eine 5V-Stromquelle, um die Relaissteuerung zu demonstrieren. Wenn Sie höhere Spannungsgeräte (wie Haushaltsgeräte) steuern, stellen Sie sicher:

* **Angemessene Spannungsbewertung**: Verwenden Sie ein Relais, das für die entsprechende Spannung und den Strom Ihres Geräts ausgelegt ist.
* **Isolation**: Sorgen Sie für eine angemessene Isolation zwischen dem Niederspannungssteuerkreis (wie dem Pico) und dem Hochspannungsgerätekreis.
* **Sicherungsschutz**: Erwägen Sie die Hinzufügung von Sicherungen oder Leistungsschaltern, um gegen Kurzschlüsse oder Überlastungen zu schützen.
* **Fachkundige Beratung**: Bei der Arbeit mit Hochspannungsstromkreisen suchen Sie immer fachkundige Beratung, um einen sicheren Betrieb zu gewährleisten.

Dieses Projekt kann als Grundlage für die Heimautomatisierung dienen, wie zum Beispiel die Steuerung von Lampen, Ventilatoren oder anderen Geräten basierend auf Timern oder Sensoren, die mit dem Raspberry Pi Pico 2 verbunden sind.

**Verwendung des NC-Terminals**

* Wenn Sie Ihren gesteuerten Stromkreis zwischen COM und NC anschließen:

  * Der Stromkreis ist geschlossen (ON), wenn das Relais nicht aktiviert ist.
  * Der Stromkreis ist offen (OFF), wenn das Relais aktiviert ist.
  * Beispiel: Steuerung eines externen Geräts
  * Warnung: Versuchen Sie nicht, Hochspannungsgeräte zu steuern, ohne angemessene Kenntnisse und Sicherheitsvorkehrungen.

* Wenn Sie einen kleinen Gleichstrommotor oder ein anderes Gerät steuern möchten:

  * Ersetzen Sie die LED durch das Gerät, das Sie steuern möchten.
  * Stellen Sie sicher, dass die Spannungs- und Stromanforderungen des Geräts kompatibel sind.
  * Bereitstellen einer geeigneten Stromversorgung für das Gerät.
  * Schließen Sie das Gerät in Reihe mit den COM- und NO- (oder NC-) Terminals des Relais an.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen anderen Stromkreis mit einem Relais und dem Raspberry Pi Pico steuert. Durch die Verwendung eines Transistors zum Schalten der Relaisspule haben Sie einen Stromkreis mit höherem Strom sicher gesteuert, ohne die GPIO-Pins des Pico zu überlasten. Das Verständnis der Verwendung von Relais eröffnet viele Möglichkeiten zur Steuerung verschiedener Geräte und Haushaltsgeräte in Ihren Projekten.

