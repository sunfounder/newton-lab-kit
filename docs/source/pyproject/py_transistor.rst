.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_transistor:

2.15 Zwei Arten von Transistoren: NPN und PNP
=================================================

In dieser Lektion werden wir zwei Transistortypen untersuchen: den **S8050 (NPN)** und den **S8550 (PNP)**. Transistoren werden häufig als elektronische Schalter verwendet. Wir werden sehen, wie beide Typen zur Steuerung einer LED mit einem Taster eingesetzt werden können.

|img_NPN&PNP|

* **NPN (S8050)**: Dieser Transistor ermöglicht den Stromfluss vom **Kollektor** zum **Emitter**, wenn ein hohes Signal an die **Basis** angelegt wird.
* **PNP (S8550)**: Beim PNP-Transistor fließt der Strom vom **Emitter** zum **Kollektor**, wenn ein niedriges Signal an die **Basis** angelegt wird.


Obwohl beide Transistoren ähnliche Zwecke erfüllen, verhalten sie sich in Bezug auf die Signalsteuerung entgegengesetzt. Lassen wir diese Transistoren eine LED basierend auf einem Tastendruck steuern.

**Benötigte Komponenten**

Für dieses Projekt werden folgende Komponenten benötigt.

Ein komplettes Kit ist besonders praktisch. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Alternativ können die Komponenten auch einzeln über die folgenden Links erworben werden.


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
        - 3 (220Ω, 1KΩ, 10KΩ)
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
        - 1 (S8050/S8550)
        - |link_transistor_buy|

**Schaltung für den NPN-Transistor (S8050)**

|sch_s8050|

In dieser Schaltung sendet das Drücken des Tasters ein **hohes Signal** an den GP14-Pin. Wenn GP15 ein hohes Signal ausgibt, leitet der NPN-Transistor Strom durch die LED, sodass sie leuchtet.

|wiring_s8050|

**Schaltung für den PNP-Transistor (S8550)**

|sch_s8550|

Beim PNP-Transistor startet der Taster mit einem niedrigen Signal an GP14 und wechselt beim Drücken auf hoch. Wenn GP15 ein **niedriges Signal** ausgibt, leitet der PNP-Transistor den Strom und die LED leuchtet.

|wiring_s8550|

**Code schreiben**

Beide Transistoren können mit demselben Code gesteuert werden. Der Status des Tasters wird ausgelesen. Abhängig davon, ob der Taster gedrückt ist oder nicht, gibt der Pico ein hohes oder niedriges Signal an GP15 aus.

.. note::

    * Öffne ``2.15_transistor.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine

    # Initialisiere den Taster und den Signalausgang
    button = machine.Pin(14, machine.Pin.IN)
    signal = machine.Pin(15, machine.Pin.OUT)

    while True:
        button_status = button.value()
        if button_status == 1:
            signal.value(1)  # Hohes Signal an den Transistor senden
        else:
            signal.value(0)  # Niedriges Signal an den Transistor senden


**Ergebnisse**

* NPN-Schaltung (S8050):  

  Die LED leuchtet, wenn der Taster gedrückt wird, da der NPN-Transistor bei einem hohen Signal an seiner Basis durchschaltet.

* PNP-Schaltung (S8550):  
  Die LED leuchtet, wenn der Taster losgelassen wird, da der PNP-Transistor bei einem niedrigen Signal an seiner Basis durchschaltet.

Beide Schaltungen zeigen, wie Transistoren zur Steuerung des Stromflusses je nach Signaltyp verwendet werden können.

**Fazit**

Durch das Experimentieren mit diesen beiden Transistortypen erhältst du ein besseres Verständnis dafür, wie NPN- und PNP-Transistoren funktionieren und wie sie in Schaltungen zur Steuerung elektronischer Geräte eingesetzt werden können.


