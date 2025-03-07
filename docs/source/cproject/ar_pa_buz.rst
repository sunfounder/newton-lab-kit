.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Werbegeschenke**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pa_buz:

3.2 Individuelle Töne mit einem passiven Summer spielen
============================================================

In dieser Lektion lernen wir, wie man einen **passiven Summer** mit dem Raspberry Pi Pico 2 verwendet, um verschiedene Töne und sogar einfache Melodien zu spielen! Im Gegensatz zu einem aktiven Summer benötigt ein passiver Summer ein wechselndes elektrisches Signal, um Ton zu erzeugen, was bedeutet, dass wir die Tonhöhe des Sounds steuern können, indem wir die Frequenz des Signals ändern.

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

Sie können sie auch einzeln über die untenstehenden Links kaufen.

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

Ein passiver Summer funktioniert wie ein kleiner Lautsprecher. Er erzeugt keinen Ton von sich aus; stattdessen benötigt er ein oszillierendes Signal, um Ton zu erzeugen. Durch die Bereitstellung von Signalen unterschiedlicher Frequenzen können wir den Summer verschiedene Tonhöhen erzeugen lassen, was es uns ermöglicht, Noten und Melodien zu spielen.

|img_buzzer|

**Schaltplan**

|sch_buzzer|

In diesem Schaltkreis wird der passive Summer über einen Transistor (**S8050** NPN) mit Strom versorgt. Der Transistor verstärkt den Strom, sodass der Summer lauter klingt, als wäre er direkt an den Pico angeschlossen.

Hier ist, was passiert:

* **GP15** gibt ein hohes Signal aus, um den Transistor zu steuern.
* Wenn der Transistor aktiviert ist, lässt er Strom durch den Summer fließen, was ihn zum Piepen bringt.

Ein **1kΩ-Widerstand** wird verwendet, um den Strom zu begrenzen und den Transistor zu schützen.

**Verdrahtungsplan**

Stellen Sie sicher, dass Sie den **passiven Summer** verwenden. Sie können erkennen, dass es der richtige ist, wenn Sie die freiliegende Leiterplatte sehen (im Gegensatz zur versiegelten Rückseite, die ein aktiver Summer wäre).

|img_buzzer|

|wiring_buzzer|

**Schreiben des Codes**


.. note::

   * Sie können die Datei ``3.2_custom_tone.ino`` aus ``newton-lab-kit/arduino/3.2_custom_tone`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port und klicken Sie dann auf "Upload".

.. code-block:: arduino

    const int buzzerPin = 15;  // GPIO pin connected to the transistor base

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      // Play a tone at 440 Hz (A4 note) for 1 second
      tone(buzzerPin, 440, 1000);
      delay(1000);  // Wait for the tone to finish
      // Wait for 1 second before playing again
      delay(1000);
    }

Der Code spielt einen Ton mit 440 Hz (Standard-A-Note) für 1 Sekunde, wartet 1 Sekunde und wiederholt dies.

* ``tone(pin, frequency, duration)``:

  * ``pin``: Der GPIO-Pin, der mit dem Summer verbunden ist (über den Transistor).
  * ``frequency``: Die Frequenz des Tons in Hertz (Hz). Höhere Frequenzen erzeugen höhere Tonhöhen.
  * ``duration (optional)``: Die Dauer, für die der Ton in Millisekunden gespielt wird.


**Eine Melodie spielen**

Erweitern wir den Code, um eine einfache Melodie zu spielen, indem wir die Noten und ihre entsprechenden Frequenzen definieren.

* Ein Array ``melody[]`` hält die Reihenfolge der zu spielenden Noten.
* Ein Array ``noteDurations[]`` definiert die Dauer jeder Note. Eine Dauer von 4 entspricht einer Viertelnote.
* Die ``for``-Schleife iteriert durch jede Note in der Melodie.

  * Berechnet die Notendauer in Millisekunden.
  * Verwendet ``tone()`` zum Spielen jeder Note.
  * Verwendet ``delay()`` zur Pause zwischen den Noten.
  * Ruft ``noTone()`` auf, um den Ton zu stoppen, bevor zur nächsten Note übergegangen wird.

.. code-block:: arduino

        // Define the buzzer pin
        const int buzzerPin = 15;

        // Define note frequencies
        #define NOTE_C4  262
        #define NOTE_D4  294
        #define NOTE_E4  330
        #define NOTE_F4  349
        #define NOTE_G4  392
        #define NOTE_A4  440
        #define NOTE_B4  494
        #define NOTE_C5  523

        // Melody notes
        int melody[] = {
          NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4,
          NOTE_G4, NOTE_A4, NOTE_B4, NOTE_C5
        };

        // Note durations: 4 = quarter note, 8 = eighth note, etc.
        int noteDurations[] = {
          4, 4, 4, 4,
          4, 4, 4, 4
        };

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

        void loop() {
          // Iterate over the notes of the melody
          for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / noteDurations[thisNote];
            tone(buzzerPin, melody[thisNote], noteDuration);
            // Pause between notes
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // Stop the tone playing
            noTone(buzzerPin);
          }
          // Add a delay before repeating the melody
          delay(2000);
        }

Nach dem Hochladen des Codes sollten Sie hören, wie der Summer die Melodie spielt. Wenn der Ton zu leise ist, stellen Sie sicher, dass alle Verbindungen sicher sind. Denken Sie daran, dass passive Summer möglicherweise keine sehr lauten Töne erzeugen.


**Weiterführendes Lernen**

* Erstellen eigener Melodien:

  Sie können eigene Melodien erstellen, indem Sie die Arrays ``melody[]`` und ``noteDurations[]`` ändern.

* Verwendung der ``pitches.h``-Bibliothek:

  Für mehr Bequemlichkeit können Sie eine Bibliotheksdatei ``pitches.h`` einbinden, die Definitionen für viele Noten enthält.
  Erstellen Sie eine Datei namens ``pitches.h`` und binden Sie sie in Ihren Sketch ein.
  
  .. code-block:: arduino

    #include "pitches.h"

**Weitere Erkundungen**

* Komponieren eines Liedes:

  Versuchen Sie, Ihr eigenes Lied zu komponieren, indem Sie eine neue Folge von Noten und Dauern definieren.

* Interaktive Musik:

  Fügen Sie Tasten oder Sensoren hinzu, um die Wiedergabe der Melodie zu steuern.

* Visuelles Feedback:

  Integrieren Sie LEDs, die im Takt der gespielten Noten aufleuchten.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen passiven Summer mit dem Raspberry Pi Pico verwendet, um verschiedene Töne und Melodien zu spielen. Durch die Steuerung der Frequenz des an den Summer gesendeten Signals können Sie verschiedene Tonhöhen erzeugen und Musik in Ihren Projekten kreieren.




