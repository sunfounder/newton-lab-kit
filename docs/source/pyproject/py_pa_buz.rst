
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_pa_buz:

3.2 Benutzerdefinierte Töne mit einem passiven Summer spielen
=================================================================

In dieser Lektion lernen wir, wie man einen **passiven Summer** mit dem Raspberry Pi Pico 2 verwendet, um verschiedene Töne und sogar einfache Melodien zu spielen! Im Gegensatz zu einem aktiven Summer benötigt ein passiver Summer ein wechselndes elektrisches Signal, um Ton zu erzeugen, was bedeutet, dass wir die Tonhöhe des Sounds durch Ändern der Frequenz des Signals steuern können.

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
        - Micro USB-Kabel
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
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Passiver :ref:`cpn_buzzer`
        - 1
        - |link_passive_buzzer_buy|

**Verständnis des passiven Summers**

Ein passiver Summer funktioniert wie ein kleiner Lautsprecher. Er erzeugt keinen Ton von sich aus; stattdessen benötigt er ein oszillierendes Signal, um Ton zu machen. Indem wir Signale unterschiedlicher Frequenzen bereitstellen, können wir den Summer verschiedene Töne erzeugen lassen, wodurch wir Noten und Melodien spielen können.

|img_buzzer|

**Schaltplan**

|sch_buzzer|

In diesem Schaltkreis wird der passive Summer über einen Transistor (**S8050** NPN) mit Strom versorgt. Der Transistor verstärkt den Strom, wodurch der Summer lauter klingt, als wäre er direkt an den Pico angeschlossen.

Hier ist, was passiert:

* **GP15** gibt ein hohes Signal aus, um den Transistor zu steuern.
* Wenn der Transistor aktiviert ist, lässt er den Strom durch den Summer fließen, was ihn piepen lässt.

Ein **1kΩ Widerstand** wird verwendet, um den Strom zu begrenzen und den Transistor zu schützen.

**Verdrahtungsdiagramm**

Stellen Sie sicher, dass Sie den **passiven Summer** verwenden. Sie können erkennen, dass es der richtige ist, indem Sie nach der freiliegenden PCB suchen (im Gegensatz zur versiegelten Rückseite, die ein aktiver Summer ist).

|img_buzzer|

|wiring_buzzer|

**Code schreiben**

Jetzt schreiben wir etwas Code, damit der Summer verschiedene Töne spielt.

.. note::

    * Öffnen Sie die Datei ``3.2_custom_tone.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.
    

.. code-block:: python

   import machine
   import utime

   # PWM auf GP15 initialisieren
   buzzer = machine.PWM(machine.Pin(15))

   def play_tone(frequency, duration):
       # Die Frequenz des PWM-Signals einstellen
       buzzer.freq(frequency)
       # Tastverhältnis auf 50% setzen
       buzzer.duty_u16(32768)
       # Den Ton für die angegebene Dauer spielen
       utime.sleep_ms(duration)
       # Den Summer ausschalten
       buzzer.duty_u16(0)

   # Einige Töne spielen
   play_tone(440, 500)  # A4-Note für 500ms
   utime.sleep_ms(200)
   play_tone(494, 500)  # B4-Note für 500ms
   utime.sleep_ms(200)
   play_tone(523, 500)  # C5-Note für 500ms

Wenn der Code ausgeführt wird, hören Sie, wie der passive Summer die A4-Note für 500ms, die B4-Note für 500ms und die C5-Note für 500ms spielt.


**Erklärung des Codes**

#. PWM initialisieren:

   * ``buzzer = machine.PWM(machine.Pin(15))``: Damit wird PWM (Pulsweitenmodulation) auf Pin GP15 eingerichtet, den wir verwenden, um den Summer zu steuern.

