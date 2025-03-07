.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_micro_switch:

Mikroschalter
========================

|img_micro_switch|

Der Aufbau eines Mikroschalters ist wirklich einfach. Die Hauptteile des Schalters sind:

|img_micro_switch2|

* 1. Stößel (Aktuator)
* 2. Abdeckung
* 3. Bewegliches Teil
* 4. Stütze
* 5. Gehäuse
* 6. NO-Kontakt: normalerweise offen
* 7. NC-Kontakt: normalerweise geschlossen
* 8. Kontakt
* 9. Bewegungsarm


Nachdem ein Mikroschalter physischen Kontakt mit einem Objekt hergestellt hat, ändern seine Kontakte die Position. Das grundlegende Arbeitsprinzip ist wie folgt.

Wenn der Stößel in der freigegebenen oder Ruheposition ist.

* Der normalerweise geschlossene Stromkreis kann Strom führen.
* Der normalerweise offene Stromkreis ist elektrisch isoliert.

Wenn der Stößel gedrückt oder umgeschaltet wird.

* Der normalerweise geschlossene Stromkreis ist geöffnet.
* Der normalerweise offene Stromkreis ist geschlossen.

|img_micro_switch1|

 **Beispiel**

* :ref:`py_micro` (For MicroPython User)
* :ref:`ar_micro` (For Arduino User)
.. * :ref:`per_service_bell` (For Piper Make User)