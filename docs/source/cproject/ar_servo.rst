.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_servo:

3.7 Schwingender Servo
==========================

In dieser Lektion lernen wir, wie man einen **Servomotor** mit dem Raspberry Pi Pico 2 steuert. Ein Servomotor ist ein Gerät, das sich auf einen spezifischen Winkel zwischen 0° und 180° drehen kann. Er wird häufig in ferngesteuerten Spielzeugen, Robotern und anderen Anwendungen eingesetzt, die eine präzise Positionssteuerung erfordern.

Lassen Sie uns beginnen und den Servo hin und her schwingen!

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

Sie können sie auch einzeln über die unten stehenden Links kaufen.

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
        - :ref:`cpn_servo`
        - 1
        - |link_servo_buy|


**Schaltplan**

|sch_servo|

**Verdrahtungsdiagramm**

|wiring_servo|

* Das orangefarbene Kabel ist das Signalkabel und ist mit GP15 verbunden.
* Das rote Kabel ist VCC und ist mit VBUS(5V) verbunden.
* Das braune Kabel ist GND und ist mit GND verbunden.

Servos können, besonders unter Last, erheblichen Strom ziehen. Da wir einen kleinen Servo verwenden und ihn nicht stark belasten, ist es für dieses einfache Experiment akzeptabel, ihn über den VBUS-Pin des Pico mit Strom zu versorgen. Für größere Servos oder mehrere Servos verwenden Sie eine externe Stromversorgung.

**Einrichten des Servoarms**

* Befestigen Sie den Servoarm (auch Horn genannt) an der Ausgangswelle des Servos.
* Sichern Sie ihn bei Bedarf mit der kleinen Schraube, die mit dem Servo geliefert wird.

**Schreiben des Codes**

.. note::

   * Sie können die Datei ``3.7_swinging_servo.ino`` aus ``newton-lab-kit/arduino/3.7_swinging_servo`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".
    
.. code-block:: arduino

    #include <Servo.h>

    Servo myServo;  // Create a servo object

    void setup() {
      myServo.attach(15);  // Attach the servo to GPIO pin 15
    }

    void loop() {
      // Move the servo from 0 to 180 degrees
      for (int angle = 0; angle <= 180; angle += 1) {
        myServo.write(angle);
        delay(15);  // Wait 15 milliseconds for the servo to reach the position
      }
      // Move the servo from 180 to 0 degrees
      for (int angle = 180; angle >= 0; angle -= 1) {
        myServo.write(angle);
        delay(15);
      }
    }

Nach dem Hochladen des Codes sollte der Servoarm reibungslos von 0° bis 180° und zurück schwingen.
Wenn sich der Servo nicht bewegt oder unregelmäßig verhält:

* Überprüfen Sie Ihre Verdrahtungsverbindungen.
* Stellen Sie sicher, dass der Servo richtig mit Strom versorgt wird.
* Achten Sie darauf, dass der Servo mechanisch nicht blockiert ist.

**Verständnis des Codes**

#. Einbinden der ``Servo``-Bibliothek:

   Bindet die ``Servo``-Bibliothek ein, die Funktionen zur Steuerung des Servomotors bietet.

   .. code-block:: arduino

        #include <Servo.h>

#. Erstellen eines ``Servo``-Objekts:

   Erstellt ein ``Servo``-Objekt namens ``myServo`` zur Steuerung des Servos.

   .. code-block:: arduino

        Servo myServo;

#. Anschließen des Servos an einen Pin:

   Schließt den Servo an den GPIO-Pin 15 am Pico an.

   .. code-block:: arduino

        myServo.attach(15);

#. Bewegen des Servos:

   * Bewegt den Servo von 0° bis 180° in 1-Grad-Schritten. Die Verzögerung (15) bietet eine kleine Verzögerung, um dem Servo zu ermöglichen, jede Position reibungslos zu erreichen.
   
   .. code-block:: arduino

        for (int angle = 0; angle <= 180; angle += 1) {
          myServo.write(angle);
          delay(15);
        }

   * Umkehrung der Bewegung: Bewegt den Servo zurück von 180° bis 0° und erzeugt so eine hin- und her schwingende Bewegung.

   .. code-block:: arduino

        for (int angle = 180; angle >= 0; angle -= 1) {
          myServo.write(angle);
          delay(15);
        }

**Weitere Erkundungen**

* Geschwindigkeit anpassen:

  Ändern Sie den Wert von ``delay()`` in den Schleifen, um den Servo schneller oder langsamer zu bewegen.

* Direkte Positionskontrolle:

  Verwenden Sie ``myServo.write(angle);`` mit einem bestimmten Winkel, um den Servo in einer festen Position einzustellen.

* Interaktive Steuerung:

  Verbinden Sie ein Potentiometer, um den Servowinkel interaktiv zu steuern.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen Servomotor mit dem Raspberry Pi Pico und der Servo-Bibliothek steuert. Durch Anpassen des Codes können Sie den Servo auf einen beliebigen Winkel zwischen 0° und 180° einstellen, was eine präzise Steuerung in Ihren Projekten ermöglicht.

