.. note::

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_light_theremin:

7.1 Erstellen eines Licht-Theremins
====================================================

In diesem spannenden Projekt werden wir ein **Licht-Theremin** mit einem Raspberry Pi Pico 2, einem Fotowiderstand und einem passiven Summer bauen. Ein Theremin ist ein einzigartiges Musikinstrument, das ohne physischen Kontakt gespielt wird und verschiedene Töne erzeugt, je nach Position der Hände des Spielers. Während wir ein traditionelles Theremin nicht vollständig nachbilden können, simulieren wir seine Funktionalität, indem wir die Lichtintensität verwenden, um die Tonfrequenz zu steuern.

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
        - 1(S8050)
        - |link_transistor_buy|
    *   - 7
        - :ref:`cpn_resistor`
        - 3(1KΩ, 220Ω, 10KΩ)
        - |link_resistor_buy|
    *   - 8
        - Passiver :ref:`cpn_buzzer`
        - 1
        - 
    *   - 9
        - :ref:`cpn_photoresistor`
        - 1
        - |link_photoresistor_buy|


**Verständnis des Konzepts**

* **Fotowiderstand:** Ein Sensor, der seinen Widerstand basierend auf der Lichtintensität ändert. Mehr Licht verringert den Widerstand, weniger Licht erhöht ihn.
* **Passiver Summer:** Benötigt ein externes Signal, um Ton zu erzeugen. Wir können seine Frequenz mit Pulsweitenmodulation (PWM) steuern.
* **Transistor (S8050):** Wird verwendet, um den Strom zu verstärken, sodass der Summer effektiv vom Pico angetrieben werden kann.

Durch das Auslesen der Werte vom Fotowiderstand können wir die Lichtintensität auf die Tonfrequenz abbilden. Das bedeutet, dass das Bewegen Ihrer Hand über den Fotowiderstand die Tonhöhe des vom Summer erzeugten Tons ändert, ähnlich wie beim Spielen eines Theremins.

**Schaltplan**

|sch_light_theremin|

Bevor Sie mit dem Projekt beginnen, bewegen Sie Ihre Hand über den Fotowiderstand, um den Bereich der Lichtintensität zu kalibrieren. Die LED, die an GP16 angeschlossen ist, dient dazu, die Debugging-Zeit anzuzeigen, und die LED leuchtet, um den Beginn des Debuggings anzuzeigen und erlischt, um das Ende des Debuggings anzuzeigen.

Wenn GP15 ein hohes Niveau ausgibt, leitet der S8050 (NPN-Transistor) und der passive Summer beginnt zu tönen.

Wenn das Licht stärker ist, ist der Wert von GP28 kleiner; umgekehrt ist er größer, wenn das Licht schwächer ist.
Durch die Programmierung des Wertes des Fotowiderstands, um die Frequenz des passiven Summers zu beeinflussen, kann ein lichtempfindliches Gerät simuliert werden.


**Verdrahtungsplan**

|wiring_light_theremin|

**Schreiben des Codes**

Lassen Sie uns ein MicroPython-Programm schreiben, das die Lichtintensität vom Fotowiderstand liest, sie auf eine Frequenz abbildet und diese Frequenz auf dem Summer spielt.

.. note::

    * Öffnen Sie die Datei ``7.1_light_theremin.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny und klicken Sie dann auf "Aktuelles Skript ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 


.. code-block:: python

    import machine
    import utime

    # Initialisierung der Komponenten
    led = machine.Pin(16, machine.Pin.OUT)  # LED an GP16
    photoresistor = machine.ADC(28)         # Fotowiderstand verbunden mit ADC0 (GP28)
    buzzer = machine.PWM(machine.Pin(15))   # Summer verbunden mit GP15

    # Variablen für die Kalibrierung
    light_low = 65535
    light_high = 0

    # Funktion, um Werte von einem Bereich in einen anderen zu mappen
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        # Stellen Sie sicher, dass in_min != in_max ist, um Division durch Null zu vermeiden
        if in_max - in_min == 0:
            return out_min
        return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Funktion, um einen Ton auf dem Summer zu spielen
    def play_tone(pin, frequency):
        if frequency <= 0:
            pin.duty_u16(0)
        else:
            pin.freq(frequency)
            pin.duty_u16(32768)  # 50% duty cycle

    # Kalibrierungsprozess
    def calibrate():
        global light_low, light_high
        print("Calibrating... Move your hand over the sensor.")
        led.value(1)  # LED einschalten zur Anzeige der Kalibrierung
        start_time = utime.ticks_ms()
        while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 Sekunden Kalibrierung
            light_value = photoresistor.read_u16()
            if light_value > light_high:
                light_high = light_value
            if light_value < light_low:
                light_low = light_value
            utime.sleep_ms(10)
        led.value(0)  # LED ausschalten nach der Kalibrierung
        print("Calibration complete.")
        print("Light Low:", light_low)
        print("Light High:", light_high)
    # Hauptfunktion
    def main():
        calibrate()
        try:
            while True:
                light_value = photoresistor.read_u16()
                # Den Lichtwert auf einen Frequenzbereich abbilden (z. B. 200 Hz bis 2000 Hz)
                frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                play_tone(buzzer, frequency)
                utime.sleep_ms(20)
        except KeyboardInterrupt:
            buzzer.deinit()
            print("Program stopped.")

    # Hauptfunktion ausführen
    if __name__ == "__main__":
        main()

Wenn der Code läuft, leuchtet die LED auf, was die Kalibrierungsphase anzeigt.

* Kalibrierung:

  * Bewegen Sie während der 5-sekündigen Kalibrierung Ihre Hand über den Fotowiderstand.
  * Dies hilft dem Programm, den Bereich der Lichtverhältnisse zu verstehen.

