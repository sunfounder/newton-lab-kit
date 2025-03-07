.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_transistor:

Transistor
============

|img_NPN&PNP|

Ein Transistor ist ein Halbleiterbauelement, das Strom durch Strom steuert. Er funktioniert, indem er schwache Signale zu stärkeren Amplituden verstärkt und wird auch als kontaktloser Schalter verwendet.

Ein Transistor besteht aus einer dreischichtigen Struktur aus P-Typ- und N-Typ-Halbleitern. Diese bilden intern drei Regionen. Die dünnere in der Mitte ist die Basisregion; die anderen beiden sind entweder N-Typ oder P-Typ – die kleinere Region mit intensiven Majoritätsträgern ist die Emitterregion, während die andere die Kollektorregion ist. Diese Zusammensetzung ermöglicht es dem Transistor, als Verstärker zu fungieren.
Aus diesen drei Regionen entstehen jeweils drei Pole, die Basis (b), der Emitter (e) und der Kollektor (c). Sie bilden zwei P-N-Übergänge, nämlich den Emitterübergang und den Kollektorübergang. Die Richtung des Pfeils im Schaltungssymbol des Transistors zeigt die des Emitterübergangs.

* `P–N junction - Wikipedia <https://en.wikipedia.org/wiki/P-n_junction>`_

Basierend auf dem Halbleitertyp können Transistoren in zwei Gruppen eingeteilt werden, die NPN- und die PNP-Typen. Aus der Abkürzung lässt sich erkennen, dass der erstere aus zwei N-Typ-Halbleitern und einem P-Typ besteht und der letztere das Gegenteil ist. Siehe die Abbildung unten.

.. note::
    s8550 ist ein PNP-Transistor und der s8050 ist der NPN-Typ, sie sehen sehr ähnlich aus, und wir müssen sorgfältig ihre Etiketten überprüfen.

|img_transistor_symbol|

Wenn ein High-Level-Signal durch einen NPN-Transistor geht, wird er aktiviert. Aber ein PNP-Typ benötigt ein Low-Level-Signal zur Steuerung. Beide Transistortypen werden häufig für kontaktlose Schalter verwendet, wie in diesem Experiment.


* `S8050 Transistor Datasheet <https://components101.com/asset/sites/default/files/component_datasheet/S8050%20Transistor%20Datasheet.pdf>`_
* `S8550 Transistor Datasheet <https://www.mouser.com/datasheet/2/149/SS8550-118608.pdf>`_

Stellen Sie die Etikettenseite zu uns und die Pins nach unten. Die Pins von links nach rechts sind Emitter(e), Basis(b) und Kollektor(c).

|img_ebc|

.. note::
    * Die Basis ist das Gate-Kontrollelement für die größere Stromversorgung.
    * Beim NPN-Transistor ist der Kollektor die größere Stromversorgung und der Emitter der Auslass dafür, beim PNP-Transistor ist es genau umgekehrt.


.. Beispiel
.. -------------------

.. :ref:`Two Kinds of Transistors`


**Beispiel**

* :ref:`py_transistor` (For MicroPython User)
* :ref:`py_relay` (For MicroPython User)
* :ref:`py_ac_buz` (For MicroPython User)
* :ref:`py_pa_buz` (For MicroPython User)
* :ref:`py_light_theremin` (For MicroPython User)
* :ref:`py_alarm_lamp` (For MicroPython User)
* :ref:`py_music_player` (For MicroPython User)
* :ref:`py_fruit_piano` (For MicroPython User)
* :ref:`py_reversing_aid` (For MicroPython User)
* :ref:`ar_ac_buz` (For Arduino User)
* :ref:`ar_pa_buz` (For Arduino User)
* :ref:`ar_transistor` (For Arduino User)
* :ref:`ar_relay` (For Arduino User)
.. * :ref:`per_service_bell` (For Piper Make User)
.. * :ref:`per_reversing_system` (For Piper Make User)
.. * :ref:`per_reaction_game` (For Piper Make User)