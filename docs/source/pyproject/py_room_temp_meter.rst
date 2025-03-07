.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

.. _py_room_temp:

7.2 Bau eines Raumthermometers
============================================================

In diesem Projekt erstellen wir ein **Raumthermometer**, das einen Thermistor und ein I2C LCD1602-Display verwendet.  
Dieses einfache, aber praktische Gerät misst die Umgebungstemperatur und zeigt sie auf dem LCD-Bildschirm an, sodass du in Echtzeit die Temperatur deiner Umgebung überwachen kannst.

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
    *   - 7
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|



**Funktionsweise der Komponenten**

* **Thermistor:** Ein Widerstand, dessen Widerstandswert sich mit der Temperatur ändert. Wir verwenden einen NTC-Thermistor (Negative Temperature Coefficient), dessen Widerstand bei steigender Temperatur sinkt.

* **Spannungsteiler:** Durch die Kombination des Thermistors mit einem festen Widerstand entsteht ein Spannungsteiler, der Spannungsänderungen in Abhängigkeit von der Temperatur ermöglicht.

* **I2C LCD1602 Display:** Ein 16x2-Zeichen-LCD mit I2C-Schnittstelle, das die Verkabelung und Programmierung durch die Nutzung von nur zwei Datenleitungen (SDA und SCL) vereinfacht.

**Schaltplan**

|sch_room_temp|

**Verdrahtungsdiagramm**

|wiring_room_temp|

**Code schreiben**

Wir schreiben ein MicroPython-Programm, das die Temperatur vom Thermistor ausliest und auf dem LCD-Display anzeigt.

.. note::

    * Öffne ``7.2_room_temperature_meter.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny, dann klicke auf "Run" oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Die Bibliothek ``lcd1602.py`` muss hochgeladen sein. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

    from lcd1602 import LCD
    from machine import I2C, Pin, ADC
    import utime
    import math

    # Initialisierung des Thermistors (ADC an Pin 28)
    thermistor = ADC(28)  # Analogeingang für den Thermistor

    # Initialisierung der I2C-Kommunikation für das LCD1602-Display
    i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)

    # Erstellen eines LCD-Objekts zur Steuerung des LCD1602-Displays
    lcd = LCD(i2c)

    # Konstanten für die Steinhart-Hart-Gleichung
    BETA = 3950  # Beta-Koeffizient des Thermistors
    R0 = 10000   # Widerstand bei 25 Grad Celsius
    T0 = 298.15  # Referenztemperatur in Kelvin (25°C)

    def read_temperature():
        # Lese den ADC-Rohwert vom Thermistor
        adc_value = thermistor.read_u16()

        # Wandle den ADC-Wert in eine Spannung um
        voltage = adc_value * 3.3 / 65535

        # Berechne den Widerstand des Thermistors
        Rt = (voltage * R0) / (3.3 - voltage)

        # Steinhart-Hart-Gleichung zur Berechnung der Temperatur in Kelvin
        tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

        # Umrechnung von Kelvin in Celsius
        tempC = tempK - 273.15

        return tempC

    def main():
        while True:
            temperature = read_temperature()
            # Temperatur mit zwei Dezimalstellen formatieren
            temp_str = "{:.2f} C".format(temperature)

            # Temperatur auf dem LCD anzeigen
            lcd.clear()
            lcd.write(0, 0, "Room Temp:")
            lcd.write(4, 1, temp_str)

            # Optionale Ausgabe der Temperatur in der Konsole
            print("Temperature:", temp_str)

            utime.sleep(1)

    if __name__ == "__main__":
        main()

Sobald der Code läuft, sollte das LCD-Display die aktuelle Raumtemperatur in Celsius anzeigen.  
Falls das Display leer bleibt, passe den Kontrast mit dem Potentiometer auf der Rückseite an.  
Die Konsole in Thonny gibt ebenfalls die gemessenen Temperaturwerte aus.

**Den Code verstehen**

#. Importe und Initialisierung:

   * ``lcd1602.LCD``: Zur Steuerung des LCD-Displays.
   * ``machine.ADC``: Zum Auslesen der analogen Werte vom Thermistor.
   * ``math``: Für die logarithmischen Berechnungen zur Temperaturumrechnung.

#. Variablen:

   * **BETA**: Der Beta-Koeffizient des Thermistors (normalerweise 3950).
   * **R0**: Der Widerstand des Thermistors bei der Referenztemperatur (üblicherweise 10 kΩ bei 25°C).
   * **T0**: Die Referenztemperatur in Kelvin (25°C + 273.15).

   .. code-block:: python

        BETA = 3950  # Beta-Koeffizient des Thermistors
        R0 = 10000   # Widerstand bei 25 Grad Celsius
        T0 = 298.15  # Referenztemperatur in Kelvin (25°C)

