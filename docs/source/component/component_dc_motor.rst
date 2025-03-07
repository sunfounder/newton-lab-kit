.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_motor:

Gleichstrommotor
===================

|img_dc_motor|

Dies ist ein 3V Gleichstrommotor. Wenn Sie an jeden der beiden Anschlüsse ein hohes und ein niedriges Signal anlegen, dreht er sich.

* **Größe**: 25*20*15MM
* **Betriebsspannung**: 1-6V
* **Leerlaufstrom** (3V): 70mA
* **Leerlaufgeschwindigkeit** (3V): 13000 U/min
* **Blockierstrom** (3V): 800mA
* **Wellendurchmesser**: 2mm

Ein Gleichstrommotor ist ein kontinuierlicher Aktuator, der elektrische Energie in mechanische Energie umwandelt. Gleichstrommotoren ermöglichen das Funktionieren von rotierenden Pumpen, Ventilatoren, Kompressoren, Impellern und anderen Geräten durch die Erzeugung kontinuierlicher Drehbewegungen.

Ein Gleichstrommotor besteht aus zwei Teilen, dem festen Teil des Motors, genannt **Stator**, und dem internen Teil des Motors, genannt **Rotor** (oder **Anker** eines Gleichstrommotors), der sich dreht, um Bewegung zu erzeugen.
Der Schlüssel zur Bewegungserzeugung ist die Positionierung des Ankers innerhalb des Magnetfelds des Permanentmagneten (dessen Feld vom Nordpol zum Südpol reicht). Die Wechselwirkung des Magnetfelds und der bewegten geladenen Partikel (der stromführende Draht erzeugt das Magnetfeld) erzeugt das Drehmoment, das den Anker dreht.

|img_dc_motor_sche|

Der Strom fließt vom positiven Pol der Batterie durch den Stromkreis, über die Kupferbürsten zum Kommutator und dann zum Anker.
Aufgrund der beiden Lücken im Kommutator kehrt sich dieser Fluss jedoch in der Mitte jeder vollständigen Drehung um.
Diese kontinuierliche Umkehr wandelt die Gleichstromleistung der Batterie im Wesentlichen in Wechselstrom um, wodurch der Anker zum richtigen Zeitpunkt in die richtige Richtung Drehmoment erfährt, um die Drehung aufrechtzuerhalten.

* `DC Motor - MagLab <https://nationalmaglab.org/education/magnet-academy/watch-play/interactive/dc-motor>`_
* `Fleming's left-hand rule for motors - Wikipedia <https://en.wikipedia.org/wiki/Fleming%27s_left-hand_rule_for_motors>`_



**Beispiel**

* :ref:`py_motor` (For MicroPython User)
* :ref:`ar_motor` (For Arduino User)
.. * :ref:`per_smart_fan` (For Piper Make User)