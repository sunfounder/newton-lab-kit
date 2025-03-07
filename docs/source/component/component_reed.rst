.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_reed:

Reedschalter
======================

|img_reed|

Der Reedschalter ist ein elektrischer Schalter, der durch ein angelegtes Magnetfeld betätigt wird. Er wurde 1936 von Walter B. Ellwood von den Bell Telephone Laboratories erfunden und am 27. Juni 1940 in den Vereinigten Staaten unter der Patentnummer 2264746 patentiert.

Das Funktionsprinzip eines Reedschalters ist sehr einfach. Zwei Reedkontakte (üblicherweise aus Eisen und Nickel, zwei Metallen) überlappen sich an den Endpunkten und sind in einem Glasröhrchen versiegelt, wobei die beiden Reeds sich überlappen und durch einen kleinen Spalt (nur etwa einige Mikrometer) getrennt sind. Das Glasröhrchen ist mit einem hochreinen inerten Gas (wie Stickstoff) gefüllt, und einige Reedschalter sind so hergestellt, dass sie im Inneren ein Vakuum haben, um ihre Hochspannungsleistung zu verbessern.

Das Reed dient als magnetischer Flussleiter. Die beiden Reeds sind im Ruhezustand nicht in Kontakt; wenn sie durch ein Magnetfeld, das von einem Permanentmagneten oder einer Elektromagnetspule erzeugt wird, durchlaufen, verursacht das angelegte Magnetfeld, dass die beiden Reeds nahe ihrer Endpunkte unterschiedliche Polaritäten aufweisen, und wenn die magnetische Kraft die Federkraft der Reeds selbst übersteigt, werden die beiden Reeds zusammengezogen, um den Stromkreis zu schließen; wenn das Magnetfeld abschwächt oder verschwindet, werden die Reeds durch ihre eigene Elastizität freigegeben, und die Kontaktflächen trennen sich, um den Stromkreis zu öffnen.

|img_reed_sche|

* `Reed Switch - Wikipedia <https://en.wikipedia.org/wiki/Reed_switch>`_



**Beispiel**

* :ref:`py_reed` (For MicroPython User)
* :ref:`ar_reed` (For Arduino User)