#. Temperaturmessung (``read_temperature Function``):

   * **ADC-Wert auslesen**: Erfasst den analogen Wert des Thermistors.
   * **Spannungsberechnung**: Wandelt den ADC-Wert in eine tatsächliche Spannung um.
   * **Widerstandsberechnung (Rt)**: Berechnet den Widerstand des Thermistors mit der Spannungsteilerformel.
   * **Steinhart-Hart-Gleichung**: Ein mathematisches Modell, das den Widerstand eines Thermistors mit der Temperatur in Beziehung setzt.
   * **Umrechnung in Celsius**: Wandelt die Temperatur von Kelvin in Celsius um.

   .. code-block:: python

        def read_temperature():
                # Rohwert des ADC vom Thermistor auslesen
                adc_value = thermistor.read_u16()

                # Umrechnung des Rohwerts in eine Spannung
                voltage = adc_value * 3.3 / 65535

                # Berechnung des Widerstands des Thermistors
                Rt = (voltage * R0) / (3.3 - voltage)

                # Anwendung der Steinhart-Hart-Gleichung zur Berechnung der Temperatur in Kelvin
                tempK = 1 / ((1 / T0) + (1 / BETA) * math.log(Rt / R0))

                # Umrechnung von Kelvin in Celsius
                tempC = tempK - 273.15

                return tempC

#. Hauptschleife (main-Funktion):

   * Liest kontinuierlich die Temperatur.
   * Formatiert und zeigt die Temperatur auf dem LCD an.
   * Gibt die Temperatur optional zur Fehlerüberprüfung in der Konsole aus.
   * Wartet eine Sekunde, bevor die nächste Messung durchgeführt wird.

   .. code-block:: python

        def main():
            while True:
                temperature = read_temperature()
                # Temperatur mit zwei Dezimalstellen formatieren
                temp_str = "{:.2f} C".format(temperature)

                # Temperatur auf dem LCD anzeigen
                lcd.clear()
                lcd.write(0, 0, "Room Temp:")
                lcd.write(4, 1, temp_str)

                # Optionale Ausgabe der Temperatur in der Konsole
                print("Temperature:", temp_str)

                utime.sleep(1)


**Fehlersuche**

* LCD zeigt keinen Text an:

  * Überprüfe die Verbindungen von SDA und SCL (GP6 und GP7).
  * Stelle sicher, dass das LCD-Modul korrekt mit Strom versorgt wird.
  * Passe den Kontrast mit dem Potentiometer auf der Rückseite des Displays an.

* Falsche Temperaturwerte:

  * Vergewissere dich, dass Thermistor und Widerstand richtig angeschlossen sind.
  * Überprüfe die Widerstandswerte.
  * Stelle sicher, dass der BETA-Wert zu deinem Thermistor passt.

* Programmfehler:

  * Prüfe, ob alle notwendigen Bibliotheken korrekt auf den Pico hochgeladen wurden.
  * Überprüfe den Code auf Tippfehler oder fehlerhafte Einrückungen.

**Weitere Experimente**

* Anzeige der Temperatur in Fahrenheit:

  Ändere die read_temperature-Funktion, um die Temperatur auch in Fahrenheit anzuzeigen:  ``tempF = (tempC * 9 / 5) + 32``.

* Luftfeuchtigkeit messen:

  Integriere einen DHT11- oder DHT22-Sensor, um zusätzlich die Luftfeuchtigkeit anzuzeigen.

* Datenprotokollierung:

  Speichere die Temperaturwerte über einen längeren Zeitraum auf dem Pico und analysiere sie auf einem Computer.

* Visuelle Alarme:

  Füge LEDs oder einen Summer hinzu, um einen Alarm auszulösen, wenn die Temperatur einen bestimmten Schwellenwert überschreitet.

**Die Wissenschaft dahinter verstehen**

* Thermistoren und Temperaturmessung:

  * Thermistoren reagieren empfindlich auf Temperaturänderungen und eignen sich daher ideal für präzise Messungen.
  * Der Spannungsteiler wandelt Widerstandsänderungen in Spannungsänderungen um, die vom ADC des Pico ausgelesen werden können.

* Steinhart-Hart-Gleichung:

  * Liefert eine genauere Temperaturberechnung als eine einfache lineare Näherung.
  * Essenziell für Anwendungen, die eine präzise Temperaturmessung erfordern.

**Fazit**

Herzlichen Glückwunsch! Du hast erfolgreich ein funktionales Raumthermometer mit dem Raspberry Pi Pico 2 gebaut.  
Dieses Projekt zeigt nicht nur, wie analoge Sensoren mit I2C-Displays kombiniert werden, sondern bietet auch praktische Erfahrungen in der Temperaturmessung und Anzeige.  
Erweitere und passe dein Thermometer an, indem du neue Funktionen hinzufügst oder weitere Sensoren integrierst.  
Dieses Projekt bildet eine solide Grundlage für die Entwicklung von Umweltüberwachungs- und Steuerungssystemen.
