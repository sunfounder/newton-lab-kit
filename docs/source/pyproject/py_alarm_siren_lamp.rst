.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu basteln? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_alarm_lamp:

7.3 Bau einer Alarm-Sirenen-Lampe
=====================================

In diesem Projekt bauen wir eine **Alarm-Sirenen-Lampe** mit dem Raspberry Pi Pico 2. Dieses Gerät simuliert das Blinklicht und das Sirenengeräusch eines Polizeiautos oder eines Einsatzfahrzeugs. Dabei lernen wir, wie man PWM (Pulsweitenmodulation), Interrupts und die Steuerung mehrerer Komponenten wie LEDs und Buzzer einsetzt.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist praktisch, ein vollständiges Kit zu erwerben. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE KOMPONENTEN
        - LINK
    *   - Newton Lab Kit	
        - 450+ Bauteile
        - |link_newton_lab_kit|

Sie können die Teile auch einzeln über die folgenden Links erwerben.


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
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 6
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3 (1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 9
        - :ref:`cpn_capacitor`
        - 1 (104)
        - |link_capacitor_buy|
    *   - 10
        - :ref:`cpn_slide_switch`
        - 1
        - 

**Funktionsweise der Komponenten**

* **Passiver Buzzer**: Erfordert ein externes Signal zur Klangerzeugung. Wir verwenden PWM, um eine Sirene mit variierender Frequenz zu erzeugen.
* **LED**: Simuliert das Blinklicht einer Sirene durch wechselnde Helligkeit.
* **Schiebeschalter**: Dient als Ein-/Ausschalter für die Alarmfunktion.
* **NPN-Transistor (S8050)**: Ermöglicht das Schalten des Buzzers, da die GPIO-Pins des Pico nicht genügend Strom liefern können.
* **Widerstände und Kondensator**: Dienen zur Entprellung des Schalters, um stabile Signale zu gewährleisten.

**Schaltplan**

|sch_alarm_siren_lamp|

* **GP17** ist mit dem mittleren Pin des Schiebeschalters verbunden und wird durch einen 10KΩ-Widerstand sowie einen parallel geschalteten Kondensator (Filter) gegen GND stabilisiert, um ein gleichmäßiges HIGH- oder LOW-Signal zu erzeugen.
* Sobald **GP15** HIGH ist, schaltet der NPN-Transistor durch und der passive Buzzer beginnt zu tönen. Die Frequenz des Buzzers wird dabei schrittweise erhöht, um den typischen Sirenensound zu erzeugen.
* Eine **LED an GP16** wird programmiert, um periodisch ihre Helligkeit zu ändern und so eine Sirene zu simulieren.

**Verdrahtungsdiagramm**

|wiring_alarm_siren_lamp|


**Code schreiben**

Wir schreiben ein MicroPython-Skript, um den Buzzer und die LED basierend auf der Schalterstellung zu steuern.

.. note::

    * Öffnen Sie ``7.3_alarm_siren_lamp.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime

    # PWM für Buzzer und LED initialisieren
    buzzer = machine.PWM(machine.Pin(15))
    led = machine.PWM(machine.Pin(16))
    led.freq(1000)  # PWM-Frequenz der LED auf 1 kHz setzen

    # Schiebeschalter initialisieren
    switch = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_DOWN)

    # Funktion zur Skalierung von Werten auf einen anderen Bereich
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Hauptschleife
    try:
        while True:
            if switch.value() == 1:
                # Alarm EIN
                # Frequenz und Helligkeit erhöhen
                for i in range(0, 100, 2):
                    # Map 'i' to LED brightness and buzzer frequency
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    # Set LED brightness
                    led.duty_u16(brightness)
                    
                    # Set buzzer frequency and duty cycle
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)  # 50 % Tastverhältnis
                    
                    utime.sleep(0.01)
                    
                # Frequenz und Helligkeit verringern
                for i in range(100, 0, -2):
                    brightness = interval_mapping(i, 0, 100, 0, 65535)
                    frequency = interval_mapping(i, 0, 100, 500, 2000)
                    
                    led.duty_u16(brightness)
                    buzzer.freq(frequency)
                    buzzer.duty_u16(32768)
                    
                    utime.sleep(0.01)
            else:
                # Alarm is OFF
                # Turn off LED and buzzer
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)
    except KeyboardInterrupt:
        # Clean up
        buzzer.deinit()
        led.deinit()
        print("Program stopped.")

