.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_servo:

3.7 Schwingender Servo
=========================

In dieser Lektion lernen wir, wie man einen **Servomotor** mit dem Raspberry Pi Pico 2 steuert.  
Ein Servomotor kann auf einen bestimmten Winkel zwischen 0° und 180° eingestellt werden.  
Er wird häufig in ferngesteuerten Spielzeugen, Robotern und Anwendungen eingesetzt, die eine präzise Positionskontrolle erfordern.

Lass uns beginnen und den Servo hin- und herbewegen!

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Schaltplan**

|sch_servo|

**Verdrahtungsdiagramm**

|wiring_servo|

* Das orangefarbene Kabel ist das Signalkabel und wird mit GP15 verbunden.
* Das rote Kabel ist VCC und wird mit VBUS (5V) verbunden.
* Das braune Kabel ist GND und wird mit GND verbunden.

Servos können unter Last einen hohen Strom ziehen.  
Da wir hier einen kleinen Servo verwenden und ihn nicht stark belasten, reicht die Stromversorgung über den VBUS-Pin des Pico aus.  
Für größere oder mehrere Servos sollte jedoch eine externe Stromquelle genutzt werden.

**Montage des Servoarms**

* Befestige den Servoarm (auch als "Horn" bezeichnet) an der Servo-Ausgangswelle.
* Falls nötig, sichere ihn mit der beiliegenden kleinen Schraube.

**Code schreiben**

Wir schreiben ein MicroPython-Programm, um den Servo kontinuierlich zwischen 0° und 180° zu schwenken.

.. note::

    * Öffne ``3.7_swinging_servo.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 


.. code-block:: python

    import machine
    import utime

    # Initialisierung des PWM-Signals auf GP15
    servo = machine.PWM(machine.Pin(15))
    servo.freq(50)  # Setzt die Frequenz auf 50Hz

    # Funktion zur Umrechnung des Winkels in den Duty Cycle
    def angle_to_duty(angle):
        min_duty = 1638  # Entspricht 0.5ms Puls (0°)
        max_duty = 8192  # Entspricht 2.5ms Puls (180°)
        duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
        return duty

    while True:
        # Servo von 0° auf 180° bewegen
        for angle in range(0, 181, 1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)
        # Servo von 180° zurück auf 0° bewegen
        for angle in range(180, -1, -1):
            servo.duty_u16(angle_to_duty(angle))
            utime.sleep_ms(20)

Wenn der Code läuft, sollte sich der Servo sanft zwischen 0° und 180° hin- und herbewegen.


**Den Code verstehen**

#. Module importieren:

   * ``machine``: Zugriff auf hardwarebezogene Funktionen.
   * ``utime``: Zeitfunktionen für Verzögerungen.

#. PWM initialisieren:

   Der PWM-Signal wird auf GP15 eingerichtet.  
   Die Frequenz wird auf 50 Hz gesetzt, da dies der Standard für Servos ist.

   .. code-block:: python

      servo = machine.PWM(machine.Pin(15))
      servo.freq(50)

#. Die Funktion ``angle_to_duty`` definieren:

   * Diese Funktion wandelt einen Winkel (0° bis 180°) in den entsprechenden PWM-Duty-Cycle um.
   * ``min_duty`` und ``max_duty`` entsprechen den minimalen und maximalen Pulsweiten für das Servosignal.
   * Die Berechnung skaliert den Winkel auf den passenden Duty-Cycle.

   .. code-block:: python

      def angle_to_duty(angle):
          min_duty = 1638  # 0.5ms Pulsweite
          max_duty = 8192  # 2.5ms Pulsweite
          duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
          return duty
    
#. Hauptschleife zur Bewegung des Servos:

   * Der Servo bewegt sich von 0° auf 180° in 1°-Schritten.
   * Anschließend bewegt er sich von 180° auf 0° zurück.
   * ``utime.sleep_ms(20)`` fügt eine kleine Verzögerung hinzu, um eine sanfte Bewegung zu gewährleisten.

   .. code-block:: python

      while True:
          for angle in range(0, 181, 1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)
          for angle in range(180, -1, -1):
              servo.duty_u16(angle_to_duty(angle))
              utime.sleep_ms(20)

**Mehr über den Code**

Servos werden durch PWM-Signale mit einer bestimmten Pulsweite gesteuert.  
Ein 50-Hz-PWM-Signal (Periode: 20 ms) ist der Standard für Servos.  
Die Pulsweite innerhalb jedes Zyklus bestimmt den Winkel:

* 0.5ms Pulsweite entspricht 0°.
* 1.5ms Pulsweite entspricht 90°.
* 2.5ms Pulsweite entspricht 180°.

Durch Anpassen des Duty-Cycles des PWM-Signals steuern wir die Pulsweite.

Der Befehl ``duty_u16()`` akzeptiert Werte von 0 bis 65535.  
Die Berechnung des passenden Duty-Cycles erfolgt mit:

.. code-block:: 

  Duty cycle = (Pulse Width / Period) * 65535

For example, for a 0.5ms pulse width:

.. code-block:: 

  Duty cycle = (0.5ms / 20ms) * 65535 ≈ 1638

**Erweiterungen und Experimente**

* **Geschwindigkeit ändern**: Passe ``utime.sleep_ms(20)`` an, um den Servo schneller oder langsamer zu bewegen.
* **Bestimmte Winkel ansteuern**: Modifiziere den Code, um den Servo auf eine feste Position zu bewegen.

  .. code-block:: python

    servo.duty_u16(angle_to_duty(90))  # Bewege den Servo auf 90°

* **Steuerung mit Eingaben**: Verbinde ein Potentiometer oder Taster, um den Winkel des Servos interaktiv zu steuern.

**Wichtige Hinweise**

* **Stromversorgung**: Stelle sicher, dass der Servo ausreichend mit Strom versorgt wird. Falls du Ruckeln oder unregelmäßige Bewegungen bemerkst, solltest du eine externe 5V-Stromquelle für den Servo in Betracht ziehen.
* **Überlastung vermeiden**: Erzwinge keine Bewegungen über die physikalischen Grenzen des Servos hinaus (normalerweise 0° bis 180°), um Schäden zu vermeiden.

**Fazit**

In dieser Lektion hast du gelernt, wie du einen Servomotor mit dem Raspberry Pi Pico 2 steuerst.  
Du verstehst nun, wie man PWM-Signale erzeugt, um den Servo auf einen bestimmten Winkel einzustellen und ihn flüssig zu bewegen.  
Diese Fähigkeit ist essenziell für Robotik- und Automatisierungsprojekte, bei denen präzise Bewegungen erforderlich sind.
