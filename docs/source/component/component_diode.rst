.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_diode:

Diode
=================

|img_diode|

Eine Diode ist ein elektronisches Bauelement mit zwei Elektroden, das Strom nur in eine Richtung fließen lässt, was oft als „Gleichrichter“-Funktion bezeichnet wird.
Somit kann eine Diode als elektronische Version eines Rückschlagventils betrachtet werden.

Die beiden Anschlüsse einer Diode sind polarisiert, wobei das positive Ende Anode und das negative Ende Kathode genannt wird.
Die Kathode ist gewöhnlich aus Silber oder hat einen farbigen Streifen.
Die Steuerung der Stromflussrichtung ist eine der Schlüsselfunktionen von Dioden — der Strom in einer Diode fließt von der Anode zur Kathode. Das Verhalten einer Diode ähnelt dem eines Rückschlagventils. Eine der wichtigsten Eigenschaften einer Diode ist die nichtlineare Strom-Spannungskennlinie. Wenn eine höhere Spannung an der Anode anliegt, fließt Strom von der Anode zur Kathode, was als Vorwärtsrichtung bekannt ist. Wird jedoch die höhere Spannung an die Kathode angelegt, leitet die Diode keinen Strom, was als Rückwärtsrichtung bezeichnet wird.

Aufgrund ihrer unidirektionalen Leitfähigkeit wird die Diode in fast allen elektronischen Schaltungen einiger Komplexität verwendet. Sie war eines der ersten Halbleiterbauelemente, das hergestellt wurde, und ihre Anwendungen sind weit verbreitet.

In Wirklichkeit zeigen Dioden jedoch keine solch perfekte Richtungsabhängigkeit, sondern eher komplexere nichtlineare elektronische Eigenschaften - die durch den spezifischen Diodentyp bestimmt werden.

Eine Diode ist ein p-n-Übergang, der aus einem p-Typ-Halbleiter und einem n-Typ-Halbleiter besteht, mit einer Raumladungszone auf beiden Seiten an der Schnittstelle und einem selbstgebauten elektrischen Feld, das im elektrischen Gleichgewicht ist, wenn keine äußere Spannung anliegt, da der Diffusionsstrom aufgrund des Unterschieds in der Ladungsträgerkonzentration zwischen den beiden Seiten des p-n-Übergangs und der Driftstrom aufgrund des selbstgebauten elektrischen Felds gleich sind. Wenn eine Vorwärtsspannung angelegt wird, erhöht die gegenseitige Unterdrückung des äußeren elektrischen Felds und des selbstgebauten elektrischen Felds den Diffusionsstrom der Ladungsträger, was den Vorwärtsstrom verursacht (das ist der Grund für die Leitfähigkeit). Wird eine Rückwärtsspannung erzeugt, werden das äußere elektrische Feld und das selbstgebaute elektrische Feld weiter verstärkt, um einen Rückwärtssättigungsstrom I0 in einem bestimmten Rückwärtsspannungsbereich zu bilden, unabhängig vom Wert der Rückwärtsspannung (was der Grund für die Nichtleitfähigkeit ist).
Wenn die angelegte Rückwärtsspannung einen bestimmten Wert erreicht, erreicht die elektrische Feldstärke in der Raumladungszone des p-n-Übergangs einen kritischen Wert, um einen Vermehrungsprozess von Ladungsträgern zu erzeugen, was zu einer großen Anzahl von Elektron-Loch-Paaren führt und einen großen Rückwärtsdurchbruchstrom erzeugt, bekannt als Durchbruchphänomen der Diode.

**1. Vorwärtscharakteristik**

Wenn die äußere Vorwärtsspannung angelegt wird, ist zu Beginn der Vorwärtscharakteristik die Vorwärtsspannung sehr klein, nicht ausreichend, um die Blockierwirkung des elektrischen Felds im p-n-Übergang zu überwinden, der Vorwärtsstrom ist fast null, dieser Abschnitt wird als Totzone bezeichnet.
Diese Vorwärtsspannung, die die Leitung der Diode nicht ermöglicht, wird als Totbandspannung bezeichnet. Wenn die Vorwärtsspannung größer als die Totbandspannung ist, wird das elektrische Feld des p-n-Übergangs überwunden, die Diode leitet vorwärts, der Strom steigt mit der Spannung und steigt schnell an.
Im normalen Nutzungsbereich des Stroms bleibt die Klemmenspannung der Diode während der Leitung nahezu konstant, diese Spannung wird als Vorwärtsspannung der Diode bezeichnet.

**2. Rückwärtscharakteristik**

Wenn die angelegte Rückwärtsspannung angelegt wird und einen bestimmten Bereich nicht überschreitet, ist der Strom durch die Diode ein paar Ladungsträger, die durch Driftbewegung eine Rückwärtsstrom bilden.
Da der Rückwärtsstrom sehr klein ist, ist die Diode im Sperrzustand. Dieser Rückwärtsstrom wird auch als Rückwärtssättigungsstrom oder Leckstrom bezeichnet und wird stark von der Temperatur beeinflusst.

**3. Durchbruch**

Wenn die angelegte Rückwärtsspannung einen bestimmten Wert überschreitet, steigt der Rückwärtsstrom plötzlich an, ein Phänomen, das als elektrischer Durchbruch bekannt ist.
Die kritische Spannung, die den elektrischen Durchbruch verursacht, wird als Rückwärtsdurchbruchspannung bezeichnet, die Diode verliert ihre unidirektionale Leitfähigkeit zum Zeitpunkt des elektrischen Durchbruchs.
Daher sollte die Verwendung der Diode vermieden werden, wenn die angelegte Rückwärtsspannung zu hoch ist.


Frühe Dioden bestanden aus „Katzenwhisker“-Kristallen und Vakuumröhren (auch „Thermionenventile“ genannt). Die meisten heutigen gängigen Dioden verwenden Halbleitermaterialien wie Silizium oder Germanium.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_
 
* `Diode - Wikipedia <https://en.wikipedia.org/wiki/Diode>`_