Sobald der Code ausgeführt wird, schalten Sie den Schiebeschalter in die ON-Position.  
Der Buzzer sollte ein Sirenengeräusch erzeugen, und die LED sollte entsprechend blinken.  
Schalten Sie den Schalter auf OFF, um den Alarm zu stoppen.

**Verständnis des Codes**

#. Initialisierung:

   * **buzzer**: PWM-Objekt an GP15.
   * **led**: PWM-Objekt an GP16, Frequenz auf 1 kHz gesetzt für eine gleichmäßige Helligkeitsregelung.
   * **switch**: Eingangspin an GP17 mit internem Pull-down-Widerstand.

#. Intervall-Mapping-Funktion:

   Ordnet einen Wert von einem Bereich einem anderen zu. Dies ist nützlich, um die Schleifenvariable auf die gewünschte Frequenz und Helligkeit zu skalieren.

   .. code-block:: python

        # Funktion zur Skalierung von Werten auf einen anderen Bereich
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Sicherstellen, dass in_min != in_max ist, um eine Division durch Null zu vermeiden
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Hauptschleife:

   * Überprüft den Status des Schalters.
   * Wenn der Schalter auf ON steht (``switch.value() == 1``):

     * Zwei Schleifen werden durchlaufen, um den Sireneneffekt zu simulieren:
     * Zunehmende Frequenz und Helligkeit.
     * Abnehmende Frequenz und Helligkeit.
     * Die Buzzer-Frequenz variiert zwischen 500 Hz und 2000 Hz.
     * Die LED-Helligkeit variiert von aus bis maximale Helligkeit und zurück.

     .. code-block:: python

        if switch.value() == 1:
            # Alarm EIN
            # Frequenz und Helligkeit erhöhen
            for i in range(0, 100, 2):
                # 'i' auf LED-Helligkeit und Buzzer-Frequenz abbilden
                brightness = interval_mapping(i, 0, 100, 0, 65535)
            ...
                
                utime.sleep(0.01)

   * Wenn der Schalter auf OFF steht: Schaltet die LED und den Buzzer aus.

     .. code-block:: python

            else:
                # Alarm AUS
                # LED und Buzzer ausschalten
                led.duty_u16(0)
                buzzer.duty_u16(0)
                utime.sleep(0.1)

   * Fehlerbehandlung: Fängt eine Tastaturunterbrechung (Strg+C) ab, um die PWM-Objekte sauber zu deaktivieren.

     .. code-block:: python
    
        except KeyboardInterrupt:
            # Aufräumen
            buzzer.deinit()
            led.deinit()
            print("Program stopped.")

**Weitere Experimente**

* Sirenen-Effekt anpassen:
  
  * Ändern Sie den Frequenzbereich in der ``interval_mapping``-Funktion, um die Tonhöhe zu verändern.
  * Passen Sie die Verzögerung in den Schleifen (``utime.sleep(0.01)``) an, um den Sirenenzyklus zu beschleunigen oder zu verlangsamen.

* Mehr LEDs hinzufügen:

  * Integrieren Sie zusätzliche LEDs in verschiedenen Farben, um eine dynamischere Lichtshow zu erzeugen.
  * Nutzen Sie mehrere GPIO-Pins und PWM-Kanäle.

* Bewegungssensor zur Aktivierung verwenden:

  Ersetzen Sie den Schiebeschalter durch einen Bewegungssensor (z. B. PIR-Sensor), um den Alarm auszulösen, wenn eine Bewegung erkannt wird.

* Fernsteuerung integrieren:

  Fügen Sie einen IR-Empfänger hinzu, um den Alarm mit einer Fernbedienung zu steuern.

**Fazit**

Sie haben erfolgreich eine Alarm-Sirenen-Lampe mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt demonstriert, wie man mehrere Komponenten steuert und interaktive Effekte erzeugt. Es bildet eine großartige Grundlage für komplexere Projekte wie Sicherheitssysteme, Notfallalarme oder kreative Lichtinstallationen.
