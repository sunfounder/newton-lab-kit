.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_potentiometer:

Potentiometer
===============

|img_pot|

Ein Potentiometer ist ebenfalls ein Widerstandsbauteil mit 3 Anschlüssen, dessen Widerstandswert entsprechend einer bestimmten Regelung angepasst werden kann.

Potentiometer gibt es in verschiedenen Formen, Größen und Werten, aber sie haben alle folgende Gemeinsamkeiten:

* Sie haben drei Anschlüsse (oder Anschlusspunkte).
* Sie haben einen Drehknopf, eine Schraube oder einen Schieberegler, der bewegt werden kann, um den Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse zu variieren.
* Der Widerstand zwischen dem mittleren Anschluss und einem der äußeren Anschlüsse variiert von 0 Ω bis zum maximalen Widerstand des Potentiometers, wenn der Drehknopf, die Schraube oder der Schieberegler bewegt wird.

Hier ist das Schaltsymbol des Potentiometers.

|img_pot_symbol|


Die Funktionen des Potentiometers in der Schaltung sind wie folgt:

#. Als Spannungsteiler

    Das Potentiometer ist ein kontinuierlich einstellbarer Widerstand. Wenn Sie die Welle oder den Schiebegriff des Potentiometers verstellen, rutscht der bewegliche Kontakt über den Widerstand. In diesem Moment kann eine Spannung ausgegeben werden, abhängig von der an das Potentiometer angelegten Spannung und dem Winkel, um den der bewegliche Arm gedreht wurde, oder der zurückgelegten Strecke.

#. Als Rheostat

    Wenn das Potentiometer als Rheostat verwendet wird, verbinden Sie den mittleren Pin und einen der anderen beiden Pins im Schaltkreis. So erhalten Sie einen gleichmäßig und kontinuierlich veränderten Widerstandswert innerhalb des Weges des beweglichen Kontakts.

#. Als Stromregler

    Wenn das Potentiometer als Stromregler wirkt, muss der Schleifkontakt als einer der Ausgangsanschlüsse verbunden werden.

Wenn Sie mehr über Potentiometer erfahren möchten, siehe: `Potentiometer - Wikipedia <https://en.wikipedia.org/wiki/Potentiometer>`_

.. Beispiel
.. -------------------

.. * :ref:`Turn the Knob` (For MicroPython User)
.. * :ref:`Table Lamp` (For C/C++(Arduino) User)


**Beispiel**

* :ref:`py_pot` (For MicroPython User)
* :ref:`ar_pot` (For Arduino User)
.. * :ref:`per_swing_servo` (For Piper Make User)