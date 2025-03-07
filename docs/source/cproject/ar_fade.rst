.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_fade:

2.3 LED-Helligkeit mit PWM steuern
======================================

In dieser Lektion lernen wir, wie man die Helligkeit einer LED mithilfe der Pulsweitenmodulation (PWM) auf dem Raspberry Pi Pico 2 steuert. PWM ist eine grundlegende Technik in der Elektronik, die es ermöglicht, Geräte wie LEDs und Motoren mit variablen Intensitäten zu betreiben.

**Was ist PWM?**

**Pulsweitenmodulation (PWM)** ist eine Methode zur Steuerung der Leistung, die an ein elektronisches Gerät geliefert wird. Dabei wird die Spannung in schnellen Intervallen ein- und ausgeschaltet. Die „Breite“ des Impulses (die Dauer, in der er eingeschaltet ist) bestimmt, wie viel Leistung das Gerät erhält.

|img_pwm_duty_cycle|

* **Duty Cycle (Tastverhältnis)**: Der prozentuale Anteil eines Zyklus, in dem das Signal aktiv ist. Ein 100 %-Duty Cycle bedeutet, dass das Signal immer an ist, ein 0 %-Duty Cycle, dass es immer aus ist.
* **Frequenz**: Gibt an, wie oft das Signal pro Sekunde zwischen Ein und Aus wechselt.

Durch Anpassen des Duty Cycles können wir analoge Signale mit digitalen Mitteln simulieren. Zum Beispiel: Wenn eine LED sehr schnell ein- und ausgeschaltet wird, nimmt unser Auge je nach Ein-Zeit der LED eine unterschiedliche Helligkeit wahr.

**Warum PWM verwenden?**

* **LED-Helligkeitssteuerung**: Stufenlose Anpassung der LED-Helligkeit.
* **Motorsteuerung**: Kontrolle der Geschwindigkeit von Gleichstrommotoren.
* **Effizienz**: PWM ist energieeffizienter als variable Widerstände, da weniger Energie in Wärme umgewandelt wird.

**PWM auf dem Raspberry Pi Pico 2**

Der Raspberry Pi Pico 2 verfügt über PWM-Funktionalität auf allen GPIO-Pins, jedoch gibt es insgesamt 8 PWM-Slices (PWM0 bis PWM7), wobei jeder Slice über zwei Kanäle (A und B) verfügt. Dies ergibt 16 unabhängige PWM-Ausgänge.

|pin_pwm|

.. note::
     Pins, die denselben PWM-Slice verwenden (z. B. GP0 und GP16), können unterschiedliche Duty Cycles haben, aber nicht unterschiedliche Frequenzen.


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

**Verdrahtungsdiagramm**

|wiring_led|

**Code schreiben**

.. note::

   * Sie können die Datei ``2.3_fading_led.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/2.3_fading_led`` öffnen. 
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: Arduino

    const int ledPin = 15; // GPIO-Pin für die LED

    void setup() {
      pinMode(ledPin, OUTPUT); // GPIO-Pin als Ausgang festlegen
    }

    void loop() {
      // Helligkeit erhöhen
      for (int value = 0; value <= 255; value += 5) {
        analogWrite(ledPin, value); // Helligkeit setzen
        delay(30);                  // 30 Millisekunden warten
      }
      // Helligkeit verringern
      for (int value = 255; value >= 0; value -= 5) {
        analogWrite(ledPin, value);
        delay(30);
      }
    }

Nach dem Hochladen des Codes sollte die LED langsam heller werden und dann wieder dunkler werden, wodurch ein sanfter Pulsierungseffekt entsteht.

**Verständnis des Codes**

#. LED-Pin definieren:
   
   Erstellt eine Konstante ``ledPin`` mit dem Wert 15, welcher dem GPIO-Pin 15 entspricht.

   .. code-block:: Arduino

        const int ledPin = 15;

#. Pin initialisieren:
   
   Die ``setup()``-Funktion wird einmal beim Start des Programms ausgeführt. Der ``ledPin`` wird als Ausgang definiert.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. Loop-Funktion:
   
    Die ``loop()``-Funktion wird kontinuierlich wiederholt. Sie enthält zwei ``for``-Schleifen:

     * Helligkeit erhöhen: Startet mit ``value = 0`` und erhöht sich in 5er-Schritten bis 255.
     * Helligkeit verringern: Startet mit ``value = 255`` und verringert sich wieder in 5er-Schritten bis 0.
     
   * Die Funktion ``analogWrite()`` schreibt ein PWM-Signal an den angegebenen Pin. Der Wert reicht von 0 (aus) bis 255 (maximale Helligkeit).
   * ``delay(30);`` sorgt für eine sichtbare Veränderung der Helligkeit.

   .. code-block:: Arduino

        void loop() {
          // Increase brightness
          for (int value = 0; value <= 255; value += 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
          // Decrease brightness
          for (int value = 255; value >= 0; value -= 5) {
            analogWrite(ledPin, value);
            delay(30);
          }
        }


**Zusätzliche Tipps**

* **Experimentieren Sie**: Ändern Sie die Inkrementwerte oder die Verzögerungszeit, um die Geschwindigkeit der Helligkeitsänderung zu steuern.
* **PWM-Einschränkungen verstehen**: Obwohl alle GPIO-Pins des Pico PWM unterstützen, können Pins desselben PWM-Slices nur unterschiedliche Duty Cycles, aber nicht unterschiedliche Frequenzen haben.
* **Sicherheit beachten**: Verwenden Sie immer einen Vorwiderstand mit der LED, um Schäden durch zu hohen Strom zu vermeiden.

**Fazit**

Sie haben erfolgreich einen sanften LED-Dimmeffekt mithilfe von PWM auf dem Raspberry Pi Pico 2 erstellt. Dieses Projekt demonstriert, wie PWM zur Simulation analoger Signale mit digitalen Mitteln genutzt wird – eine grundlegende Technik in der Mikrocontroller-Programmierung.
