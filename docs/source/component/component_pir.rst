.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_pir:

PIR-Bewegungssensormodul
==================================

|img_pir|

Der PIR-Sensor erkennt Infrarotwärmestrahlung, die genutzt werden kann, um die Anwesenheit von Organismen zu erkennen, die Infrarotwärme ausstrahlen.

Der PIR-Sensor ist in zwei Schlitze unterteilt, die mit einem Differenzverstärker verbunden sind. Wenn sich ein stationäres Objekt vor dem Sensor befindet, empfangen die beiden Schlitze die gleiche Menge an Strahlung, und der Ausgang ist null. Bewegt sich jedoch ein Objekt vor dem Sensor, erhält einer der Schlitze mehr Strahlung als der andere, was dazu führt, dass der Ausgang hoch oder niedrig schwankt. Diese Änderung der Ausgangsspannung ist ein Ergebnis der Bewegungserkennung.

|img_PIR_working_principle|

Nachdem das Sensormodul verkabelt ist, gibt es eine einminütige Initialisierung. Während der Initialisierung gibt das Modul 0-3 mal in Intervallen einen Ausgang. Danach befindet sich das Modul im Standby-Modus. Bitte halten Sie die Störung von Lichtquellen und anderen Quellen fern von der Oberfläche des Moduls, um eine Fehlfunktion durch das störende Signal zu vermeiden. Es ist sogar besser, das Modul ohne zu viel Wind zu verwenden, da der Wind ebenfalls den Sensor stören kann.

|img_pir_back|

**Entfernungsanpassung**

Durch Drehen des Knopfes des Entfernungsanpassungspotentiometers im Uhrzeigersinn erhöht sich der Bereich der Erfassungsentfernung, und die maximale Erfassungsdistanz beträgt etwa 0-7 Meter. Wenn man es gegen den Uhrzeigersinn dreht, verringert sich der Bereich der Erfassungsentfernung, und die minimale Erfassungsentfernung beträgt etwa 0-3 Meter.

**Verzögerungsanpassung**

Drehen Sie den Knopf des Verzögerungsanpassungspotentiometers im Uhrzeigersinn, können Sie auch sehen, dass die Erfassungsverzögerung zunimmt. Das Maximum der Erfassungsverzögerung kann bis zu 300s betragen. Im Gegenteil, wenn Sie es gegen den Uhrzeigersinn drehen, können Sie die Verzögerung verkürzen, mit einem Minimum von 5s. 

**Zwei Auslösemodi**

Wählen Sie unterschiedliche Modi durch Verwendung der Jumperkappe.

* **H**: Wiederholbarer Auslösemodus, nachdem der menschliche Körper erkannt wurde, gibt das Modul ein Hochsignal aus. Während der anschließenden Verzögerungszeit, wenn jemand den Erfassungsbereich betritt, bleibt der Ausgang auf hohem Niveau.
* **L**: Nicht wiederholbarer Auslösemodus, gibt ein Hochsignal aus, wenn der menschliche Körper erkannt wird. Nach der Verzögerung wechselt der Ausgang automatisch von Hoch- auf Niedrigniveau.

.. Beispiel 
.. -------------------

.. :ref:`Intruder Alarm`


**Beispiel**

* :ref:`py_pir` (For MicroPython User)
* :ref:`py_passage_counter` (For MicroPython User)
* :ref:`ar_pir` (For Arduino User)
.. * :ref:`per_lucky_cat` (For Piper Make User)