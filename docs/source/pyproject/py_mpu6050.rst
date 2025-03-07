
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich gemeinsam mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_mpu6050:

6.3 Daten vom MPU-6050 lesen
===============================

In dieser Lektion werden wir lernen, wie man den **MPU-6050** 6-Achsen-Bewegungssensor mit dem Raspberry Pi Pico 2 verwendet. Der MPU-6050 kombiniert ein 3-Achsen-Gyroskop und einen 3-Achsen-Beschleunigungsmesser und übermittelt rohe Sensordaten über das I2C-Kommunikationsprotokoll.

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

Sie können sie auch einzeln über die untenstehenden Links kaufen.


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
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Verständnis des MPU-6050 Sensors**

Der **MPU-6050** Sensor wird weit verbreitet in Projekten eingesetzt, die Bewegungserfassung und Orientierungsdetektion erfordern, wie z.B. Drohnen, Robotik und Gaming-Geräte.

* **Beschleunigungsmesser**: Misst Beschleunigungskräfte entlang der X-, Y- und Z-Achsen. Dies umfasst die Schwerkraftbeschleunigung, die es Ihnen ermöglicht, die Neigung oder Orientierung des Sensors zu bestimmen.
* **Gyroskop**: Misst die Rotationsgeschwindigkeit um die X-, Y- und Z-Achsen und liefert Informationen darüber, wie schnell sich der Sensor dreht.

**Schaltplan**

|sch_mpu6050_ar|


**Verdrahtungsdiagramm**

|wiring_mpu6050_ar|

**Code schreiben**

Lassen Sie uns ein MicroPython-Skript schreiben, um Beschleunigungsmesser- und Gyroskopdaten vom MPU-6050-Sensor zu lesen.

.. note::

    * Öffnen Sie die Datei ``6.3_6axis_motion_tracking.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Run" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
     
    * Hier benötigen Sie die Bibliothek ``imu.py`` und ``vector3d.py``, bitte überprüfen Sie, ob sie auf den Pico hochgeladen wurde, für ein detailliertes Tutorial siehe :ref:`add_libraries_py`.


.. code-block:: python

   from machine import I2C, Pin
   import utime
   from imu import MPU6050

   # Initialisieren der I2C-Schnittstelle (I2C0) mit SDA auf GP4 und SCL auf GP5
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # Initialisieren des MPU-6050-Sensors
   mpu = MPU6050(i2c)

   def read_accelerometer():
      """Reads accelerometer data and returns it as a tuple (x, y, z)."""
      accel = mpu.accel
      return accel.x, accel.y, accel.z

   def read_gyroscope():
      """Reads gyroscope data and returns it as a tuple (x, y, z)."""
      gyro = mpu.gyro
      return gyro.x, gyro.y, gyro.z

   def main():
      """Main loop to read and print sensor data."""
      while True:
         # Lesen der Daten des Beschleunigungsmessers
         ax, ay, az = read_accelerometer()
         print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
         
         # Pause zur besseren Lesbarkeit
         utime.sleep(0.5)
         
         # Lesen der Daten des Gyroskops
         gx, gy, gz = read_gyroscope()
         print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
         
         # Pause vor der nächsten Datensatz
         utime.sleep(0.5)

   # Die Hauptfunktion ausführen
   if __name__ == "__main__":
      main()


Das Skript gibt abwechselnd alle 0,5 Sekunden Daten des Beschleunigungsmessers und des Gyroskops aus.

* Ausgabe des Beschleunigungsmessers:

  .. code-block::

     Beschleunigungsmesser (g) - X: 0.000, Y: 0.000, Z: 1.000

  Im Ruhezustand sollten Sie Werte nahe 0 g auf den X- und Y-Achsen und etwa 1 g auf der Z-Achse aufgrund der Schwerkraft sehen.

* Ausgabe des Gyroskops:

  .. code-block::

     Gyroscope (°/s) - X: 0.000, Y: 0.000, Z: 0.000

  Im Stillstand sollten die Gyroskopwerte nahe 0 °/s auf allen Achsen liegen.
  Eine Drehung des Sensors wird diese Werte ändern und die Winkelgeschwindigkeit widerspiegeln.

**Code verstehen**

#. Importe und Einrichtung:


   * ``machine.I2C und machine.Pin``: Für die Hardware-Schnittstelle.
   * ``utime``: Für Zeitfunktionen.
   * ``MPU6050``: Die Sensorklasse aus der imu.py-Bibliothek.

