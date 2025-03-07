.. note:: 

    Hallo, willkommen in der Community der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_neopixel:

3.3 Steuerung eines RGB-LED-Streifens
===========================================================

In dieser Lektion lernen wir, wie man einen **RGB-LED-Streifen** (speziell vom Typ WS2812) mit dem Raspberry Pi Pico 2 und MicroPython steuert.

Der WS2812 ist ein intelligenter LED, der einen Steuerkreis und einen RGB-Chip in einem 5050-LED-Paket integriert. Jede LED verfügt über einen eigenen integrierten Controller, was es uns ermöglicht, jede LED einzeln über eine einzige Datenleitung zu steuern. Dies bedeutet, dass wir die Farbe und Helligkeit jeder LED auf dem Streifen unabhängig ändern können.


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
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schaltplan**

|sch_ws2812|


**Verdrahtungsplan**

|wiring_ws2812|

Seien Sie vorsichtig mit dem Stromverbrauch. Während der VBUS-Pin des Pico Strom für eine kleine Anzahl von LEDs (wie 8) liefern kann, kann die Verwendung von mehr LEDs eine externe Stromversorgung erforderlich machen, um eine Überlastung des Pico zu vermeiden.


**Schreiben des Codes**

.. note::

    * Sie können die Datei ``3.3_rgb_led_strip.ino`` aus ``newton-lab-kit/arduino/3.3_rgb_led_strip`` öffnen. 
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".
    * Die Bibliothek ``Adafruit_NeoPixel`` wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_neopixel.png

.. code-block:: arduino

  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0    // Digital IO pin connected to the NeoPixels
  #define PIXEL_COUNT  8    // Number of NeoPixels

  // Declare our NeoPixel strip object
  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();           // Initialize the NeoPixel library
    strip.show();            // Turn OFF all pixels ASAP
  }

  void loop() {
    // Set the color of each pixel
    strip.setPixelColor(0, strip.Color(255, 0, 0));   // Red
    strip.setPixelColor(1, strip.Color(0, 255, 0));   // Green
    strip.setPixelColor(2, strip.Color(0, 0, 255));   // Blue
    strip.setPixelColor(3, strip.Color(255, 255, 0)); // Yellow
    strip.setPixelColor(4, strip.Color(0, 255, 255)); // Cyan
    strip.setPixelColor(5, strip.Color(255, 0, 255)); // Magenta
    strip.setPixelColor(6, strip.Color(255, 255, 255)); // White
    strip.setPixelColor(7, strip.Color(0, 0, 0));     // Off

    strip.show();  // Update the strip with new contents
    delay(1000);   // Wait for a second

    // Turn off all pixels
    strip.clear();
    strip.show();
    delay(1000);   // Wait for a second
  }

Nach dem Hochladen des Codes sollten Sie sehen, dass die LEDs in verschiedenen Farben aufleuchten, eine Sekunde lang eingeschaltet bleiben und dann eine Sekunde lang ausgeschaltet werden.

**Verständnis des Codes**

#. Bibliothek einbinden:

   .. code-block:: arduino
    
      #include <Adafruit_NeoPixel.h>

#. Konstanten definieren:

   * ``PIXEL_PIN``: Der GPIO-Pin, der mit dem Dateneingang des LED-Streifens verbunden ist (GP0).
   * ``PIXEL_COUNT``: Die Anzahl der LEDs auf dem Streifen.

#. Streifen initialisieren:

   ``NEO_GRB + NEO_KHZ800``: Gibt die Farbreihenfolge und die Kommunikationsgeschwindigkeit an.

   .. code-block:: arduino
    
      Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);
      
#. In der ``setup()``-Funktion:

   * ``strip.begin()``: Initialisiert die NeoPixel-Bibliothek.
   * ``strip.show()``: Stellt sicher, dass alle Pixel ausgeschaltet sind.

#. In der ``loop()``-Funktion:

   * ``strip.setPixelColor(index, color)``: Stellt die Farbe eines bestimmten Pixels ein.
   * ``strip.Color(r, g, b)``: Erstellt einen 24-Bit-Farbwert aus Rot-, Grün- und Blaukomponenten (0-255).
   * ``strip.show()``: Sendet die aktualisierten Farbdaten an den Streifen.
   * ``strip.clear()``: Löscht die Pixeldaten im Speicher (schaltet die Pixel beim nächsten ``show()`` aus).

