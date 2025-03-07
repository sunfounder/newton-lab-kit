.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt des Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Verkauf aufkommende Probleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _ar_keypad:

4.2 Nutzung eines 4x4-Tastenfelds
=================================================

In dieser Lektion lernen wir, wie man ein **4x4-Matrix-Tastenfeld** mit dem Raspberry Pi Pico 2 verbindet, um zu erkennen, welche Tasten gedrückt werden. Matrix-Tastaturen werden häufig in Geräten wie Taschenrechnern, Telefonen, Verkaufsautomaten und Sicherheitssystemen für die numerische Eingabe verwendet.

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
        - :ref:`cpn_keypad`
        - 1
        - |link_keypad_buy|

**Verständnis des 4x4-Tastenfelds**

Ein 4x4-Tastenfeld besteht aus:

* **16 Tasten**, angeordnet in 4 Reihen und 4 Spalten.
* **8 Pins**: 4 verbunden mit den Reihen und 4 mit den Spalten.

Wenn Sie eine Taste drücken, wird eine spezifische Reihe und Spalte verbunden, was es uns ermöglicht, die Taste basierend auf den Reihen- und Spaltennummern zu identifizieren.

So sind die Tasten angeordnet:

|img_keypad|

**Schaltplan**

|sch_keypad_ar|


Die Reihen der Tastatur (G2 ~ G5) sind so programmiert, dass sie hoch gehen; wenn einer von G6 ~ G9 hoch gelesen wird, dann wissen wir, welche Taste gedrückt ist.

Beispielsweise, wenn G6 hoch gelesen wird, dann wird die numerische Taste 1 gedrückt; dies liegt daran, dass die Steuerpins der numerischen Taste 1 G2 und G6 sind, wenn die numerische Taste 1 gedrückt wird, werden G2 und G6 zusammen verbunden und G6 ist auch hoch.

**Verdrahtung**

|wiring_keypad_ar|


**Schreiben des Codes**


.. note::

    * Sie können die Datei ``4.2_4x4_keypad.ino`` aus ``newton-lab-kit/arduino/4.2_4x4_keypad`` öffnen.
    * Oder kopieren Sie diesen Code in die **Arduino IDE**.
    * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".
    * Die ``Adafruit Keypad``-Bibliothek wird hier verwendet, Sie können sie aus dem **Library Manager** installieren.

      .. image:: img/lib_ad_keypad.png

.. code-block:: arduino

    #include "Adafruit_Keypad.h"

    // Define the number of rows and columns
    const byte ROWS = 4;
    const byte COLS = 4;

    // Define the keymap for the keypad
    char keys[ROWS][COLS] = {
      { '1', '2', '3', 'A' },
      { '4', '5', '6', 'B' },
      { '7', '8', '9', 'C' },
      { '*', '0', '#', 'D' }
    };

    // Connect to the row pinouts of the keypad
    byte rowPins[ROWS] = { 2, 3, 4, 5 };

    // Connect to the column pinouts of the keypad
    byte colPins[COLS] = { 6, 7, 8, 9 };

    // Create the Keypad object
    Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

    void setup() {
      // Initialize Serial communication
      Serial.begin(115200);

      // Initialize the keypad
      myKeypad.begin();
    }

    void loop() {
      // Update the state of keys
      myKeypad.tick();

      // Check if there are any new keypad events
      while (myKeypad.available()) {
        // Read the keypad event
        keypadEvent e = myKeypad.read();

        // Check if the event is a key press
        if (e.bit.EVENT == KEY_JUST_PRESSED) {
          // Print the key value to the Serial Monitor
          Serial.println((char)e.bit.KEY);
        }
      }

      delay(10); // Short delay to improve stability
    }

Nach dem Hochladen des Codes drücken Sie eine beliebige Taste auf dem Tastenfeld. Das entsprechende Tastenlabel (z. B. '1', 'A') sollte im Seriellen Monitor erscheinen.

