.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_motor:

3.5 Steuerung eines kleinen Ventilators (Gleichstrommotor)
==============================================================

In dieser Lektion lernen wir, wie man einen **Gleichstrommotor** (wie einen kleinen Ventilator) mit dem Raspberry Pi Pico 2 und einem **L293D Motortreiber** steuert. Der L293D ermöglicht es uns, die Drehrichtung des Motors zu steuern – sowohl im Uhrzeigersinn als auch gegen den Uhrzeigersinn. Da Gleichstrommotoren mehr Strom benötigen, als der Pico direkt liefern kann, verwenden wir eine externe Stromversorgung, um den Motor sicher zu betreiben.

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 8
        - 9V Batterie
        - 1
        - 
 
**Schaltplan**

|sch_motor|


Der L293D ist ein Motortreiber-Chip, EN ist mit 5V verbunden, damit der L293D funktioniert. 1A und 2A sind die Eingänge, die jeweils mit GP15 und GP14 verbunden sind; 1Y und 2Y sind die Ausgänge, die mit den beiden Enden des Motors verbunden sind.

Y (Ausgang) ist in Phase mit A (Eingang), also kann die Drehrichtung des Motors geändert werden, wenn GP15 und GP14 unterschiedliche Pegel erhalten.


**Verdrahtungsplan**

|wiring_motor|

In diesem Schaltkreis sehen Sie, dass der Knopf mit dem RUN-Pin verbunden ist. Dies liegt daran, dass der Motor mit zu viel Strom arbeitet, was dazu führen kann, dass der Pico sich vom Computer trennt, und der Knopf muss gedrückt werden (damit der RUN-Pin des Pico ein niedriges Level erhält), um zurückzusetzen.

Da Gleichstrommotoren einen hohen Strom benötigen, verwenden wir hier aus Sicherheitsgründen ein Stromversorgungsmodul, um den Motor zu betreiben.


**Schreiben des Codes**

.. note::

   * Sie können die Datei ``3.5_small_fan.ino`` aus ``newton-lab-kit/arduino/3.5_small_fan`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

    const int IN1 = 15; // GPIO pin connected to Input 1A
    const int IN2 = 14; // GPIO pin connected to Input 2A

    void setup() {
      pinMode(IN1, OUTPUT);
      pinMode(IN2, OUTPUT);
    }

    void loop() {
      // Rotate motor clockwise
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      delay(2000); // Run for 2 seconds

      // Stop motor
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // Stop for 1 second

      // Rotate motor counterclockwise
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      delay(2000); // Run for 2 seconds

      // Stop motor
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // Stop for 1 second
    }

Nach dem Hochladen des Codes:

* Sollte sich der Motor 2 Sekunden lang in eine Richtung drehen.
* Dann hält er für 1 Sekunde an.
* Dann dreht er sich 2 Sekunden lang in die entgegengesetzte Richtung.
* Dieser Zyklus wiederholt sich unendlich.

**Verständnis des Codes**

#. Definieren der Steuerpins:

   .. code-block:: arduino

        const int IN1 = 15; // Connected to Input 1A
        const int IN2 = 14; // Connected to Input 2A

#. Einstellen der Pin-Modi:

   .. code-block:: arduino

        void setup() {
          pinMode(IN1, OUTPUT);
          pinMode(IN2, OUTPUT);
        }

#. Steuern der Motordrehrichtung:

   * **Drehung im Uhrzeigersinn**: Setzt IN1 auf HIGH und IN2 auf LOW, was den Motor in eine Richtung dreht.

   .. code-block:: arduino

        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);

   * **Drehung gegen den Uhrzeigersinn**: Setzt IN1 auf LOW und IN2 auf HIGH, was den Motor in die entgegengesetzte Richtung dreht.

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);


#. Anhalten des Motors:

   Setzt beide Eingänge auf LOW, was den Motor anhält.

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);

**Weitere Erkundungen**

* Geschwindigkeitssteuerung:

  Verwenden Sie die Pulsweitenmodulation (PWM), um die Geschwindigkeit des Motors zu steuern, indem Sie den EN1-Pin mit einem PWM-fähigen GPIO-Pin verbinden und den Tastgrad variieren.

* Steuerung mehrerer Motoren:

  Der L293D kann zwei Motoren steuern. Versuchen Sie, einen zweiten Motor hinzuzufügen und ihn unabhängig zu steuern.

* Integration von Sensoren:

  Integrieren Sie Sensoren (z. B. Endschalter, Encoder), um komplexere Motorsysteme zu erstellen.


**Sicherheitsvorkehrungen**

* Stromversorgung:

  * Stellen Sie sicher, dass die Spannung der externen Stromversorgung mit der Spannungsbewertung des Motors übereinstimmt.
  * Speisen Sie den Motor nicht direkt vom 3,3V-Pin des Pico.

* Stromaufnahme:

  * Motoren können insbesondere beim Start oder bei Blockierung erheblichen Strom ziehen.
  * Stellen Sie sicher, dass Ihre Stromversorgung den Strombedarf des Motors bewältigen kann.

* Zurücksetzen des Pico:

  * In einigen Fällen kann der Stromverbrauch des Motors zu Spannungseinbrüchen führen, die dazu führen, dass der Pico zurückgesetzt wird oder die Verbindung abbricht.
  * Wenn Sie Probleme haben, Code hochzuladen, nachdem der Motor gelaufen ist, können Sie den Pico manuell zurücksetzen, indem Sie den RUN-Pin kurzzeitig mit GND verbinden.

  |wiring_run_reset|


**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Gleichstrommotor mit dem Raspberry Pi Pico und dem L293D Motortreiber steuert. Durch Steuern der Eingänge des L293D können Sie die Drehrichtung des Motors ändern. Dieses grundlegende Konzept ist wesentlich in der Robotik, Automatisierung und vielen anderen Anwendungen, die Motoren verwenden.

