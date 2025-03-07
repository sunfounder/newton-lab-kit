.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feierlichkeiten teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_led:

2.1 Hallo, LED!
==================

Willkommen zu Ihrem ersten Hardware-Projekt mit dem Raspberry Pi Pico 2! In dieser Lektion lernen wir, wie man eine LED mit MicroPython blinken lässt. Dieses einfache Projekt ist ein großartiger Einstieg in die physische Computertechnik und zeigt, wie man Hardware mit Code steuert.


**Was Sie benötigen**

Für dieses Projekt benötigen Sie die folgenden Komponenten.

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

Sie können diese auch einzeln über die untenstehenden Links kaufen.


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
        - 1(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 1
        - |link_led_buy|

**Schaltplan**

|sch_led|

Durch das Einstellen des GPIO-Pins auf hoch oder niedrig steuern Sie die Spannungsausgabe dieses Pins. Wenn der Pin hoch ist, fließt Strom durch die LED (begrenzt durch den Widerstand), was dazu führt, dass sie aufleuchtet. Wenn der Pin niedrig ist, fließt kein Strom, und die LED erlischt.

**Verdrahtungsplan**

|wiring_led|


**Schreiben des Codes**

.. note::

    * Öffnen Sie die Datei ``2.1_hello_led.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        led.value(1)      # Schalten Sie die LED ein
        utime.sleep(1)    # Warten Sie 1 Sekunde
        led.value(0)      # Schalten Sie die LED aus
        utime.sleep(1)    # Warten Sie 1 Sekunde

Wenn der Code läuft, leuchtet die LED für 1 Sekunde und erlischt dann für 1 Sekunde.

**Verständnis des Codes**

#. Importieren von Bibliotheken:

   * ``machine``: Bietet Zugriff auf die Hardwarekomponenten.
   * ``utime``: Ermöglicht die Nutzung von zeitbezogenen Funktionen wie Verzögerungen.

#. Einrichten des LED-Pins:

   * ``led = machine.Pin(15, machine.Pin.OUT)``: Initialisiert GP15 als Ausgangspin und weist ihn der Variablen ``led`` zu.


#. Erstellen einer Endlosschleife:

   * ``while True``: Startet eine endlose Schleife, um den darin enthaltenen Code kontinuierlich auszuführen.

#. Steuerung der LED:

   * ``led.value(1)``: Stellt den Pin-Ausgang auf hoch (3,3V), schaltet die LED ein.
   * ``utime.sleep(1)``: Pausiert das Programm für 1 Sekunde.
   * ``led.value(0)``: Stellt den Pin-Ausgang auf niedrig (0V), schaltet die LED aus.
   * ``utime.sleep(1)``: Pausiert das Programm für eine weitere Sekunde.

**Weiteres Experimentieren**

* **Blinkrate ändern**: Ändern Sie die Werte in ``utime.sleep(1)``, um die LED schneller oder langsamer blinken zu lassen.
* **Verwenden unterschiedlicher Pins**: Versuchen Sie, die LED an einen anderen GPIO-Pin anzuschließen und aktualisieren Sie entsprechend den Code.
* **Mehrere LEDs**: Fügen Sie weitere LEDs an unterschiedlichen Pins hinzu und steuern Sie diese in Ihrem Code.

**Fehlerbehebung**

* LED leuchtet nicht:

  * Überprüfen Sie die Orientierung der LED. Stellen Sie sicher, dass Anode und Kathode korrekt angeschlossen sind.
  * Überprüfen Sie, ob alle Verbindungen sicher sind.
  * Stellen Sie sicher, dass der Widerstand in Serie mit der LED verbunden ist.

* Fehlermeldungen in Thonny:

  * Stellen Sie sicher, dass Sie den richtigen Interpreter ausgewählt haben.
  * Überprüfen Sie Ihren Code auf Tippfehler.

**Schlussfolgerung**

Herzlichen Glückwunsch! Sie haben erfolgreich eine LED zum Blinken gebracht, indem Sie den Raspberry Pi Pico 2 und MicroPython verwendet haben. Dieses grundlegende Projekt führt Sie in die Steuerung von Hardware mit Code ein und ebnet den Weg für komplexere Projekte.


**Referenzen**

* |link_mpython_machine_pin|
* |link_mpython_machine|
* |link_mpython_utime|
* |link_python_while|