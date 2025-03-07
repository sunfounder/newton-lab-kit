
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in Raspberry Pi, Arduino und ESP32 mit anderen Begeisterten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_motor:

3.5 Steuerung eines kleinen Ventilators (Gleichstrommotor)
=============================================================

In dieser Lektion lernen wir, wie man einen **Gleichstrommotor** (wie einen kleinen Ventilator) mit dem Raspberry Pi Pico 2 und einem **L293D Motor-Treiber** steuert. Der L293D ermöglicht es uns, die Drehrichtung des Motors zu steuern – sowohl im Uhrzeigersinn als auch gegen den Uhrzeigersinn. Da Gleichstrommotoren mehr Strom benötigen, als der Pico direkt liefern kann, verwenden wir eine externe Stromversorgung, um den Motor sicher zu betreiben.

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 8
        - 9V Batterie
        - 1
        - 

**Schaltplan**

|sch_motor|


Der L293D ist ein Motor-Treiber-Chip, EN ist mit 5V verbunden, damit der L293D funktioniert. 1A und 2A sind die Eingänge, die jeweils mit GP15 und GP14 verbunden sind; 1Y und 2Y sind die Ausgänge, die mit den beiden Enden des Motors verbunden sind.

Y (Ausgang) ist in Phase mit A (Eingang), daher kann die Drehrichtung des Motors geändert werden, wenn GP15 und GP14 unterschiedliche Pegel erhalten.


**Verdrahtungsdiagramm**

|wiring_motor|

In diesem Schaltkreis sehen Sie, dass der Knopf mit dem RUN-Pin verbunden ist. Dies liegt daran, dass der Motor mit zu viel Strom betrieben wird, was dazu führen kann, dass der Pico von dem Computer getrennt wird, und der Knopf muss gedrückt werden (damit der RUN-Pin des Pico ein niedriges Niveau erhält), um zurückzusetzen.

Da Gleichstrommotoren einen hohen Strom benötigen, verwenden wir hier aus Sicherheitsgründen ein Netzteilmodul, um den Motor zu betreiben.

**Code schreiben**

Schreiben wir ein MicroPython-Programm zur Steuerung des Motors.

.. note::

    * Öffnen Sie die Datei ``3.5_small_fan.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.

    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Steuerpins definieren
    motor_in1 = machine.Pin(14, machine.Pin.OUT)
    motor_in2 = machine.Pin(15, machine.Pin.OUT)

    def rotate_clockwise():
        motor_in1.high()
        motor_in2.low()

    def rotate_counterclockwise():
        motor_in1.low()
        motor_in2.high()

    def stop_motor():
        motor_in1.low()
        motor_in2.low()

    while True:
        rotate_clockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)
        rotate_counterclockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)

Wenn der Code läuft, dreht sich der Motor eine Sekunde lang im Uhrzeigersinn, hält eine Sekunde an, dreht sich eine Sekunde lang gegen den Uhrzeigersinn und hält dann wieder eine Sekunde an, in einer Schleife.

**Code verstehen**

#. Initialisierung der Pins:

   ``motor_in1`` und ``motor_in2`` sind mit GP14 und GP15 verbunden und steuern die Drehrichtung des Motors.

   .. code-block:: python

      motor_in1 = machine.Pin(14, machine.Pin.OUT)
      motor_in2 = machine.Pin(15, machine.Pin.OUT)

#. Funktionen definieren:

   * ``rotate_clockwise()``: Setzt ``motor_in1`` auf high und ``motor_in2`` auf low, um den Motor im Uhrzeigersinn zu drehen.
   * ``rotate_counterclockwise()``: Setzt ``motor_in1`` auf low und ``motor_in2`` auf high, um gegen den Uhrzeigersinn zu drehen.
   * ``stop_motor()``: Setzt sowohl ``motor_in1`` als auch ``motor_in2`` auf low, um den Motor anzuhalten.

#. Hauptschleife:

   Der Motor dreht sich im Uhrzeigersinn, hält an, dreht sich gegen den Uhrzeigersinn und hält wieder an, jeweils eine Sekunde lang, wiederholt.

   .. code-block:: python

      while True:
          rotate_clockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)
          rotate_counterclockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)

**Fehlerbehebungstipps**

* Motor dreht sich weiter nach Stoppen des Skripts:

  Wenn der Motor weiterläuft, nachdem das Programm gestoppt wurde, müssen Sie möglicherweise den Pico zurücksetzen. Verwenden Sie einen Draht oder einen Knopf, um den RUN-Pin kurzzeitig mit GND zu verbinden, was den Pico zurücksetzt.

  |wiring_run_reset|

* Pico trennt sich oder reagiert nicht mehr:

  Der Motor kann zu viel Strom ziehen, was zu Spannungsschwankungen führt. Stellen Sie sicher, dass Sie eine separate Stromversorgung für den Motor verwenden und dass alle Masseverbindungen angeschlossen sind.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man einen Gleichstrommotor mit dem L293D Motor-Treiber und dem Raspberry Pi Pico 2 steuert. Sie können jetzt die Drehrichtung des Motors steuern und Projekte wie einen kleinen Ventilator oder ein motorisiertes Gerät erstellen.

**Nächste Schritte**

* **Geschwindigkeitskontrolle**: Versuchen Sie, die Geschwindigkeit des Motors mit PWM (Pulsweitenmodulation) zu steuern, indem Sie den EN1-Pin an einen PWM-fähigen GPIO-Pin anschließen.
* **Mehrere Motoren steuern**: Verwenden Sie die anderen Kanäle des L293D, um zusätzliche Motoren zu steuern.
* **Sensorintegration**: Integrieren Sie Sensoren, um den Motor basierend auf Eingaben (z. B. Temperatur, Licht) zu steuern.
