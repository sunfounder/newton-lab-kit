
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_micro:

2.8 Sanft Drücken
==========================

In dieser Lektion lernen wir, wie man einen **Mikroschalter** (auch als Endschalter bekannt) mit dem Raspberry Pi Pico 2 verwendet, um zu erkennen, wann er gedrückt oder losgelassen wird. Mikroschalter werden häufig in Geräten wie Mikrowellentüröffnern, Druckerabdeckungen oder als Endanschläge in 3D-Druckern verwendet, weil sie zuverlässig sind und häufige Aktivierungen vertragen.

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
        - :ref:`cpn_capacitor`
        - 1(104)
        - |link_capacitor_buy|
    *   - 7
        - :ref:`cpn_micro_switch`
        - 1
        - 

**Verständnis des Mikroschalters**

Ein Mikroschalter hat typischerweise drei Anschlüsse:

|img_micro_switch|

- **Common (C)**: Der mittlere Pin.
- **Normally Open (NO)**: Verbunden mit dem Common-Pin, wenn der Schalter **gedrückt** ist.
- **Normally Closed (NC)**: Verbunden mit dem Common-Pin, wenn der Schalter **nicht gedrückt** ist.

Durch entsprechendes Verbinden des Schalters können wir erkennen, wann er gedrückt wird, indem wir die Spannung an einem GPIO-Pin ablesen.

**Schaltplan**

|sch_limit_sw|

Standardmäßig ist GP14 niedrig und wenn gedrückt, wird GP14 hoch.

Der Zweck des 10K-Widerstands ist es, den GP14 während des Drückens niedrig zu halten.

Wenn Sie einen mechanischen Schalter drücken, können die Kontakte prellen, was zu mehreren schnellen Übergängen zwischen offenen und geschlossenen Zuständen führt. Der Kondensator, der zwischen GP14 und GND geschaltet ist, hilft, dieses Rauschen zu filtern.

* **Schalter nicht gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NC**-Pin verbunden, der mit **GND** verbunden ist.
  * **GP14** liest **NIEDRIG** (0V).

* **Schalter gedrückt**:

  * Der **Common (C)**-Pin ist mit dem **NO**-Pin verbunden, der mit **3.3V** verbunden ist.
  * **GP14** liest **HOCH** (3.3V).

**Verdrahtungsdiagramm**

|wiring_limit_sw|


**Code schreiben**

Wir schreiben ein MicroPython-Programm, das erkennt, wann der Mikroschalter gedrückt wird und entsprechend eine Nachricht ausgibt.

.. note::

  * Öffnen Sie die Datei ``2.8_micro_switch.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.

  * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

  

.. code-block:: python

    import machine
    import utime

    # Initialisieren von GP14 als Eingangspin
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # Entprellverzögerung

Wenn der Code läuft, wird das folgende Phänomen beobachtet:

* **Nicht gedrückt**: Es sollte keine Nachricht erscheinen.
* **Gedrückt**: "Der Schalter ist gedrückt!" sollte jedes Mal in der Konsole erscheinen, wenn der Schalter gedrückt wird.

**Code verstehen**

#. Import-Module:

   * ``import machine``: Zugang zu Hardware-Funktionen.
   * ``import utime``: Zeitbezogene Funktionen.

#. Initialisierung des Schalter-Pins:

   * ``switch = machine.Pin(14, machine.Pin.IN)``: Stellt GP14 als Eingangspin ein.

#. Hauptschleife:

   * ``while True``: Startet eine unendliche Schleife.
   * ``if switch.value() == 1``: Überprüft, ob der Schalter gedrückt ist (GP14 liest HOCH).
   * ``print("The switch is pressed!")``: Gibt eine Nachricht in der Konsole aus.
   * ``utime.sleep(0.5)``: Fügt eine Verzögerung hinzu, um den Schalter zu entprellen und mehrfache Erkennungen von einem einzigen Druck zu verhindern.


**Alternative Verdrahtung: Verwendung des internen Pull-Down-Widerstands**

Wenn Sie die Verdrahtung weiter vereinfachen möchten, können Sie sich ausschließlich auf den internen Pull-Down-Widerstand verlassen:

* Schaltkreis ändern:

  * Entfernen Sie den externen 10 kΩ-Widerstand und den 0.1 µF-Kondensator.
  * Mikroschalterverbindungen:

    * **Common (C) Terminal**: Verbinden mit GP14 am Pico.
    * **Normally Open (NO) Terminal**: Verbinden mit 3.3V am Pico.
    * **Normally Closed (NC) Terminal**: Unverbunden lassen.

* Geänderter Code:

  .. code-block:: python

      import machine
      import utime

      # Initialisieren von GP14 als Eingangspin mit internem Pull-Down-Widerstand
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # Entprellverzögerung
    

**Praktische Anwendungen**

* **Grenzerkennung**: Verwenden Sie den Mikroschalter als Endanschlag in CNC-Maschinen oder 3D-Druckern, um das Bewegungslimit zu erkennen.
* **Sicherheitsverriegelungen**: Stellen Sie sicher, dass ein Gerät nur funktioniert, wenn bestimmte Bedingungen erfüllt sind (z. B. eine Tür ist geschlossen).
* **Benutzereingabe**: Integrieren Sie ihn in Projekte, bei denen ein robuster und zuverlässiger Knopf benötigt wird.

**Weiterführende Experimente**

* Steuern einer LED:

  Verbinden Sie eine LED mit einem anderen GPIO-Pin (z. B. GP15) mit einem geeigneten Widerstand. Ändern Sie den Code, um die LED einzuschalten, wenn der Schalter gedrückt wird.
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # LED einschalten
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # LED ausschalten

* Zählen von Drücken:

  Ändern Sie den Code, um zu zählen, wie oft der Schalter gedrückt wurde.

  * Steuern einer LED:

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**Schlussfolgerung**

Die Verwendung eines Mikroschalters mit dem Raspberry Pi Pico 2 ermöglicht es Ihnen, physische Interaktionen zuverlässig zu erkennen. Das Verständnis, wie man den Schalter verdrahtet und seinen Zustand in Ihrem Code liest, ist entscheidend für die Erstellung reaktiver und interaktiver Projekte.
