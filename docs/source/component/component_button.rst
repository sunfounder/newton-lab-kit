.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_button:

Taster
==========

|img_button|

Taster sind eine gängige Komponente zur Steuerung elektronischer Geräte. Sie werden üblicherweise als Schalter verwendet, um Stromkreise zu schließen oder zu öffnen. Obwohl Taster in verschiedenen Größen und Formen erhältlich sind, wird hier ein 6-mm-Mini-Taster verwendet, wie in den folgenden Bildern gezeigt.
Pin 1 ist mit Pin 2 verbunden und Pin 3 mit Pin 4. Sie müssen also nur entweder Pin 1 mit Pin 3 oder Pin 2 mit Pin 4 verbinden.

Folgendes ist die interne Struktur eines Tasters. Das Symbol rechts unten wird üblicherweise verwendet, um einen Taster in Schaltkreisen darzustellen.

|img_button_symbol|

Da Pin 1 mit Pin 2 und Pin 3 mit Pin 4 verbunden ist, werden beim Drücken des Tasters die 4 Pins verbunden, wodurch der Stromkreis geschlossen wird.

|img_button2|



**Beispiel**

* :ref:`py_button` (For MicroPython User)
* :ref:`ar_button` (For Arduino User)
.. * :ref:`per_button` (For Piper Make User)
.. * :ref:`per_rainbow_light` (For Piper Make User)
.. * :ref:`per_drum_kit` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)