.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_rgb:

2.4 Buntes Licht
====================

In dieser Lektion erkunden wir, wie man mit einer RGB-LED und dem Raspberry Pi Pico 2 verschiedene Farben erzeugt.  
Durch das Anpassen der Intensität der roten, grünen und blauen Komponenten können wir Licht mischen und eine Vielzahl von Farben erzeugen.  
Dieses Konzept basiert auf der additiven Farbmischung.

**Was ist additive Farbmischung?**

Die additive Farbmischung kombiniert verschiedene Lichtfarben, um neue Farben zu erzeugen.  
Wenn rotes, grünes und blaues Licht in unterschiedlichen Intensitäten kombiniert werden, kann jede Farbe des sichtbaren Spektrums entstehen. Zum Beispiel:

* **Rot + Grün = Gelb**
* **Rot + Blau = Magenta**
* **Grün + Blau = Cyan**
* **Rot + Grün + Blau = Weiß**

|img_rgb_mix|

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Ein komplettes Kit ist besonders praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten auch einzeln über die folgenden Links erworben werden.

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
        - 3 (1x 330Ω, 2x 220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|


**Schaltplan**

|sch_rgb|

Die PWM-Pins GP13, GP14 und GP15 steuern die roten, grünen und blauen Pins der RGB-LED.  
Die gemeinsame Kathode wird mit GND verbunden. Dadurch kann die RGB-LED durch unterschiedliche PWM-Werte Lichtfarben überlagern und verschiedene Farben anzeigen.

**Verdrahtungsdiagramm**

|img_rgb_pin|

Die RGB-LED hat vier Pins: Der längste Pin ist die gemeinsame Kathode und wird üblicherweise mit GND verbunden. Der linke Pin neben der Kathode ist **Rot**, die beiden rechten Pins sind **Grün** und **Blau**.

Da rote LEDs bei gleicher Stromstärke typischerweise heller sind als grüne und blaue LEDs, wird für Rot ein höherer Widerstand verwendet.

|wiring_rgb|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, das mit Pulsweitenmodulation (PWM) die Intensität jeder Farbe steuert, um unterschiedliche Farben zu erzeugen.

.. note::

    * Öffne ``2.4_colorful_light.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 


.. code-block:: python

    import machine
    import utime

    # Initialisierung der PWM-Pins für Rot, Grün und Blau
    red = machine.PWM(machine.Pin(13))
    green = machine.PWM(machine.Pin(14))
    blue = machine.PWM(machine.Pin(15))

    # Setze die PWM-Frequenz
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    def map_value(x, in_min, in_max, out_min, out_max):
        # Wertebereich von einer Skala auf eine andere umrechnen
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    def set_color(r, g, b):
        # Setze die Farbe durch Anpassen der PWM-Duty-Cycles
        red.duty_u16(map_value(r, 0, 255, 0, 65535))
        green.duty_u16(map_value(g, 0, 255, 0, 65535))
        blue.duty_u16(map_value(b, 0, 255, 0, 65535))

    # Beispiel: Setze die Farbe auf Orange
    set_color(255, 165, 0)

Wenn der Code läuft, sollte die RGB-LED orange leuchten.

**Den Code verstehen**

#. Bibliotheken importieren:

   * ``machine``: Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Zeitfunktionen (in diesem Beispiel nicht genutzt, aber für Animationen hilfreich).

#. PWM-Objekte initialisieren:

   * PWM-Objekte für die RGB-LED erstellen und die Frequenz auf 1000 Hz setzen.

   .. code-block:: python

        # Initialize PWM for red, green, and blue pins
        red = machine.PWM(machine.Pin(13))
        green = machine.PWM(machine.Pin(14))
        blue = machine.PWM(machine.Pin(15))

        # Set the PWM frequency
        red.freq(1000)
        green.freq(1000)
        blue.freq(1000)

#. Die Funktion ``map_value`` definieren:

   * Die ``duty_u16``-Methode benötigt Werte von 0 bis 65535, während RGB-Werte üblicherweise zwischen 0 und 255 liegen.
   * ``map_value`` skaliert die Werte entsprechend.

   .. code-block:: python

        def map_value(x, in_min, in_max, out_min, out_max):
            # Map a value from one range to another
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Die Funktion ``set_color`` definieren:

   Diese Funktion nimmt RGB-Werte (0–255) entgegen und stellt den Duty-Cycle der PWM-Kanäle entsprechend ein.

   .. code-block:: python

        def set_color(r, g, b):
            # Set the color by adjusting duty cycles
            red.duty_u16(map_value(r, 0, 255, 0, 65535))
            green.duty_u16(map_value(g, 0, 255, 0, 65535))
            blue.duty_u16(map_value(b, 0, 255, 0, 65535))

#. Wunschfarbe einstellen: 

   Rufe ``set_color(255, 165, 0)`` auf, um die RGB-LED auf Orange zu setzen.  
   Du kannst die Werte beliebig ändern, um andere RGB-Farben zu erzeugen.

**Beispiel: Farbwechsel**

Lass uns den Code erweitern, um verschiedene Farben automatisch durchlaufen zu lassen.

#. Um die RGB-Werte für verschiedene Farben zu finden, kannst du eine Grafiksoftware oder einen Online-Farbwähler verwenden. Beispielsweise:

   * Rot: (255, 0, 0)
   * Grün: (0, 255, 0)
   * Blau: (0, 0, 255)
   * Weiß: (255, 255, 255)
   * Lila: (128, 0, 128)

#. Schreibe den Code.

   Wir definieren eine Liste mit RGB-Tupeln, die verschiedene Farben repräsentieren.  
   Die ``while True``-Schleife durchläuft die Liste, setzt die RGB-LED auf die jeweilige Farbe und wartet eine Sekunde, bevor zur nächsten Farbe gewechselt wird.

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialisierung der PWM für die RGB-Pins
       red = machine.PWM(machine.Pin(13))
       green = machine.PWM(machine.Pin(14))
       blue = machine.PWM(machine.Pin(15))
   
       # Setze die PWM-Frequenz
       red.freq(1000)
       green.freq(1000)
       blue.freq(1000)
   
       def map_value(x, in_min, in_max, out_min, out_max):
           return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)
   
       def set_color(r, g, b):
           red.duty_u16(map_value(r, 0, 255, 0, 65535))
           green.duty_u16(map_value(g, 0, 255, 0, 65535))
           blue.duty_u16(map_value(b, 0, 255, 0, 65535))
   
       # Liste der Farben zum Durchlaufen
       colors = [
           (255, 0, 0),     # Rot
           (0, 255, 0),     # Grün
           (0, 0, 255),     # Blau
           (255, 255, 0),   # Gelb
           (0, 255, 255),   # Cyan
           (255, 0, 255),   # Magenta
           (255, 255, 255)  # Weiß
       ]
   
       while True:
           for color in colors:
               set_color(*color)
               utime.sleep(1)

Sobald der Code läuft, wird die RGB-LED eine Sequenz von Farben durchlaufen: Rot, Grün, Blau, Gelb, Cyan, Magenta und Weiß.

Jede Farbe wird eine Sekunde lang angezeigt, bevor zur nächsten übergegangen wird.

**Fazit**

Durch die Steuerung der Intensität der roten, grünen und blauen Komponenten einer RGB-LED mittels PWM können wir eine Vielzahl von Farben erzeugen.  
Dieses Projekt demonstriert die Grundlagen der additiven Farbmischung und bildet eine solide Basis für farbenfrohe Lichtprojekte mit Mikrocontrollern.

**Referenzen**

* |link_mpython_pwm|
