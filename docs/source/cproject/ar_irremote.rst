.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_irremote:

6.4 Verwendung einer Infrarot-Fernbedienung
==========================================================

In dieser Lektion lernen wir, wie man eine **Infrarot-(IR)-Fernbedienung** und einen **IR-Empfänger** mit dem Raspberry Pi Pico 2 verwendet. Dadurch können wir Signale einer IR-Fernbedienung empfangen und dekodieren, um unsere Projekte drahtlos zu steuern.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Bauteile.

Ein komplettes Kit ist besonders praktisch, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE IM KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten auch einzeln über die untenstehenden Links erworben werden.


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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Funktionsweise der Infrarotkommunikation**

Die Infrarotkommunikation erfolgt durch das drahtlose Übertragen von Daten mithilfe von Infrarotlicht. Viele Haushaltsgeräte wie Fernseher und DVD-Player werden mit IR-Fernbedienungen gesteuert.

* **IR-Sender (Fernbedienung):** Sendet moduliertes Infrarotlicht aus, wenn eine Taste gedrückt wird.
* **IR-Empfänger:** Erkennt das modulierte IR-Signal und wandelt es in elektrische Signale um, die dekodiert werden können.

**Schaltplan**

|sch_irrecv|

**Verdrahtungsdiagramm**

|wiring_irrecv|


**Code schreiben**

Wir schreiben ein Programm, das den IR-Empfänger initialisiert, eingehende IR-Signale empfängt, dekodiert und die erkannten Tastendrücke im Seriellen Monitor anzeigt.

.. note::

    * Sie können die Datei ``6.4_ir_remote_control.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/6.4_ir_remote_control`` öffnen. 
    * Oder diesen Code in die **Arduino IDE** kopieren.
    * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.
    * Die ``IRremote`` wird hier verwendet und kann über den **Library Manager** installiert werden.

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #define SEND_PWM_BY_TIMER

    #include <IRremote.hpp>  // Include the IRremote library

    const int receiverPin = 17;  // Define the pin number for the IR Sensor

    void setup() {
      // Start serial communication at a baud rate of 115200
      Serial.begin(115200);
      // Initialize the IR receiver on the specified pin with LED feedback enabled
      IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
    }

    void loop() {
      if (IrReceiver.decode()) {  // Check if the IR receiver has received a signal
        bool result = 0;
        String key = decodeKeyValue(IrReceiver.decodedIRData.command);
        if (key != "ERROR") {
          Serial.println(key);  // Print the readable command
          delay(100);
        }
      IrReceiver.resume();  // Prepare the IR receiver to receive the next signal
      }
    }

    // Function to map received IR signals to corresponding keys
    String decodeKeyValue(long result) {
      switch (result) {
        case 0x45: return "POWER";
        case 0x47: return "MUTE";
        case 0x46: return "MODE";
        case 0x44: return "PLAY/PAUSE";
        case 0x40: return "BACKWARD";
        case 0x43: return "FORWARD";
        case 0x7: return "EQ";
        case 0x15: return "-";
        case 0x9: return "+";
        case 0x19: return "CYCLE";
        case 0xD: return "U/SD";
        case 0x16: return "0";
        case 0xC: return "1";
        case 0x18: return "2";
        case 0x5E: return "3";
        case 0x8: return "4";
        case 0x1C: return "5";
        case 0x5A: return "6";
        case 0x42: return "7";
        case 0x52: return "8";
        case 0x4A: return "9";
        case 0x0: return "ERROR";
        default: return "ERROR";
      }
    }

Nach dem Hochladen des Codes drücken Sie Tasten auf der IR-Fernbedienung und beobachten die zugehörigen Tastennamen im Seriellen Monitor.

.. code-block:: arduino

    BACKWARD
    CYCLE
    POWER
    MODE
    EQ
    5
    9

.. note::

  Neue Fernbedienungen haben möglicherweise eine Plastiklasche, um die Batterie zu isolieren. Ziehen Sie diese heraus, um die Fernbedienung zu aktivieren.


**Verständnis des Codes**

#. Header und Konstanten:

   * ``#define SEND_PWM_BY_TIMER``: Definiert eine Makrovariable, die hier nicht weiter verwendet wird.
   * ``#include <IRremote.hpp>``: Inkludiert die IRremote-Bibliothek, um IR-Signale zu senden und zu empfangen.
   * ``const int receiverPin = 17;``: Weist den IR-Empfänger dem GPIO-Pin 17 zu.

#. Setup-Funktion:

   * ``Serial.begin(115200);``: Startet die serielle Kommunikation mit 115200 Baud.
   * ``IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);``: Initialisiert den IR-Empfänger und aktiviert die LED-Feedback-Funktion.
   
      .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        IrReceiver.begin(receiverPin, ENABLE_LED_FEEDBACK);
      }
  
