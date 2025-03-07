.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefe dich mit Gleichgesinnten in Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung deiner Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genieße exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Gewinnspiele**: Nimm an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicke auf [|link_sf_facebook|] und tritt heute bei!

.. _py_guess_number:

7.7 Erstellen eines "Rate die Zahl"-Spiels
=============================================================

In diesem Projekt werden wir ein interaktives Spiel namens **"Rate die Zahl"** mit dem Raspberry Pi Pico 2, einer 4x4 Matrix-Tastatur und einem I2C LCD1602 Display entwickeln. Das Spiel generiert eine zufällige Zahl zwischen 0 und 99, und die Spieler wechseln sich beim Raten ab. Nach jedem Versuch verengt das Spiel den Bereich, abhängig davon, ob die Vermutung zu hoch oder zu niedrig war, bis jemand die richtige Zahl errät.

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
        - :ref:`cpn_resistor`
        - 4(10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Verständnis der Komponenten**

* **4x4 Matrix-Tastatur**: Eine Tastatur mit 16 Tasten, angeordnet in einer Matrix aus 4 Reihen und 4 Spalten. Wir verwenden sie zur Eingabe von Zahlen und Befehlen.
* **I2C LCD1602 Display**: Ein 16x2 Zeichen LCD-Display mit einem I2C-Interface, das die Verkabelung vereinfacht, indem nur zwei Datenleitungen (SDA und SCL) verwendet werden.

**Schaltplan**

|sch_guess_number|

Dieser Schaltkreis basiert auf :ref:`py_keypad` mit der Ergänzung eines I2C LCD1602 zur Anzeige der gedrückten Tasten.

**Verdrahtungsplan**

|wiring_game_guess_number| 

Um die Verdrahtung zu erleichtern, sind im obigen Diagramm die Spaltenreihen der Matrix-Tastatur und die 10K-Widerstände gleichzeitig in die Löcher eingeführt, wo G10 ~ G13 liegen.


**Code schreiben**

Wir werden ein MicroPython-Programm schreiben, das:

* Eine zufällige Zahl zwischen 0 und 99 generiert.
* Eingaben von der Tastatur liest.
* Das LCD-Display mit Hinweisen und Spieler-Eingaben aktualisiert.
* Den Bereich nach jedem Versuch einschränkt.

.. note::

    * Öffne die Datei ``7.7_game_guess_number.py`` aus dem ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier benötigst du die Bibliothek namens ``lcd1602.py``, bitte prüfe, ob sie auf den Pico hochgeladen wurde, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin
    import utime
    import urandom

    # Initialisiere die I2C-Kommunikation für das LCD1602-Display
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    lcd = LCD(i2c)

    # Tastatur-Zuordnung für eine 4x4 Matrix-Tastatur
    keypad_map = [
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]
    ]

    # Definiere Zeilen- und Spalten-Pins
    row_pins = [Pin(pin_num, Pin.OUT) for pin_num in [21, 20, 19, 18]]  # R1-R4
    col_pins = [Pin(pin_num, Pin.IN, Pin.PULL_DOWN) for pin_num in [13, 12, 11, 10]]  # C1-C4

    # Funktion zum Abtasten der Tastatur
    def read_keypad():
        for row_num, row_pin in enumerate(row_pins):
            row_pin.high()
            for col_num, col_pin in enumerate(col_pins):
                if col_pin.value() == 1:
                    row_pin.low()
                    return keypad_map[row_num][col_num]
            row_pin.low()
        return None

    # Initialisiere Spielvariablen
    def init_game():
        global target_number, lower_bound, upper_bound, guess
        target_number = urandom.randint(0, 99)
        lower_bound = 0
        upper_bound = 99
        guess = ""
        lcd.clear()
        lcd.message("Press A to Start")

    # Anzeigefunktion
    def update_display(message):
        lcd.clear()
        lcd.message(message)

    # Hauptprogramm
    init_game()
    game_started = False

    while True:
        key = read_keypad()
        if key:
            utime.sleep(0.2)  # Entprellverzögerung

            if not game_started:
                if key == "A":
                    game_started = True
                    update_display("Enter your guess:")
            else:
                if key in "0123456789":
                    if len(guess) < 2:
                        guess += key
                        update_display("Guess: {}\n{} < ? < {}".format(guess, lower_bound, upper_bound))
                elif key == "D":
                    if guess != "":
                        guess_number = int(guess)
                        if guess_number < lower_bound or guess_number > upper_bound:
                            update_display("Out of range!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number > target_number:
                            upper_bound = guess_number - 1
                            guess = ""
                            update_display("Too High!\n{} < ? < {}".format(lower_bound, upper_bound))
                        elif guess_number < target_number:
                            lower_bound = guess_number + 1
                            guess = ""
                            update_display("Too Low!\n{} < ? < {}".format(lower_bound, upper_bound))
                        else:
                            update_display("Correct!\nNumber is {}".format(target_number))
                            game_started = False
                            utime.sleep(2)
                            init_game()
                    else:
                        update_display("Enter a number")
                elif key == "A":
                    # Spiel neustarten
                    init_game()
                    game_started = True
                    update_display("Enter your guess:")
                elif key == "B":
                    # Aktuellen Tipp löschen
                    guess = ""
                    update_display("Guess cleared")
                elif key == "C":
                    # Hinweis oder andere Funktionalität anzeigen
                    update_display("Hint not available")
        utime.sleep(0.1)

Nachdem der Code ausgeführt wurde, folge diesen Schritten, um das Spiel zu spielen:

* Spiel starten:

  Drücke die Taste 'A' auf der Tastatur.

* Tipps eingeben:

  * Verwende die Zifferntasten, um deinen Tipp (0-99) einzugeben.
  * Drücke 'D', um deinen Tipp abzugeben.

* Rückmeldung erhalten:

  * Das LCD zeigt an, ob dein Tipp zu hoch, zu niedrig oder korrekt ist.
  * Der Bereich wird entsprechend angepasst.

* Gewinnen des Spiels:

  * Wenn du die richtige Zahl rätst, zeigt das LCD "Richtig! Zahl ist XX" an.
  * Das Spiel setzt sich automatisch nach kurzer Verzögerung zurück.

**Verständnis des Codes**

#. Importe und Initialisierung:

   * ``lcd1602.LCD``: Zur Steuerung des LCD-Displays.
   * ``machine.Pin``: Zur Interaktion mit GPIO-Pins.
   * ``urandom``: Zur Generierung zufälliger Zahlen.
   * Initialisiere die I2C-Kommunikation für das LCD1602-Display.

#. Tastaturabtastfunktion (``read_keypad``):

   * Setzt jede Zeile nacheinander auf Hoch.
   * Überprüft, ob eine Spalte hoch liest, was auf einen Tastendruck hinweist.
   * Gibt den Buchstaben zurück, der der gedrückten Taste entspricht.

   .. code-block:: python

        def read_keypad():
            for row_num, row_pin in enumerate(row_pins):
                row_pin.high()
                for col_num, col_pin in enumerate(col_pins):
                    if col_pin.value() == 1:
                        row_pin.low()
                        return keypad_map[row_num][col_num]
                row_pin.low()
            return None

#. Spielvariablen und -initialisierung (``init_game``):

   * ``target_number``: Zufällige Zahl zwischen 0 und 99.
   * ``lower_bound und upper_bound``: Starten jeweils bei 0 und 99.
   * ``guess``: Zeichenkette zum Speichern der aktuellen Tipp-Eingabe.

   .. code-block:: python

        def init_game():
            global target_number, lower_bound, upper_bound, guess
            target_number = urandom.randint(0, 99)
            lower_bound = 0
            upper_bound = 99
            guess = ""
            lcd.clear()
            lcd.message("Press A to Start")

#. Display Update Function (``update_display``):

   Löscht das LCD und zeigt die bereitgestellte Nachricht an.

   .. code-block:: python

        # Anzeigefunktion
        def update_display(message):
            lcd.clear()
            lcd.message(message)

#. Hauptprogrammschleife:

   * Wartet auf Tastendrücke und handhabt die Spiellogik.
   * Taste ``A``: Startet oder startet das Spiel neu.
   * Ziffern ``0``-``9``: Bildet die aktuelle Tippnummer.
   * Taste ``D``: Sendet den Tipp ab und aktualisiert den Bereich.
   * Überprüft, ob der Tipp innerhalb der aktuellen Grenzen liegt.
   * Aktualisiert ``lower_bound`` oder ``upper_bound`` basierend auf dem Tipp.
   * Setzt den Tipp für die nächste Eingabe zurück.
   * Wenn der Tipp korrekt ist, wird eine Erfolgsmeldung angezeigt und das Spiel zurückgesetzt.
   * Taste ``B``: Löscht den aktuellen Tipp.
   * Taste ``C``: Reserviert für zusätzliche Funktionalität (z. B. Hinweise).

   .. code-block:: python

        while True:
            key = read_keypad()
            if key:
                utime.sleep(0.2)  # Entprellverzögerung

                if not game_started:
                    if key == "A":
                        game_started = True
                        update_display("Enter your guess:")
        ...
        ...
            utime.sleep(0.1)

#. Entprellen und Verzögerungen:


   * ``utime.sleep(0.2)``: Kurze Verzögerung nach einem Tastendruck zum Entprellen.
   * ``utime.sleep(0.1)``: Kleine Verzögerung in der Hauptschleife, um die CPU-Auslastung zu reduzieren.

**Fehlerbehebung**

* LCD zeigt keinen Text an:

  * Überprüfe die SDA- und SCL-Verbindungen (GP6 und GP7).
  * Stelle sicher, dass das LCD korrekt mit Strom versorgt wird.
  * Stelle den Kontrastpotentiometer auf der Rückseite des LCD-Moduls ein.

* Tastatur reagiert nicht:

  * Überprüfe alle Zeilen- und Spaltenverbindungen.
  * Stelle sicher, dass Pull-Down-Widerstände angeschlossen sind, wenn keine internen Pull-Downs verwendet werden.
  * Überprüfe, ob die Tastatur ordnungsgemäß funktioniert.

* Zufallszahl ändert sich nicht:

  * Stelle sicher, dass ``urandom`` korrekt importiert und verwendet wird.
  * Der Zufallssamen muss möglicherweise für bessere Zufälligkeit initialisiert werden.

* Probleme mit der Spiellogik:

  * Überprüfe die Bedingungen und Grenzen bei der Verarbeitung von Tipps doppelt.
  * Stelle sicher, dass die oberen und unteren Grenzen korrekt aktualisiert werden.

**Erweiterungen und Verbesserungen**

* Unterstützung für Mehrspieler hinzufügen:

  * Behalte die Anzahl der Versuche jedes Spielers im Auge.
  * Wechsle die Züge zwischen den Spielern.

* Punktesystem implementieren:

  * Verleihe Punkte basierend darauf, wie schnell die Zahl erraten wird.
  * Zeige die Punktzahlen auf dem LCD an.

* Hinweise geben:

  Verwende die Taste 'C', um Hinweise zu geben, wie z. B. "Zahl ist gerade" oder "Zahl ist ein Vielfaches von 5".

* Bereich erhöhen:

  * Ändere das Spiel, um Zahlen zwischen 0 und 999 zu erraten.
  * Passe die Anzeige und die Eingabemethoden entsprechend an.

* Visuelles und akustisches Feedback:

  Füge LEDs oder einen Summer hinzu, um zusätzliches Feedback zu geben.

**Fazit**

Du hast erfolgreich ein interaktives Rate-die-Zahl-Spiel mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt kombiniert Benutzereingaben, Zufallszahlengenerierung und Anzeigeausgabe, um ein unterhaltsames und ansprechendes Spiel zu schaffen. Es ist eine hervorragende Möglichkeit, den Umgang mit Tastaturen, LCD-Anzeigen und Spiellogik in MicroPython zu üben.

Fühle dich frei, das Spiel weiter zu verbessern, indem du neue Funktionen hinzufügst oder die Schnittstelle verbesserst. Dieses Projekt kann als Grundlage für komplexere interaktive Anwendungen dienen.
