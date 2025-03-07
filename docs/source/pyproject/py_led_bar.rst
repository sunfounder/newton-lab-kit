.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feierlichkeiten teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_led_bar:

2.2 Den Pegel anzeigen
=============================

In dieser Lektion lernen wir, wie man mit dem Raspberry Pi Pico 2 eine LED-Balkenanzeige steuert. Eine LED-Balkenanzeige besteht aus 10 LEDs in einer Linie, die typischerweise verwendet wird, um Pegel wie Lautstärke, Signalstärke oder andere Messwerte anzuzeigen. Wir werden die LEDs nacheinander aufleuchten lassen, um einen Pegelanzeigeeffekt zu erzeugen.

|img_led_bar_pin|


**Was Sie benötigen**

Für dieses Projekt benötigen Sie die folgenden Komponenten.

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

Sie können diese auch einzeln über die untenstehenden Links kaufen.


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
        - 10(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led_bar`
        - 1
        - 

**Schaltplan**

|sch_ledbar|

In diesem Projekt ist jede der 10 LEDs in der LED-Balkenanzeige mit dem Raspberry Pi Pico 2 verbunden. Die Anoden (positive Pole) der LEDs sind mit den GPIO-Pins GP6 bis GP15 verbunden. Die Kathoden (negative Pole) sind über 220Ω Widerstände mit dem GND (Erdung) Pin verbunden.

**Verdrahtungsplan**

|wiring_ledbar|

**Schreiben des Codes**

.. note::

  * Öffnen Sie die Datei ``2.2_display_the_level.py`` unter dem Pfad ``newton-lab-kit/micropython`` oder kopieren Sie den untenstehenden Code in Thonny. Dann klicken Sie auf "Run Current Script" oder drücken Sie **F5**, um es auszuführen.
  * Stellen Sie sicher, dass der Interpreter "MicroPython (Raspberry Pi Pico).COMxx" in der unteren rechten Ecke von Thonny ausgewählt ist.

.. code-block:: python

  import machine
  import utime

  # Definieren Sie die GPIO-Pins, die mit den LEDs verbunden sind
  pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  leds = []

  # Initialisieren Sie jeden Pin als Ausgang und speichern Sie ihn in der Liste leds
  for pin_number in pins:
      led = machine.Pin(pin_number, machine.Pin.OUT)
      leds.append(led)

  while True:
      # LEDs nacheinander einschalten, um den Pegel zu erhöhen
      for led in leds:
          led.value(1)  # Schalten Sie die LED ein
          utime.sleep(0.2)
      # LEDs nacheinander ausschalten, um den Pegel zu verringern
      for led in leds:
          led.value(0)  # Schalten Sie die LED aus
          utime.sleep(0.2)

Wenn Sie das Programm ausführen, leuchten die LEDs auf der LED-Balkenanzeige nacheinander von der ersten bis zur letzten auf, was einen ansteigenden Pegel-Effekt erzeugt. Dann schalten sie sich nacheinander aus, was einen absteigenden Pegel simuliert.

**Verständnis des Codes**

In diesem Projekt steuern wir mehrere LEDs mit Listen und Schleifen in MicroPython, was den Code effizient und leicht lesbar macht.

Lassen Sie uns die Schlüsselteile des Codes durchgehen:

1. Importieren von Modulen:

   * ``import machine``: Bietet Zugriff auf die Hardware-Funktionalitäten des Raspberry Pi Pico 2.
   * ``import utime``: Ermöglicht die Nutzung von zeitbezogenen Funktionen wie Verzögerungen.

2. Pins definieren und LEDs initialisieren:

   * Wir erstellen eine Liste ``pins`` mit den GPIO-Pinnummern, die mit den LEDs verbunden sind, und initialisieren eine leere Liste ``leds``, um die LED-Objekte zu speichern.

     .. code-block:: python

      # Definieren Sie die GPIO-Pins, die mit den LEDs verbunden sind
      pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      leds = []
     
   * Mit einer ``for``-Schleife iterieren wir über jede Pinnummer, stellen sie als Ausgangspin ein und fügen das entsprechende ``Pin``-Objekt zur Liste ``leds`` hinzu.
     
     .. code-block:: python

        for pin_number in pins:
            led = machine.Pin(pin_number, machine.Pin.OUT)
            leds.append(led)
     
3. Den Pegel-Anzeigeeffekt erstellen:

   * Die Schleife ``while True:`` läuft unendlich.
   * Pegel erhöhen:

     * Verwenden Sie eine ``for``-Schleife, um über jede ``led`` in der Liste ``leds`` zu iterieren.
     * ``led.value(1)`` schaltet die LED ein.
     * ``utime.sleep(0.2)`` fügt eine 200-ms-Verzögerung hinzu, bevor die nächste LED eingeschaltet wird.
     
     .. code-block:: python

        for led in leds:
            led.value(1)
            utime.sleep(0.2)
     
   * Pegel verringern:

     * Schalten Sie jede LED nacheinander aus, indem Sie eine weitere ``for``-Schleife verwenden.
     * ``led.value(0)`` schaltet die LED aus.

     .. code-block:: python

        for led in leds:
            led.value(0)
            utime.sleep(0.2)
  
**Weitere Experimente**

Fühlen Sie sich frei, mit dem Code zu experimentieren:

* Geschwindigkeit ändern:

  * Passen Sie die Verzögerung in ``utime.sleep(0.2)`` an, um die LEDs schneller oder langsamer leuchten zu lassen.

* Reihenfolge umkehren:

  * Verwenden Sie ``reversed(leds)``, um die Reihenfolge der LEDs umzukehren.

    .. code-block:: python

        for led in reversed(leds):
            led.value(1)
            utime.sleep(0.2)
    
* Ping-Pong-Effekt erstellen:

  * Lassen Sie die LEDs von links nach rechts und dann wieder von rechts nach links aufleuchten.

    .. code-block:: python

        while True:
            for led in leds:
                led.value(1)
                utime.sleep(0.1)
            for led in reversed(leds):
                led.value(0)
                utime.sleep(0.1)
    
**Fazit**

Indem wir jede LED einzeln steuern, haben wir eine einfache, aber effektive Pegelanzeige mit dem Raspberry Pi Pico 2 erstellt. Dieses Projekt demonstriert die Leistungsfähigkeit von Listen und Schleifen in Python und ermöglicht es uns, mehrere Ausgänge effizient zu verwalten.

Das Verständnis dafür, wie man mit mehreren GPIO-Pins arbeitet und Programmierstrukturen wie Listen und Schleifen verwendet, ist essentiell für komplexere Projekte, wie das Erstellen von Animationen, die Steuerung mehrerer Sensoren oder den Bau interaktiver Geräte.

**Referenzen**

* |link_python_for|
* |link_python_list|
