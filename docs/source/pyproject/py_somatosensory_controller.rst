.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_somato_controller:

7.11 Bau eines Somatosensorischen Controllers
=================================================

In diesem spannenden Projekt erstellen wir einen **Somatosensorischen Controller** mit dem Raspberry Pi Pico 2, einem MPU6050-Beschleunigungsmesser und Gyroskopmodul sowie einem Servomotor.  
Dieses Gerät erfasst menschliche Bewegungen – insbesondere die Neigung deiner Hand – und übersetzt sie in die Bewegung des Servomotors.  
Diese Technologie wird häufig in der Robotik und in Fernsteuerungssystemen wie chirurgischen Robotern oder Roboterarmen eingesetzt.

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
        - :ref:`cpn_mpu6050`
        - 1
        - 
    *   - 6
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|

**Funktionsweise der Komponenten**

* **MPU6050 Beschleunigungsmesser und Gyroskop**: Ein 6-Achsen-Bewegungssensor, der Beschleunigung und Winkelgeschwindigkeit entlang der X-, Y- und Z-Achsen misst. Wir verwenden ihn, um die Neigung deiner Hand zu erkennen.
* **Servomotor**: Ein Motor, der auf einen bestimmten Winkel eingestellt werden kann. Er wird die von der MPU6050 erfassten Bewegungen nachahmen.

**Schaltplan**

|sch_somato|

Der MPU6050 berechnet den Lagewinkel basierend auf den Beschleunigungswerten in jeder Richtung.

Das Programm steuert den Servo entsprechend dem veränderten Lagewinkel.

**Verdrahtungsdiagramm**

|wiring_somatosensory_controller| 

**Code schreiben**

Das folgende MicroPython-Skript:

* Liest die Beschleunigungsdaten des MPU6050 aus.
* Berechnet den Neigungswinkel deiner Hand.
* Steuert den Servomotor entsprechend der erkannten Neigung.

.. note::

    * Öffne ``7.11_somatosensory_controller.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Die Dateien ``imu.py`` und ``vector3d.py`` müssen hochgeladen sein. Eine Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import I2C, Pin, PWM
    import utime
    import math

    # Initialisierung der I2C-Kommunikation für MPU6050
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # Initialisierung des PWM-Signals für den Servomotor an GP15
    servo = PWM(Pin(15))
    servo.freq(50)  # Setzt die Frequenz auf 50 Hz für den Servo

    # Funktion zur Umrechnung des Winkels in den PWM-Duty-Cycle
    def angle_to_duty(angle):
        # Convert angle (0-180) to duty cycle (0.5ms - 2.5ms pulse width)
        # Duty cycle range is from 2% to 12% for 0.5ms to 2.5ms at 50Hz
        duty_cycle = (angle / 18) + 2
        duty_u16 = int(duty_cycle / 100 * 65535)
        return duty_u16

    # Funktion zur Berechnung des Neigungswinkels anhand der Beschleunigungsdaten
    def get_tilt_angle():
        accel = mpu.accel
        x = accel.x
        y = accel.y
        z = accel.z
        angle = math.atan2(y, z) * (180 / math.pi)
        return angle + 90  # Justiert den Winkel auf den Bereich 0 bis 180 Grad

    # Hauptschleife
    try:
        while True:
            angle = get_tilt_angle()
            if angle < 0:
                angle = 0
            elif angle > 180:
                angle = 180
            duty = angle_to_duty(angle)
            servo.duty_u16(duty)
            utime.sleep(0.1)
    except KeyboardInterrupt:
        servo.deinit()
        print("Program stopped.")

Nach dem Start des Programms kannst du deine Hand kippen.  
Der Servomotor sollte diese Bewegung entsprechend nachahmen.  
Beobachte, wie der Servo auf deine Handbewegungen reagiert.

**Den Code verstehen**

#. Initialisierung:

   * **I2C-Kommunikation**: Wird eingerichtet, um Daten vom MPU6050 zu lesen.
   * **PWM für den Servomotor**: Initialisiert an GP15 mit einer Frequenz von 50 Hz.