**Erweitertes Beispiel: Farbwisch-Animation**

Erstellen wir eine einfache Animation, bei der jeder LED nacheinander aufleuchtet.

* ``colorWipe()``: Lässt jeden Pixel nacheinander in der angegebenen Farbe aufleuchten.
* Ruft ``colorWipe()`` mit verschiedenen Farben auf, um eine Animation zu erstellen.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialize all pixels to 'off'
  }

  void loop() {
    colorWipe(strip.Color(255, 0, 0), 50); // Red
    colorWipe(strip.Color(0, 255, 0), 50); // Green
    colorWipe(strip.Color(0, 0, 255), 50); // Blue
  }

  void colorWipe(uint32_t color, int wait) {
    for(int i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, color);
      strip.show();
      delay(wait);
    }
  }

Nach dem Hochladen des Codes sollten Sie sehen, dass die LEDs nacheinander in Rot, dann Grün, dann Blau aufleuchten.

**Erweitertes Beispiel: Regenbogenzyklus-Animation**

* ``rainbowCycle()`` Funktion: Durchläuft die Farben des Regenbogens über alle Pixel.
* Die verschachtelten Schleifen erzeugen einen fließenden Übergang der Farben.
* ``Wheel()`` Funktion: Erzeugt Regenbogenfarben über 0-255 Positionen.

.. code-block:: arduino
    
  #include <Adafruit_NeoPixel.h>

  #define PIXEL_PIN    0
  #define PIXEL_COUNT  8

  Adafruit_NeoPixel strip(PIXEL_COUNT, PIXEL_PIN, NEO_GRB + NEO_KHZ800);

  void setup() {
    strip.begin();
    strip.show(); // Initialize all pixels to 'off'
  }

  void loop() {
    rainbowCycle(20); // Rainbow cycle with 20ms delay per step
  }

  void rainbowCycle(int wait) {
    uint16_t i, j;

    for(j=0; j<256*5; j++) { // 5 cycles of all colors on the wheel
      for(i=0; i< strip.numPixels(); i++) {
        strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
      }
      strip.show();
      delay(wait);
    }
  }

  // Input a value 0 to 255 to get a color value.
  // The colors are a transition r - g - b - back to r.
  uint32_t Wheel(byte WheelPos) {
    if(WheelPos < 85) {
      return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
    } else if(WheelPos < 170) {
      WheelPos -= 85;
      return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
    } else {
      WheelPos -= 170;
      return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
    }
  }

Nach dem Hochladen des Codes sollte der LED-Streifen einen fließenden Regenbogen von Farben anzeigen.

**Weitere Erkundungen**

* Eigene Animationen erstellen:

  * Experimentieren Sie mit verschiedenen Farben und Animationen.
  * Kombinieren Sie mehrere Animationsfunktionen.

* Reaktion auf Sensoren:

  Verwenden Sie Eingaben von Sensoren, um die LED-Farben oder -Muster zu ändern.

* Visualisierer bauen:

  Erstellen Sie einen Musikvisualisierer, der die LEDs basierend auf der Soundeingabe ändert.

**Stromüberlegungen**

* Stromverbrauch:

  * Jede LED kann bei voller Helligkeit bis zu 60 mA ziehen.
  * Für 8 LEDs sind das bis zu 480 mA.
  * Stellen Sie sicher, dass Ihre Stromquelle den erforderlichen Strom liefern kann.

* Externe Stromversorgung:

  * Für größere Streifen oder höhere Helligkeit verwenden Sie eine externe 5V-Stromversorgung.
  * Verbinden Sie das Massekabel der externen Stromquelle mit dem Masseanschluss des Pico.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen WS2812 RGB-LED-Streifen mit dem Raspberry Pi Pico und der Adafruit NeoPixel-Bibliothek steuert. Durch die Steuerung einzelner Pixel können Sie beeindruckende visuelle Effekte für Ihre Projekte kreieren.

