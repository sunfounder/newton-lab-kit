.. note:: 
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich in Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Verlosungen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ar_transistor:

2.15 Zwei Arten von Transistoren: NPN und PNP
================================================

In dieser Lektion erkunden wir zwei Typen von Transistoren: den **S8050 (NPN)** und den **S8550 (PNP)**. Transistoren werden häufig als elektronische Schalter verwendet, und wir werden sehen, wie beide Typen verwendet werden können, um eine LED mit einem Knopf zu steuern.

|img_NPN&PNP|

* **NPN (S8050)**: Dieser Transistortyp lässt Strom vom **Kollektor** zum **Emitter** fließen, wenn ein hohes Signal an die **Basis** angelegt wird.
* **PNP (S8550)**: Bei PNP-Transistoren fließt der Strom vom **Emitter** zum **Kollektor**, wenn ein niedriges Signal an die **Basis** angelegt wird.


Obwohl beide Transistoren ähnliche Zwecke erfüllen, verhalten sie sich gegenüber der Signalsteuerung genau entgegengesetzt. Lassen Sie uns diese Transistoren verwenden, um eine LED basierend auf der Eingabe eines Knopfes zu steuern.

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

Sie können sie auch einzeln über die unten stehenden Links kaufen.


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
        - Micro USB Kabel
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
        - 3(220Ω, 1KΩ, 10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_button`
        - 1
        - |link_button_buy|
    *   - 8
        - :ref:`cpn_transistor`
        - 1(S8050/S8550)
        - |link_transistor_buy|

**Verdrahtung des NPN (S8050) Transistors**

|sch_s8050|

In diesem Schaltkreis führt das Drücken des Knopfes dazu, dass ein **hohes Signal** an den GP14-Pin gesendet wird. Wenn GP15 ein hohes Signal ausgibt, leitet der NPN-Transistor und ermöglicht den Stromfluss durch die LED, was sie zum Leuchten bringt.

|wiring_s8050|

**Verdrahtung des PNP (S8550) Transistors**

|sch_s8550|

Im Schaltkreis für den PNP-Transistor beginnt der Knopf mit einem niedrigen Signal an GP14 und wechselt zu hoch, wenn er gedrückt wird. Wenn GP15 ein **niedriges Signal** ausgibt, leitet der PNP-Transistor und ermöglicht den Stromfluss, was die LED zum Leuchten bringt.

|wiring_s8550|

**Schreiben des Codes**

.. note::

   * Sie können die Datei ``2.15_transistor.ino`` aus ``newton-lab-kit/arduino/2.15_transistor`` öffnen. 
   * Oder kopieren Sie diesen Code in **Arduino IDE**.
   * Wählen Sie das **Raspberry Pi Pico 2** Board und den richtigen Port, dann klicken Sie auf "Upload".

.. code-block:: arduino

    // Define the pins
    const int buttonPin = 14;  // Button connected to GP14
    const int transistorPin = 15;  // Transistor base connected to GP15

    int buttonState = 0;  // Variable to hold the button state

    void setup() {
      pinMode(buttonPin, INPUT);
      pinMode(transistorPin, OUTPUT);
    }

    void loop() {
      // Read the state of the button
      buttonState = digitalRead(buttonPin);

      // control the transistor
      digitalWrite(transistorPin, buttonState);

      delay(10);  // Small delay for debouncing
    }

**Ergebnisse**

* Für den NPN-Transistor (S8050):

  Wenn Sie den Knopf drücken, sollte die LED leuchten.
  Wenn Sie den Knopf loslassen, sollte die LED erlöschen.

* Für den PNP-Transistor (S8550):

  Wenn Sie den Knopf drücken, sollte die LED erlöschen.
  Wenn Sie den Knopf loslassen, sollte die LED leuchten.

**Verständnis des Codes**

#. Lesen des Knopfzustands:

   Liest den aktuellen Zustand des Knopfes.

   .. code-block:: arduino

        buttonState = digitalRead(buttonPin);

#. Steuerung des Transistors:

   * **Für den NPN-Transistor**: Wenn der Knopf gedrückt ist (``buttonState`` ist HIGH), wird der Transistor eingeschaltet, was den Stromfluss und das Leuchten der LED ermöglicht.
   * **Für den PNP-Transistor**: Wenn der Knopf gedrückt ist (``buttonState`` ist HIGH), wird der Transistor ausgeschaltet (LOW), und wenn der Knopf nicht gedrückt ist, wird der Transistor eingeschaltet.

   .. code-block:: arduino

        digitalWrite(transistorPin, buttonState);


**Weiterführende Experimente**

* Steuerung größerer Lasten:

  Verwenden Sie Transistoren, um Geräte zu steuern, die mehr Strom benötigen, als der Pico direkt bereitstellen kann, wie z.B. Motoren oder Relais.

* Transistor als Verstärker:

  Erforschen Sie, wie Transistoren zur Verstärkung von Signalen verwendet werden können.

* Experiment mit Darlington-Paar:

  Verwenden Sie zwei Transistoren, um ein Darlington-Paar für eine höhere Stromverstärkung zu erstellen.

**Fazit**

In dieser Lektion haben Sie gelernt, wie man sowohl NPN- als auch PNP-Transistoren verwendet, um eine LED mit einem Raspberry Pi Pico und einem Knopf zu steuern. Das Verständnis der Unterschiede zwischen NPN- und PNP-Transistoren ist entscheidend für die Gestaltung von Schaltungen, die Schaltung oder Verstärkung erfordern.

