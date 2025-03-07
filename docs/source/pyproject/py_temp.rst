.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_temp:

2.13 Thermometer
===========================

In dieser Lektion lernen wir, wie man einen **Thermistor** mit dem Raspberry Pi Pico 2 verwendet, um die Temperatur zu messen. Ein Thermistor ist ein Widerstand, dessen Widerstandswert sich stark mit der Temperatur verändert. Konkret nutzen wir einen NTC-Thermistor (Negative Temperature Coefficient), dessen Widerstand mit steigender Temperatur abnimmt.

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
        - 1 (10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_thermistor`
        - 1
        - |link_thermistor_buy|

**Funktionsweise des Thermistors**

Ein NTC-Thermistor ist ein temperaturabhängiger Widerstand. Sein Widerstand sinkt mit steigender Temperatur. Durch die Integration in einen Spannungsteiler können wir die Spannung über dem Thermistor messen, die sich mit der Temperatur ändert.  
Mit dem Analog-Digital-Wandler (ADC) des Raspberry Pi Pico 2 können wir diese Spannung auslesen und die entsprechende Temperatur berechnen.

**Schaltplan**

|sch_temp|

In dieser Schaltung bilden ein 10KΩ-Widerstand und ein NTC-Thermistor einen Spannungsteiler. GP28 misst die Spannung über dem Thermistor. Der 10KΩ-Widerstand dient zudem als Schutzwiderstand zur Begrenzung des Stroms.

* **Hohe Temperatur**: Der Widerstand des Thermistors sinkt, wodurch die gemessene Spannung an GP28 niedriger wird. Bei sehr hohen Temperaturen nähert sich der Widerstand null, und GP28 liest nahezu 0.
* **Niedrige Temperatur**: Der Widerstand des Thermistors steigt, wodurch die Spannung an GP28 erhöht wird. In extrem kalten Umgebungen steigt der Widerstand nahezu ins Unendliche, und GP28 liest einen Wert nahe 65535.

Der 10KΩ-Widerstand verhindert eine direkte Verbindung zwischen 3.3V und GND, wodurch ein Kurzschluss vermieden wird.

**Verdrahtungsdiagramm**

|wiring_temp|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, das den Analogwert des Thermistors ausliest, die Temperatur in Celsius und Fahrenheit berechnet und diese ausgibt.

.. note::

    * Öffne ``2.13_thermometer.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    import math

    # Konstanten
    BETA = 3950  # Beta-Koeffizient des Thermistors
    T0 = 298.15  # Referenztemperatur (25°C in Kelvin)
    R0 = 10000   # Widerstand bei T0 (10 kΩ)

    # Initialisierung des ADC auf GP28
    thermistor = machine.ADC(28)

    while True:
        # Lese den Analogwert (0-65535)
        analog_value = thermistor.read_u16()

        # Wandle den Analogwert in eine Spannung um
        voltage = analog_value * 3.3 / 65535

        # Berechne den Widerstand des Thermistors
        Rt = (voltage * R0) / (3.3 - voltage)

        # Berechne die Temperatur in Kelvin mit der Beta-Formel
        tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

        # Wandle Kelvin in Celsius um
        tempC = tempK - 273.15

        # Wandle Celsius in Fahrenheit um
        tempF = tempC * 9 / 5 + 32

        # Ausgabe der Temperaturwerte
        print('Temperature: {:.2f}°C  {:.2f}°F'.format(tempC, tempF))

        # Warte 2 Sekunden vor der nächsten Messung
        utime.sleep(2)

Wenn der Code läuft, wird die Temperatur in Celsius und Fahrenheit in der Konsole angezeigt.

* Berühre den Thermistor mit den Fingern, um zu sehen, wie die Temperatur steigt.
* Kühle ihn mit Eis oder einem kalten Objekt ab, um die Temperatur sinken zu sehen.

**Den Code verstehen**

#. Module importieren:

   * ``machine``: Zugriff auf Hardware-Funktionen.
   * ``utime``: Nutzung von Zeitfunktionen wie ``sleep``.
   * ``math``: Enthält mathematische Funktionen wie ``log``.

#. Konstanten setzen:

   * ``BETA``: Beta-Koeffizient des Thermistors (aus dem Datenblatt, meist 3950).
   * ``T0``: Referenztemperatur in Kelvin (25°C + 273.15).
   * ``R0``: Widerstand des Thermistors bei T0 (10 kΩ).

#. ADC-Pin initialisieren:

   * ``thermistor = machine.ADC(28)``: Setzt GP28 als analogen Eingang.

#. Hauptschleife: 

   * ``analog_value = thermistor.read_u16()``: Liest den rohen Analogwert aus.
   * ``voltage = analog_value * 3.3 / 65535``: Wandelt den Rohwert in eine Spannung um.
   * ``Rt = (voltage * R0) / (3.3 - voltage)``: Verwendet die Spannungsteilerformel zur Berechnung des Thermistor-Widerstands.
   * ``tempK = 1 / ( (1 / T0) + (1 / BETA) * math.log(Rt / R0) )``: Nutzt die vereinfachte Steinhart-Hart-Gleichung für einen einzelnen Beta-Wert.
   * Umrechnung von Kelvin in Celsius und Fahrenheit:
     
     .. code-block:: python
    
        tempC = tempK - 273.15
        tempF = tempC * 9 / 5 + 32

   * ``print('Temperatur: {:.2f}°C {:.2f}°F'.format(tempC, tempF))``: Gibt die Temperaturwerte aus.
   * ``utime.sleep(2)``: Wartet 2 Sekunden vor der nächsten Messung.


**Die Temperaturberechnung verstehen**

* Steinhart-Hart-Gleichung:

Die Steinhart-Hart-Gleichung beschreibt den Widerstand eines Thermistors in Abhängigkeit von der Temperatur:

|temp_format|

* ``T`` ist die Temperatur des Thermistors in Kelvin.
* ``T0`` ist eine Referenztemperatur, üblicherweise 25°C (entspricht 273.15 + 25 in Kelvin).
* ``B`` ist der Beta-Koeffizient des Materials. Der in diesem Kit verwendete NTC-Thermistor hat einen Beta-Wert von 3950.
* ``R`` ist der gemessene Widerstand.
* ``R0`` ist der Widerstand bei der Referenztemperatur T0 (bei 25°C beträgt der Widerstand des Thermistors in diesem Kit 10 Kiloohm).

**Sicherheitshinweis**

Sei vorsichtig beim Erhitzen des Thermistors. Setze ihn keinen hohen Temperaturen aus, die ihn oder den Raspberry Pi Pico 2 beschädigen könnten.

**Weitere Experimente**

* **Datenaufzeichnung**: Ändere den Code so, dass Temperaturwerte in einer Datei auf dem Pico gespeichert werden.
* **Temperaturschwellen definieren**: Füge Bedingungen hinzu, um Aktionen auszulösen, wenn die Temperatur bestimmte Grenzwerte über- oder unterschreitet (z. B. eine LED einschalten oder einen Summer aktivieren).
* **Anzeige der Werte**: Verbinde ein LCD- oder OLED-Display, um die Temperaturmesswerte anzuzeigen.

**Fazit**

Durch die Verwendung eines Thermistors mit dem Raspberry Pi Pico 2 hast du ein grundlegendes Thermometer erstellt, das Temperaturänderungen messen kann.  
Dieses Projekt zeigt, wie analoge Eingaben ausgelesen, Berechnungen durchgeführt und Sensordaten interpretiert werden, um nützliche Informationen zu gewinnen.
