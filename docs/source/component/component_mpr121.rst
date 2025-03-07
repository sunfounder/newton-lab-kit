.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_mpr121:

MPR121 Modul
===========================

|img_mpr121|


* **3.3V**: Stromversorgung
* **IRQ**: Open Collector Interrupt-Ausgang, aktiv niedrig
* **SCL**: I2C-Takt
* **SDA**: I2C-Daten
* **ADD**: I2C-Adressauswahleingang. Verbinden Sie den ADD-Pin mit den Linien VSS, VDD, SDA oder SCL, die resultierenden I2C-Adressen sind 0x5A, 0x5B, 0x5C und 0x5D.
* **GND**: Masse
* **0~11**: Elektrode 0~11, eine Elektrode ist ein Berührungssensor. Typischerweise können Elektroden einfach aus einem Stück Metall oder einem Draht bestehen. Manchmal kann jedoch die Länge des Drahtes oder das Material, auf dem sich die Elektrode befindet, das Auslösen des Sensors erschweren. Aus diesem Grund ermöglicht der MPR121 die Konfiguration dessen, was benötigt wird, um eine Elektrode zu aktivieren oder zu deaktivieren.

**ÜBERBLICK ÜBER MPR121**

Der MPR121 ist die zweite Generation von kapazitiven Berührungssensor-Controllern nach der 
Erstveröffentlichung der MPR03x-Serie. Der MPR121 verfügt über erhöhte interne Intelligenz; 
einige der wichtigsten Ergänzungen umfassen eine erhöhte Elektrodenanzahl, eine hardwarekonfigurierbare 
I2C-Adresse, ein erweitertes Filtersystem mit Debouncing und vollständig unabhängige Elektroden mit 
eingebauter Auto-Konfiguration. Das Gerät bietet auch einen 13. simulierten Sensorkanal, der für die 
Näherungserkennung über die multiplexierten Sensoreingänge genutzt wird.

* `MPR121 Datasheet <https://cdn-shop.adafruit.com/datasheets/MPR121.pdf>`_

**Merkmale**

* Niedriger Stromverbrauch
    • Betrieb mit 1,71 V bis 3,6 V
    • 29 μA Betriebsstrom bei einer Abtastintervallperiode von 16 ms
    • 3 μA Strom im Stop-Modus
* 12 kapazitive Sensoreingänge
    • 8 Eingänge sind multifunktional für LED-Treiber und GPIO
* Vollständige Berührungserkennung
    • Auto-Konfiguration für jeden Sensoreingang
    • Auto-Kalibrierung für jeden Sensoreingang
    • Berührungs-/Freigabeschwelle und Debouncing für die Berührungserkennung
* I2C-Schnittstelle mit Interrupt-Ausgang
* 3 mm x 3 mm x 0,65 mm 20 Lead QFN-Paket
* Betriebstemperaturbereich von -40°C bis +85°C



**Beispiel**

* :ref:`py_mpr121` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_mpr121` (For Arduino User)