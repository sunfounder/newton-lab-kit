.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_joystick:

Joystick-Modul
=======================

|img_joystick_pic|

Die Grundidee eines Joysticks besteht darin, die Bewegung eines Sticks in elektronische Informationen umzusetzen, die ein Computer verarbeiten kann.

Um einem Computer eine vollständige Bewegungspalette mitzuteilen, 
muss ein Joystick die Position des Sticks auf zwei Achsen messen – der X-Achse (links nach rechts) und der Y-Achse (oben nach unten).
Wie in der Grundgeometrie geben die X-Y-Koordinaten genau die Position des Sticks an.

Um den Standort des Sticks zu bestimmen, überwacht das Joystick-Steuerungssystem einfach die Position jeder Achse.
Das herkömmliche analoge Joystick-Design macht dies mit zwei Potentiometern oder variablen Widerständen.

Der Joystick verfügt auch über einen digitalen Eingang, der betätigt wird, wenn der Joystick nach unten gedrückt wird.

|img_joystick|


*  `Joystick - Wikipedia <https://en.wikipedia.org/wiki/Analog_stick>`_


**Beispiel**


* :ref:`py_joystick` (For MicroPython User)
* :ref:`ar_joystick` (For Arduino User)