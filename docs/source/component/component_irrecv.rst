.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_ir_receiver:

Infrarot-Empfänger
=================================

IR-Empfänger
----------------------------

|img_irrecv|

* S: Signalausgang
* +: VCC
* -: GND

Ein Infrarot-Empfänger ist eine Komponente, die Infrarotsignale empfängt und unabhängig Infrarotstrahlen empfangen und Signale ausgeben kann, die mit TTL-Niveau kompatibel sind. Er ähnelt in Größe einem normal verpackten Transistor und eignet sich für alle Arten von Infrarot-Fernbedienungen und Infrarot-Übertragungen.

Infrarotkommunikation, oder IR-Kommunikation, ist eine beliebte, kostengünstige und einfach zu verwendende drahtlose Kommunikationstechnologie. Infrarotlicht hat eine etwas längere Wellenlänge als sichtbares Licht, daher ist es für das menschliche Auge unsichtbar - ideal für drahtlose Kommunikation. Ein gängiges Modulationsschema für die Infrarotkommunikation ist die 38KHz-Modulation.

* Verwendet HX1838 IR-Empfängersensor, hohe Sensitivität
* Kann für Fernbedienungen verwendet werden
* Stromversorgung: 3.3~5V
* Schnittstelle: Digital
* Modulationsfrequenz: 38Khz


Fernbedienung
-------------------------

|img_controller|

Dies ist eine Mini-dünne Infrarot-Fernbedienung mit 21 Funktionstasten und einer Übertragungsdistanz von bis zu 8 Metern, geeignet für die Bedienung einer Vielzahl von Geräten in einem Kinderzimmer.

* Größe: 85x39x6mm
* Reichweite der Fernbedienung: 8-10m
* Batterie: 3V Knopfzellen-Lithium-Mangan-Batterie
* Infrarot-Trägerfrequenz: 38KHz
* Oberflächenklebematerial: 0.125mm PET
* Effektive Lebensdauer: mehr als 20.000 Mal


**Beispiel**

* :ref:`py_irremote` (For MicroPython User)
* :ref:`ar_irremote` (For Arduino User)