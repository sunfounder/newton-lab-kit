.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _thonny_ide:

1.2 Installation und Vorstellung der Thonny IDE
===================================================

Um den Pico mit MicroPython zu programmieren, benötigen Sie eine integrierte Entwicklungsumgebung (IDE). Hier empfehlen wir Thonny. Python 3.7 ist bereits in der Thonny IDE vorinstalliert, sodass Sie sie nur installieren müssen.

Herunterladen aus dem Web
----------------------------

Bevor Sie anfangen können, den Pico mit MicroPython zu programmieren, benötigen Sie eine integrierte Entwicklungsumgebung (IDE). Hier empfehlen wir Thonny. Thonny kommt mit Python 3.7 eingebaut, es ist nur ein einfacher Installer notwendig und Sie sind bereit zum Programmieren.

.. note::

    Da der Raspberry Pi Pico 2 Interpreter nur mit der Thonny-Version 3.3.3 oder höher funktioniert, können Sie dieses Kapitel überspringen, wenn Sie diese bereits haben; andernfalls aktualisieren oder installieren Sie sie bitte.


#. Sie können sie von der |link_thonny| Webseite herunterladen. Wenn Sie die Seite öffnen, sehen Sie oben rechts ein hellgraues Feld, klicken Sie auf den Link, der zu Ihrem Betriebssystem passt.

   .. image:: img/download_thonny.png
    :width: 400

#. Die Installationsprogramme wurden mit einem neuen Zertifikat signiert, das noch keinen Ruf aufgebaut hat. Möglicherweise müssen Sie die Warnung Ihres Browsers durchklicken (z. B. „Behalten“ statt „Verwerfen“ in Chrome) und die Windows Defender-Warnung (**Mehr Info** ⇒ **Trotzdem ausführen**).

   .. image:: img/install_thonny1.png

#. Klicken Sie anschließend auf **Weiter** und **Installieren**, um die Installation von Thonny abzuschließen.

   .. image:: img/install_thonny6.png

Einführung in die Thonny IDE
----------------------------------

* Ref: `realpython <https://realpython.com/micropython/>`_

.. image:: img/thonny_ide.jpg

* **A**: Die Menüleiste mit Neu, Speichern, Bearbeiten, Ansicht, Ausführen, Debuggen usw.
* **B**: Dieses Papier-Symbol ermöglicht es Ihnen, eine neue Datei zu erstellen.
* **C**: Wenn Ihr Raspberry Pi Pico 2 bereits mit Ihrem Computer verbunden ist, können Sie Dateien öffnen, die bereits auf Ihrem Computer oder Pico existieren.
* **D**: Klicken Sie auf das Diskettensymbol, um den Code zu speichern. Sie können auch wählen, ob Sie den Code auf Ihrem Computer oder dem Raspberry Pi Pico 2 speichern möchten.
* **E**: Das Wiedergabe-Symbol ermöglicht es Ihnen, den Code auszuführen. Speichern Sie den Code, bevor Sie ihn ausführen, falls Sie dies noch nicht getan haben.
* **F**: Das Debug-Symbol ermöglicht es Ihnen, Ihren Code zu debuggen. Beim Schreiben von Code werden unweigerlich Fehler auftreten. Es gibt viele Arten von Fehlern, einschließlich falscher Syntax und logischer Fehler. Debuggen ist das Werkzeug zum Finden und Untersuchen von Fehlern.

.. note::

    Wenn MicroPython (Raspberry Pi Pico).COMxx als Interpreter ausgewählt ist, kann das Debug-Tool nicht verwendet werden.
    
    Um Ihren Code zu debuggen, wählen Sie den Interpreter als Standardinterpreter und speichern Sie ihn nach dem Debuggen auf Ihrem Computer.

    Sie können nun den debuggten Code auf Ihren Raspberry Pi Pico 2 speichern, indem Sie den Interpreter MicroPython (Raspberry Pi Pico).COMxx erneut auswählen, auf die Schaltfläche Speichern unter klicken und erneut auf die Schaltfläche Speichern klicken.

* Wenn Sie auf das Debug-Symbol klicken, können Sie das Programm Schritt für Schritt mit den Pfeilsymbolen G, H und I ausführen. Wenn Sie auf jedes Pfeilsymbol klicken, erscheint eine gelb hervorgehobene Leiste, um anzuzeigen, welche Python-Zeile oder welcher Abschnitt bewertet wird.

    * **G**: Einen großen Schritt machen, was bedeutet, zur nächsten Zeile oder zum nächsten Block von Code zu springen.
    * **H**: Einen kleinen Schritt machen bedeutet, jeden Bestandteil in der Tiefe auszudrücken.
    * **I**: Aus dem Debugger aussteigen.
* **J**: Klicken Sie darauf, um vom Debug-Modus in den Wiedergabe-Modus zurückzukehren.
* **K**: Verwenden Sie das Stopp-Symbol, um den laufenden Code zu stoppen.
* **L**: Skriptbereich, in dem Sie Ihren Python-Code schreiben können.
* **M**: Python-Shell, in der Sie einen einzelnen Befehl eingeben können, und wenn Sie die Eingabetaste drücken, wird der einzelne Befehl ausgeführt und Informationen über das laufende Programm bereitgestellt. Dies wird auch als REPL bezeichnet, was für "Read, Evaluate, Print und Loop" steht.
* **N**: Interpreter, in dem die aktuelle Version von Python angezeigt wird, die verwendet wird, um Ihr Programm auszuführen. Sie können manuell auf eine andere Version umschalten, indem Sie darauf klicken.

.. note::

   **Keine MicroPython(Raspberry Pi Pico 2) Interpreter-Option?**

   * Stellen Sie sicher, dass Ihr Pico über ein USB-Kabel mit Ihrem Computer verbunden ist.
   * Der Raspberry Pi Pico 2 Interpreter ist nur in der Thonny-Version 3.3.3 oder höher verfügbar. Wenn Sie eine ältere Version verwenden, aktualisieren Sie bitte.
