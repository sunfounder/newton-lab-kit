.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_l293d:

IC L293D 
=================

|img_l293d0|

Der L293D ist ein 4-Kanal-Motortreiber-IC, der für hohe Spannungen und hohe Ströme ausgelegt ist.
Er ist konzipiert für den Anschluss an Standard-DTL-, TTL-Logikpegel und zum Ansteuern induktiver Lasten (wie Relaisspulen, Gleichstrom-, Schrittmotoren) und Leistungsschalttransistoren usw.
Gleichstrommotoren sind Geräte, die Gleichstromenergie in mechanische Energie umwandeln. Sie werden häufig in elektrischen Antrieben eingesetzt, da sie eine überlegene Geschwindigkeitsregulierungsleistung bieten.

Siehe die Pin-Abbildung unten. Der L293D hat zwei Pins (Vcc1 und Vcc2) zur Stromversorgung.
Vcc2 dient zur Stromversorgung des Motors, während Vcc1 den Chip versorgt. Da hier ein kleiner Gleichstrommotor verwendet wird, verbinden Sie beide Pins mit +5V.

|img_l293d1| 

Folgend ist die interne Struktur des L293D.
Pin EN ist ein Enable-Pin und funktioniert nur auf hohem Niveau; A steht für Eingang und Y für Ausgang.
Unten rechts sehen Sie die Beziehung zwischen ihnen.
Wenn Pin EN auf hohem Niveau ist, liefert Y bei hohem A ein hohes Niveau; bei niedrigem A gibt Y ein niedriges Niveau aus. Wenn Pin EN auf niedrigem Niveau ist, funktioniert der L293D nicht.

|img_l293d2|

* `L293D Datasheet <https://cdn-shop.adafruit.com/datasheets/l293d.pdf>`_

**Beispiel**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
* :ref:`py_pump` (For MicroPython User)
* :ref:`ar_pump` (For Arduino User)
.. * :ref:`per_smart_fan` (For Piper Make User)