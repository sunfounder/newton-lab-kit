.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_joystick:

4.1 Werte eines Joysticks auslesen
======================================

In dieser Lektion lernen wir, wie man einen **Joystick** mit dem Raspberry Pi Pico 2 verwendet, um analoge Werte auszulesen und Tastendrücke zu erkennen. Ein Joystick ist ein weit verbreitetes Eingabegerät, mit dem Bewegungen entlang zwei Achsen (X und Y) gesteuert werden können. Viele Joysticks verfügen zudem über eine Drucktaste (Z-Achse).

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
        - :ref:`cpn_joystick`
        - 1
        - 

**Funktionsweise des Joysticks**

Ein typisches Joystick-Modul enthält zwei Potentiometer, die in einem 90-Grad-Winkel zueinander stehen:

* **X-Achse (VRx-Potentiometer)**: Misst die Links-Rechts-Bewegung.
* **Y-Achse (VRy-Potentiometer)**: Misst die Auf-Ab-Bewegung.
* **Z-Achse (Schalter)**: Eine digitale Taste, die durch Drücken des Joysticks ausgelöst wird.

Durch das Auslesen der analogen Werte der X- und Y-Achse kann die Position des Joysticks bestimmt werden. Der Z-Achsen-Schalter erkennt, wenn der Joystick gedrückt wird.

**Schaltplan**

|sch_joystick|

Der **SW-Pin** des Joysticks ist mit einem 10KΩ-Pull-up-Widerstand verbunden, um im nicht gedrückten Zustand einen stabilen HIGH-Zustand zu gewährleisten. Ohne diesen Widerstand könnte sich der Zustand zwischen HIGH und LOW unvorhersehbar ändern.

**Verdrahtungsdiagramm**

|wiring_joystick|

**Code schreiben**

.. note::

   * Sie können die Datei ``4.1_toggle_the_joystick.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/4.1_toggle_the_joystick`` öffnen. 
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: arduino

   // Define the pins
   const int joystickX = 26;  // GP26 (ADC0) connected to VRx
   const int joystickY = 27;  // GP27 (ADC1) connected to VRy
   const int joystickSW = 22; // GP22 connected to SW (button)

   void setup() {
     // Initialize serial communication at 115200 baud
     Serial.begin(115200);

     // Initialize the joystick switch pin as input
     pinMode(joystickSW, INPUT_PULLUP);

   }

   void loop() {
     // Read analog values from the joystick
     int xValue = analogRead(joystickX);
     int yValue = analogRead(joystickY);

     // Read the joystick button state
     int buttonState = digitalRead(joystickSW);

     // Print the joystick values to the Serial Monitor
     Serial.print("X: ");
     Serial.print(xValue);
     Serial.print(" | Y: ");
     Serial.print(yValue);
     Serial.print(" | Button: ");
     Serial.println(buttonState == LOW ? "Pressed" : "Released");

     delay(500); // Wait for half a second before the next reading
   }

Sobald der Code läuft und der serielle Monitor geöffnet ist:

* Bewegen Sie den Joystick in verschiedene Richtungen (links, rechts, oben, unten) und beobachten Sie, wie sich die X- und Y-Werte im seriellen Monitor ändern.
* Drücken Sie den Joystick nach unten (Z-Achse) und beobachten Sie, wie sich der Tastenstatus von „Losgelassen“ auf „Gedrückt“ ändert.


**Verständnis des Codes**

#. Definieren der Pins:

   * ``joystickX`` und ``joystickY``: Analoge Eingänge für die Achsen X und Y.
   * ``joystickSW``: Digitaler Eingang für den Taster (Z-Achse).

#. Setup-Funktion:

   * Initialisiert die serielle Kommunikation für Debugging und Datenanzeige.
   * Setzt den Joystick-Taster als Eingang mit internem Pull-up-Widerstand zur Stabilisierung des Signals.

   .. code-block:: arduino

        void setup() {
          Serial.begin(115200); // Initialize serial communication at 115200 baud
          pinMode(joystickSW, INPUT_PULLUP); // Set joystick button as input with pull-up resistor
        }
  
#. ``loop()``-Funktion:

   * Analoge Werte auslesen:
       
     Liest die aktuelle Position des Joysticks entlang der X- und Y-Achse. Die Werte liegen zwischen 0 und 1023, entsprechend den Spannungswerten.

     .. code-block:: arduino
   
           int xValue = analogRead(joystickX);
           int yValue = analogRead(joystickY);
       
   * Tastenstatus auslesen:
       
     Prüft, ob der Joystick gedrückt wurde. ``LOW`` bedeutet gedrückt, ``HIGH`` bedeutet nicht gedrückt.

     .. code-block:: arduino
   
           int buttonState = digitalRead(joystickSW);
       
   * Werte im seriellen Monitor ausgeben:
       
     Gibt die aktuellen X-, Y-Werte sowie den Tastenstatus aus.

     .. code-block:: arduino
   
       Serial.print("X: ");
       Serial.print(xValue);
       Serial.print(" | Y: ");
       Serial.print(yValue);
       Serial.print(" | Button: ");
       Serial.println(buttonState == LOW ? "Pressed" : "Released");

**Weitere Experimente**

* Joystick-Werte zur Steuerung von Aktionen nutzen:  
  Verwenden Sie den Joystick zur Steuerung von Servos, LEDs oder Motoren basierend auf Bewegungsrichtung und Intensität.

* Deadzone implementieren:  
  Definieren Sie eine Totzone, um ungewollte Bewegungen aufgrund von kleinen Joystick-Fluktuationen zu vermeiden.

* Joystick mit weiteren Sensoren kombinieren:  
  Integrieren Sie den Joystick mit Bewegungssensoren oder Distanzsensoren, um komplexere Steuerungssysteme zu entwickeln.

* Game-Controller erstellen: 
  Nutzen Sie mehrere Joysticks und Taster, um einen benutzerdefinierten Controller für einfache Spiele oder Robotersteuerung zu bauen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Joystick mit dem Raspberry Pi Pico verbindet, um analoge Werte der X- und Y-Achse zu lesen und Tastendrücke auf der Z-Achse zu erkennen. Dieses Wissen kann für Fernsteuerungen, Robotik und interaktive Installationen
