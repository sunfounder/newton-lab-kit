.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 zusammen mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1.1 Einführung in MicroPython
======================================

MicroPython ist eine Softwareimplementierung einer Programmiersprache, die weitgehend mit Python 3 kompatibel ist, in C geschrieben wurde und optimiert ist, um auf einem Mikrocontroller zu laufen.

MicroPython besteht aus einem Python-Compiler zu Bytecode und einem Laufzeitinterpreter dieses Bytecodes. Dem Benutzer wird eine interaktive Eingabeaufforderung (das REPL) präsentiert, um unterstützte Befehle sofort auszuführen. Eingeschlossen sind eine Auswahl von Kern-Python-Bibliotheken; MicroPython enthält Module, die dem Programmierer Zugang zu Hardware auf niedriger Ebene geben.

* Referenz: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_

Die Geschichte beginnt hier
--------------------------------

2013 änderte sich alles, als Damien George eine Crowdfunding-Kampagne (Kickstarter) startete.

Damien war ein Student an der Universität Cambridge und ein begeisterter Robotikprogrammierer. Er wollte die Welt von Python von einer Gigabyte-Maschine auf ein Kilobyte reduzieren. Seine Kickstarter-Kampagne sollte seine Entwicklung unterstützen, während er seinen Proof of Concept in eine fertige Implementierung umwandelte.

MicroPython wird von einer vielfältigen Pythonista-Community unterstützt, die ein starkes Interesse am Erfolg des Projekts hat.

Neben dem Testen und Unterstützen der Codebasis haben die Entwickler Tutorials, Codebibliotheken und Hardware-Portierungen bereitgestellt, sodass Damien sich auf andere Aspekte des Projekts konzentrieren konnte.

* Referenz: `realpython <https://realpython.com/micropython/>`_

Warum MicroPython？
---------------------

Obwohl die ursprüngliche Kickstarter-Kampagne MicroPython als Entwicklungsboard "pyboard" mit STM32F4 herausbrachte, unterstützt MicroPython viele auf ARM basierende Produktarchitekturen. Die hauptsächlich unterstützten Ports sind ARM Cortex-M (viele STM32-Boards, TI CC3200/WiPy, Teensy-Boards, Nordic nRF-Serie, SAMD21 und SAMD51), ESP8266, ESP32, 16-Bit-PIC, Unix, Windows, Zephyr und JavaScript.
Zweitens ermöglicht MicroPython schnelles Feedback. Dies liegt daran, dass Sie REPL verwenden können, um Befehle interaktiv einzugeben und Antworten zu erhalten. Sie können sogar Code anpassen und ihn sofort ausführen, anstatt den Zyklus Code-Kompilieren-Hochladen-Ausführen zu durchlaufen.

Während Python dieselben Vorteile bietet, sind einige Mikrocontroller-Boards wie der Raspberry Pi Pico 2 klein, einfach und haben zu wenig Speicher, um die Python-Sprache überhaupt auszuführen. Deshalb hat sich MicroPython entwickelt, wobei die Hauptmerkmale von Python beibehalten und eine Reihe neuer Funktionen hinzugefügt wurden, um mit diesen Mikrocontroller-Boards zu arbeiten.

Als Nächstes lernen Sie, MicroPython auf dem Raspberry Pi Pico 2 zu installieren.

* Referenz: `MicroPython - Wikipedia <https://en.wikipedia.org/wiki/MicroPython>`_
* Referenz: `realpython <https://realpython.com/micropython/>`_
