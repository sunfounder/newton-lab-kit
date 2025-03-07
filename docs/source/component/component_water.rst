.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_water_level:

Wasserstandssensor-Modul
=================================

|img_water_sensor|

Der Wasserstandssensor übermittelt das erfasste Wasserstandssignal an den Controller, und der Computer im Controller vergleicht das gemessene Wasserstandssignal mit dem eingestellten Signal, um die Abweichung abzuleiten. Anschließend erteilt er "Ein"- und "Aus"-Befehle an das Wasserzulaufventil, je nach Art der Abweichung, um sicherzustellen, dass das Gefäß den eingestellten Wasserstand erreicht.


Der Wasserstandssensor verfügt über zehn freiliegende Kupferspuren, fünf für die Stromspuren und fünf für die Sensorspuren, die bei Überflutung durch Wasser gekreuzt und überbrückt werden.
Die Platine hat eine Betriebs-LED, die aufleuchtet, wenn die Platine unter Strom steht.

Die Kombination dieser Spuren wirkt wie ein variabler Widerstand, der seinen Widerstandswert entsprechend dem Wasserstand ändert.
Um genauer zu sein, je mehr Wasser der Sensor eintaucht, desto besser die Leitfähigkeit und desto niedriger der Widerstand. Umgekehrt ist es weniger leitfähig und der Widerstand ist höher.
Anschließend verarbeitet der Sensor die Ausgangssignalspannung, die an den Mikrocontroller gesendet wird, was uns hilft, den Wasserstand zu bestimmen.


.. warning:: 
    Der Sensor darf nicht vollständig im Wasser untergetaucht werden, bitte lassen Sie nur den Teil, an dem sich die zehn Spuren befinden, mit Wasser in Kontakt kommen. Darüber hinaus beschleunigt das Einschalten des Sensors in feuchter Umgebung die Korrosion der Sonde und verkürzt die Lebensdauer des Sensors, daher empfehlen wir, ihn nur beim Ablesen mit Strom zu versorgen.


**Beispiel**

* :ref:`py_water` (For MicroPython User)
* :ref:`ar_water` (For Arduino User)
.. * :ref:`per_water_tank` (For Piper Make User)