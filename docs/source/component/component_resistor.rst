.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_resistor:

Widerstand
============

|img_res|

Ein Widerstand ist ein elektronisches Element, das den Strom in einem Zweig begrenzen kann.
Ein Festwiderstand ist eine Art Widerstand, dessen Widerstandswert nicht verändert werden kann, während der eines Potentiometers oder eines variablen Widerstands eingestellt werden kann.

Es gibt zwei allgemein verwendete Schaltsymbole für Widerstände. Normalerweise ist der Widerstandswert darauf markiert. Wenn Sie diese Symbole in einer Schaltung sehen, steht dies für einen Widerstand.

|img_res_symbol|

**Ω** ist die Einheit des Widerstands und die größeren Einheiten umfassen KΩ, MΩ usw.
Ihre Beziehung kann wie folgt dargestellt werden: 1 MΩ = 1000 KΩ, 1 KΩ = 1000 Ω. Normalerweise ist der Wert des Widerstands darauf markiert.

Wenn Sie einen Widerstand verwenden, müssen Sie zuerst seinen Widerstand kennen. Hier sind zwei Methoden: Sie können die Bänder auf dem Widerstand beobachten oder ein Multimeter verwenden, um den Widerstand zu messen. Es wird empfohlen, die erste Methode zu verwenden, da sie bequemer und schneller ist.

|img_res_card|

Wie auf der Karte gezeigt, steht jede Farbe für eine Zahl.

.. list-table::

   * - Schwarz
     - Braun
     - Rot
     - Orange
     - Gelb
     - Grün
     - Blau
     - Violett
     - Grau
     - Weiß
     - Gold
     - Silber
   * - 0
     - 1
     - 2
     - 3
     - 4
     - 5
     - 6
     - 7
     - 8
     - 9
     - 0.1
     - 0.01

Häufig verwendet werden 4- und 5-Band-Widerstände, auf denen 4 bzw. 5 farbige Bänder zu sehen sind.

Normalerweise, wenn Sie einen Widerstand erhalten, kann es schwierig sein zu entscheiden, an welchem Ende Sie mit dem Lesen der Farbe beginnen sollen.
Der Tipp ist, dass der Abstand zwischen dem 4. und 5. Band vergleichsweise größer ist.

Daher können Sie den Abstand zwischen den beiden farbigen Bändern an einem Ende des Widerstands beobachten;
wenn er größer ist als jeder andere Bandabstand, dann können Sie von der gegenüberliegenden Seite lesen.

Sehen wir uns an, wie der Widerstandswert eines 5-Band-Widerstands wie unten gezeigt gelesen wird.

|img_220ohm|

Für diesen Widerstand sollte der Widerstandswert von links nach rechts gelesen werden.
Der Wert sollte in diesem Format sein: 1. Band 2. Band 3. Band x 10^Multiplier (Ω) und der zulässige Fehler beträgt ±Toleranz%.
Der Widerstandswert dieses Widerstands beträgt 2(rot) 2(rot) 0(schwarz) x 10^0(schwarz) Ω = 220 Ω,
und der zulässige Fehler beträgt ± 1 % (braun).

.. list-table:: Common resistor color band
    :header-rows: 1

    * - :ref:`cpn_resistor` 
      - Farbband  
    * - 10Ω   
      - braun schwarz schwarz silber braun
    * - 100Ω   
      - braun schwarz schwarz schwarz braun
    * - 220Ω 
      - rot rot schwarz schwarz braun
    * - 330Ω 
      - orange orange schwarz schwarz braun
    * - 1kΩ 
      - braun schwarz schwarz braun braun
    * - 2kΩ 
      - rot schwarz schwarz braun braun
    * - 5.1kΩ 
      - grün braun schwarz braun braun
    * - 10kΩ 
      - braun schwarz schwarz rot braun 
    * - 100kΩ 
      - braun schwarz schwarz orange braun 
    * - 1MΩ 
      - braun schwarz schwarz grün braun 

Sie können mehr über Widerstände auf Wiki lernen: `Resistor - Wikipedia <https://en.wikipedia.org/wiki/Resistor>`_.
