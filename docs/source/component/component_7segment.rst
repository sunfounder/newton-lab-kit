.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_7_segment:

7-Segment-Anzeige
======================

|img_7seg|


Eine 7-Segment-Anzeige ist eine Komponente in der Form einer 8, die 7 LEDs umfasst. Jede LED wird als Segment bezeichnet - wenn sie aktiviert wird, bildet ein Segment einen Teil einer Zahl, die angezeigt werden soll.

Es gibt zwei Arten von Pin-Verbindungen: Gemeinsame Kathode (Common Cathode, CC) und Gemeinsame Anode (Common Anode, CA). Wie der Name schon sagt, sind bei einer CC-Anzeige alle Kathoden der 7 LEDs verbunden, während bei einer CA-Anzeige alle Anoden der 7 Segmente verbunden sind.

In diesem Kit verwenden wir die 7-Segment-Anzeige mit gemeinsamer Kathode, hier ist das elektronische Symbol.

|img_7seg_cathode|

Jede der LEDs in der Anzeige hat ein positioniertes Segment, wobei einer der Anschlusspins aus dem rechteckigen Kunststoffgehäuse herausgeführt wird. Diese LED-Pins sind von „a“ bis „g“ gekennzeichnet und repräsentieren jede einzelne LED. Die anderen LED-Pins sind miteinander verbunden und bilden einen gemeinsamen Pin. Indem die entsprechenden Pins der LED-Segmente in einer bestimmten Reihenfolge in Vorwärtsrichtung vorgespannt werden, leuchten einige Segmente auf, während andere dunkel bleiben, wodurch der entsprechende Charakter auf der Anzeige dargestellt wird.


* `Seven-segment Display - Wikipedia <https://en.wikipedia.org/wiki/Seven-segment_display>`_

**Anzeigecodes** 

Um Ihnen zu zeigen, wie 7-Segment-Anzeigen (mit gemeinsamer Kathode) Zahlen darstellen, haben wir die folgende Tabelle erstellt. Zahlen sind die Zahlen 0-F, die auf der 7-Segment-Anzeige dargestellt werden; (DP) GFEDCBA bezieht sich auf die entsprechenden LEDs, die auf 0 oder 1 gesetzt werden, zum Beispiel bedeutet 00111111, dass DP und G auf 0 gesetzt sind, während die anderen auf 1 sind. Daher wird die Zahl 0 auf der 7-Segment-Anzeige angezeigt, während HEX-Code der entsprechenden Hexadezimalzahl entspricht.

.. list-table:: Glyph Code
    :widths: 20 20 20
    :header-rows: 1

    *   - Zahlen	
        - Binärcode
        - Hex-Code  
    *   - 0	
        - 00111111	
        - 0x3f
    *   - 1	
        - 00000110	
        - 0x06
    *   - 2	
        - 01011011	
        - 0x5b
    *   - 3	
        - 01001111	
        - 0x4f
    *   - 4	
        - 01100110	
        - 0x66
    *   - 5	
        - 01101101	
        - 0x6d
    *   - 6	
        - 01111101	
        - 0x7d
    *   - 7	
        - 00000111	
        - 0x07
    *   - 8	
        - 01111111	
        - 0x7f
    *   - 9	
        - 01101111	
        - 0x6f
    *   - A	
        - 01110111	
        - 0x77
    *   - B
        - 01111100	
        - 0x7c
    *   - C	
        - 00111001	
        - 0x39
    *   - D	
        - 01011110	
        - 0x5e
    *   - E	
        - 01111001	
        - 0x79
    *   - F	
        - 01110001	
        - 0x71

.. Beispiel
.. -------------------

.. :ref:`LED-Segmentanzeige`


**Beispiel**

* :ref:`py_74hc_7seg` (For MicroPython User)
* :ref:`ar_74hc_7seg` (For Arduino User)