#. Die Funktion ``play_tone`` definieren: 

   .. code-block:: python

      def play_tone(frequency, duration):
          buzzer.freq(frequency)
          buzzer.duty_u16(32768)
          utime.sleep_ms(duration)
          buzzer.duty_u16(0)

   * ``frequency``: Die Tonhöhe des Tons. Höhere Frequenz bedeutet eine höhere Tonhöhe.
   * ``duration``: Wie lange der Ton spielt, in Millisekunden.
   * ``buzzer.duty_u16(32768)``: Setzt das Tastverhältnis auf 50% (die Hälfte von 65535), was ideal ist, um Ton zu erzeugen.
   * Nach der Dauer wird der Summer ausgeschaltet, indem das Tastverhältnis auf 0 gesetzt wird.

#. Noten spielen:

   Wir rufen ``play_tone`` mit verschiedenen Frequenzen auf, die musikalischen Noten entsprechen.

   .. code-block:: python

      # Einige Töne spielen
      play_tone(440, 500)  # A4-Note für 500ms
      utime.sleep_ms(200)
      play_tone(494, 500)  # B4-Note für 500ms
      utime.sleep_ms(200)
      play_tone(523, 500)  # C5-Note für 500ms

   
**Eine Melodie spielen**

Jetzt, da wir gelernt haben, wie man einzelne Töne mit dem passiven Summer spielt, lassen Sie uns eine einfache Melodie erstellen! Das hilft uns zu verstehen, wie man Noten anordnet und ihre Dauer kontrolliert, um Musik zu erzeugen.

.. code-block:: python

    import machine
    import utime

    # Notenfrequenzen (in Hz)
    NOTE_C4 = 262
    NOTE_D4 = 294
    NOTE_E4 = 330
    NOTE_F4 = 349
    NOTE_G4 = 392
    NOTE_A4 = 440
    NOTE_B4 = 494
    NOTE_C5 = 523

    melody = [
        NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
        NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
    ]

    note_durations = [
        500, 500, 500, 500,
        500, 500, 500, 500
    ]

    # PWM auf GP15 initialisieren
    buzzer = machine.PWM(machine.Pin(15))

    def play_tone(frequency, duration):
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
        utime.sleep_ms(duration)
        buzzer.duty_u16(0)
        utime.sleep_ms(50)  # Kurze Pause zwischen den Noten

    for i in range(len(melody)):
        play_tone(melody[i], note_durations[i])

Wenn Sie diesen Code ausführen, spielt der Summer eine einfache Melodie, indem er jede Note in der Reihenfolge erklingen lässt. Jede Note dauert 500 Millisekunden, und es gibt eine kurze Pause zwischen den Noten. Sie hören den Summer eine aufsteigende Tonleiter von Mittel-C (C4) bis zum C der nächsten Oktave (C5).

**Weiter experimentieren**

* **Erstellen Sie Ihre eigene Melodie**: Ändern Sie die Noten und Dauern in der Melodie und den ``note_durations``-Listen, um Ihre eigene Melodie zu komponieren.
* **Das Tempo anpassen**: Ändern Sie die Werte in ``note_durations``, um die Melodie schneller oder langsamer zu machen.
* **Weitere Noten hinzufügen**: Definieren Sie zusätzliche Noten durch Hinzufügen ihrer Frequenzen und schließen Sie sie in Ihre Melodie ein.
* **Die Lautstärke ändern**: Passen Sie das Tastverhältnis in ``buzzer.duty_u16()`` an, um den Summer lauter oder leiser zu machen. Ein Wert um 32768 gibt ein Tastverhältnis von 50%.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man einen passiven Summer verwendet, um Töne und Melodien mit dem Raspberry Pi Pico 2 zu spielen. Indem Sie die Frequenz des PWM-Signals kontrollieren, können Sie eine Vielzahl von Klängen erzeugen und sogar einfache Lieder spielen. Dies ist eine großartige Möglichkeit, Ihren Projekten akustisches Feedback oder unterhaltsame musikalische Elemente hinzuzufügen.```
