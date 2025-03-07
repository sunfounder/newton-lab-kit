.. note::
   
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Tutorials zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspiele und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _cpn_keypad:

4x4-Tastenfeld
========================

In einem Mikrocontrollersystem, insbesondere wenn viele Tasten wie bei einem elektronischen Codeschloss, einem Telefon-Keypad usw. verwendet werden, kommen generell mindestens 12 bis 16 Tasten zum Einsatz, die üblicherweise in einem Matrix-Keypad angeordnet sind.

Ein Matrix-Keypad wird auch als Reihen-Tastenfeld bezeichnet. Es ist ein Keypad mit vier I/O-Leitungen als Zeilenleitungen und vier I/O-Leitungen als Spaltenleitungen. An jedem Schnittpunkt der Zeilen- und Spaltenleitungen ist eine Taste angebracht. Somit ergibt sich eine Anzahl von Tasten auf der Tastatur von 4*4. Diese Zeilen- und Spalten-Struktur des Keypads kann die Nutzung der I/O-Ports in einem Mikrocontrollersystem effektiv verbessern.

Die Kontakte sind über einen Header zugänglich, der für den Anschluss eines Flachbandkabels oder zum Einsetzen in eine gedruckte Schaltplatte geeignet ist.
Bei einigen Keypads verbindet jede Taste mit einem separaten Kontakt im Header, während alle Tasten eine gemeinsame Masse teilen.

|img_keypad|

Häufiger sind die Tasten matrixcodiert, was bedeutet, dass jede von ihnen ein einzigartiges Paar von Leitern in einer Matrix überbrückt.
Diese Konfiguration eignet sich für das Abfragen durch einen Mikrocontroller, der so programmiert werden kann, dass er nacheinander einen Ausgangsimpuls an jede der vier horizontalen Leitungen sendet.
Während jedes Impulses überprüft er nacheinander die verbleibenden vier vertikalen Leitungen, um festzustellen, welche davon, falls zutreffend, ein Signal führt.
Pull-up- oder Pull-down-Widerstände sollten den Eingangsleitungen hinzugefügt werden, um zu verhindern, dass die Eingänge des Mikrocontrollers unvorhersehbar reagieren, wenn kein Signal vorhanden ist.

* `Keypad - Wikipedia <https://en.wikipedia.org/wiki/Keypad>`_

**Beispiel**

* :ref:`py_keypad` (For MicroPython User)
* :ref:`py_guess_number` (For MicroPython User)
* :ref:`ar_keypad` (For Arduino User)