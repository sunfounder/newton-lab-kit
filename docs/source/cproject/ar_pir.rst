.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Werbegeschenke**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_pir:

2.10 Menschliche Bewegungen erkennen
========================================

In dieser Lektion lernen wir, wie man einen Passiv-Infrarot (PIR) Sensor mit dem Raspberry Pi Pico 2 verwendet, um menschliche Bewegungen zu erkennen. PIR-Sensoren werden häufig in Sicherheitssystemen, automatischer Beleuchtung und anderen Anwendungen eingesetzt, bei denen Bewegungserkennung erforderlich ist. Sie erkennen die von warmen Objekten wie Menschen oder Tieren in ihrem Sichtfeld ausgestrahlte Infrarotstrahlung.


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
        - :ref:`cpn_pir`
        - 1
        - |link_pir_buy|


**Schaltplan**

|sch_pir|

Wenn das PIR-Modul eine vorbeigehende Person erkennt, ist GP14 hoch, ansonsten niedrig.

.. note::

    Der PIR-Sensor verfügt über zwei Potentiometer:

    * **Empfindlichkeitseinstellung**: Steuert den Erkennungsbereich.
    * **Zeitverzögerungseinstellung**: Steuert, wie lange der Ausgang nach erkannter Bewegung HOCH bleibt.

    Für die Ersttests beide Potentiometer gegen den Uhrzeigersinn auf ihre minimale Position drehen. Dies setzt den Sensor auf die höchste Empfindlichkeit und die kürzeste Verzögerungseinstellung, sodass Sie sofortige Reaktionen beobachten können.

    |img_PIR_TTE|

**Verdrahtungsplan**

|wiring_pir|


**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.10_detect_human_movement.ino`` aus ``newton-lab-kit/arduino/2.10_detect_human_movement`` öffnen. 
   * Oder kopieren Sie diesen Code in die **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2**-Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: python

   const int pirPin = 14;     // PIR sensor output pin connected to GP14
   int pirState = LOW;        // Current state of PIR sensor
   int val = 0;               // Variable to store the PIR reading

   void setup() {
     Serial.begin(115200);    // Initialize Serial Monitor
     pinMode(pirPin, INPUT);  // Set the PIR pin as input
     Serial.println("PIR Sensor Test");
     delay(2000);             // Allow the PIR sensor to stabilize
   }

   void loop() {
     val = digitalRead(pirPin);  // Read the PIR sensor

     if (val == HIGH) {
       if (pirState == LOW) {
         Serial.println("Motion detected!");
         pirState = HIGH;
       }
     } else {
       if (pirState == HIGH) {
         Serial.println("Motion ended!");
         pirState = LOW;
       }
     }
     delay(500);  // Wait half a second before checking again
   }

Wenn der Code läuft und der serielle Monitor geöffnet ist:

* Bewegen Sie sich vor dem PIR-Sensor. Der serielle Monitor sollte "Bewegung erkannt!" anzeigen.
* Hören Sie auf sich zu bewegen oder bewegen Sie sich außerhalb der Reichweite des Sensors. Nach einer kurzen Verzögerung sollte der serielle Monitor "Bewegung beendet!" anzeigen.

**Verständnis des Codes**

#. Lesen des PIR-Sensors:

   Liest den aktuellen Zustand des PIR-Sensors. Er ist HOCH, wenn Bewegung erkannt wird, und NIEDRIG, wenn keine Bewegung erkannt wird.

   .. code-block:: Arduino

      val = digitalRead(pirPin);

#. Bewegung erkennen:

   * Wenn eine Bewegung erkannt wird und es die erste Erkennung ist, wird "Bewegung erkannt!" gedruckt und pirState aktualisiert.
   * Wenn die Bewegung endet, wird "Bewegung beendet!" gedruckt und pirState aktualisiert.
  
   .. code-block:: Arduino

      if (val == HIGH) {
        if (pirState == LOW) {
          Serial.println("Motion detected!");
          pirState = HIGH;
        }
      } else {
        if (pirState == HIGH) {
          Serial.println("Motion ended!");
          pirState = LOW;
        }
      }


**Praktische Anwendungen**

* **Sicherheitssysteme**: Eindringlinge oder unerlaubte Bewegungen erkennen.
* **Automatische Beleuchtung**: Lichter einschalten, wenn Bewegung erkannt wird.
* **Energiesparen**: Geräte ausschalten, wenn keine Bewegung erkannt wird.

**Tipps zur Fehlerbehebung**

* Fehlauslösungen:

  * PIR-Sensoren können empfindlich auf Umgebungsfaktoren wie Temperaturänderungen oder Sonnenlicht reagieren.
  * Vermeiden Sie es, den Sensor direkt auf Wärmequellen oder Fenster zu richten.

* Sensor erkennt keine Bewegung:

  * Stellen Sie sicher, dass der Sensor Zeit hatte, sich zu initialisieren (einige Sensoren benötigen bis zu 60 Sekunden).
  * Stellen Sie den Empfindlichkeitspotentiometer ein.

* Störungen: 

  * Halten Sie den Sensor fern von Elektronik, die elektromagnetische Störungen verursachen könnte.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man einen PIR-Sensor mit dem Raspberry Pi Pico verwendet, um menschliche Bewegungen zu erkennen. Sie haben die Hardware eingerichtet, Code geschrieben, um den Ausgang des Sensors zu lesen, und getestet, wie er auf Bewegungen reagiert. Das Verständnis dafür, wie man die Einstellungen des PIR-Sensors anpasst, ermöglicht es Ihnen, ihn auf Ihre spezifische Anwendung zuzuschneiden, sei es für Sicherheit, Automatisierung oder interaktive Projekte.

