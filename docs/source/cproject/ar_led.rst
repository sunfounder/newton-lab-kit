.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Unterstützung unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_led:

2.1 Hallo, LED!
===================

Willkommen zu Ihrem ersten Hardware-Projekt mit dem Raspberry Pi Pico 2! In dieser Lektion lernen wir, wie man eine LED mit MicroPython blinken lässt. Dieses einfache Projekt ist ein großartiger Einstieg in die physikalische Computertechnik und vermittelt, wie man Hardware mit Code steuert.


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

Durch das Setzen des GPIO-Pins auf hoch oder niedrig steuern Sie die Spannungsausgabe dieses Pins. Wenn der Pin hoch ist, fließt Strom durch die LED (begrenzt durch den Widerstand), was dazu führt, dass sie leuchtet. Wenn der Pin niedrig ist, fließt kein Strom, und die LED erlischt.

**Verdrahtungsplan**

|wiring_led|

**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.1_hello_led.ino`` aus ``newton-lab-kit/arduino/2.1_hello_led`` öffnen.
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: Arduino

    const int ledPin = 15;  // GPIO pin connected to the LED

    void setup() {
      pinMode(ledPin, OUTPUT);  // Initialize the GPIO pin as an output
    }

    void loop() {
      digitalWrite(ledPin, HIGH);  // Turn the LED on
      delay(1000);                 // Wait for 1 second
      digitalWrite(ledPin, LOW);   // Turn the LED off
      delay(1000);                 // Wait for 1 second
    }

Nach dem Hochladen des Codes sollten Sie sehen, wie die LED 1 Sekunde lang eingeschaltet und 1 Sekunde lang ausgeschaltet wird.

**Verständnis des Codes**

#. Variablendeklaration:

   Deklarieren Sie eine konstante Ganzzahl ``ledPin`` und weisen Sie ihr den Wert 15 zu, der dem GPIO-Pin 15 entspricht, an dem die LED angeschlossen ist.

   .. code-block:: Arduino

        const int ledPin = 15;

#. Setup-Funktion:

   Die ``setup()``-Funktion wird einmal ausgeführt, wenn das Board eingeschaltet oder zurückgesetzt wird. Hier initialisieren wir ``ledPin`` als Ausgangspin mit ``pinMode()``.

   .. code-block:: Arduino

        void setup() {
          pinMode(ledPin, OUTPUT);
        }

#. Loop-Funktion:

   * Die ``loop()``-Funktion wird wiederholt nach ``setup()`` ausgeführt.
   * Verwenden Sie ``digitalWrite()`` um die Spannung von ``ledPin`` einzustellen. Durch das Setzen auf ``HIGH`` wird 3,3V bereitgestellt, was die LED einschaltet. Durch das Setzen auf ``LOW`` fällt die Spannung auf 0V, was die LED ausschaltet.
   * Die Funktion ``delay(1000)`` erzeugt eine 1-sekündige Pause zwischen den Ein- und Ausschaltzuständen.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(ledPin, HIGH);
          delay(1000);
          digitalWrite(ledPin, LOW);
          delay(1000);
        }

**Zusätzliche Tipps**

* **Verständnis des Widerstands**: Der 220Ω-Widerstand begrenzt den Stromfluss durch die LED und verhindert, dass sie durchbrennt.
* **Polarität beachten**: Stellen Sie sicher, dass die LED richtig angeschlossen ist. Das längere Bein ist die positive Anode und sollte mit dem Widerstand verbunden sein, der zum GPIO-Pin führt.
* **Experimentieren**: Versuchen Sie, die ``delay(1000)``-Werte zu ändern, um die LED schneller oder langsamer blinken zu lassen.

**Fazit**

Herzlichen Glückwunsch! Sie haben Ihr erstes Hardware-Projekt mit dem Raspberry Pi Pico 2 aufgebaut. Dieses einfache LED-Blinkprojekt ist ein grundlegender Schritt in die Welt der physikalischen Computertechnik. Von hier aus können Sie komplexere Projekte erkunden, indem Sie Tasten, Sensoren und andere Komponenten hinzufügen.
