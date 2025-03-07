.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_relay:

Relais
==========================================

|img_relay|

Wie wir wissen, ist ein Relais ein Gerät, das verwendet wird, um eine Verbindung zwischen 
zwei oder mehr Punkten oder Geräten als Reaktion auf das angelegte Eingangssignal herzustellen. 
Mit anderen Worten, Relais bieten eine Isolierung zwischen dem Steuergerät und dem Gerät, da Geräte 
sowohl mit Wechselstrom als auch mit Gleichstrom arbeiten können. Sie erhalten jedoch Signale von 
einem Mikrocontroller, der mit Gleichstrom arbeitet, was ein Relais erfordert, um die Lücke zu überbrücken. 
Relais sind äußerst nützlich, wenn Sie eine große Menge Strom oder Spannung mit einem kleinen elektrischen Signal steuern müssen.


Ein Relais besteht aus 5 Teilen:

**Elektromagnet** - Besteht aus einem Eisenkern, der von Spulen
umwickelt ist. Wenn Strom hindurchfließt, wird er magnetisch.
Deshalb wird er Elektromagnet genannt.

**Anker** - Der bewegliche magnetische Streifen wird als Anker bezeichnet. Wenn
Strom durch sie fließt, wird die Spule aktiviert und erzeugt ein
magnetisches Feld, das verwendet wird, um die normalerweise offenen (N/O) oder
normalerweise geschlossenen (N/C) Punkte herzustellen oder zu unterbrechen. Und der Anker kann mit Gleichstrom (DC) sowie Wechselstrom (AC) bewegt werden.

**Feder** - Wenn kein Strom durch die Spule am
Elektromagnet fließt, zieht die Feder den Anker weg, sodass der Stromkreis nicht
geschlossen werden kann.

Satz elektrischer **Kontakte** - Es gibt zwei Kontaktstellen:

-  Normalerweise offen - verbunden, wenn das Relais aktiviert ist, und getrennt, wenn es inaktiv ist.

-  Normalerweise geschlossen - nicht verbunden, wenn das Relais aktiviert ist, und verbunden, wenn es inaktiv ist.

**Gehäuse** - Relais sind zum Schutz mit Kunststoff überzogen.

Das Funktionsprinzip des Relais ist einfach. Wenn Strom an das
Relais geliefert wird, beginnt der Strom durch die Steuerspule zu fließen; als Ergebnis
beginnt der Elektromagnet zu arbeiten. Dann wird der Anker von der
Spule angezogen, zieht den beweglichen Kontakt nach unten, der sich damit mit den
normalerweise offenen Kontakten verbindet. So wird der Stromkreis mit der Last aktiviert. Das Unterbrechen des Stromkreises wäre ähnlich, da der bewegliche Kontakt durch die Kraft der Feder zu den normalerweise geschlossenen Kontakten hochgezogen wird.
Auf diese Weise kann das Ein- und Ausschalten des Relais den Zustand
eines Laststromkreises steuern.

|img_relay_sche|


* `Relay - Wikipedia <https://en.wikipedia.org/wiki/Relay>`_

**Beispiel**


* :ref:`py_relay` (For MicroPython User)
* :ref:`ar_relay` (For Arduino User)