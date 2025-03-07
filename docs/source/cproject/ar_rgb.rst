.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_rgb:

2.4 Buntes Licht
====================

In dieser Lektion werden wir erforschen, wie man verschiedene Farben mit einer RGB-LED und dem Raspberry Pi Pico 2 erzeugt. Durch die Anpassung der Intensität der roten, grünen und blauen Komponenten können wir Licht mischen und eine breite Palette von Farben erzeugen. Dieses Konzept basiert auf der additiven Methode der Farbmischung.

**Was ist additive Farbmischung?**

Additive Farbmischung beinhaltet das Kombinieren verschiedener Lichtfarben, um neue Farben zu erzeugen. Wenn rotes, grünes und blaues Licht in verschiedenen Intensitäten kombiniert werden, können sie jede Farbe im sichtbaren Spektrum erzeugen. Zum Beispiel:

* **Rot + Grün = Gelb**
* **Rot + Blau = Magenta**
* **Grün + Blau = Cyan**
* **Rot + Grün + Blau = Weiß**

|img_rgb_mix|

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
        - 3(1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|


**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern die Rot-, Grün- und Blau-Pins der RGB-LED und verbinden den gemeinsamen Kathodenpin mit GND. Dies ermöglicht es der RGB-LED, eine bestimmte Farbe anzuzeigen, indem Licht auf diesen Pins mit unterschiedlichen PWM-Werten überlagert wird.


**Verdrahtungsdiagramm**

|img_rgb_pin|

Die RGB-LED hat 4 Pins: der längste Pin ist der gemeinsame Kathodenpin, der üblicherweise mit GND verbunden wird; der linke Pin neben dem längsten Pin ist Rot; und die zwei Pins rechts sind Grün und Blau.

Wir verwenden einen höheren Widerstand für die rote LED, da sie typischerweise heller ist als die grünen und blauen LEDs bei gleichem Strom.

|wiring_rgb|


**Schreiben des Codes**

Hier können wir unsere Lieblingsfarbe in Zeichensoftware (wie Paint) wählen und sie mit der RGB-LED anzeigen.

.. note::

   * Sie können die Datei ``2.4_colorful_light.ino`` aus ``newton-lab-kit/arduino/2.4_colorful_light`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

   // Define the GPIO pins connected to the RGB LED
   const int redPin = 13;   // Red pin
   const int greenPin = 14; // Green pin
   const int bluePin = 15;  // Blue pin

   void setup() {
     // Initialize each RGB LED pin as an output
     pinMode(redPin, OUTPUT);
     pinMode(greenPin, OUTPUT);
     pinMode(bluePin, OUTPUT);
   }

   // Function to set the color
   void setColor(unsigned char red, unsigned char green, unsigned char blue) {
     analogWrite(redPin, red);
     analogWrite(greenPin, green);
     analogWrite(bluePin, blue);
   }

   void loop() {
     // Red color
     setColor(255, 0, 0);
     delay(1000);

     // Green color
     setColor(0, 255, 0);
     delay(1000);

     // Blue color
     setColor(0, 0, 255);
     delay(1000);

     // Yellow color (Red + Green)
     setColor(255, 255, 0);
     delay(1000);

     // Cyan color (Green + Blue)
     setColor(0, 255, 255);
     delay(1000);

     // Magenta color (Red + Blue)
     setColor(255, 0, 255);
     delay(1000);

     // White color (Red + Green + Blue)
     setColor(255, 255, 255);
     delay(1000);

     // Turn off
     setColor(0, 0, 0);
     delay(1000);
   }

Nach dem Hochladen des Codes sollte die RGB-LED durch Rot, Grün, Blau, Gelb, Cyan, Magenta, Weiß und dann Ausschalten zyklisch durchlaufen, wobei jede Farbe für eine Sekunde angezeigt wird.

**Verständnis des Codes**

#. Definition der Pins:

   Zuweisen der GPIO-Pins, die mit den RGB-LED-Komponenten verbunden sind.

   .. code-block:: Arduino

        const int redPin = 13;
        const int greenPin = 14;
        const int bluePin = 15;

#. Initialisierung der Pins:

   Einstellen der RGB-LED-Pins als Ausgänge.

   .. code-block:: Arduino

        void setup() {
          pinMode(redPin, OUTPUT);
          pinMode(greenPin, OUTPUT);
          pinMode(bluePin, OUTPUT);
        }

#. Einstellen der Farbe:

   Die Funktion ``setColor`` verwendet PWM (Pulsweitenmodulation), um die Helligkeit jeder Farbkomponente anzupassen.

   .. code-block:: Arduino

        void setColor(unsigned char red, unsigned char green, unsigned char blue) {
          analogWrite(redPin, red);
          analogWrite(greenPin, green);
          analogWrite(bluePin, blue);
        }

#. Durchlaufen der Farben:

   In der Funktion ``loop()`` rufen wir ``setColor()`` mit verschiedenen Werten auf, um verschiedene Farben anzuzeigen, jeweils gefolgt von einer einsekündigen Verzögerung.


   .. code-block:: Arduino

        void loop() {
          // Red color
          setColor(255, 0, 0);
          delay(1000);
          ...

          // Turn off
          setColor(0, 0, 0);
          delay(1000);
        }


**Experimentieren mit Farben**

Sie können eigene Farben erstellen, indem Sie die Werte, die an ``setColor()`` übergeben werden, anpassen. Die Werte reichen von 0 (aus) bis 255 (volle Helligkeit). Zum Beispiel:

* Orange: setColor(255, 165, 0);
* Purple: setColor(128, 0, 128);

Um RGB-Werte für spezifische Farben zu finden, können Sie ein Farbwähler-Tool oder Software wie **Paint** verwenden.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man eine RGB-LED mit dem Raspberry Pi Pico steuert und wie man verschiedene Farben durch Mischen von rotem, grünem und blauem Licht erzeugt. Dieses Wissen ist grundlegend für Projekte, die LED-Displays, Stimmungslichter oder jede Anwendung, die Farbsteuerung erfordert, involvieren.
