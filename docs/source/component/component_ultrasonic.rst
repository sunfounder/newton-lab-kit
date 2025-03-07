.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ultrasonic:

Ultraschallmodul
================================

|img_ultrasonic|

* **TRIG**: Trigger-Impulseingang
* **ECHO**: Echo-Impulsausgang
* **GND**: Masse
* **VCC**: 5V Versorgung

Dies ist der HC-SR04 Ultraschall-Entfernungssensor, der eine berührungslose Messung von 2 cm bis 400 cm mit einer Genauigkeit von bis zu 3 mm ermöglicht. Das Modul enthält einen Ultraschall-Sender, einen Empfänger und eine Steuerschaltung.

Sie müssen nur 4 Pins verbinden: VCC (Stromversorgung), Trig (Auslösen), Echo (Empfang) und GND (Masse), um es einfach für Ihre Messprojekte zu verwenden.

**Merkmale**

* Betriebsspannung: DC5V
* Betriebsstrom: 16mA
* Arbeitsfrequenz: 40Hz
* Maximale Reichweite: 500cm
* Minimale Reichweite: 2cm
* Trigger-Eingangssignal: 10uS TTL-Puls
* Echo-Ausgangssignal: Eingangs-TTL-Pegelsignal und der Bereich im Verhältnis
* Stecker: XH2.54-4P
* Abmessungen: 46x20,5x15 mm

**Prinzip**

Die grundlegenden Prinzipien sind wie folgt:

* Verwendung des IO-Triggers für mindestens 10us Hochpegelsignal.

* Das Modul sendet einen 8-Zyklen-Schallimpuls mit 40 kHz und erkennt, ob ein Signal empfangen wird.

* Echo gibt ein Hochpegelsignal aus, wenn ein Signal zurückkommt; die Dauer des Hochpegels entspricht der Zeit von der Emission bis zur Rückkehr.

* Entfernung = (Hochpegelzeit x Schallgeschwindigkeit (340M/S)) / 2

|ultrasonic_prin|


Formel:

* us / 58 = Entfernung in Zentimetern
* us / 148 = Entfernung in Zoll
* Entfernung = Hochpegelzeit x Geschwindigkeit (340M/S) / 2

.. note::

    Dieses Modul sollte nicht unter Strom angeschlossen werden, wenn nötig, sollte zuerst die Masse des Moduls angeschlossen werden. Andernfalls kann dies die Funktion des Moduls beeinträchtigen.

    Die Fläche des zu messenden Objekts sollte mindestens 0,5 Quadratmeter groß und möglichst flach sein. Andernfalls kann dies die Ergebnisse beeinflussen.


**Beispiel**

* :ref:`py_ultrasonic` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ultrasonic` (For Arduino User)
.. * :ref:`per_reversing_system` (For Piper Make User)