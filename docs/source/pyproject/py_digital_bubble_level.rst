.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in Raspberry Pi, Arduino und ESP32 mit anderen Technikbegeisterten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Löse Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugriff auf neue Produktankündigungen und Sneak Peeks.
    - **Spezielle Rabatte**: Profitiere von exklusiven Rabatten auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nimm an Gewinnspielen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu experimentieren und zu erschaffen? Klicke auf [|link_sf_facebook|] und tritt noch heute bei!

.. _py_bubble_level:

7.12 Bau einer digitalen Wasserwaage
=========================================

In diesem Projekt erstellen wir eine **digitale Wasserwaage** mit dem Raspberry Pi Pico 2, einem MPU6050-Beschleunigungs- und Gyroskopsensor sowie einer 8x8-LED-Matrix, die über zwei 74HC595-Schieberegister gesteuert wird. Dieses Gerät funktioniert ähnlich wie eine herkömmliche Wasserwaage und zeigt die Neigung einer Oberfläche an. Je nach Neigung des MPU6050 bewegt sich eine auf der LED-Matrix dargestellte "Blase" entsprechend und ermöglicht eine visuelle Anzeige der Ebenheit.

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Verständnis der Komponenten**

* **MPU6050 Beschleunigungssensor und Gyroskop**: Liefert Beschleunigungs- und Rotationsdaten entlang der X-, Y- und Z-Achsen, die zur Berechnung der Neigungswinkel verwendet werden.
* **8x8-LED-Matrix**: Ein Raster aus LEDs, das es ermöglicht, Muster oder Bilder darzustellen, indem einzelne LEDs gesteuert werden.
* **74HC595 Schieberegister**: Ermöglichen die Steuerung mehrerer Ausgänge (in diesem Fall Zeilen und Spalten der LED-Matrix) mit nur wenigen GPIO-Pins des Pico.

**Schaltplan**

|sch_bubble_level|

Der MPU6050 erfasst die Beschleunigungswerte in jeder Richtung und berechnet den Neigungswinkel.

Basierend auf diesen Daten zeichnet das Programm einen 2x2-Pixel-Punkt auf der LED-Matrix mithilfe der beiden 74HC595-Chips.

Wenn sich der Neigungswinkel ändert, sendet das Programm unterschiedliche Daten an die 74HC595-Chips, wodurch sich die Position des Punkts ändert und ein "Blaseneffekt" entsteht.

**Verdrahtung**

|wiring_digital_bubble_level| 


**Code schreiben**

Wir schreiben ein MicroPython-Skript, das:

* Die Beschleunigungsdaten vom MPU6050 liest.
* Die Neigungswinkel entlang der X- und Y-Achsen berechnet.
* Die Neigungswinkel auf Positionen der 8x8-LED-Matrix abbildet.
* Eine "Blase" (eine 2x2-Pixel-Darstellung) anzeigt, die sich entsprechend der Neigung bewegt.

.. note::

    * Öffne ``7.12_digital_bubble_level.py`` aus ``newton-lab-kit/micropython`` oder kopiere den Code in Thonny und klicke dann auf „Run“ oder drücke F5.
    * Stelle sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier benötigst du die Bibliotheken ``imu.py`` und ``vector3d.py``. Überprüfe, ob sie bereits auf den Pico hochgeladen wurden. Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

