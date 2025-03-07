.. note::
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und trete heute bei!

.. _py_fade:

2.3 LED dimmen
========================

In dieser Lektion lernen wir, wie wir die Helligkeit einer LED mit Hilfe der Pulsweitenmodulation (PWM) auf dem Raspberry Pi Pico 2 steuern können. Dies ist eine grundlegende Technik in der Elektronik, die es uns ermöglicht, Geräte wie LEDs und Motoren mit unterschiedlichen Intensitäten zu steuern.

**Was ist PWM?**

**Pulsweitenmodulation (PWM)** ist eine Methode zur Steuerung der Leistung, die einem elektronischen Gerät zugeführt wird, indem die Leistung mit hoher Frequenz ein- und ausgeschaltet wird. Die „Breite“ des Impulses (die Dauer, in der er eingeschaltet bleibt) bestimmt, wie viel Leistung das Gerät erhält.

|img_pwm_duty_cycle|

* **Tastverhältnis**: Der Prozentsatz einer Periode, in der ein Signal aktiv ist. Ein 100%iges Tastverhältnis bedeutet, dass das Signal immer an ist, und 0% bedeutet, dass es immer aus ist.
* **Frequenz**: Wie oft das Signal pro Sekunde ein- und ausgeschaltet wird.

Durch Anpassen des Tastverhältnisses können wir einen analogen Ausgang mit digitalen Signalen simulieren. Wenn wir beispielsweise eine LED schnell ein- und ausschalten, nehmen unsere Augen je nach Dauer, wie lange die LED in jedem Zyklus eingeschaltet bleibt, unterschiedliche Helligkeitsstufen wahr.

**Warum PWM verwenden?**

* **LED-Helligkeitssteuerung**: Stelle die Helligkeit von LEDs sanft ein.
* **Motor Geschwindigkeitskontrolle**: Steuere die Geschwindigkeit von Gleichstrommotoren.
* **Effizienz**: PWM ist effizienter als die Verwendung von variablen Widerständen, da sie den Energieverlust in Form von Wärme reduziert.

**Verständnis von PWM auf dem Raspberry Pi Pico 2**

Der Raspberry Pi Pico 2 bietet PWM-Fähigkeiten auf allen seinen GPIO-Pins, verfügt jedoch tatsächlich über 8 PWM-Slices (von PWM0 bis PWM7), die jeweils über zwei Kanäle (A und B) verfügen und somit insgesamt 16 unabhängige PWM-Ausgänge bieten.

|pin_pwm|

.. note::
     Pins, die denselben PWM-Slice teilen (wie GP0 und GP16), können nicht unterschiedliche Frequenzen haben, aber sie können unterschiedliche Tastverhältnisse haben.


**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Du kannst sie auch einzeln über die untenstehenden Links kaufen.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

**Verdrahtungsplan**

|wiring_led|

**Schreiben des Codes**

.. note::

  * Öffne die Datei ``2.3_fading_led.py`` aus dem ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
  * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
  

.. code-block:: python

    import machine
    import utime

    # Einrichten von PWM auf Pin GP15
    led = machine.PWM(machine.Pin(15))
    led.freq(1000)  # Frequenz auf 1000Hz setzen

    # Helligkeit schrittweise erhöhen
    for duty in range(0, 65536, 64):
        led.duty_u16(duty)  # Tastverhältnis einstellen (16-Bit-Wert)
        utime.sleep(0.01)   # 10ms warten

    # LED ausschalten
    led.duty_u16(0)

Wenn der Code läuft, wird die an Pin GP15 angeschlossene LED schrittweise von aus bis zur vollen Helligkeit heller.

**Verständnis des Codes**

* Bibliotheken importieren:

  * ``machine``: Ermöglicht Zugriff auf die Hardwarekomponenten.
  * ``utime``: Ermöglicht es uns, Verzögerungen hinzuzufügen.

* PWM einrichten:

  * ``machine.PWM(machine.Pin(15))``: Initialisiert PWM auf GP15.
  * ``led.freq(1000)``: Setzt die PWM-Frequenz auf 1000Hz (1ms pro Zyklus).

* Tastverhältnis anpassen:

  * ``for duty in range(0, 65536, 64)``: Schleife von 0 bis 65535 in Schritten von 64.
  * ``led.duty_u16(duty)``: Stellt das Tastverhältnis ein. Die Funktion ``duty_u16`` akzeptiert einen 16-Bit-Wert (0 bis 65535), wobei 0 ein Tastverhältnis von 0% und 65535 ein Tastverhältnis von 100% bedeutet.
  * ``utime.sleep(0.01)``: Fügt eine kleine Verzögerung hinzu, damit die Änderung der Helligkeit wahrnehmbar ist.

* LED ausschalten:

  * ``led.duty_u16(0)``: Stellt das Tastverhältnis auf 0% ein, was die LED ausschaltet.


**Weitere Experimente**

* **Ein- und Ausblenden**: Ändere den Code, damit die LED ein- und dann ausblendet.
* **Geschwindigkeit ändern**: Passe den Wert von ``utime.sleep()`` an, um zu ändern, wie schnell sich die Helligkeit ändert.
* **Verschiedene Frequenzen**: Probiere verschiedene PWM-Frequenzen mit ``led.freq()`` aus, um zu sehen, wie sie die LED beeinflussen.

**Fazit**

PWM ist eine leistungsstarke Technik zur Steuerung von Geräten, die analoge Eingaben über digitale Ausgänge benötigen. Das Verständnis von PWM eröffnet Möglichkeiten für komplexere Projekte wie die Steuerung von Motoren, Audiosignalen und mehr.

Durch das Beherrschen der Grundlagen von PWM auf dem Raspberry Pi Pico 2 bist du auf dem besten Weg, anspruchsvollere Elektronikprojekte zu erstellen.

**Referenzen**

* |link_mpython_pwm|