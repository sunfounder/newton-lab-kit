.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 ein und tausche dich mit anderen Technikbegeisterten aus.

    **Warum solltest du beitreten?**

    - **Experten-Support**: Erhalte Hilfe von unserer Community und unserem Team, um Probleme nach dem Kauf und technische Herausforderungen zu lösen.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf neue Produktankündigungen und exklusive Einblicke.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Feiertagsaktionen und Gewinnspiele**: Nimm an Verlosungen und Sonderaktionen zu Feiertagen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_button:

2.5 Tasterwert auslesen
=============================

In dieser Lektion lernen wir, wie man Eingaben von einem Taster mit dem Raspberry Pi Pico 2 liest. Bisher haben wir die GPIO-Pins hauptsächlich für Ausgaben genutzt, beispielsweise um LEDs zu steuern. Nun verwenden wir einen GPIO-Pin als Eingang, um zu erkennen, wann ein Taster gedrückt wird. Dies ist eine grundlegende Fähigkeit für interaktive Projekte.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir folgende Komponenten:

Es ist auf jeden Fall praktisch, ein komplettes Kit zu kaufen. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit	
        - 450+	
        - |link_newton_lab_kit|

Alternativ kannst du die Komponenten auch einzeln erwerben:


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
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|


**Schaltplan**

|sch_button|

Solange eine Seite des Tasters mit 3,3 V verbunden ist und die andere mit GP14, wird GP14 beim Drücken des Tasters HIGH.  
Wenn der Taster nicht gedrückt wird, befindet sich GP14 in einem undefinierten Zustand und kann HIGH oder LOW sein.  
Damit GP14 im nicht gedrückten Zustand stabil auf LOW bleibt, wird ein 10KΩ-Pull-down-Widerstand zwischen GP14 und GND angeschlossen.

* **Taster nicht gedrückt**: GP14 ist über den Widerstand mit GND verbunden und liest **LOW (0)**.
* **Taster gedrückt**: GP14 wird direkt mit 3,3 V verbunden und liest **HIGH (1)**.

**Verdrahtungsdiagramm**

Ein vierpoliger Taster hat die Form eines „H“. Die beiden linken oder rechten Pins sind miteinander verbunden. Das bedeutet, dass beim Überbrücken der zentralen Lücke zwei halbe Reihen mit derselben Reihennummer verbunden werden. (Zum Beispiel sind in meiner Schaltung E23 und F23 bereits verbunden, ebenso wie E25 und F25).

Solange der Taster nicht gedrückt wird, bleiben die linken und rechten Pins voneinander isoliert, sodass kein Strom von einer Seite zur anderen fließen kann.

|wiring_button|


**Code schreiben**

Wir schreiben ein einfaches Programm, das eine Nachricht ausgibt, wenn der Taster gedrückt wird.

.. note::

  * Öffne die Datei ``2.5_read_button_value.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny. Klicke dann auf "Run" oder drücke F5.
  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.

.. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 als Eingabepin
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # Entprellverzögerung

Wenn der Code ausgeführt wird, passiert Folgendes:

* **Nicht gedrückt**: Keine Ausgabe in der Konsole.
* **Gedrückt**: "Taster gedrückt!" erscheint in der Konsole.



**Den Code verstehen**

#. Module importieren:

   * ``machine``: Ermöglicht den Zugriff auf die Hardwarefunktionen.
   * ``utime``: Bietet Zeitfunktionen wie Verzögerungen.

#. Taster-Pin konfigurieren:

   * ``button = machine.Pin(14, machine.Pin.IN)``: Initialisiert GPIO14 als Eingang.

#. Hauptschleife:

   * ``while True``: Erstellt eine Endlosschleife.
   * ``if button.value() == 1``: Überprüft, ob der Taster gedrückt wurde.
   * ``button.value()`` gibt 1 zurück, wenn der Pin auf HIGH (Taster gedrückt) steht.
   * ``print("Button pressed!")``: Gibt eine Nachricht in der Konsole aus.
   * ``utime.sleep(0.2)``: Wartet 200 Millisekunden, um den Taster zu entprellen.

**Alternative Verkabelung mit Pull-up-Widerstand**

Der Taster kann auch mit einem Pull-up-Widerstand angeschlossen werden:

#. Schalte einen 10KΩ-Widerstand zwischen GP14 und 3,3 V, sodass der Pin HIGH bleibt, wenn der Taster nicht gedrückt wird.

    |sch_button_pullup|

    |wiring_button_pullup|

  * **Taster nicht gedrückt**: Der GP14-Pin ist über den Widerstand mit 3,3 V verbunden und wird daher als HIGH (1) gelesen.
  * **Taster gedrückt**: Der GP14-Pin ist über den Taster mit GND verbunden und wird daher als LOW (0) gelesen.

#. Angepasster Code für Pull-up-Konfiguration:

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialisiere GP14 als Eingangspin
       button = machine.Pin(14, machine.Pin.IN)
   
       while True:
           if button.value() == 0:
               print("Button pressed!")
               utime.sleep(0.2)

**Interne Pull-up/Pull-down-Widerstände nutzen**

Der Raspberry Pi Pico 2 ermöglicht das Aktivieren interner Pull-up- oder Pull-down-Widerstände, sodass externe Widerstände überflüssig werden.

Die Verwendung interner Widerstände vereinfacht die Verdrahtung und spart Platz, da keine zusätzlichen externen Widerstände auf dem Breadboard erforderlich sind.

* Interner Pull-down-Widerstand:

  .. code-block:: python
  
      import machine
      import utime
  
      # Initialisiere GP14 mit internem Pull-down-Widerstand
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* Interner Pull-up-Widerstand:

  .. code-block:: python

    import machine
    import utime

    # Initialisiere GP14 mit internem Pull-up-Widerstand
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Weitere Experimente**

* **Mehrere Taster verwenden**: Verbinde zusätzliche Taster mit anderen GPIO-Pins und erweitere den Code entsprechend.
* **LED-Steuerung**: Kombiniere die Tastereingabe mit einer LED-Ausgabe, um die LED mit dem Taster umzuschalten.

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # LED-Zustand umschalten
            led.value(led_state)
            utime.sleep(0.2)

**Fazit**

Das Lesen von Eingaben über einen Taster ist eine grundlegende Fähigkeit bei der Mikrocontroller-Programmierung. Mit Pull-up- und Pull-down-Widerständen kann man stabile Eingaben sicherstellen, um interaktive Projekte zu erstellen.
