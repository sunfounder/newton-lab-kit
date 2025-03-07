.. note:: 
    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie Ihre Kenntnisse über Raspberry Pi, Arduino und ESP32 gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Sonderangebote**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pump:

3.6 Steuerung einer Wasserpumpe
===================================

In dieser Lektion lernen wir, wie man eine **kleine Wasserpumpe** mit dem Raspberry Pi Pico 2 und einem **L293D-Motortreiber** steuert. Eine kleine Zentrifugalpumpe kann für Projekte wie automatische Pflanzenbewässerungssysteme oder das Erstellen von Miniatur-Wassermerkmalen verwendet werden. Die Steuerung der Pumpe ähnelt der Steuerung eines Gleichstrommotors, da sie dieselben Prinzipien verwendet.

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 7
        - 9V Batterie
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Wichtige Hinweise vor Beginn**

* **Pumpenaufbau**: Schließen Sie den Schlauch an den Ausgang der Pumpe an. Tauchen Sie die Pumpe vor dem Einschalten ins Wasser.
* **Trockenlauf vermeiden**: Stellen Sie sicher, dass die Pumpe immer untergetaucht ist. Trockenlauf kann Überhitzung verursachen und den Motor beschädigen.
* **Verstopfung verhindern**: Wenn Sie die Pumpe zum Bewässern von Pflanzen verwenden, stellen Sie sicher, dass das Wasser frei von Schmutz ist, um Verstopfungen zu vermeiden.
* **Ansaugen der Pumpe**: Wenn anfangs kein Wasser austritt, könnte Luft im Schlauch gefangen sein. Sie müssen möglicherweise die Pumpe ansaugen, indem Sie Wasser durchfließen lassen, um Luftblasen zu entfernen.

**Schaltplan**

|sch_pump|

Der L293D ist ein Motortreiber-Chip, EN ist mit 5V verbunden, um den L293D zu betreiben. 1A und 2A sind die Eingänge, die mit GP15 bzw. GP14 verbunden sind; 1Y und 2Y sind die Ausgänge, die mit den beiden Enden des Motors verbunden sind.

Y (Ausgang) ist in Phase mit A (Eingang), daher kann die Drehrichtung des Motors geändert werden, wenn GP15 und GP14 unterschiedliche Pegel erhalten.


**Verdrahtungsdiagramm**

|wiring_pump|

In diesem Schaltkreis sehen Sie, dass der Knopf mit dem RUN-Pin verbunden ist. Dies liegt daran, dass der Motor mit zu viel Strom betrieben wird, was dazu führen kann, dass sich der Pico vom Computer trennt, und der Knopf muss gedrückt werden (damit der RUN-Pin des Pico ein niedriges Niveau erhält), um zurückzusetzen.


**Schreiben des Codes**

.. note::

   * Sie können die Datei ``3.6_pumping.ino`` aus ``newton-lab-kit/arduino/3.6_pumping`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

    const int IN1 = 15; // GPIO pin connected to Input 1A
    const int IN2 = 14; // GPIO pin connected to Input 2A

    void setup() {
      pinMode(IN1, OUTPUT);
      pinMode(IN2, OUTPUT);
    }

    void loop() {
      // Turn the pump on
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      delay(5000); // Run for 5 seconds

      // Stop the pump
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(5000); // Stop for 5 seconds
    }

Nach dem Hochladen des Codes:

* Die Pumpe sollte 5 Sekunden lang laufen, Wasser durch den Schlauch pumpen.
* Dann wird sie für 5 Sekunden stoppen.
* Dieser Zyklus wiederholt sich unendlich.
* Wenn anfänglich kein Wasser fließt, stellen Sie sicher, dass die Pumpe untergetaucht ist und keine Luftblasen im Schlauch sind.

**Sicherheitsvorkehrungen**

* Wasser und Elektrizität:

  * Seien Sie äußerst vorsichtig, Wasser von Pico und anderen elektronischen Komponenten fernzuhalten.
  * Stellen Sie sicher, dass alle Verbindungen sicher und bei Bedarf isoliert sind.

* Stromversorgung:

  * Verwenden Sie eine Stromquelle, die den Spannungsanforderungen der Pumpe entspricht (typischerweise 3V-6V).
  * Betreiben Sie die Pumpe nicht direkt vom 3,3V-Pin des Pico.

* Stromaufnahme:

  * Pumpen können einen erheblichen Strom ziehen.
  * Stellen Sie sicher, dass Ihre Stromquelle die Stromanforderungen der Pumpe bewältigen kann.

* Zurücksetzen des Pico:

  Wenn Sie Probleme beim Hochladen von Code nach dem Betrieb der Pumpe haben, können Sie den Pico manuell zurücksetzen, indem Sie den RUN-Pin kurzzeitig mit GND verbinden.

  |wiring_run_reset|

**Weitere Erkundungen**

* Automatische Pflanzenbewässerung:

  Integrieren Sie Bodenfeuchtigkeitssensoren, um den Bewässerungsprozess basierend auf der Trockenheit des Bodens zu automatisieren.

* PWM-Geschwindigkeitskontrolle:

  Verwenden Sie die Pulsweitenmodulation (PWM), um die Geschwindigkeit der Pumpe durch Veränderung der Spannung zu steuern.

* Zeitplanung und Planung:

  Implementieren Sie komplexere Zeitpläne mit Echtzeituhren oder Planern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man eine kleine Wasserpumpe mit dem Raspberry Pi Pico und dem L293D-Motortreiber steuert. Diese Technik kann in verschiedenen Projekten wie automatischen Pflanzenbewässerungssystemen, Brunnen oder Hydrokulturanlagen verwendet werden.