#. Winkelberechnung:

   * ``get_tilt_angle()``: Berechnet den Neigungswinkel basierend auf den Beschleunigungswerten.

   .. code-block:: python

        def get_tilt_angle():
            accel = mpu.accel
            x = accel.x
            y = accel.y
            z = accel.z
            angle = math.atan2(y, z) * (180 / math.pi)
            return angle + 90  # Justierung auf den Bereich 0 bis 180 Grad

#. Servo-Steuerung:

   * ``angle_to_duty(angle)``: Wandelt den Winkel in das entsprechende PWM-Signal um.
   * PWM-Berechnung: Der Servo erwartet Impulse zwischen 0,5 ms (0 Grad) und 2,5 ms (180 Grad) bei 50 Hz.

   .. code-block:: python

        def angle_to_duty(angle):
            # Convert angle (0-180) to duty cycle (0.5ms - 2.5ms pulse width)
            # Duty cycle range is from 2% to 12% for 0.5ms to 2.5ms at 50Hz
            duty_cycle = (angle / 18) + 2
            duty_u16 = int(duty_cycle / 100 * 65535)
            return duty_u16

#. Hauptschleife: 

   * Liest den Neigungswinkel aus.
   * Passt den Winkel an, um sicherzustellen, dass er im Bereich von 0 bis 180 Grad bleibt.
   * Setzt die Servoposition entsprechend dem berechneten Winkel.
   * Enthält eine kurze Verzögerung, um Vibrationen zu vermeiden.
   * Fängt eine Tastaturunterbrechung ab, um den Servo sicher zu deaktivieren.

   .. code-block:: python

        try:
            while True:
                angle = get_tilt_angle()
                if angle < 0:
                    angle = 0
                elif angle > 180:
                    angle = 180
                duty = angle_to_duty(angle)
                servo.duty_u16(duty)
                utime.sleep(0.1)
        except KeyboardInterrupt:
            servo.deinit()
            print("Program stopped.")

**Fehlersuche**

* Servo bewegt sich nicht:

  * Überprüfe, ob der Servo korrekt mit Strom versorgt wird.
  * Stelle sicher, dass das Signalkabel mit GP15 verbunden ist.
  * Prüfe, ob die Masse zwischen dem Pico und dem Servo richtig verbunden ist.

* Ungenaue Bewegungen:

  * Achte darauf, dass der MPU6050 sicher befestigt ist und nicht übermäßig wackelt.
  * Falls nötig, passe die Berechnungen für den Neigungswinkel an.

* Programmfehler:

  * Stelle sicher, dass imu.py und vector3d.py korrekt hochgeladen wurden.
  * Überprüfe den Code auf Tippfehler oder fehlerhafte Einrückungen.

**Erweiterungen und Verbesserungen**

* Steuerung mehrerer Servos:

  * Ergänze weitere Servos, um zusätzliche Achsen zu steuern.
  * Erweitere den Code, um Drehungen um mehrere Achsen zu verarbeiten.

* Kabellose Kommunikation:

  Verwende Bluetooth- oder Wi-Fi-Module, um Sensordaten an ein anderes Gerät zur Steuerung der Servos zu senden.

* Daten-Glättung:

  Implementiere Filter (z. B. Kalman-Filter), um die Sensordaten zu stabilisieren.

* Visuelles Feedback:

  Integriere ein OLED- oder LCD-Display, um die Echtzeit-Winkelwerte anzuzeigen.

**Fazit**

Du hast erfolgreich einen Somatosensorischen Controller entwickelt, der menschliche Bewegungen erfasst und in mechanische Bewegungen umsetzt.  
Dieses Projekt zeigt, wie Sensoren und Aktoren zusammenarbeiten, um interaktive Systeme zu erstellen – ähnlich denen, die in der Robotik und Fernsteuerung verwendet werden.

Erweitere dieses Projekt gerne durch zusätzliche Funktionen oder integriere es in größere Systeme!
