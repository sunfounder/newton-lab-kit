.. note:: 

    Hallo und herzlich willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook!  
    Tauche gemeinsam mit anderen Technikbegeisterten tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Fachkundige Unterstützung**: Erhalte Hilfe von unserer Community und unserem Team bei technischen Herausforderungen und Problemen nach dem Kauf.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Sonderaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_pot:

2.11 Den Drehregler nutzen
=============================

In dieser Lektion lernen wir, wie analoge Eingaben mithilfe des integrierten Analog-Digital-Wandlers (ADC) des Raspberry Pi Pico 2 ausgelesen werden können, um damit die Helligkeit einer LED zu steuern. Als analoges Eingabegerät verwenden wir ein Potentiometer, einen einstellbaren Widerstand. Durch das Drehen des Potentiometerknopfs verändert sich die Spannung, die vom Pico gelesen wird, und diese nutzen wir zur Steuerung der LED-Helligkeit über Pulsweitenmodulation (PWM).


**Verständnis von analogen Eingaben**

Bisher haben wir digitale Eingänge und Ausgänge verwendet, die entweder EIN (hohe Spannung) oder AUS (niedrige Spannung) sind. Viele Signale aus der realen Welt sind jedoch analog und variieren kontinuierlich innerhalb eines Wertebereichs, z. B. Lichtintensität, Temperatur oder Lautstärke.

Der Raspberry Pi Pico 2 besitzt einen ADC, der analoge Spannungen erfasst und in digitale Werte umwandelt.

Der ADC berechnet den digitalen Wert aus der analogen Spannung mit der Formel:

.. code-block::

  Digital Value = (Analog Voltage/3.3V) * 65535


**Pico's ADC-Pins**

|pin_adc|

Der Pico verfügt über drei GPIO-Pins für analoge Eingaben:

* **GP26** (ADC0)
* **GP27** (ADC1)
* **GP28** (ADC2)

Zusätzlich gibt es einen vierten ADC-Kanal, der mit einem internen Temperatursensor verbunden ist (ADC4), den wir in späteren Lektionen untersuchen werden.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt:  

Ein vollständiges Kit ist hier erhältlich:  

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten einzeln erworben werden:


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
        - 1 (220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_potentiometer`
        - 1
        - |link_potentiometer_buy|

**Schaltplan**

|sch_pot|

**Verdrahtung**

|wiring_pot|


**Code schreiben**

.. note::

  * Öffne die Datei ``2.11_turn_the_knob.py`` unter ``newton-lab-kit/micropython`` oder kopiere den folgenden Code in Thonny. Klicke dann auf „Run Current Script“ oder drücke **F5**.
  * Stelle sicher, dass der Interpreter „MicroPython (Raspberry Pi Pico).COMxx“ unten rechts in Thonny ausgewählt ist.
  * Detaillierte Anweisungen findest du unter :ref:`open_run_code_py`.

.. code-block:: python

  import machine
  import utime

  # ADC auf GP28 initialisieren
  potentiometer = machine.ADC(28)

  # PWM auf GP15 initialisieren
  led = machine.PWM(machine.Pin(15))
  led.freq(1000)  # PWM-Frequenz auf 1000Hz setzen

  while True:
      # Analogen Wert auslesen (0-65535)
      value = potentiometer.read_u16()
      print("Potentiometer value:", value)

      # LED-Helligkeit setzen
      led.duty_u16(value)

      # Kleine Verzögerung zur Stabilisierung der Messwerte
      utime.sleep_ms(200)

Beim Ausführen des Programms ändert sich die LED-Helligkeit je nach Position des Potentiometers. Zusätzlich zeigt die Konsole den aktuellen analogen Wert des Potentiometers an.

**Code verstehen**

#. Analoge Messung:

   * ``potentiometer = machine.ADC(28)`` initialisiert den ADC auf GP28.
   * ``value = potentiometer.read_u16()`` liest die analoge Spannung aus und gibt einen 16-Bit-Wert zwischen **0** und **65535** zurück.
     
     * **0** entspricht **0V**.
     * **65535** entspricht **3.3V** (Betriebsspannung des Pico).

#. LED-Helligkeit mit PWM steuern:

   * ``led = machine.PWM(machine.Pin(15))`` setzt PWM auf GP15.
   * ``led.freq(1000)`` setzt die PWM-Frequenz auf 1000Hz.
   * ``led.duty_u16(value)`` setzt das Tastverhältnis der PWM basierend auf dem Potentiometerwert.

     * Ein höherer ``value`` erhöht das Tastverhältnis → LED wird heller.
     * Ein niedrigerer ``value`` verringert das Tastverhältnis → LED wird dunkler.

#. Wert in der Konsole ausgeben:

   * ``print("Potentiometer value:", value)`` gibt den aktuellen Wert zur Überwachung aus.

**Weitere Experimente**

* **PWM-Frequenz ändern**: Probiere verschiedene Frequenzen mit ``led.freq()`` aus und beobachte die LED.

* **ADC-Wert skalieren**: Skaliere den ADC-Wert auf einen anderen Bereich, um die LED anders zu steuern.

* **Andere ADC-Pins nutzen**: Schließe das Potentiometer an GP26 oder GP27 an und passe den Code entsprechend an.

**Fehlersuche**

* LED ändert Helligkeit nicht:

  * Überprüfe die Verdrahtung der LED und des Widerstands.
  * Stelle sicher, dass das Potentiometer korrekt angeschlossen ist.

* Falsche ADC-Werte:

  * Überprüfe die Verbindung zu GP28.
  * Stelle sicher, dass die äußeren Pins des Potentiometers mit 3,3V und GND verbunden sind.

**Fazit**

Durch die Kombination von analogen Eingaben mit PWM-Ausgabe haben wir eine einfache, aber leistungsstarke Möglichkeit geschaffen, die Helligkeit einer LED mit einem Potentiometer zu steuern. Dieses Projekt zeigt, wie analoge Signale erfasst und zur Steuerung anderer Komponenten genutzt werden können – eine grundlegende Fähigkeit in der Mikrocontroller-Programmierung.

**Referenzen**

* |link_wiki_pwm|
* |link_mpython_adc|

