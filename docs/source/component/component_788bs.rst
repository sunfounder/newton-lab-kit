.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_dot_matrix:

LED-Punktmatrix
==========================

|img_led_matrix|

Generell gibt es zwei Arten von LED-Punktmatrizen: gemeinsame Kathode (Common Cathode, CC) 
und gemeinsame Anode (Common Anode, CA). Sie sehen sich sehr ähnlich, unterscheiden sich jedoch intern. 
Man kann dies durch Tests feststellen. In diesem Kit wird eine CA-Variante verwendet. 
Sie können die Beschriftung 788BS an der Seite sehen.

Siehe die Abbildung unten. Die Pins sind an den beiden Enden auf der Rückseite angeordnet. 
Nehmen Sie die beschriftete Seite als Referenz: Pins an diesem Ende sind Pin 1-8, und am 
anderen Ende sind es Pin 9-16.

Die externe Ansicht:

|img_788bs_i|


Unten zeigen die Abbildungen ihre interne Struktur. In einer CA-LED-Punktmatrix repräsentiert ROW 
die Anode der LED und COL ist die Kathode; bei einer CC ist es umgekehrt. Eine Gemeinsamkeit besteht 
darin, dass für beide Typen die Pins 13, 3, 4, 10, 6, 11, 15 und 16 alle COL sind, während Pin 9, 14, 8, 12, 1, 7, 2 und 5 alle ROW sind. 
Wenn Sie die erste LED in der oberen linken Ecke einschalten möchten, setzen Sie bei einer CA-LED-Punktmatrix Pin 9 auf Hoch und Pin 13 auf Niedrig, 
und bei einer CC setzen Sie Pin 13 auf Hoch und Pin 9 auf Niedrig. Wenn Sie die gesamte erste Spalte beleuchten möchten, setzen Sie bei CA Pin 13 auf 
Niedrig und die ROW 9, 14, 8, 12, 1, 7, 2 und 5 auf Hoch, bei CC setzen Sie Pin 13 auf Hoch und die ROW 9, 14, 8, 12, 1, 7, 2 und 5 auf Niedrig. 
Betrachten Sie die folgenden Abbildungen für ein besseres Verständnis.

Die interne Ansicht:

|img_788bs_sche|

Pinnummerierung entsprechend den oben genannten Reihen und Spalten:

=========== ====== ====== ===== ====== ===== ====== ====== ======
**COL**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **13** **3**  **4** **10** **6** **11** **15** **16**
**ROW**     **1**  **2**  **3** **4**  **5** **6**  **7**  **8**
**Pin No.** **9**  **14** **8** **12** **1** **7**  **2**  **5**
=========== ====== ====== ===== ====== ===== ====== ====== ======

Zusätzlich werden hier zwei 74HC595-Chips verwendet. Einer steuert die Reihen der LED-Punktmatrix, 
der andere die Spalten.


**Beispiel**

* :ref:`py_74hc_788bs` (For MicroPython User)
* :ref:`py_bubble_level` (For MicroPython User)
* :ref:`ar_74hc_788bs` (For Arduino User)