.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspiele und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_led:

LED
==========

|img_led|

Die Halbleiter-Leuchtdiode, auch bekannt als LED (Light-Emitting Diode), ist eine Komponente, die elektrische Energie mittels PN-Übergängen in Lichtenergie umwandelt. Nach der Wellenlänge kann sie in Laserdiode, Infrarot-Leuchtdiode und sichtbare Leuchtdiode unterteilt werden, die üblicherweise einfach als LED bezeichnet wird.

Die Diode hat eine unidirektionale Leitfähigkeit, sodass der Stromfluss wie im Schaltsymbol dargestellt verläuft. Man sollte der Anode positives und der Kathode negatives Potential zuführen, damit die LED leuchtet.

|img_led_symbol|

Eine LED hat zwei Pins. Der längere ist die Anode und der kürzere die Kathode. Achten Sie darauf, sie nicht verkehrt herum anzuschließen. LEDs haben einen festen Vorwärtsspannungsabfall, daher können sie nicht direkt mit dem Stromkreis verbunden werden, da die Versorgungsspannung diesen Spannungsabfall überschreiten und die LED verbrennen könnte. Die Vorwärtsspannung der roten, gelben und grünen LED beträgt 1,8 V und die der weißen 2,6 V. Die meisten LEDs können einen maximalen Strom von 20 mA aushalten, daher ist es notwendig, einen Strombegrenzungswiderstand in Serie zu schalten.

Die Formel für den Widerstandswert lautet wie folgt:

    R = (Vsupply – VD)/I

**R** steht für den Widerstandswert des Strombegrenzungswiderstands, **Vsupply** für die Versorgungsspannung, **VD** für den Spannungsabfall und **I** für den Arbeitsstrom der LED.

Hier ist die detaillierte Einführung für die LED: `LED - Wikipedia <https://en.wikipedia.org/wiki/Light-emitting_diode>`_.

.. **Example**

.. * :ref:`Hello, Breadboard!` (For MicroPython User)
.. * :ref:`fading_led_micropython` (For MicroPython User)
.. * :ref:`fading_led_arduino` (For C/C++(Arduino) User)
.. * :ref:`hello_led_arduino` (For C/C++(Arduino) User)


**Beispiel**

* :ref:`py_led` (For MicroPython User)
* :ref:`py_fade` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_led` (For Arduino User)
* :ref:`ar_fade` (For Arduino User)
.. * :ref:`per_blink` (For Piper Make User)
.. * :ref:`per_button` (For Piper Make User)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)