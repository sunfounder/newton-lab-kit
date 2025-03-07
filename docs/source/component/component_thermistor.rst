.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_thermistor:

Thermistor
===============

|img_thermistor|

Ein Thermistor ist ein Typ von Widerstand, dessen Widerstand stark temperaturabhängig ist, mehr als bei Standardwiderständen. Der Begriff ist eine Kombination aus "thermal" und "resistor". Thermistoren werden häufig als Einschaltstrombegrenzer, Temperatursensoren (typischerweise vom Typ mit negativem Temperaturkoeffizienten oder NTC), selbst rückstellende Überstromschutzgeräte und selbstregulierende Heizelemente (typischerweise vom Typ mit positivem Temperaturkoeffizienten oder PTC) verwendet.

* `Thermistor - Wikipedia <https://en.wikipedia.org/wiki/Thermistor>`_

Hier ist das elektronische Symbol eines Thermistors.

|img_thermistor_symbol|

Es gibt zwei grundlegende Arten von Thermistoren:

* Bei NTC-Thermistoren nimmt der Widerstand mit steigender Temperatur ab, meist aufgrund einer Zunahme von Leitungselektronen, die durch thermische Anregung aus dem Valenzband gestoßen werden. Ein NTC wird üblicherweise als Temperatursensor verwendet oder in Serie mit einem Schaltkreis als Einschaltstrombegrenzer eingesetzt.
* Bei PTC-Thermistoren steigt der Widerstand mit zunehmender Temperatur, meist aufgrund erhöhter thermischer Gitterschwingungen, insbesondere jener von Verunreinigungen und Unregelmäßigkeiten. PTC-Thermistoren werden häufig in Serie mit einem Schaltkreis installiert und dienen als rückstellbare Sicherungen zum Schutz gegen Überstrombedingungen.

In diesem Kit verwenden wir einen NTC. Jeder Thermistor hat einen Normalwiderstand. Hier beträgt er 10k Ohm, gemessen bei 25 Grad Celsius.

Hier ist die Beziehung zwischen Widerstand und Temperatur:

    RT = RN * expB(1/TK - 1/TN)   

* **RT** ist der Widerstand des NTC-Thermistors bei der Temperatur TK. 
* **RN** ist der Widerstand des NTC-Thermistors bei der Nenntemperatur TN. Hier beträgt der numerische Wert von RN 10k.
* **TK** ist eine Kelvin-Temperatur und die Einheit ist K. Hier beträgt der numerische Wert von TK 273,15 + Grad Celsius.
* **TN** ist eine Nenn-Kelvin-Temperatur; die Einheit ist ebenfalls K. Hier beträgt der numerische Wert von TN 273,15+25.
* Und **B(beta)**, die Materialkonstante des NTC-Thermistors, wird auch als Hitzeempfindlichkeitsindex bezeichnet mit einem numerischen Wert von 3950.      
* **exp** ist die Abkürzung für Exponential, und die Basiszahl e ist eine natürliche Zahl und beträgt ungefähr 2,7.  

Diese Formel TK=1/(ln(RT/RN)/B+1/TN) wird umgewandelt, um die Kelvin-Temperatur zu erhalten, die minus 273,15 Grad Celsius entspricht.

Diese Beziehung ist eine empirische Formel. Sie ist nur genau, wenn die Temperatur und der Widerstand innerhalb des effektiven Bereichs liegen.

.. Beispiel
.. -------------------

.. :ref:`Thermometer`


**Beispiel**

* :ref:`py_temp` (For MicroPython User)
* :ref:`py_room_temp` (For MicroPython User)
* :ref:`ar_temp` (For Arduino User)