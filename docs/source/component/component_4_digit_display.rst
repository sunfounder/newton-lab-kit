.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_4_dit_7_segment:

4-stellige 7-Segment-Anzeige
==================================

Eine 4-stellige 7-Segment-Anzeige besteht aus vier zusammenarbeitenden 7-Segment-Anzeigen.

|img_4-digit-sche|

Die 4-stellige 7-Segment-Anzeige arbeitet unabhängig. Sie nutzt das Prinzip der visuellen Persistenz des menschlichen Auges, 
um die Zeichen jedes 7-Segmentes schnell hintereinander anzuzeigen und so fortlaufende Zeichenfolgen zu bilden.

Beispielsweise wird bei der Anzeige von „1234“ die „1“ im ersten 7-Segment dargestellt, 
während „234“ nicht angezeigt wird. Nach einer gewissen Zeit zeigt das zweite 7-Segment „2“, 
die ersten, dritten und vierten 7-Segmente zeigen nichts, und so weiter. Die Anzeige der vier 
Ziffern erfolgt nacheinander. Dieser Prozess ist sehr kurz (typischerweise 5ms), und aufgrund 
des optischen Nachleuchtens und des Prinzips des visuellen Nachbildes können wir vier Zeichen gleichzeitig sehen.

|img_4-digit-sche-ca|

**Anzeigecodes**

Um Ihnen zu zeigen, wie 7-Segment-Anzeigen (mit gemeinsamer Kathode) Zahlen darstellen, haben wir die folgende Tabelle erstellt. Zahlen sind die Zahlen 0-F, die auf der 7-Segment-Anzeige dargestellt werden; (DP) GFEDCBA bezieht sich auf die entsprechenden LEDs, die auf 0 oder 1 gesetzt werden, zum Beispiel bedeutet 00111111, dass DP und G auf 0 gesetzt sind, während die anderen auf 1 sind. Daher wird die Zahl 0 auf der 7-Segment-Anzeige angezeigt, während HEX-Code der entsprechenden Hexadezimalzahl entspricht.

.. list-table:: Glyphen-Code
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

**Beispiel**

* :ref:`py_74hc_4dig` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`py_traffic_light` (For MicroPython User)
* :ref:`ar_74hc_4dig` (For Arduino User)