#. Loop Function: 

   * ``if (IrReceiver.decode())``: Überprüft, ob der IR-Empfänger ein gültiges IR-Signal empfangen hat. Falls ja, wird das Signal dekodiert.
   * ``decodeKeyValue(IrReceiver.decodedIRData.command)``: Ruft eine Funktion auf, die den empfangenen IR-Befehl in eine lesbare Taste (z. B. "POWER" oder "MUTE") umwandelt.
   * ``Serial.println(key);``: Gibt die dekodierte Taste im Seriellen Monitor aus.
   * ``delay(100);``: Fügt eine kurze Verzögerung hinzu, um Mehrfachausgaben desselben Signals zu vermeiden.
   * ``IrReceiver.resume();``: Bereitet den IR-Empfänger darauf vor, das nächste Signal zu empfangen, indem das vorherige gelöscht wird.

   .. code-block:: arduino

      void loop() {
        if (IrReceiver.decode()) {
          bool result = 0;
          String key = decodeKeyValue(IrReceiver.decodedIRData.command);
          if (key != "ERROR") {
            Serial.println(key);
            delay(100);
          }
          IrReceiver.resume();
        }
      }

#. ``decodeKeyValue``-Funktion:

   * Diese Funktion nimmt einen lon-Wert (den rohen IR-Befehl) und ordnet ihn über eine switch-Anweisung einer bestimmten Taste zu. Jeder Fall entspricht einer anderen Taste auf der Fernbedienung.
   * Zum Beispiel entspricht 0x45 der Taste "POWER", und 0x47 der Taste "MUTE".
   * Falls der empfangene Befehl keiner bekannten Taste zugeordnet werden kann, gibt die Funktion "ERROR" zurück.

   .. code-block:: arduino

      String decodeKeyValue(long result) {
        switch (result) {
          case 0x45: return "POWER";
          case 0x47: return "MUTE";
          case 0x46: return "MODE";
          ...
          case 0x4A: return "9";
          case 0x0: return "ERROR";
          default: return "ERROR";
        }
      }

**Fehlersuche**

* Keine Signale werden angezeigt:

  * Überprüfen Sie, ob der IR-Empfänger korrekt mit GPIO 17 verbunden ist.
  * Stellen Sie sicher, dass der IR-Empfänger mit VCC und GND richtig verbunden ist.
  * Prüfen Sie, ob der richtige GPIO-Pin im Code definiert ist (``receiverPin``).

* Falsche Signale:

  * Vergewissern Sie sich, dass die Fernbedienung mit dem IR-Empfänger kompatibel ist.
  * Prüfen Sie, ob die ``decodeKeyValue``-Funktion die IR-Codes Ihrer Fernbedienung korrekt zuordnet.
  * Nutzen Sie eine universelle Fernbedienung, um Kompatibilitätsprobleme auszuschließen.

* Unbekannte Befehle:

  * Aktualisieren Sie die ``decodeKeyValue``-Funktion, um die spezifischen IR-Codes Ihrer Fernbedienung hinzuzufügen.
  * Verwenden Sie ein IR-Decoder-Tool oder eine Referenz, um die exakten Codes Ihrer Fernbedienung zu ermitteln.

* Signalstörungen:

  * Achten Sie darauf, dass sich keine Hindernisse zwischen der Fernbedienung und dem IR-Empfänger befinden.
  * Platzieren Sie den Sensor nicht in der Nähe anderer IR-emittierender Geräte, um Interferenzen zu vermeiden.

**Weitere Experimente**

* Geräte mit IR-Signalen steuern:

  Verwenden Sie dekodierte IR-Signale, um LEDs, Motoren, Servos oder andere Aktoren basierend auf Fernbedienungseingaben zu steuern.

* Eine universelle Fernbedienung erstellen:

  Erweitern Sie die ``decodeKeyValue()``-Funktion, um mehrere Fernbedienungen zu unterstützen, indem Sie eine größere Anzahl an IR-Codes zuordnen.

* Feedback-Mechanismen hinzufügen:

  Integrieren Sie ein LCD- oder OLED-Display, um den aktuellen Status oder empfangene Befehle anzuzeigen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie eine Infrarot-(IR)-Fernbedienung und einen IR-Empfänger mit dem Raspberry Pi Pico verwenden, um IR-Signale zu empfangen und zu dekodieren. Durch die Nutzung der IRremote-Bibliothek können Sie Fernbedienungseingaben einfach interpretieren und zur Steuerung Ihrer Projekte nutzen. Dieses Setup ist eine grundlegende Technik für die Entwicklung ferngesteuerter Geräte, automatisierter Systeme und benutzerfreundlicher Schnittstellen.