* Theremin spielen:

  * Nach der Kalibrierung erlischt die LED.
  * Bewegen Sie Ihre Hand über den Fotowiderstand.
  * Der Summer gibt Töne aus, deren Tonhöhe sich je nach Lichtintensität ändert.
  * Experimentieren Sie mit verschiedenen Handpositionen und Bewegungen, um Töne zu erzeugen.


**Verständnis des Codes**

#. Initialisierung:

   * **LED-Anzeige**: Wird verwendet, um anzuzeigen, wann die Kalibrierung stattfindet.
   * **Fotowiderstand**: Liest analoge Werte, die der Lichtintensität entsprechen.
   * **Summer**: Wird mit PWM gesteuert, um Töne in verschiedenen Frequenzen zu erzeugen.

#. Kalibrierungsfunktion (``calibrate()``):

   * Läuft 5 Sekunden lang, währenddessen die minimalen und maximalen Lichtwerte aufgezeichnet werden.
   * Instruiert den Benutzer, die Hand über den Sensor zu bewegen, um den Bereich zu erfassen.
   * Verwendet die LED als visuellen Indikator.

   .. code-block:: python

        # Kalibrierungsprozess
        def calibrate():
            global light_low, light_high
            print("Calibrating... Move your hand over the sensor.")
            led.value(1)  # LED einschalten zur Anzeige der Kalibrierung
            start_time = utime.ticks_ms()
            while utime.ticks_diff(utime.ticks_ms(), start_time) < 5000:  # 5 Sekunden Kalibrierung
                light_value = photoresistor.read_u16()
                if light_value > light_high:
                    light_high = light_value
                if light_value < light_low:
                    light_low = light_value
                utime.sleep_ms(10)
            led.value(0)  # LED ausschalten nach der Kalibrierung
            print("Calibration complete.")
            print("Light Low:", light_low)
            print("Light High:", light_high)


#. Intervall-Mapping-Funktion (``interval_mapping()``):

   * Mappt die Werte des Lichtsensors auf einen Frequenzbereich, der für den Summer geeignet ist.
   * Verhindert Fehler durch Division durch Null.

   .. code-block:: python

        # Funktion, um Werte von einem Bereich in einen anderen zu mappen
        def interval_mapping(x, in_min, in_max, out_min, out_max):
            # Stellen Sie sicher, dass in_min != in_max ist, um Division durch Null zu vermeiden
            if in_max - in_min == 0:
                return out_min
            return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

#. Töne spielen (``play_tone()``):

   * Stellt die Frequenz des Summers mithilfe von PWM ein.
   * Wenn die Frequenz null oder negativ ist, wird der Summer ausgeschaltet.

   .. code-block:: python

        # Funktion, um einen Ton auf dem Summer zu spielen
        def play_tone(pin, frequency):
            if frequency <= 0:
                pin.duty_u16(0)
            else:
                pin.freq(frequency)
                pin.duty_u16(32768)  # 50% duty cycle

#. Hauptschleife:

   * Liest kontinuierlich den Lichtwert vom Fotowiderstand.
   * Mappt diesen Wert auf eine Frequenz.
   * Spielt den Ton, der der Frequenz entspricht.
   * Beinhaltet Fehlerbehandlung, um beim Beenden aufzuräumen.

   .. code-block:: python

        # Hauptfunktion
        def main():
            calibrate()
            try:
                while True:
                    light_value = photoresistor.read_u16()
                    # Den Lichtwert auf einen Frequenzbereich abbilden (z. B. 200 Hz bis 2000 Hz)
                    frequency = interval_mapping(light_value, light_low, light_high, 200, 2000)
                    play_tone(buzzer, frequency)
                    utime.sleep_ms(20)
            except KeyboardInterrupt:
                buzzer.deinit()
                print("Program stopped.")

**Weitere Experimente**

* Frequenzbereich anpassen:

  Ändern Sie die Werte in ``interval_mapping()`` um den Tonbereich zu verändern. Beispiel: Ändern Sie 200, 2000 zu 100, 5000 für einen breiteren Bereich.

* Visuelles Feedback:

  Verwenden Sie zusätzliche LEDs, um visuelle Hinweise entsprechend der Tonhöhe zu geben.

* Zweiten Sensor hinzufügen:

  Führen Sie einen weiteren Fotowiderstand ein, um die Lautstärke oder einen anderen Parameter zu steuern.

* Ein Musikinstrument erstellen:

  Kombinieren Sie es mit anderen Sensoren oder Eingängen, um ein komplexeres Instrument zu bauen.

**Verständnis der Einschränkungen**

* Umgebungslicht:

  Änderungen im Umgebungslicht können die Leistung beeinflussen. Stellen Sie eine konsistente Beleuchtung sicher oder kalibrieren Sie bei Bedarf neu.

* Sensorempfindlichkeit:

  Der Fotowiderstand reagiert möglicherweise nicht schnell auf schnelle Handbewegungen.

* Klangqualität:

  Passive Summer haben eine begrenzte Klangqualität. Für besseren Audioausgang erwägen Sie die Verwendung eines aktiven Lautsprechers mit einem DAC-Ausgang.

**Fazit**

Sie haben erfolgreich ein Licht-Theremin mit dem Raspberry Pi Pico 2 erstellt! Dieses Projekt zeigt, wie Sensoren und Aktoren kombiniert werden können, um interaktive und spaßige Experimente zu erstellen. Weiter erforschen und modifizieren Sie das Projekt, um Ihr Verständnis und Ihre Kreativität zu erweitern.
