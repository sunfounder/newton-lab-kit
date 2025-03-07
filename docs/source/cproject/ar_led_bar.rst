.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_led_bar:

2.2 Den Pegel anzeigen
=============================

In dieser Lektion lernen wir, wie man einen LED-Balkenanzeiger mit dem Raspberry Pi Pico 2 steuert. Ein LED-Balkenanzeiger besteht aus 10 LEDs in einer Reihe, die typischerweise verwendet werden, um Pegel wie Lautstärke, Signalstärke oder andere Messwerte anzuzeigen. Wir werden die LEDs nacheinander aufleuchten lassen, um einen Pegelanzeigeeffekt zu erzeugen.

|img_led_bar_pin|


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
        - Micro USB-Kabel
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
        - 10 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

In diesem Projekt ist jede der 10 LEDs im LED-Balkenanzeiger mit dem Raspberry Pi Pico 2 verbunden. Die Anoden (positive Pole) der LEDs sind an die GPIO-Pins GP6 bis GP15 angeschlossen. Die Kathoden (negative Pole) sind über 220Ω-Widerstände mit dem GND (Ground)-Pin verbunden.

**Verdrahtungsplan**

|wiring_ledbar|

**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.2_display_the_level.ino`` aus ``newton-lab-kit/arduino/2.2_display_the_level`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

    // Define the GPIO pins connected to the LED Bar Graph
    const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

    void setup() {
      // Initialize each pin as an output
      for (int i = 0; i < 10; i++) {
        pinMode(ledPins[i], OUTPUT);
      }
    }

    void loop() {
      // Turn on LEDs sequentially
      for (int i = 0; i < 10; i++) {
        digitalWrite(ledPins[i], HIGH); // Turn on LED
        delay(500);                     // Wait 500 milliseconds
        digitalWrite(ledPins[i], LOW);  // Turn off LED
        delay(500);                     // Wait 500 milliseconds
      }
    }    

Nach dem Hochladen des Codes sollten die LEDs auf dem Balkenanzeiger nacheinander aufleuchten und einen Pegelanzeigeeffekt erzeugen. Jede LED leuchtet eine halbe Sekunde und erlischt dann, bevor die nächste aufleuchtet.

**Verständnis des Codes**

#. Definition der LED-Pins:

   Erstellen Sie ein Array ``ledPins``, das die GPIO-Pinnummern enthält, die mit jeder LED auf dem Balkendiagramm verbunden sind.

   .. code-block:: Arduino

      const int ledPins[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};

#. Initialisierung der Pins:

   In der Funktion ``setup()`` stellen wir jeden Pin im Array ``ledPins`` als Ausgang ein.

   .. code-block:: Arduino

      void setup() {
        for (int i = 0; i < 10; i++) {
          pinMode(ledPins[i], OUTPUT);
        }
      }

#. Steuerung der LEDs:

   In der Funktion ``loop()`` verwenden wir eine ``for``-Schleife, um durch jede LED zu iterieren. Wir schalten sie ein, warten 500 Millisekunden, schalten sie aus und warten dann weitere 500 Millisekunden, bevor wir zur nächsten LED übergehen.

   .. code-block:: Arduino

      void loop() {
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(500);
          digitalWrite(ledPins[i], LOW);
          delay(500);
        }
      }

**Weiteres Experimentieren**

* **Reihenfolge umkehren**: Ändern Sie den Code, um die LEDs in umgekehrter Reihenfolge aufleuchten zu lassen.

* **Bounce-Effekt erstellen**: Nachdem die letzte LED erreicht wurde, soll die Sequenz umkehren und zum ersten LED zurückkehren.

  .. code-block:: Arduino
    
      void loop() {
        // Ascending sequence
        for (int i = 0; i < 10; i++) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
        // Descending sequence
        for (int i = 8; i >= 0; i--) {
          digitalWrite(ledPins[i], HIGH);
          delay(200);
          digitalWrite(ledPins[i], LOW);
        }
      }

* **Geschwindigkeit anpassen**: Ändern Sie die Verzögerungszeiten, um die LEDs schneller oder langsamer aufleuchten zu lassen.



**Fazit**

In dieser Lektion haben Sie gelernt, wie man mehrere LEDs mit dem Raspberry Pi Pico steuert und wie man mit einfachen Programmierkonstrukten wie Schleifen und Verzögerungen visuelle Effekte erzeugt. Dieses Grundwissen ist wesentlich für fortgeschrittenere Projekte mit LED-Anzeigen und Indikatoren.
