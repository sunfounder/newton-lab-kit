.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_tilt:

Neigungsschalter
=============================

|img_tilt| 

Der hier verwendete Neigungsschalter ist ein Kugelschalter mit einer Metallkugel im Inneren. Er dient dazu, Neigungen eines kleinen Winkels zu erkennen.

Das Prinzip ist sehr einfach. Wenn der Schalter in einem bestimmten Winkel geneigt wird, rollt die Kugel nach unten und berührt die beiden mit den äußeren Pins verbundenen Kontakte, wodurch Schaltkreise ausgelöst werden. Andernfalls bleibt die Kugel von den Kontakten entfernt, wodurch die Schaltkreise unterbrochen werden.

|img_tilt_symbol|

* `SW520D Tilt Switch Datasheet <https://www.tme.com/Document/f1e6cedd8cb7feeb250b353b6213ec6c/SW-520D.pdf>`_

.. * :ref:`Reading Button Value`


**Beispiel**

* :ref:`py_tilt` (For MicroPython User)
* :ref:`py_10_second` (For MicroPython User)
* :ref:`ar_tilt` (For Arduino User)
.. * :ref:`per_flowing_leds` (For Piper Make User)