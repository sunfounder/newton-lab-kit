.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Technikbegeisterten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf neue Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_dht11:

6.2 Messen von Temperatur und Luftfeuchtigkeit mit dem DHT11
===============================================================

In dieser Lektion lernen wir, wie man den **DHT11 Temperatur- und Luftfeuchtigkeitssensor** mit dem Raspberry Pi Pico 2 verwendet. Der DHT11 ist ein kostengünstiger digitaler Sensor, der die Umgebungstemperatur und Luftfeuchtigkeit messen und ein kalibriertes digitales Signal ausgeben kann.

**Benötigte Komponenten**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein komplettes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ENTHALTENE TEILE
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Du kannst sie auch einzeln über die folgenden Links kaufen.


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
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|


**Verständnis des DHT11-Sensors**

Der **DHT11** Sensor verwendet einen kapazitiven Feuchtigkeitssensor und einen Thermistor, um die Umgebungsluft zu messen. Er gibt ein digitales Signal über den Datenpin aus und ist relativ einfach zu verwenden, erfordert jedoch eine präzise Timing-Steuerung.

* Temperaturbereich: 0–50 °C mit ±2 °C Genauigkeit
* Luftfeuchtigkeitsbereich: 20–80 % RH mit ±5 % Genauigkeit
* Abtastrate: 1 Hz (einmal pro Sekunde)

**Schaltplan**

|sch_dht11|

**Verdrahtungsdiagramm**

|wiring_dht11|

**Code schreiben**

Lass uns ein MicroPython-Programm schreiben, um Temperatur- und Luftfeuchtigkeitswerte vom DHT11-Sensor zu lesen.

.. note::

    * Öffne ``6.2_temperature_humidity.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny und klicke dann auf „Run“ oder drücke F5.

    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 



    * Hier benötigst du die Bibliothek ``dht.py``. Überprüfe, ob sie bereits auf den Pico hochgeladen wurde. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python

   from machine import Pin
   import utime
   import dht

   # Initialisierung des DHT11-Sensors
   sensor = dht.DHT11(Pin(16))

   while True:
      try:
         # Messung auslösen
         sensor.measure()
         # Werte auslesen
         temperature = sensor.temperature  # In Celsius
         humidity = sensor.humidity        # In Prozent
         # Werte ausgeben
         print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
      except OSError as e:
         print("Failed to read sensor.")
      # Wartezeit vor der nächsten Messung
      utime.sleep(2)

Sobald der Code läuft, werden die Temperatur- und Luftfeuchtigkeitswerte in der Thonny-Shell angezeigt.

.. code-block::

  Temperature: 29.3°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.1°C   Humidity: 60.0%
  Temperature: 29.2°C   Humidity: 60.0%
  Temperature: 29.3°C   Humidity: 60.0%

**Verständnis des Codes**

#. Module importieren:

   * ``machine.Pin``: Steuert die GPIO-Pins.
   * ``utime``: Enthält zeitbezogene Funktionen.
   * ``dht``: Bibliothek für DHT-Sensoren.

#. Initialisierung des Sensors:

   .. code-block:: python

      sensor = dht.DHT11(Pin(16))
      Creates an instance of the DHT11 sensor connected to GP16.

#. Hauptschleife:

   * ``sensor.measure()``: Löst eine Messung aus.
   * ``sensor.temperature``: Liest die Temperatur in Celsius aus.
   * ``sensor.humidity``: Liest die Luftfeuchtigkeit in Prozent aus.
   * ``Exception Handling``: Fängt Fehler beim Lesen des Sensors ab.
   * ``utime.sleep(2)``: Wartet 2 Sekunden zwischen den Messungen.

   .. code-block:: python

      while True:
         try:
            sensor.measure()
            temperature = sensor.temperature
            humidity = sensor.humidity
            print("Temperature: {}°C   Humidity: {}%".format(temperature, humidity))
         except OSError as e:
            print("Failed to read sensor.")
         utime.sleep(2)

**Weitere Experimente**

* Umwandlung der Temperatur in Fahrenheit:

   .. code-block:: python

      temperature_f = temperature * 9 / 5 + 32
      print("Temperature: {}°F   Humidity: {}%".format(temperature_f, humidity))

* Messwerte auf einem LCD anzeigen:

  Integriere ein LCD-Display, um die Werte ohne einen Computer anzuzeigen.


* Warnmeldungen einrichten:

  Nutze eine LED oder einen Summer, um zu warnen, wenn Temperatur oder Luftfeuchtigkeit bestimmte Schwellenwerte überschreiten.

**Fehlersuche**

* Falsche Werte:

  * Stelle sicher, dass der Sensor korrekt angeschlossen ist.
  * Überprüfe lose Verbindungen oder schlechte Kontakte.

* Fehler beim Lesen des Sensor:

  Dies kann gelegentlich aufgrund von Timing-Problemen auftreten. Der Code enthält eine try-except-Routine, um dies zu handhaben.

* Pull-Up-Widerstand:

  Falls der Sensor nicht funktioniert, überprüfe, ob ein Pull-Up-Widerstand zwischen VCC und Daten-Pin erforderlich ist.

**Fazit**

In dieser Lektion hast du gelernt, wie du den DHT11 Temperatur- und Luftfeuchtigkeitssensor mit dem Raspberry Pi Pico 2 verwendest. Die Überwachung von Umweltbedingungen ist eine grundlegende Funktion für viele Projekte, von Wetterstationen bis hin zu Hausautomatisierungssystemen.

* `Try Statement - Python Docs <https://docs.python.org/3/reference/compound_stmts.html?#the-try-statement>`_
