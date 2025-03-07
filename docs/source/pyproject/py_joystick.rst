.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_joystick:

4.1 Auslesen von Werten eines Joysticks
==========================================

In dieser Lektion lernen wir, wie man einen **Joystick** mit dem Raspberry Pi Pico 2 verwendet, um analoge Werte zu lesen und Tastendrücke zu erkennen. Ein Joystick ist ein gängiges Eingabegerät, das die Steuerung der Bewegung entlang zweier Achsen (X und Y) ermöglicht und oft einen Knopf umfasst, der beim Herunterdrücken aktiviert wird (Z-Achse).

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
        - :ref:`cpn_resistor`
        - 1(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_joystick`
        - 1
        - 

**Verständnis des Joysticks**

Ein typisches Joystick-Modul besteht aus zwei Potentiometern, die rechtwinklig zueinander positioniert sind:

* **X-Achsen-Potentiometer**: Misst die Bewegung nach links und rechts.
* **Y-Achsen-Potentiometer**: Misst die Bewegung nach oben und unten.
* **Z-Achse (Schalter)**: Ein digitaler Knopf, der aktiviert wird, wenn man auf den Joystick drückt.

Durch das Auslesen der analogen Werte von den X- und Y-Achsen können Sie die Position des Joysticks bestimmen. Der Z-Achsen-Knopf ermöglicht es Ihnen zu erkennen, wann der Joystick heruntergedrückt wird.

**Schaltplan**

|sch_joystick|

Der SW-Pin ist mit einem 10K Pull-Up-Widerstand verbunden, um ein stabiles hohes Signal am SW-Pin (Z-Achse) zu erhalten, wenn der Joystick nicht gedrückt ist; andernfalls ist der SW in einem schwebenden Zustand und der Ausgabewert kann zwischen 0/1 variieren.

**Verdrahtungsplan**

|wiring_joystick|

**Code schreiben**

Lassen Sie uns ein MicroPython-Programm schreiben, um die X- und Y-Positionen des Joysticks zu lesen und Tastendrücke zu erkennen.

.. note::

    * Öffnen Sie die Datei ``4.1_toggle_the_joystick.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.

    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Initialisieren Sie ADC für die X- und Y-Achsen
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Initialisieren Sie den digitalen Eingang für den Schalter
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        # Lesen Sie die analogen Werte (0-65535)
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Lesen Sie den Schalterzustand (0 oder 1)
        z_state = z_button.value()
        
        # Drucken Sie die Werte
        print("X:", x_value, "Y:", y_value, "Button:", z_state)
        
        # Kleine Verzögerung, um die Ausgabe lesbar zu machen
        utime.sleep(0.2)


**Verständnis des Codes**

#. Importieren Sie Module:

   * ``machine``: Bietet Zugang zu hardwarebezogenen Funktionen.
   * ``utime``: Enthält zeitbezogene Funktionen für Verzögerungen.

#. Initialisieren Sie die ADC-Eingänge:

   Wir richten Analog-Digital-Wandler (ADC) an den Pins GP27 und GP26 ein, um die X- und Y-Positionen des Joysticks zu lesen.

   .. code-block:: python

      x_adc = machine.ADC(27)  # X-Achse an GP27 angeschlossen
      y_adc = machine.ADC(26)  # Y-Achse an GP26 angeschlossen

#. Initialisieren Sie den Digitalen Eingang:

   * Konfigurieren Sie GP22 als digitalen Eingang mit einem internen Pull-Up-Widerstand für den Knopf des Joysticks (Z-Achse).
   * Der Parameter ``machine.Pin.PULL_UP`` stellt sicher, dass der Pin hoch (1) liest, wenn er nicht gedrückt wird, und niedrig (0), wenn er gedrückt wird.

   .. code-block:: python

      z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

#. Hauptschleife zum Lesen der Werte:

   * Analoge Werte lesen: ``read_u16()`` liest einen 16-Bit-Wert (0 bis 65535), der das Spannungsniveau darstellt.
   * Werte drucken: Zeigt die X- und Y-Positionen und den Schalterzustand in der Konsole an.

   .. code-block:: python

      while True:
          x_value = x_adc.read_u16()
          y_value = y_adc.read_u16()
          z_state = z_button.value()
          
          print("X:", x_value, "Y:", y_value, "Button:", z_state)
          
          utime.sleep(0.2)

Nachdem das Programm ausgeführt wurde, öffnen Sie das Shell- oder REPL-Fenster in Thonny.

* Sie sollten sehen, wie die X-, Y- und Button-Werte ausgegeben werden.
* Bewegen Sie den Joystick in verschiedene Richtungen und drücken Sie den Knopf, um zu sehen, wie sich die Werte ändern.

**Werte interpretieren**

* X- und Y-Werte:

  * Bereich von 0 bis 65535.
  * Mittelposition: Um 32768.
  * Ganz links oder oben: Nahe 0.
  * Ganz rechts oder unten: Nahe 65535.

* Schalterzustand:

  * Nicht gedrückt: 1.
  * Gedrückt: 0.

**Weitere Experimente**

* Werte normalisieren:

  Konvertieren Sie die rohen ADC-Werte in einen Bereich von -100 bis 100 für eine einfachere Interpretation.

  .. code-block:: python

    import machine
    import utime

    # Initialisieren Sie ADC für die X- und Y-Achsen
    x_adc = machine.ADC(27)  # GP27
    y_adc = machine.ADC(26)  # GP26

    # Initialisieren Sie den digitalen Eingang für den Schalter
    z_button = machine.Pin(22, machine.Pin.IN, machine.Pin.PULL_UP)

    # Funktion zum Normalisieren der ADC-Werte in einen Bereich von -100 bis 100
    def normalize(value):
        return int((value - 32768) / 327.68)

    while True:
        # Lesen Sie die analogen Werte (0-65535)
        x_value = x_adc.read_u16()
        y_value = y_adc.read_u16()
        
        # Lesen Sie den Schalterzustand (0 oder 1)
        z_state = z_button.value()
        
        # Normalisieren Sie die Werte auf -100 bis 100
        x_normalized = normalize(x_value)
        y_normalized = normalize(y_value)
        
        # Drucken Sie die normalisierten Werte
        print("X:", x_normalized, "Y:", y_normalized, "Button:", z_state)
        
        # Kleine Verzögerung, um die Ausgabe lesbar zu machen
        utime.sleep(0.2)


* Steuern Sie ein Ausgabeelement:

  Verwenden Sie den Joystick-Eingang, um eine LED, einen Servo oder einen Motor zu steuern. Beispielsweise können Sie ein Objekt basierend auf dem X-Achsen-Wert nach links oder rechts bewegen.

* Erstellen Sie einen Spielcontroller:

  Kombinieren Sie die Joystick-Eingaben, um ein einfaches Spiel oder eine grafische Ausgabe zu steuern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man analoge und digitale Eingänge eines Joysticks mit dem Raspberry Pi Pico 2 liest. Dieses Wissen ermöglicht es Ihnen, Joystick-Steuerungen in Ihre Projekte einzubinden und interaktive Anwendungen wie Roboter, Spiele oder Fernbedienungen zu ermöglichen.