Stellen Sie sicher, dass jeder Tastendruck genau erkannt und angezeigt wird. Testen Sie alle Tasten, um die korrekte Funktionalität zu bestätigen.

**Verständnis des Codes**

#. Einschließen der Bibliothek:

   Diese Zeile schließt die Adafruit Keypad-Bibliothek ein, die Funktionen zur Interaktion mit dem Tastenfeld bietet.

   .. code-block:: arduino

      #include "Adafruit_Keypad.h"

#. Definition des Tastenfeld-Layouts:

   ``ROWS`` und ``COLS`` definieren die Abmessungen des Tastenfelds. ``keys`` ist ein 2D-Array, das das Label jeder Taste auf dem Tastenfeld darstellt.

   .. code-block:: arduino

      const byte ROWS = 4;
      const byte COLS = 4;

      char keys[ROWS][COLS] = {
        { '1', '2', '3', 'A' },
        { '4', '5', '6', 'B' },
        { '7', '8', '9', 'C' },
        { '*', '0', '#', 'D' }
      };

#. Anschließen des Tastenfelds an GPIO-Pins:

   ``rowPins`` und ``colPins`` sind Arrays, die die GPIO-Pins speichern, die mit den Reihen und Spalten des Tastenfelds verbunden sind.

   .. code-block:: arduino

      byte rowPins[ROWS] = { 2, 3, 4, 5 };
      byte colPins[COLS] = { 6, 7, 8, 9 };

#. Initialisieren des Tastenfeld-Objekts:

   Diese Zeile erstellt eine Instanz der Klasse ``Adafruit_Keypad``, die mit dem Tastenfeldschema und den Pin-Konfigurationen initialisiert wird.

   .. code-block:: arduino

      Adafruit_Keypad myKeypad = Adafruit_Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

#. Setup-Funktion:

   Initialisiert die serielle Kommunikation für das Debugging und startet das Tastenfeld.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);    // Initialize serial communication at 115200 baud
        myKeypad.begin();        // Initialize the keypad
      }

#. Loop-Funktion:

   * Überprüft kontinuierlich auf Tastenereignisse.
   * Wenn eine Taste gedrückt wird, wird der Tastenwert im Seriellen Monitor angezeigt.

   .. code-block:: arduino

      void loop() {
        myKeypad.tick(); // Update the state of keys

        while (myKeypad.available()) {
          keypadEvent e = myKeypad.read(); // Read the keypad event

          if (e.bit.EVENT == KEY_JUST_PRESSED) {
            Serial.println((char)e.bit.KEY); // Print the pressed key
          }
        }
        delay(10); // Short delay to improve stability
      }

**Weiterführende Untersuchungen**

* Implementierung der Tasten-Entprellung:

  Verbessern Sie die Zuverlässigkeit der Tastenerkennung, indem Sie Entprelltechniken implementieren, um falsche Auslösungen durch mechanisches Rauschen zu filtern.

* Erstellung eines Passworteingabesystems:

  Verwenden Sie das Tastenfeld zur Eingabe eines Passworts und zur Steuerung des Zugangs zu bestimmten Funktionen in Ihrem Projekt.

* Integration mit anderen Komponenten:

  Kombinieren Sie das Tastenfeld mit LCD-Displays, LEDs oder Summer, um komplexere Benutzeroberflächen zu erstellen.

* Bau eines einfachen Taschenrechners:

  Verwenden Sie das Tastenfeld, um Zahlen einzugeben und grundlegende Rechenoperationen durchzuführen, die auf einem LCD angezeigt werden.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man ein 4x4-Matrix-Tastenfeld mit dem Raspberry Pi Pico unter Verwendung der Adafruit Keypad-Bibliothek verbindet. Durch die Erkennung von Tastendrücken können Sie interaktive Projekte wie tastaturbasierte Eingabesysteme, Passworteingabemechanismen und mehr erstellen. Das Verständnis, wie Tasteneingaben gelesen und verarbeitet werden, ist wesentlich für den Bau benutzerfreundlicher Schnittstellen in Ihren Elektronikprojekten.