#. I2C-Initialisierung:

   Richtet den I2C-Bus 0 mit SDA auf GP4 und SCL auf GP5 ein. Die Frequenz ist auf 400 kHz eingestellt für schnelle Kommunikation.

   .. code-block:: python

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)


#. Sensor-Initialisierung:

   Erstellt eine Instanz des MPU-6050-Sensors mit der I2C-Schnittstelle.

   .. code-block:: python

      mpu = MPU6050(i2c)

#. Beschleunigungsmessdaten lesen:

   Greift auf die Daten des Beschleunigungsmessers zu und gibt die Werte X, Y, Z zurück.

   .. code-block:: python

      def read_accelerometer():
         accel = mpu.accel
         return accel.x, accel.y, accel.z


#. Gyroskopdaten lesen:
   
   Greift auf die Daten des Gyroskops zu und gibt die Werte X, Y, Z zurück.

   .. code-block:: python

      def read_gyroscope():
         gyro = mpu.gyro
         return gyro.x, gyro.y, gyro.z


#. Hauptschleife:

   * Liest und gibt die Daten des Beschleunigungsmessers aus.
   * Wartet 0,5 Sekunden.
   * Liest und gibt die Daten des Gyroskops aus.
   * Wartet weitere 0,5 Sekunden, bevor der Vorgang wiederholt wird.

   .. code-block:: python

      def main():
         while True:
            # Daten des Beschleunigungsmessers lesen und ausgeben
            ax, ay, az = read_accelerometer()
            print("Accelerometer (g) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(ax, ay, az))
            
            utime.sleep(0.5)
            
            # Daten des Gyroskops lesen und ausgeben
            gx, gy, gz = read_gyroscope()
            print("Gyroscope (°/s) - X: {:.3f}, Y: {:.3f}, Z: {:.3f}".format(gx, gy, gz))
            
            utime.sleep(0.5)


#. Programmentstiegspunkt:

   Stellt sicher, dass ``main()`` aufgerufen wird, wenn das Skript direkt ausgeführt wird.

   .. code-block:: python

      if __name__ == "__main__":
         main()


**Weiterführende Experimente**

* **Fokus auf einen Sensor**: Um sich auf die Daten des Beschleunigungsmessers oder des Gyroskops zu konzentrieren, können Sie die Ausgabeanweisungen für den anderen Sensor auskommentieren.
* **Datenvisualisierung**: Verwenden Sie Werkzeuge oder Software, um die Sensordaten in Echtzeit zu visualisieren und so besser darzustellen.
* **Orientierung berechnen**: Implementieren Sie Algorithmen zur Berechnung von Neigung und Rollen aus den Daten des Beschleunigungsmessers.
* **Bewegungserkennung**: Erstellen Sie ein Programm, das Aktionen ausführt, wenn bestimmte Bewegungsschwellen überschritten werden.

**Verständnis der Sensordaten**

* Beschleunigungsmesser:

  * Misst Beschleunigungskräfte in g (Gravitationskraft).
  * Nützlich zur Erkennung von Orientierung, Neigung und linearer Bewegung.

* Gyroskop:

  * Misst die Rotationsgeschwindigkeit in Grad pro Sekunde (°/s).
  * Nützlich zur Erkennung von Rotation und Winkelbewegung.

**Fehlerbehebungstipps**

* Keine Ausgabe oder Fehler:

  * Überprüfen Sie die Verdrahtungsverbindungen, insbesondere die SDA- und SCL-Leitungen.
  * Stellen Sie sicher, dass der Sensor korrekt mit Strom versorgt wird.

* Statische Messwerte:

  * Wenn sich die Messwerte bei Bewegung des Sensors nicht ändern, überprüfen Sie auf lockere Verbindungen.
  * Stellen Sie sicher, dass die richtige I2C-Adresse verwendet wird.

* Inkonsistente Daten:

  * Umgebungsbedingte Vibrationen können die Sensorwerte beeinflussen.
  * Platzieren Sie den Sensor während des Tests auf einer stabilen Oberfläche.

**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man den MPU-6050 Beschleunigungsmesser und Gyroskop-Sensor mit dem Raspberry Pi Pico 2 verbindet. Durch das Lesen der rohen Sensordaten können Sie eine Vielzahl von Anwendungen erkunden, die Bewegungserkennung, Orientierungsverfolgung und mehr umfassen.
