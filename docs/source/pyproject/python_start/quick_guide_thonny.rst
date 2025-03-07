.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1.5 Schnelleinstieg in Thonny
==================================

.. _open_run_code_py:

Direktes Öffnen und Ausführen von Code
---------------------------------------------

Der Codeabschnitt in den Projekten gibt genau an, welcher Code verwendet wird. Doppelklicken Sie auf die Datei ``.py`` mit der Seriennummer im Pfad ``newton-lab-kit/micropython/``, um sie zu öffnen.

Zuvor müssen Sie jedoch das Paket herunterladen und die Bibliothek hochladen, wie in :ref:`download_upload` beschrieben.

#. Code öffnen

   Zum Beispiel ``2.1_hello_led.py``.
   
   Wenn Sie darauf doppelklicken, öffnet sich ein neues Fenster auf der rechten Seite. Sie können gleichzeitig mehr als einen Code öffnen.

   .. image:: img/open_code.png

#. Richtigen Interpreter wählen

   Verbinden Sie den Pico mit Ihrem Computer mit einem Micro USB-Kabel und wählen Sie den Interpreter "MicroPython (Raspberry Pi Pico).COMxx".

   .. image:: img/sec_inter.png

#. Code ausführen

   Um das Skript auszuführen, klicken Sie auf die Schaltfläche **Aktuelles Skript ausführen** oder drücken Sie F5.

   .. image:: img/run_it.png

   Wenn der Code Informationen enthält, die ausgegeben werden sollen, erscheinen sie in der Shell; ansonsten erscheint nur die folgende Information.

   Klicken Sie auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es nicht in Ihrem Thonny erscheint.

   .. code-block::
      
      MicroPython v1.24.0-preview.201.g269a0e0e1 on 2024-08-09; Raspberry Pi Pico 22 with RP2350
      Type "help()" for more information.
      >>> %Run -c $EDITOR_CONTENT

   * Die erste Zeile zeigt die Version von MicroPython, das Datum und Ihre Geräteinformationen.
   * Die zweite Zeile fordert Sie auf, "help()" einzugeben, um Hilfe zu erhalten.
   * Die dritte Zeile ist ein Befehl von Thonny, der den MicroPython-Interpreter auf Ihrem Pico anweist, den Inhalt des Skriptbereichs auszuführen - "EDITOR_CONTENT".
   * Wenn nach der dritten Zeile eine Nachricht erscheint, handelt es sich in der Regel um eine Nachricht, die Sie MicroPython ausgeben lassen, oder um eine Fehlermeldung für den Code.

#. Ausführung stoppen

   .. image:: img/stop_it.png

   Um die laufende Codeausführung zu stoppen, klicken Sie auf die Schaltfläche **Backend stoppen/neu starten**. Der Befehl **%RUN -c $EDITOR_CONTENT** verschwindet nach dem Anhalten.

#. Speichern oder Speichern unter

   Sie können Änderungen an dem geöffneten Beispiel speichern, indem Sie **Ctrl+S** drücken oder auf die Schaltfläche **Speichern** in Thonny klicken.
   
   * Der Code kann als separate Datei innerhalb des Raspberry Pi Pico 2 gespeichert werden, indem Sie auf **Datei** -> **Speichern unter** klicken.

     .. image:: img/save_as.png

   * Wählen Sie **Raspberry Pi Pico 2** aus.

     .. image:: img/sec_pico.png

   * Klicken Sie dann nach Eingabe des Dateinamens und der Erweiterung **.py** auf **OK**. Auf dem Laufwerk des Raspberry Pi Pico 2 sehen Sie Ihre gespeicherte Datei.

     .. image:: img/sec_name.png

     .. note::
        Unabhängig davon, welchen Namen Sie Ihrem Code geben, ist es am besten, zu beschreiben, welche Art von Code es ist, und ihm keinen bedeutungslosen Namen wie ``abc.py`` zu geben.
        Wenn Sie den Code als ``main.py`` speichern, wird er automatisch beim Einschalten ausgeführt.


Datei erstellen und ausführen
------------------------------


Der Code wird direkt im Codeabschnitt angezeigt. Sie können ihn in Thonny kopieren und wie folgt ausführen.

