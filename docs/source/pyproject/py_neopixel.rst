
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_neopixel:

3.3 Steuerung eines RGB-LED-Streifens
===========================================================

In dieser Lektion lernen wir, wie man einen **RGB-LED-Streifen** (speziell den Typ WS2812) mit dem Raspberry Pi Pico 2 und MicroPython steuert.

Der WS2812 ist eine intelligente LED, die einen Steuerkreis und einen RGB-Chip in einem 5050-LED-Gehäuse integriert. Jede LED verfügt über einen eigenen integrierten Controller, der es uns ermöglicht, jede LED individuell über eine einzige Datenleitung zu steuern. Das bedeutet, dass wir die Farbe und Helligkeit jeder LED auf dem Streifen unabhängig ändern können.


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

Sie können sie auch einzeln über die untenstehenden Links kaufen.

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
        - :ref:`cpn_ws2812`
        - 1
        - |link_ws2812_buy|

**Schaltplan**

|sch_ws2812|


**Verdrahtungsdiagramm**

|wiring_ws2812|

Seien Sie vorsichtig mit dem Stromverbrauch. Während der VBUS-Pin des Pico Strom für eine kleine Anzahl von LEDs (wie 8) liefern kann, kann die Verwendung mehrerer LEDs eine externe Stromversorgung erfordern, um eine Überlastung des Pico zu vermeiden.

**Code schreiben**

.. note::

    * Öffnen Sie die Datei ``3.3_rgb_led_strip.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.

    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

     
    
    * Hier benötigen Sie die Bibliothek namens ``ws2812.py``, bitte überprüfen Sie, ob sie auf den Pico hochgeladen wurde, für ein detailliertes Tutorial siehe :ref:`add_libraries_py`.


.. code-block:: python

    import machine
    from ws2812 import WS2812

    # Initialisieren des LED-Streifens
    led_strip = WS2812(machine.Pin(0), 8)  # Verwendung von GP0, 8 LEDs

    # Farben für jede LED einstellen
    led_strip[0] = [255, 0, 0]     # Rot
    led_strip[1] = [0, 255, 0]     # Grün
    led_strip[2] = [0, 0, 255]     # Blau
    led_strip[3] = [255, 255, 0]   # Gelb
    led_strip[4] = [0, 255, 255]   # Cyan
    led_strip[5] = [255, 0, 255]   # Magenta
    led_strip[6] = [255, 255, 255] # Weiß
    led_strip[7] = [128, 128, 128] # Grau

    # Den LED-Streifen aktualisieren, um die Farben anzuzeigen
    led_strip.write()

Wenn dieser Code ausgeführt wird, zeigt der mit dem Pin GP0 verbundene WS2812 LED-Streifen mit 8 LEDs folgende Farben:

* **LED 0**: Rot (255, 0, 0)
* **LED 1**: Grün (0, 255, 0)
* **LED 2**: Blau (0, 0, 255)
* **LED 3**: Gelb (255, 255, 0)
* **LED 4**: Cyan (0, 255, 255)
* **LED 5**: Magenta (255, 0, 255)
* **LED 6**: Weiß (255, 255, 255)
* **LED 7**: Grau (128, 128, 128)

**Code verstehen**

#. Bibliotheken importieren:

   * ``machine``: Bietet Zugang zu hardwarebezogenen Funktionen.
   * ``WS2812``: Die Bibliothek zur Steuerung des WS2812 LED-Streifens.

#. LED-Streifen initialisieren:

   * ``led_strip = WS2812(machine.Pin(0), 8)``: Initialisiert den LED-Streifen, der mit Pin GP0 verbunden ist und 8 LEDs hat.

#. Farben einstellen:

   * ``led_strip[0] = [255, 0, 0]``: Weist jeder LED eine Farbe zu, die RGB-Werte verwendet (Rot, Grün, Blau), die von 0 bis 255 reichen.

#. LED-Streifen aktualisieren:

   * ``led_strip.write()``: Sendet die Farbdaten an den LED-Streifen, um die Farben anzuzeigen.

**Lassen Sie uns einen fließenden Regenbogeneffekt erstellen!**

Jetzt erstellen wir einen farbenfrohen fließenden Lichteffekt, indem wir zufällig Farben generieren und sie entlang des Streifens verschieben.

.. code-block:: python

    import machine
    from ws2812 import WS2812
    import utime
    import urandom

    # Anzahl der LEDs im Streifen
    NUM_LEDS = 8

    # LED-Streifen mit 8 LEDs initialisieren
    led_strip = WS2812(machine.Pin(0), NUM_LEDS)

    def flowing_light():
        # Farben entlang des Streifens verschieben
        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]
        # Eine zufällige Farbe für die erste LED generieren
        led_strip[0] = [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]
        # Den Streifen aktualisieren
        led_strip.write()
        # Kleine Verzögerung für eine fließende Animation
        utime.sleep_ms(100)

    # Hauptzyklus
    while True:
        flowing_light()


Wenn der Code ausgeführt wird, zeigt der LED-Streifen einen dynamischen fließenden Effekt mit zufälligen Farben, bei dem eine neue zufällige Farbe am Anfang eingeführt und mit jedem Zyklus zum Ende verschoben wird.

**Code verstehen**

#. Zufällige Farbgenerierung: Erzeugt eine zufällige RGB-Farbe, bei der jede Komponente von 0 bis 255 reicht.

   .. code-block:: python

        [urandom.getrandbits(8), urandom.getrandbits(8), urandom.getrandbits(8)]

#. Farben verschieben: Bewegt jede LED-Farbe auf die nächste Position und erzeugt einen fließenden Effekt.

   .. code-block:: python

        for i in range(NUM_LEDS - 1, 0, -1):
            led_strip[i] = led_strip[i - 1]

#. Endlosschleife: Aktualisiert kontinuierlich den LED-Streifen, um die Animation am Laufen zu halten.

   .. code-block:: python

        while True:
            flowing_light()

**Weiter experimentieren**

* **Geschwindigkeit anpassen**: Ändern Sie ``utime.sleep_ms(100)``, um den fließenden Effekt schneller oder langsamer zu machen.
* **Mehr LEDs**: Wenn Sie einen längeren Streifen haben, ändern Sie die Zahl in ``WS2812(machine.Pin(0), number_of_leds)`` entsprechend.
* **Eigene Animationen**: Experimentieren Sie mit verschiedenen Mustern und Farbkombinationen, um Ihre eigenen Animationen zu erstellen.

**Schlussfolgerung**

Sie haben erfolgreich gelernt, wie man einen RGB-LED-Streifen mit dem Raspberry Pi Pico 2 und MicroPython steuert! Dies eröffnet eine Welt von Möglichkeiten für die Erstellung atemberaubender Lichtdisplays, Stimmungsbeleuchtung oder sogar interaktiver Kunstprojekte.
