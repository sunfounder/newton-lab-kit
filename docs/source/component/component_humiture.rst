.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_dht11:

DHT11 Feuchtigkeits- und Temperatursensor
==============================================

Der digitale Temperatur- und Feuchtigkeitssensor DHT11 ist ein Verbundsensor, der einen kalibrierten digitalen Signalausgang für Temperatur und Feuchtigkeit enthält.
Die Technologie spezieller digitaler Module zur Datensammlung und die Technologie zur Temperatur- und Feuchtigkeitsmessung werden angewandt, um sicherzustellen, dass das Produkt hohe Zuverlässigkeit und ausgezeichnete Langzeitstabilität aufweist.

Der Sensor beinhaltet einen resistiven Feuchtigkeitssensor und ein NTC-Temperaturmessgerät und ist mit einem leistungsstarken 8-Bit-Mikrocontroller verbunden.

.. Das Schaltbild des Feuchtigkeits- und Temperatursensormoduls wird wie folgt dargestellt: |img_Hum-sch| 

Nur drei Pins stehen zur Verfügung: VCC, GND und DATA.
Der Kommunikationsprozess beginnt damit, dass die DATA-Leitung Startsignale an den DHT11 sendet und der DHT11 die Signale empfängt und ein Antwortsignal zurücksendet.
Dann empfängt der Host das Antwortsignal und beginnt, 40-Bit-Feuchtigkeits- und Temperaturdaten zu empfangen (8-Bit Feuchtigkeit ganzzahlig + 8-Bit Feuchtigkeit dezimal + 8-Bit Temperatur ganzzahlig + 8-Bit Temperatur dezimal + 8-Bit Prüfsumme).

|img_Dht11|

**Merkmale**

    #. Feuchtigkeitsmessbereich: 20 - 90 %RH
    #. Temperaturmessbereich: 0 - 60℃
    #. Ausgabe digitaler Signale, die Temperatur und Feuchtigkeit anzeigen
    #. Betriebsspannung: DC 5V; PCB-Größe: 2,0 x 2,0 cm
    #. Genauigkeit der Feuchtigkeitsmessung: ±5 %RH
    #. Genauigkeit der Temperaturmessung: ±2℃


* `DHT11 Datasheet <http://wiki.sunfounder.cc/images/c/c7/DHT11_datasheet.pdf>`_

**Beispiel**

* :ref:`py_dht11` (For MicroPython User)
* :ref:`ar_dht11` (For Arduino User)