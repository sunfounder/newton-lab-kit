.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_servo:

Servo
===========

|img_servo|

Ein Servo besteht in der Regel aus folgenden Teilen: Gehäuse, Welle, Getriebesystem, Potentiometer, Gleichstrommotor und eingebettete Platine.

So funktioniert es: Der Mikrocontroller sendet PWM-Signale an das Servo, und die eingebettete Platine im Servo empfängt die Signale über den Signalpin und steuert den Motor, um sich zu drehen. Infolgedessen treibt der Motor das Getriebesystem an, welches dann die Welle nach einer Verzögerung bewegt. Die Welle und das Potentiometer des Servos sind miteinander verbunden. Wenn sich die Welle dreht, treibt sie das Potentiometer an, sodass das Potentiometer ein Spannungssignal an die eingebettete Platine ausgibt. Die Platine bestimmt dann die Drehrichtung und -geschwindigkeit basierend auf der aktuellen Position, sodass es genau in der definierten Position stoppen und dort halten kann.

|img_servo_i|

Der Winkel wird durch die Dauer eines Impulses bestimmt, der auf das Steuerkabel gegeben wird. Dies wird als Pulsweitenmodulation bezeichnet. Das Servo erwartet alle 20 ms einen Impuls. Die Länge des Impulses bestimmt, wie weit der Motor dreht. Zum Beispiel bewirkt ein 1,5-ms-Impuls, dass sich der Motor auf die 90-Grad-Position (neutrale Position) dreht.
Wenn ein Impuls an ein Servo gesendet wird, der kürzer als 1,5 ms ist, dreht sich das Servo in eine Position und hält seine Ausgangswelle einige Grad gegen den Uhrzeigersinn vom Neutralpunkt. Wenn der Impuls breiter als 1,5 ms ist, tritt das Gegenteil ein. Die minimale und die maximale Impulsbreite, die das Servo anweist, sich in eine gültige Position zu drehen, sind Funktionen jedes Servos. In der Regel wird der minimale Impuls etwa 0,5 ms breit sein und der maximale Impuls wird 2,5 ms breit sein.

|img_servo_duty|


.. Beispiel
.. -------------------

.. :ref:`Swinging Servo`

**Beispiel**

* :ref:`py_servo` (For MicroPython User)
* :ref:`py_somato_controller` (For MicroPython User)
* :ref:`ar_servo` (For Arduino User)
.. * :ref:`per_water_tank` (For Piper Make User)
.. * :ref:`per_swing_servo` (For Piper Make User)
.. * :ref:`per_lucky_cat` (For Piper Make User)