.. code-block:: python 

    import machine
    from machine import I2C, Pin
    import time
    import math
    from imu import MPU6050
    
    # Initialisierung der I2C-Kommunikation mit dem MPU6050-Sensor
    i2c = I2C(1, sda=Pin(6), scl=Pin(7), freq=400000)
    mpu = MPU6050(i2c)
    
    # Funktion zur Berechnung der Distanz zwischen zwei Punkten
    def dist(a, b):
        return math.sqrt((a * a) + (b * b))
    
    # Funktion zur Berechnung der Rotation entlang der y-Achse
    def get_y_rotation(x, y, z):
        radians = math.atan2(x, dist(y, z))
        return -math.degrees(radians)
    
    # Funktion zur Berechnung der Rotation entlang der x-Achse
    def get_x_rotation(x, y, z):
        radians = math.atan2(y, dist(x, z))
        return math.degrees(radians)
    
    # Funktion zur Ermittlung der aktuellen Winkel vom MPU6050-Sensor
    def get_angle():
        y_angle = get_y_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        x_angle = get_x_rotation(mpu.accel.x, mpu.accel.y, mpu.accel.z)
        return x_angle, y_angle
    
    # Initialisierung der Schieberegister-Pins zur Steuerung der LED-Matrix
    sdi = machine.Pin(18, machine.Pin.OUT)
    rclk = machine.Pin(19, machine.Pin.OUT)
    srclk = machine.Pin(20, machine.Pin.OUT)
    
    # Funktion, um Daten ins Schieberegister zu schieben
    def hc595_in(dat):
        for bit in range(7, -1, -1):
            srclk.low()
            time.sleep_us(30)
            sdi.value(1 & (dat >> bit))
            time.sleep_us(30)
            srclk.high()
    
    # Funktion, um die Daten vom Schieberegister auf die LED-Matrix auszugeben
    def hc595_out():
        rclk.high()
        time.sleep_us(200)
        rclk.low()
    
    # Funktion zur Anzeige eines Glyphs (8x8-Matrix) auf der LED-Matrix
    def display(glyph):
        for i in range(0, 8):
            hc595_in(glyph[i])
            hc595_in(0x80 >> i)
            hc595_out()
    
    # Konvertierung einer 2D-Matrix in ein Glyph, das auf der LED-Matrix angezeigt werden kann
    def matrix_2_glyph(matrix):
        glyph = [0 for i in range(8)]
        for i in range(8):
            for j in range(8):
                glyph[i] += matrix[i][j] << j
        return glyph
    
    # Klemmen eines Werts zwischen einem festgelegten Minimum und Maximum
    def clamp_number(val, min_val, max_val):
        return min_val if val < min_val else max_val if val > max_val else val
    
    # Abbilden eines Werts von einem Bereich auf einen anderen
    def interval_mapping(x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    # Berechnung der Position der Blase in der Matrix basierend auf den MPU6050-Lesungen
    sensitivity = 4  # Empfindlichkeit der Blasenbewegung
    matrix_range = 7  # Die Matrixgröße ist 8x8, also ist der Bereich 0-7
    point_range = matrix_range - 1  # Die Position der Blase sollte zwischen 0 und 6 liegen
    
    # Funktion zur Berechnung der Position der Blase basierend auf Sensordaten
    def bubble_position():
        y, x = get_angle()  # Erhalten der aktuellen Rotationswinkel
        x = int(clamp_number(interval_mapping(x, 90, -90, 0 - sensitivity, point_range + sensitivity), 0, point_range))
        y = int(clamp_number(interval_mapping(y, -90, 90, point_range + sensitivity, 0 - sensitivity), 0, point_range))
        return [x, y]
    
    # Fallenlassen der Blase (dargestellt durch das Ausschalten von 2x2 LEDs) in die Matrix
    def drop_bubble(matrix, bubble):
        matrix[bubble[0]][bubble[1]] = 0
        matrix[bubble[0] + 1][bubble[1]] = 0
        matrix[bubble[0]][bubble[1] + 1] = 0
        matrix[bubble[0] + 1][bubble[1] + 1] = 0
        return matrix
    
    # Hauptschleife
    while True:
        matrix = [[1 for i in range(8)] for j in range(8)]  # Erstellen einer leeren Matrix (alle LEDs an)
        bubble = bubble_position()  # Erhalten der aktuellen Blasenposition basierend auf Sensordaten
        matrix = drop_bubble(matrix, bubble)  # Fallenlassen der Blase in die Matrix
        display(matrix_2_glyph(matrix))  # Anzeigen der Matrix auf dem LED-Gitter
        time.sleep(0.1)  # Kleine Verzögerung, um Aktualisierungen zu verlangsamen


Wenn der Code ausgeführt wird, platziere die Schaltung auf einer ebenen Fläche.
Die Blase (ein 2x2-Pixel-Bereich) sollte sich im Zentrum der LED-Matrix befinden.
Neige das Breadboard oder das MPU6050-Modul.
Beobachte, wie sich die Blase auf der LED-Matrix in Richtung der Neigung bewegt und eine echte Wasserwaage simuliert.

**Verständnis des Codes**

Dieser Code liest Daten von einem MPU6050-Beschleunigungs- und Gyroskopsensor, um die Neigung des Geräts zu bestimmen, und zeigt eine "Blase" auf einer 8x8-LED-Matrix an, die eine digitale Wasserwaage simuliert.

#. Importe und Initialisierung:

   * ``machine``: Zugriff auf die Hardwarekomponenten des Mikrocontrollers.
   * ``I2C``, ``Pin``: Für I2C-Kommunikation und GPIO-Pin-Steuerung.
   * ``time``: Zeitfunktionen für Verzögerungen.
   * ``math``: Mathematische Funktionen für Berechnungen.
   * ``MPU6050`` aus ``imu``: Bibliothek zur Schnittstelle mit dem MPU6050-Sensor.

#. I2C-Initialisierung:

   * Einrichtung der I2C-Kommunikation mit SDA auf Pin 6 und SCL auf Pin 7.
   * Die Frequenz wird auf 400 kHz für eine schnelle Datenübertragung eingestellt.
   * Ein ``mpu``-Objekt wird erstellt, um mit dem MPU6050-Sensor zu kommunizieren.

#. Mathematische Funktionen:

   * ``dist(a, b)``:

     * Berechnet die euklidische Distanz zwischen zwei Werten.
     * Wird zur Berechnung der Größe der Komponenten in den Winkelberechnungen verwendet.

   * ``get_y_rotation(x, y, z)``:

     * Berechnet die Rotation um die Y-Achse in Grad.
     * Nutzt ``math.atan2``, um den Arkustangens von x und der Distanz zwischen y und z zu berechnen.
     * Das Ergebnis wird negiert, um die gewünschte Ausrichtung zu erhalten.

   * ``get_x_rotation(x, y, z)``:

     * Berechnet die Rotation um die X-Achse in Grad.
     * Ähnlich wie ``get_y_rotation``, aber mit Berechnung des Arkustangens von y und der Distanz zwischen x und z.

   * ``get_angle()``:

     * Ruft die aktuellen Beschleunigungsdaten vom MPU6050-Sensor ab.
     * Berechnet die X- und Y-Rotationswinkel basierend auf den Beschleunigungswerten.

#. Schieberegister-Funktionen:

   * Pin-Definitionen:

     * ``sdi``: Serial Data Input (Pin 18).
     * ``rclk``: Register Clock (Latch) (Pin 19).
     * ``srclk``: Shift Register Clock (Pin 20).

   * ``hc595_in(dat)``:

     * Schiebt ein 8-Bit-Datenbyte in das Schieberegister.
     * Iteriert über jedes Bit vom MSB zum LSB.
     * Steuert ``srclk`` und ``sdi``, um die Bits in das Register zu schieben.

   * ``hc595_out()``:

     * Latcht die Daten vom Schieberegister auf die Ausgänge.
     * Kippt das ``rclk``-Signal, um die Daten auszugeben.

#. LED-Matrix-Anzeigefunktionen:

   * ``display(glyph)``:

     * Zeigt ein 8x8-Glyph auf der LED-Matrix an.
     * Iteriert durch jede Zeile des Glyphs.
     * Verschiebt die Zeilendaten und den entsprechenden Spaltenselektor.
     * Ruft ``hc595_out()`` auf, um die Anzeige zu aktualisieren.

   * ``matrix_2_glyph(matrix)``:

     * Wandelt eine 8x8 2D-Matrix von 0en und 1en in ein 8-Byte-Glyph um.
     * Jedes Byte im Glyph repräsentiert eine Zeile in der LED-Matrix.
     * Bits in jedem Byte entsprechen den LEDs in dieser Zeile.

#. Hilfsfunktionen:

   * ``clamp_number(val, min_val, max_val)``:

     * Stellt sicher, dass ``val`` innerhalb des angegebenen Bereichs bleibt.
     * Verhindert, dass die Blase sich außerhalb der LED-Matrix bewegt.

   * ``interval_mapping(x, in_min, in_max, out_min, out_max)``:

     * Ordnet einen Wert ``x`` von einem numerischen Bereich auf einen anderen zu.
     * Wird verwendet, um Winkelmessungen in Matrixpositionen zu übersetzen.

#. Blasen-Positionsberechnung:

   * Empfindlichkeitseinstellungen:

     * ``sensitivity = 4``: Bestimmt, wie empfindlich die Blase auf Neigungsänderungen reagiert.
     * ``matrix_range = 7``: Der maximale Index für die 8x8-Matrix (0 bis 7).
     * ``point_range = matrix_range - 1``: Angepasster Bereich, um die Blase innerhalb der Grenzen zu halten (0 bis 6).

   * ``bubble_position()``:

     * Ruft die aktuellen X- und Y-Rotationswinkel ab.
     * Ordnet die Winkel auf Positionen auf der LED-Matrix zu, indem ``interval_mapping`` verwendet wird.
     * Begrenzt die Positionen, um sicherzustellen, dass sie innerhalb der Matrix bleiben.

#. Blasen-Anzeigefunktion:

   * ``drop_bubble(matrix, bubble)``:

     * Ändert die LED-Matrix, um die Blase an der angegebenen Position darzustellen.
     * Schaltet einen 2x2-Block von LEDs aus, der sich um die Blasenkoordinaten befindet.
     * Aktualisiert die Matrix, um den visuellen Effekt einer sich bewegenden Blase zu erzeugen.

#. Hauptschleife

   * Läuft kontinuierlich, um die Anzeige basierend auf den Sensoreingaben zu aktualisieren.
   * Initialisiert eine frische 8x8-Matrix mit allen eingeschalteten LEDs (Wert ``1``).
   * Ruft die aktuelle Blasenposition von ``bubble_position()`` ab.
   * Aktualisiert die Matrix mit ``drop_bubble()``, um die neue Position der Blase anzuzeigen.
   * Wandelt die Matrix mit ``matrix_2_glyph()`` in ein Glyph um.
   * Zeigt das Glyph auf der LED-Matrix mit ``display()`` an.
   * Wartet 0,1 Sekunden vor der Wiederholung, um die Aktualisierungsrate zu steuern.

**Fehlersuche**

* LED-Matrix wird nicht korrekt angezeigt:

  * Überprüfe alle Verdrahtungen zwischen den Schieberegistern und der LED-Matrix.
  * Stelle sicher, dass die Schieberegister korrekt mit dem Pico verbunden sind.
  * Prüfe, ob die Konfiguration der gemeinsamen Anode oder Kathode deiner LED-Matrix mit der Code-Logik übereinstimmt.

* Blasenbewegung ist inkorrekt:

  * Stelle sicher, dass der MPU6050 richtig angeschlossen und funktionsfähig ist.
  * Überprüfe, ob der MPU6050 korrekt ausgerichtet ist.

* Programmfehler:

  * Stelle sicher, dass ``imu.py`` und ``vector3d.py`` korrekt hochgeladen wurden.
  * Prüfe den Code auf Tippfehler oder Einrückungsfehler.

**Weiterführende Experimente**

* Empfindlichkeit anpassen:

  Ändere die Skalierung der Winkel-zu-Matrix-Zuordnung, um die Blasenbewegung fein abzustimmen.

* Anzeigeverbesserungen:

  * Ändere die Größe oder Form der Blase.
  * Füge visuelle Effekte wie Nachzieheffekte oder verschiedene Muster hinzu.

* Kalibrierung hinzufügen:

  Implementiere eine Kalibrierungsroutine, um einen Nullpunkt zu setzen, wenn das Gerät auf einer unebenen Oberfläche liegt.

* Alternative Anzeigen:

  Verwende ein OLED- oder LCD-Display, um numerische Winkelwerte zusätzlich zur visuellen Blase anzuzeigen.

**Fazit**

Du hast erfolgreich eine digitale Wasserwaage mit dem Raspberry Pi Pico 2 gebaut! Dieses Projekt zeigt, wie Beschleunigungsdaten genutzt werden können, um Orientierung und Neigung visuell darzustellen, und wie eine LED-Matrix-Anzeige mithilfe von Schieberegistern gesteuert wird.

Erweitere das Projekt mit zusätzlichen Funktionen oder integriere es in größere Systeme!

