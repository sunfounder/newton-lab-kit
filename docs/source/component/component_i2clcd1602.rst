.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_i2c_lcd:

I2C LCD1602
==============

|img_i2c_lcd1602|

* **GND**: Masse
* **VCC**: Stromversorgung, 5V.
* **SDA**: Serielle Datenleitung. Verbinden Sie diese über einen Pull-up-Widerstand mit VCC.
* **SCL**: Serielle Taktleitung. Verbinden Sie diese über einen Pull-up-Widerstand mit VCC.

Wie allgemein bekannt ist, bereichern LCD und andere Displays zwar die Mensch-Maschine-Interaktion, teilen aber eine gemeinsame Schwäche. Wenn sie an einen Controller angeschlossen werden, belegen sie mehrere IOs des Controllers, der nicht viele externe Ports hat. Dies schränkt auch andere Funktionen des Controllers ein.

Daher wurde das LCD1602 mit einem I2C-Modul entwickelt, um dieses Problem zu lösen. Das I2C-Modul verfügt über einen integrierten PCF8574 I2C-Chip, der I2C-Serien-Daten in parallele Daten für das LCD-Display umwandelt.

* `PCF8574 Datasheet <https://www.ti.com/lit/ds/symlink/pcf8574.pdf?ts=1627006546204&ref_url=https%253A%252F%252Fwww.google.com%252F>`_

**I2C-Adresse**

Die Standardadresse ist grundsätzlich 0x27, in einigen Fällen kann sie auch 0x3F sein.

Die Geräteadresse kann geändert werden, indem die Pads A0/A1/A2 kurzgeschlossen werden; im Standardzustand ist A0/A1/A2 1, und wenn das Pad kurzgeschlossen wird, ist A0/A1/A2 0.

|i2c_address|

**Hintergrundbeleuchtung/Kontrast**

Die Hintergrundbeleuchtung kann durch einen Jumper aktiviert werden, ziehen Sie den Jumper ab, um die Hintergrundbeleuchtung zu deaktivieren. Das blaue Potentiometer auf der Rückseite wird verwendet, um den Kontrast einzustellen (das Verhältnis der Helligkeit zwischen dem hellsten Weiß und dem dunkelsten Schwarz).

|back_lcd1602|

* **Kurzschlusskappe**: Die Hintergrundbeleuchtung kann durch diese Kappe aktiviert werden, ziehen Sie diese Kappe ab, um die Hintergrundbeleuchtung zu deaktivieren.
* **Potentiometer**: Es wird verwendet, um den Kontrast (die Klarheit des angezeigten Textes) einzustellen, der im Uhrzeigersinn erhöht und gegen den Uhrzeigersinn verringert wird.




**Beispiel**

* :ref:`py_lcd` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_lcd` (For Arduino User)