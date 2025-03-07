.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ws2812:

WS2812 RGB 8-LED-Streifen
============================

|img_ws2812|

Der WS2812 RGB 8-LED-Streifen besteht aus 8 RGB-LEDs. 
Es wird nur ein einziger Pin benötigt, um alle LEDs zu steuern. Jede RGB-LED verfügt über einen WS2812-Chip, der unabhängig gesteuert werden kann. 
Er ermöglicht eine 256-stufige Helligkeitsdarstellung und eine vollständige Echtfarbdarstellung mit 16.777.216 Farben. 
Gleichzeitig enthält jeder Pixelpunkt eine intelligente digitale Schnittstelle mit Datenlatch-Signalformung und Verstärker-Treiber-Schaltung. 
Ein integrierter Signalformungsschaltkreis stellt sicher, dass die Farbhelligkeit jedes einzelnen Pixelpunkts gleichmäßig bleibt.

Der Streifen ist flexibel, kann verbunden, gebogen und nach Belieben zugeschnitten werden. 
Auf der Rückseite befindet sich ein Klebestreifen, der eine einfache Befestigung auf unebenen Oberflächen ermöglicht. Dadurch ist er auch für enge Räume geeignet.

**Merkmale**

* Betriebsspannung: DC5V
* IC: Ein IC steuert eine RGB-LED
* Stromverbrauch: 0,3 W pro LED
* Betriebstemperatur: -15°C bis 50°C
* Farbe: Vollfarbig RGB
* RGB-Typ: 5050RGB (integrierter IC WS2812B)
* Dicke des LED-Streifens: 2 mm
* Jede LED kann individuell gesteuert werden

**WS2812B Einführung**

* `WS2812B Datenblatt <https://cdn-shop.adafruit.com/datasheets/WS2812B.pdf>`_

WS2812B ist eine intelligente LED-Lichtquelle, bei der die Steuerungsschaltung und der RGB-Chip in einem 5050-Gehäuse integriert sind. 
Intern umfasst sie eine intelligente digitale Datenlatch-Schnittstelle, eine Signalformung mit Verstärkerschaltung sowie einen hochpräzisen internen Oszillator. 
Zudem besitzt sie eine programmierbare Konstantstromquelle für eine stabile 12V-Spannungsregelung, die für gleichmäßige Farbhelligkeit sorgt.

Das Datenübertragungsprotokoll verwendet einen einzelnen NZR-Kommunikationsmodus. Nach dem Einschalten empfängt der DIN-Port die Daten vom Controller. 
Das erste Pixel sammelt die ersten 24-Bit-Daten und speichert sie intern. Alle weiteren Daten werden durch den internen Signalverstärker aufbereitet und über den DO-Port an das nächste Pixel weitergeleitet. 
Nach jeder Pixelübertragung reduziert sich das Signal um 24 Bit. Dank der automatischen Signalverstärkung gibt es praktisch keine Begrenzung für die Anzahl der in Reihe geschalteten Pixel – sie hängt nur von der Übertragungsgeschwindigkeit des Signals ab.

Diese LEDs zeichnen sich durch ihre niedrige Betriebsspannung, Umweltfreundlichkeit, Energieeinsparung, hohe Helligkeit, einen breiten Abstrahlwinkel, niedrigen Stromverbrauch, lange Lebensdauer und einfache Installation aus. 
Durch die Integration des Steuerchips direkt in die LED wird die Schaltung weiter vereinfacht.

**Beispiel**

* :ref:`py_neopixel` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`ar_neopixel` (For Arduino User)
.. * :ref:`per_flowing_leds` (For Piper Make User)