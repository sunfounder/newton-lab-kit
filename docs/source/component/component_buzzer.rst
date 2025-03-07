.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_buzzer:

Summer
=======


Als eine Art elektronischer Summer mit integrierter Struktur werden Summer, die von Gleichstrom versorgt werden, weit verbreitet in Computern, Druckern, Kopiergeräten, Alarmen, elektronischen Spielzeugen, Kfz-Elektronik, Telefonen, Timern und anderen elektronischen Produkten oder Sprachgeräten eingesetzt.

Summer können als aktiv und passiv kategorisiert werden (siehe folgendes Bild). Drehen Sie den Summer so, dass seine Pins nach oben zeigen, und der Summer mit einer grünen Platine ist ein passiver Summer, während der mit einem schwarzen Band umschlossene ein aktiver Summer ist.

|img_buzzer|

Der Unterschied zwischen einem aktiven und einem passiven Summer: 

Ein aktiver Summer hat eine eingebaute Oszillationsquelle und macht Geräusche, wenn er unter Strom steht. Ein passiver Summer hat jedoch keine solche Quelle, sodass er nicht piept, wenn Gleichstromsignale verwendet werden; stattdessen benötigen Sie zum Antrieb Rechteckwellen mit einer Frequenz zwischen 2K und 5K. Der aktive Summer ist oft teurer als der passive wegen der mehrfachen eingebauten Oszillierungsschaltungen.

Folgendes ist das elektrische Symbol eines Summers. Er hat zwei Pins mit positiven und negativen Polen. Ein + auf der Oberfläche repräsentiert den Anodenpol und der andere den Kathodenpol.

|img_buzzer_symbol|

Sie können die Pins des Summers überprüfen, der längere ist der Anodenpol und der kürzere der Kathodenpol. Bitte verwechseln Sie diese nicht beim Anschließen, sonst macht der Summer keinen Ton.

`Buzzer - Wikipedia <https://en.wikipedia.org/wiki/Buzzer>`_

.. Beispiel
.. -------------------

.. :ref:`Intruder Alarm`

.. :ref:`Custom Tone`

**Beispiel**

* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)