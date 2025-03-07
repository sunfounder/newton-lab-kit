.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_ac_buz:

3.1 Den Summer zum Piepen bringen!
====================================

In dieser Lektion lernen wir, wie man einen **Summer** mit dem Raspberry Pi Pico 2 steuert. Ein Summer ist ein digitales Ausgangsgerät, ähnlich einer LED, und sehr einfach zu bedienen. Wir verwenden einen **aktiven Summer**, der beim Anlegen eines Signals selbstständig einen Ton erzeugt.

**Was ist ein aktiver Summer?**

Ein **aktiver Summer** besitzt einen internen Oszillator, wodurch er besonders einfach zu verwenden ist. Es genügt, ein Signal an den Summer zu senden, um ihn piepen zu lassen – eine komplexe Frequenzsteuerung ist nicht erforderlich. Im Gegensatz dazu benötigt ein **passiver Summer** ein externes Signal zur Klangerzeugung.

|img_buzzer|


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
        - :ref:`cpn_transistor`
        - 1 (S8050)
        - |link_transistor_buy|
    *   - 6
        - :ref:`cpn_resistor`
        - 1 (1KΩ)
        - |link_resistor_buy|
    *   - 7
        - Aktiver :ref:`cpn_buzzer`
        - 1
        - 


**Schaltplan**

|sch_buzzer|

In dieser Schaltung wird der Summer über einen **S8050 NPN-Transistor** mit Strom versorgt. Der Transistor verstärkt den Stromfluss, sodass der Summer lauter klingt, als wenn er direkt an den Pico angeschlossen wäre.

Funktionsweise:

* **GP15** gibt ein High-Signal aus, um den Transistor zu steuern.
* Sobald der Transistor aktiviert wird, fließt Strom durch den Summer, wodurch ein Ton erzeugt wird.

Ein **1kΩ-Widerstand** begrenzt den Strom, um den Transistor zu schützen.

**Verdrahtungsdiagramm**

Stellen Sie sicher, dass Sie den **aktiven Summer** verwenden. Sie können ihn daran erkennen, dass seine Rückseite versiegelt ist (im Gegensatz zum passiven Summer, bei dem die Platine sichtbar ist).

|img_buzzer|

|wiring_beep|


**Code schreiben**


.. note::

   * Sie können die Datei ``3.1_beep.ino`` aus dem Verzeichnis ``newton-lab-kit/arduino/3.1_beep`` öffnen. 
   * Oder diesen Code in die **Arduino IDE** kopieren.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port aus und klicken Sie auf „Hochladen“.

.. code-block:: Arduino

    const int buzzerPin = 15;  // GPIO pin connected to the transistor base

    void setup() {
      pinMode(buzzerPin, OUTPUT);
    }

    void loop() {
      digitalWrite(buzzerPin, HIGH);  // Turn the buzzer on
      delay(1000);                    // Wait for 1 second
      digitalWrite(buzzerPin, LOW);   // Turn the buzzer off
      delay(1000);                    // Wait for 1 second
    }

Nach dem Hochladen des Codes:

Der Summer sollte für 1 Sekunde piepen, dann für 1 Sekunde still bleiben und dieses Muster kontinuierlich wiederholen.
Falls kein Ton zu hören ist, überprüfen Sie die Verkabelung und stellen Sie sicher, dass alle Verbindungen korrekt sind.
Vergewissern Sie sich außerdem, dass ein aktiver Summer verwendet wird.

**Verständnis des Codes**

#. Definition des Summer-Pins:

   Der ``buzzerPin`` wird GPIO 15 zugewiesen, welcher den Transistor steuert und damit den Summer.

   .. code-block:: Arduino

        const int buzzerPin = 15;  // GPIO pin connected to the transistor base

#. Konfiguration des Pins:

   Der ``buzzerPin`` wird als Ausgang konfiguriert.

   .. code-block:: Arduino

        void setup() {
          pinMode(buzzerPin, OUTPUT);
        }

#. Steuerung des Summers: Die ``loop()``-Funktion wiederholt das Ein- und Ausschalten des Summers.

   * ``digitalWrite(buzzerPin, HIGH)``: Schaltet den ``buzzerPin`` auf HIGH, wodurch der Transistor durchschaltet und der Summer aktiviert wird.
   * ``delay(1000)``: Wartet 1000 Millisekunden (1 Sekunde).
   * ``digitalWrite(buzzerPin, LOW)``: Schaltet den ``buzzerPin`` auf LOW, wodurch der Transistor sperrt und der Summer ausgeschaltet wird.

   .. code-block:: Arduino

        void loop() {
          digitalWrite(buzzerPin, HIGH);  // Summer einschalten
          delay(1000);                    // 1 Sekunde warten
          digitalWrite(buzzerPin, LOW);   // Summer ausschalten
          delay(1000);                    // 1 Sekunde warten
        }


**Weitere Experimente**

* Anpassung der Piepton-Dauer:

  * Ändern Sie die ``delay()``-Werte, um die Dauer des Pieptons zu variieren.
  * Experimentieren Sie mit kürzeren oder längeren Wartezeiten.

* Erstellen von Mustern:

  * Erzeugen Sie komplexe Signalmuster durch Anpassung der ``loop()``-Funktion.
  * Beispielsweise können Sie ein SOS-Signal im Morsecode erstellen.

* Verwendung eines passiven Summers:

  * Testen Sie einen passiven Summer mit der ``tone()``-Funktion, um unterschiedliche Frequenzen zu erzeugen.
  * Beachten Sie, dass die Verkabelung und der Code für einen passiven Summer anders sind.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie einen aktiven Summer mit dem Raspberry Pi Pico und einem Transistor steuern. Durch die Verwendung eines GPIO-Pins zur Steuerung des Transistors kann der Summer sicher ein- und ausgeschaltet werden, ohne die GPIO-Pins des Pico zu überlasten. Dieses einfache Konzept kann erweitert werden, um komplexere Tonsignale zu erzeugen oder den Summer in Alarmanlagen, Benachrichtigungen oder interaktiven Projekten zu nutzen.
