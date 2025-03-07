.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_rgb:

RGB-LED
=================

|img_rgb|
    
RGB-LEDs emittieren Licht in verschiedenen Farben. Eine RGB-LED integriert drei LEDs in Rot, Grün und Blau in einer transparenten oder halbtransparenten Kunststoffhülle. Sie kann verschiedene Farben durch Veränderung der Eingangsspannung der drei Pins darstellen und diese überlagern, was statistisch gesehen 16.777.216 verschiedene Farben erzeugen kann.

|img_rgb_light|

RGB-LEDs können in gemeinsame Anode und gemeinsame Kathode unterteilt werden. In diesem Kit wird letztere verwendet. Die **gemeinsame Kathode**, oder CC, bedeutet, dass die Kathoden der drei LEDs verbunden sind. Wenn Sie sie mit GND verbinden und die drei Pins anschließen, wird die LED die entsprechende Farbe anzeigen.

Das Schaltsymbol wird wie folgt dargestellt.

|img_rgb_symbol| 

Eine RGB-LED hat 4 Pins: Der längste Pin ist der gemeinsame Kathodenpin, der üblicherweise mit GND verbunden wird, der linke Pin neben dem längsten Pin ist Rot, und die 2 Pins rechts sind Grün und Blau.

|img_rgb_pin|


**Merkmale**

* Farbe: Tri-Farbe (Rot/Grün/Blau)
* Gemeinsame Kathode
* 5mm klare, runde Linse
* Vorwärtsspannung: Rot: DC 2.0 - 2.2V; Blau&Grün: DC 3.0 - 3.2V (IF=20mA)
* 0,06 Watt DIP RGB LED
* Helligkeit bis zu +20% erhöht
* Betrachtungswinkel: 30°


.. Beispiel
.. -------------------

.. :ref:`Colorful Light`


**Beispiel**

* :ref:`py_rgb` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`ar_rgb` (For Arduino User)
.. * :ref:`per_rainbow_light` (For Piper Make User)