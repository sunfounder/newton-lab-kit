.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich mit Gleichgesinnten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Anleitungen aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Beteilige dich an Gewinnspielen und Feiertagsaktionen.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt uns heute bei!

.. _py_fruit_piano:

7.9 Bau eines Fruchtklaviers
=================================================

In diesem Projekt werden wir ein **Fruchtklavier** mit dem Raspberry Pi Pico 2, einem MPR121-Kapazitätssensor, einem Summer und einer RGB-LED erstellen. Indem wir Früchte (oder andere leitfähige Objekte) mit dem Kapazitätssensor verbinden, verwandeln wir sie in Klaviertasten, die beim Berühren musikalische Noten spielen und farbenfrohe Lichter anzeigen.

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
        - :ref:`cpn_transistor`
        - 1(S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 4(1-1KΩ, 1-330Ω, 2-220Ω)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|
    *   - 8
        - :ref:`cpn_rgb`
        - 1
        - |link_rgb_led_buy|
    *   - 9
        - :ref:`cpn_mpr121`
        - 1
        - 


**Verständnis der Komponenten**

*  **MPR121 Kapazitätssensor**: Ein Controller für Kapazitätssensoren, der bis zu 12 Berührungseingaben verarbeiten kann. Er erkennt Veränderungen in der Kapazität, die durch das Berühren verbundener Elektroden verursacht werden.
*  **Passiver Summer**: Eine elektronische Komponente, die Töne erzeugt, wenn sie mit einem PWM-Signal angesteuert wird. Wir verwenden sie, um verschiedene musikalische Noten zu spielen.
*  **RGB-LED**: Eine LED, die rote, grüne und blaue LEDs in einem Gehäuse kombiniert. Durch die Anpassung der Intensität jeder Farbe können wir eine breite Palette von Farben erzeugen.
*  **Früchte oder leitfähige Objekte**: Gegenstände wie Früchte, Metallgegenstände oder sogar Wasser können als leitfähige Berührungseingaben fungieren, wenn sie mit dem MPR121 verbunden sind.

**Schaltplan**

|sch_fruit_piano| 

Um die Frucht in eine Klaviertaste zu verwandeln, müssen Sie noch die Elektroden am MPR121 mit der Frucht verbinden (z.B. in den Bananengriff).

Zu Beginn wird der MPR121 initialisiert und jede Elektrode erhält einen Wert basierend auf der aktuellen Ladung; wenn ein Leiter (wie ein menschlicher Körper) eine Elektrode berührt, verschiebt sich die Ladung und gleicht sich neu aus.
Als Ergebnis ist der Wert der Elektrode anders als sein Ausgangswert, was dem Hauptsteuerbrett mitteilt, dass sie berührt wurde.
Während dieses Prozesses stellen Sie sicher, dass die Verkabelung jeder Elektrode stabil ist, damit ihre Ladung bei der Initialisierung ausgeglichen ist.


**Verdrahtungsplan**


|wiring_fruit_piano| 

**Code schreiben**

Wir werden ein MicroPython-Skript schreiben, das:

* Den MPR121-Berührungssensor initialisiert.
* Berührungseingaben von den angeschlossenen Früchten erkennt.
* Entsprechende musikalische Noten auf dem Summer spielt.
* Die RGB-LED mit zufälligen Farben beleuchtet.

.. note::

    * Öffne die Datei ``7.9_fruit_piano.py`` aus dem ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Ausführen" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    * Hier musst du die Bibliothek ``mpr121.py`` verwenden, bitte prüfe, ob sie auf den Pico hochgeladen wurde. Für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

.. code-block:: python

    from mpr121 import MPR121
    from machine import Pin, I2C, PWM
    import time
    import urandom

    # I2C-Verbindung für MPR121-Kapazitätssensor initialisieren
    i2c = I2C(1, sda=Pin(6), scl=Pin(7))
    mpr = MPR121(i2c)

    # Notenfrequenzen definieren (in Hertz)
    NOTE_FREQUENCIES = [
        220,  # A3
        247,  # B3
        262,  # C4
        294,  # D4
        330,  # E4
        349,  # F4
        392,  # G4
        440,  # A4
        494,  # B4
        523,  # C5
        587,  # D5
        659   # E5
    ]

    # PWM für Summer auf GP15 initialisieren
    buzzer = PWM(Pin(15))

    # PWM für RGB-LED auf GP13 (Rot), GP12 (Grün), GP11 (Blau) initialisieren
    red = PWM(Pin(13))
    green = PWM(Pin(12))
    blue = PWM(Pin(11))

    # PWM-Frequenz für LEDs festlegen
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Funktion, um einen Ton abzuspielen
    def play_tone(frequency):
        if frequency == 0:
            buzzer.duty_u16(0)
        else:
            buzzer.freq(frequency)
            buzzer.duty_u16(32768)  # 50% Tastverhältnis

    # Funktion, um den Ton zu stoppen
    def stop_tone():
        buzzer.duty_u16(0)

    # Funktion, um eine zufällige Farbe auf der RGB-LED einzustellen
    def set_random_color():
        red.duty_u16(urandom.getrandbits(16))
        green.duty_u16(urandom.getrandbits(16))
        blue.duty_u16(urandom.getrandbits(16))

    # Funktion, um die RGB-LED auszuschalten
    def turn_off_led():
        red.duty_u16(0)
        green.duty_u16(0)
        blue.duty_u16(0)

    # Hauptloop
    try:
        last_touched = mpr.touched()
        while True:
            current_touched = mpr.touched()
            for i in range(12):
                pin_bit = 1 << i
                if current_touched & pin_bit and not last_touched & pin_bit:
                    # Elektrode i wurde gerade berührt
                    print("Pin {} touched".format(i))
                    play_tone(NOTE_FREQUENCIES[i])
                    set_random_color()
                if not current_touched & pin_bit and last_touched & pin_bit:
                    # Elektrode i wurde gerade losgelassen
                    print("Pin {} released".format(i))
                    stop_tone()
                    turn_off_led()
            last_touched = current_touched
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass
    finally:
        stop_tone()
        turn_off_led()

.. note::
    
    Berühre die Früchte oder leitfähigen Objekte nicht, bevor das Programm gestartet wird, um eine ordnungsgemäße Initialisierung zu gewährleisten.

Nachdem das Programm gestartet wurde, berühre die Früchte sanft.

* Der Summer wird die entsprechende musikalische Note spielen.
* Die RGB-LED wird mit einer zufälligen Farbe aufleuchten.
* Experimentiere, indem du verschiedene Früchte berührst, um unterschiedliche Noten zu spielen.

**Verständnis des Codes**

#. Initialisierung:

   * **I2C-Verbindung**: Richtet die Kommunikation mit dem MPR121-Sensor ein.
   * **PWM-Einrichtung**: Initialisiert PWM für den Summer und die RGB-LED-Pins.

#. Notenfrequenzen:

   Eine Liste von Frequenzen, die den musikalischen Noten (A3 bis E5) entsprechen.

#. Funktionen:

   * ``play_tone(frequency)``: Beginnt einen Ton bei der angegebenen Frequenz zu spielen.
   * ``stop_tone()``: Stoppt den Summer.
   * ``set_random_color()``: Stellt die RGB-LED auf eine zufällige Farbe ein.
   * ``turn_off_led()``: Schaltet die RGB-LED aus.

#. Hauptloop:

   * **Berührungserkennung**: Überprüft kontinuierlich die Berührungsereignisse an den Elektroden.
   * **Berührungsverarbeitung**:

     * Wenn eine Elektrode berührt wird, spielt sie die entsprechende Note und beleuchtet die RGB-LED.
     * Wenn eine Elektrode losgelassen wird, stoppt der Ton und die LED wird ausgeschaltet.

   * **Prellen vermeiden**: Eine kurze Verzögerung (``time.sleep(0.01)``), um Prellprobleme zu verhindern.

#. Ausnahmebehandlung:

   * Verwendet einen Try-Block, um einen geordneten Ausstieg bei einem Tastaturinterrupt zu ermöglichen.
   * Stellt sicher, dass der Summer und die LED im Finally-Block ausgeschaltet werden.


**Fehlerbehebung**

* Kein Ton oder Licht:

  * Überprüfe alle Verdrahtungsverbindungen.
  * Stelle sicher, dass der MPR121 korrekt mit dem Pico verbunden ist.
  * Überprüfe, ob die Früchte sicher mit den Elektroden verbunden sind.
  * Stelle sicher, dass ``mpr121.py`` korrekt auf den Pico hochgeladen wurde.

* Berührung wird nicht erkannt:

  * Stelle sicher, dass du nicht gleichzeitig mehrere Elektroden berührst.
  * Vermeide direktes Berühren der Drähte; berühre die Früchte oder leitfähigen Objekte.
  * Stelle sicher, dass die Früchte nicht zu trocken sind; feuchte Früchte leiten besser.

* Unstabiles Verhalten:

  * Stelle sicher, dass der Pico und der Sensor keiner statischen Elektrizität ausgesetzt sind.
  * Halte die Drähte und Verbindungen stabil, um konsistente Kapazitätswerte zu gewährleisten.

**Weiteres Experimentieren**

* Instrument erweitern:

  * Verwende verschiedene leitfähige Materialien (z.B. Wasser, Metallgegenstände) als Tasten.
  * Erhöhe die Anzahl der Noten, indem du mehr Frequenzen den Elektroden zuordnest.

* Visuelle Effekte:

  * Modifiziere die Funktion ``set_random_color()``, um spezifische Farbmuster zu erstellen.
  * Füge weitere LEDs hinzu, um das visuelle Erlebnis zu verbessern.

* Empfindlichkeit anpassen:

  Experimentiere mit den Berührungsschwelleneinstellungen des MPR121, um die Empfindlichkeit anzupassen.

* Kombination mit anderen Sensoren:

  Integriere andere Sensoren (z.B. Lichtsensoren), um die Ton- oder Lichte

ffekte basierend auf den Umgebungsbedingungen zu modifizieren.

**Fazit**

Du hast erfolgreich ein Fruchtklavier mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt zeigt, wie kapazitive Berührungserkennung mit Ton und Licht kombiniert werden kann, um interaktive Erlebnisse zu schaffen. Es ist eine unterhaltsame Art, die Prinzipien der Leitfähigkeit, Berührungserkennung und kreativen Programmierung zu erforschen.

Fühle dich frei, dieses Projekt zu erweitern, indem du neue Funktionen hinzufügst, mit verschiedenen Materialien experimentierst oder zusätzliche Komponenten integrierst.