#. Neue Datei erstellen

   Öffnen Sie Thonny IDE und klicken Sie auf die Schaltfläche **Neu**, um eine neue leere Datei zu erstellen.

   .. image:: img/new_file.png

#. Code kopieren

   Kopieren Sie den Code aus dem Projekt in die Thonny IDE.

   .. image:: img/copy_file.png

#. Richtigen Interpreter wählen

   Verbinden Sie den Pico mit Ihrem Computer mit einem Micro USB-Kabel und wählen Sie den Interpreter "MicroPython (Raspberry Pi Pico).COMxx" in der rechten unteren Ecke.

   .. image:: img/sec_inter.png

#. Code ausführen und speichern

   Sie müssen auf **Aktuelles Skript ausführen** klicken oder einfach F5 drücken, um es auszuführen. Wenn Ihr Code noch nicht gespeichert wurde, erscheint ein Fenster, das Sie auffordert, ihn auf **Diesem Computer** oder **Raspberry Pi Pico 2** zu speichern.

   .. image:: img/where_save.png

   .. note::
        Thonny speichert Ihr Programm auf dem Raspberry Pi Pico 2, wenn Sie ihn dazu auffordern. Wenn Sie den Pico ausstecken und in einen anderen Computer stecken, bleibt Ihr Programm intakt.

   * Klicken Sie nach der Auswahl des Ortes, der Namensgebung und dem Hinzufügen der Erweiterung **.py** auf OK.

     .. image:: img/sec_name.png

     .. note::
        Unabhängig davon, welchen Namen Sie Ihrem Code geben, ist es am besten, zu beschreiben, welche Art von Code es ist, und ihm keinen bedeutungslosen Namen wie ``abc.py`` zu geben.
        Wenn Sie den Code als ``main.py`` speichern, wird er automatisch beim Einschalten ausgeführt.

   * Sobald Ihr Programm gespeichert ist, wird es automatisch ausgeführt und Sie sehen die folgenden Informationen im Shell-Bereich.

   * Klicken Sie auf **Ansicht** -> **Bearbeiten**, um das Shell-Fenster zu öffnen, falls es nicht in Ihrem Thonny erscheint.


     .. code-block::

        MicroPython v1.24.0-preview.201.g269a0e0e1 on 2024-08-09; Raspberry Pi Pico 22 with RP2350

        Type "help()" for more information.
        >>> %Run -c $EDITOR_CONTENT


     * Die erste Zeile zeigt die Version von MicroPython, das Datum und Ihre Geräteinformationen.
     * Die zweite Zeile fordert Sie auf, "help()" einzugeben, um Hilfe zu erhalten.
     * Die dritte Zeile ist ein Befehl von Thonny, der den MicroPython-Interpreter auf Ihrem Pico anweist, den Inhalt des Skriptbereichs auszuführen - "EDITOR_CONTENT".
     * Wenn nach der dritten Zeile eine Nachricht erscheint, handelt es sich in der Regel um eine Nachricht, die Sie MicroPython ausgeben lassen, oder um eine Fehlermeldung für den Code.

#. Ausführung stoppen

   Um die laufende Codeausführung zu stoppen, klicken Sie auf die Schaltfläche **Backend stoppen/neu starten**. Der Befehl **%RUN -c $EDITOR_CONTENT** verschwindet nach dem Anhalten.

   .. image:: img/stop_it.png

#. Datei öffnen

   Hier sind zwei Möglichkeiten, eine gespeicherte Code-Datei zu öffnen.

   * Die erste Methode besteht darin, das Öffnen-Symbol in der Thonny-Symbolleiste anzuklicken, genau wie beim Speichern eines Programms. Ihnen wird dann gefragt, ob Sie es von **diesem Computer** oder **Raspberry Pi Pico 2** öffnen möchten. Zum Beispiel klicken Sie auf **Raspberry Pi Pico 2** und sehen eine Liste aller Programme, die Sie auf dem Pico gespeichert haben.
   * Die zweite Möglichkeit besteht darin, die Dateivorschau direkt zu öffnen, indem Sie auf **Ansicht** -> **Datei** klicken und dann auf die entsprechende ``.py``-Datei doppelklicken, um sie zu öffnen.
