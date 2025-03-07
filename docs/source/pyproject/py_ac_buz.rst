.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie mit anderen Enthusiasten tiefer in Raspberry Pi, Arduino und ESP32 ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitieren Sie von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Verlosungen**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu basteln? Klicken Sie auf [|link_sf_facebook|] und treten Sie noch heute bei!

.. _py_ac_buz:

3.1 Den Buzzer zum Piepen bringen!
=====================================

In dieser Lektion lernen wir, wie man einen **Buzzer** mit dem Raspberry Pi Pico 2 zum Piepen bringt. Ein Buzzer ist ein digitales Ausgabegerät, ähnlich einer LED, und sehr einfach zu steuern. Für dieses Projekt verwenden wir einen **aktiven Buzzer**, der automatisch einen Ton erzeugt, sobald er ein Signal erhält.

**Was ist ein aktiver Buzzer?**

Ein aktiver Buzzer hat einen integrierten Oszillator, was ihn besonders einfach zu verwenden macht. Man muss ihm lediglich ein Signal senden, damit er piept – eine komplizierte Frequenzsteuerung ist nicht erforderlich. Das unterscheidet ihn von einem **passiven Buzzer**, der eine externe Steuersignalquelle benötigt, um Töne zu erzeugen.

|img_buzzer|


**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist praktisch, ein vollständiges Kit zu erwerben. Hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE KOMPONENTEN
        - LINK
    *   - Newton Lab Kit	
        - 450+ Bauteile
        - |link_newton_lab_kit|

Sie können die Teile auch einzeln über die folgenden Links erwerben.


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

In dieser Schaltung wird der Buzzer über einen **S8050** NPN-Transistor betrieben. Der Transistor verstärkt den Strom, sodass der Buzzer lauter ist, als wenn er direkt an den Pico angeschlossen wäre.

Funktionsweise:

* **GP15** gibt ein HIGH-Signal aus, um den Transistor zu aktivieren.
* Wenn der Transistor durchgeschaltet wird, kann Strom durch den Buzzer fließen und er gibt einen Ton aus.

Ein **1kΩ-Widerstand** begrenzt den Stromfluss, um den Transistor zu schützen.

**Verdrahtungsdiagramm**

Vergewissern Sie sich, dass Sie den **aktiven Buzzer** verwenden. Sie können ihn an der versiegelten Rückseite erkennen (im Gegensatz zu einem offenen PCB, das für einen passiven Buzzer typisch ist).

|img_buzzer|

|wiring_beep|

**Code schreiben**

Nun schreiben wir ein einfaches MicroPython-Programm zur Steuerung des Buzzers.

.. note::

    * Öffnen Sie ``3.1_beep.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Initialisierung des Buzzer-Pins (GP15)
    buzzer = machine.Pin(15, machine.Pin.OUT)

    while True:
        # Schleife, um den Buzzer viermal piepen zu lassen
        for i in range(4):
            buzzer.value(1)  # Buzzer einschalten
            utime.sleep(0.3)  # 0,3 Sekunden warten
            buzzer.value(0)  # Buzzer ausschalten
            utime.sleep(0.3)  # 0,3 Sekunden warten
        utime.sleep(1)  # Längere Pause vor dem nächsten Zyklus

Wenn der Code läuft, hören Sie:

* Der Buzzer piept viermal hintereinander mit einer Pause von 0,3 Sekunden zwischen den Tönen.
* Nach den vier Pieptönen gibt es eine längere Pause von einer Sekunde, bevor der Zyklus erneut beginnt.

**Erklärung des Codes**

#. Initialisierung des Buzzers:

   * ``buzzer = machine.Pin(15, machine.Pin.OUT)``: Initialisiert GP15 als Ausgangspin zur Steuerung des Buzzers.

#. Hauptschleife:

   * Die ``while True``-Schleife stellt sicher, dass der Code ununterbrochen läuft.
   * Innerhalb der Schleife wird der Buzzer viermal ein- (``buzzer.value(1)``) und ausgeschaltet (``buzzer.value(0)``), jeweils mit einer Verzögerung von 0,3 Sekunden.
   * Nach den vier Pieptönen folgt eine Pause von 1 Sekunde, bevor der Zyklus erneut beginnt.


**Weitere Experimente**

* **Dauer des Pieptons ändern**: Ändern Sie die Werte in ``utime.sleep(0.3)`` um längere oder kürzere Pieptöne zu erzeugen.
* **Anzahl der Pieptöne variieren** : Ändern Sie die Anzahl der Durchläufe in der Schleife, um den Buzzer mehr oder weniger oft piepen zu lassen.
* **Buzzer mit Taster steuern** : Schließen Sie einen Taster an GP14 an und ändern Sie den Code so, dass der Buzzer nur piept, wenn der Taster gedrückt wird.

**Fazit**

In dieser Lektion haben Sie gelernt, wie Sie einen aktiven Buzzer mit einem Transistor und dem Raspberry Pi Pico 2 steuern. Sie haben nun ein grundlegendes Verständnis dafür, wie digitale Ausgänge zur Erzeugung von Tönen verwendet werden können. Die gleichen Prinzipien lassen sich auch auf andere Ausgabegeräte wie LEDs, Motoren und mehr anwenden.
