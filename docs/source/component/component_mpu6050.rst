.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_mpu6050:

MPU6050 Modul
===========================

**MPU6050**

|img_mpu6050|

Der MPU-6050 ist ein 6-Achsen-Bewegungssensor, der einen 3-Achsen-Gyroskop und 
einen 3-Achsen-Beschleunigungsmesser kombiniert.

Seine drei Koordinatensysteme sind wie folgt definiert:

Legen Sie den MPU6050 flach auf den Tisch, sodass die Seite mit dem Etikett nach 
oben zeigt und ein Punkt auf dieser Oberfläche sich in der oberen linken Ecke befindet. 
Dann ist die aufrechte Richtung nach oben die Z-Achse des Chips. Die Richtung von links 
nach rechts gilt als X-Achse. Entsprechend wird die Richtung von hinten nach vorne als Y-Achse definiert.

|img_mpu6050_a| 


**3-Achsen-Beschleunigungsmesser**

Der Beschleunigungsmesser funktioniert nach dem Prinzip des piezoelektrischen Effekts, 
der Fähigkeit bestimmter Materialien, eine elektrische Ladung als Reaktion auf mechanischen Druck zu erzeugen.

Stellen Sie sich hier eine quaderförmige Box vor, die eine kleine Kugel enthält, 
wie im obigen Bild. Die Wände dieser Box bestehen aus piezoelektrischen Kristallen. 
Wenn Sie die Box kippen, wird die Kugel durch die Schwerkraft gezwungen, sich in 
Richtung der Neigung zu bewegen. Die Wand, mit der die Kugel kollidiert, erzeugt 
winzige piezoelektrische Ströme. Es gibt insgesamt drei Paare gegenüberliegender 
Wände in einem Quader. Jedes Paar entspricht einer Achse im 3D-Raum: X-, Y- und 
Z-Achsen. Abhängig von den Strömen, die von den piezoelektrischen Wänden erzeugt 
werden, können wir die Richtung der Neigung und deren Stärke bestimmen.

|img_mpu6050_a2|


Wir können den MPU6050 verwenden, um seine Beschleunigung auf jeder Koordinatenachse zu erkennen 
(im stationären Zustand auf dem Schreibtisch ist die Beschleunigung der Z-Achse 1
Gravitationseinheit, und die X- und Y-Achsen sind 0). Wenn er geneigt ist oder sich 
in einem schwerelosen/überlasteten Zustand befindet, ändert sich der entsprechende Wert.

Es gibt vier wählbare Messbereiche: +/-2g, +/-4g, +/-8g und +/-16g (standardmäßig 2g), die jeweils einer bestimmten Präzision entsprechen. Die Werte reichen von -32768 bis 32767.

Die Beschleunigungsablesung wird in einen Beschleunigungswert umgewandelt, indem die Ablesung aus dem Ablesungsbereich in den Messbereich abgebildet wird.

Beschleunigung = (Rohdaten der Beschleunigungsmesserachse / 65536 * voller Skalenbeschleunigungsbereich) g

Nehmen Sie als Beispiel die X-Achse, wenn die Rohdaten der Beschleunigungsmesser X-Achse 16384 betragen und der Bereich als +/-2g ausgewählt ist:

**Beschleunigung entlang der X-Achse = (16384 / 65536 * 4) g** **=1g**

**3-Achsen-Gyroskop**

Gyroskope funktionieren nach dem Prinzip der Coriolis-Beschleunigung. 
Stellen Sie sich vor, dass es eine gabelähnliche Struktur gibt, die sich 
ständig hin und her bewegt. Sie wird mit piezoelektrischen Kristallen an 
Ort und Stelle gehalten. Wenn Sie versuchen, diese Anordnung zu kippen, 
erfahren die Kristalle eine Kraft in Richtung der Neigung. Dies ist auf 
die Trägheit der sich bewegenden Gabel zurückzuführen. Die Kristalle erzeugen 
daher einen Strom im Einklang mit dem piezoelektrischen Effekt, und dieser 
Strom wird verstärkt.

|img_mpu6050_g|

Das Gyroskop hat auch vier wählbare Messbereiche: +/- 250, +/- 500,
+/- 1000, +/- 2000. Die Berechnungsmethode und Beschleunigung sind
im Wesentlichen konsistent.

Die Formel zur Umrechnung der Ablesung in Winkelgeschwindigkeit lautet wie folgt:

Winkelgeschwindigkeit = (Rohdaten der Gyroskopachse / 65536 * voller Skalengyroskopbereich) °/s

Zum Beispiel, die Beschleunigungsmesser X-Achse Rohdaten betragen 16384 und
Bereiche + / - 250°/ s:

**Winkelgeschwindigkeit entlang der X-Achse = (16384 / 65536 * 500)°/s** **=125°/s**

**Beispiel**

* :ref:`py_mpu6050` (For MicroPython User)
* :ref:`py_somato_controller` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_mpu6050` (For Arduino User)