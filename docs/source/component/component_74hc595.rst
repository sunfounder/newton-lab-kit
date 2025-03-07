.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_74hc595:

74HC595
===========

|img_74hc595|

Der 74HC595 besteht aus einem 8-Bit-Schieberegister und einem Speicherregister mit dreizuständigen parallelen Ausgängen. Er wandelt serielle Eingaben in parallele Ausgaben um, sodass Sie IO-Ports eines MCUs einsparen können.

* Wenn MR (Pin10) auf hohem Pegel und OE (Pin13) auf niedrigem Pegel ist, werden Daten am ansteigenden Rand von SHcp eingegeben und gehen durch den ansteigenden Rand von SHcp ins Speicherregister über. 
* Wenn die beiden Uhren zusammengelegt werden, ist das Schieberegister immer einen Impuls früher als das Speicherregister. 
* Es gibt einen seriellen Schiebeeingangspin (Ds), einen seriellen Ausgangspin (Q) und eine asynchrone Zurücksetztaste (niedriger Pegel) im Speicherregister. 
* Das Speicherregister gibt einen Bus mit einem parallelen 8-Bit und in drei Zuständen aus. 
* Wenn OE aktiviert ist (niedriger Pegel), werden die Daten im Speicherregister auf den Bus (Q0 ~ Q7) ausgegeben.

* `74HC595 Datenblatt <https://www.ti.com/lit/ds/symlink/cd74hc595.pdf?ts=1617341564801>`_

|img_74jc595_pin|

Pins des 74HC595 und ihre Funktionen:

* **Q0-Q7**: 8-Bit parallele Datenausgänge, können direkt 8 LEDs oder 8 Pins einer 7-Segment-Anzeige steuern.
* **Q7'**: Serieller Ausgangspin, verbunden mit DS eines weiteren 74HC595, um mehrere 74HC595 in Serie zu verbinden
* **MR**: Zurücksetzpin, aktiv bei niedrigem Pegel;
* **SHcp**: Zeitsequenzeingang des Schieberegisters. Am ansteigenden Rand bewegen sich die Daten im Schieberegister sukzessive um ein Bit, d.h. Daten in Q1 bewegen sich zu Q2 und so weiter. Am abfallenden Rand bleiben die Daten im Schieberegister unverändert.
* **STcp**: Zeitsequenzeingang des Speicherregisters. Am ansteigenden Rand bewegen sich Daten im Schieberegister ins Speicherregister.
* **CE**: Ausgabefreigabepin, aktiv bei niedrigem Pegel.
* **DS**: Serieller Dateneingangspin
* **VCC**: Positive Versorgungsspannung.
* **GND**: Erdung.

.. Beispiel
.. -------------------

.. :ref:`Microchip - :ref:`cpn_74hc595``

**Beispiel**

* :ref:`py_74hc_led` (For MicroPython User)
* :ref:`py_74hc_7seg` (For MicroPython User)
* :ref:`py_74hc_4dig` (For MicroPython User)
* :ref:`py_74hc_788bs` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_74hc_led` (For Arduino User)
* :ref:`ar_74hc_7seg` (For Arduino User)
* :ref:`ar_74hc_4dig` (For Arduino User)
* :ref:`ar_74hc_788bs` (For Arduino User)