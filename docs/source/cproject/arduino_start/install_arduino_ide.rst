.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _install_arduino:

1.1 Arduino IDE installieren (Wichtig)
========================================

Die Arduino IDE (Integrated Development Environment) bietet alle notwendigen Software-Tools, um ein Arduino-Projekt zu realisieren. Sie ist eine speziell für Arduino entwickelte Programmiersoftware, die vom Arduino-Team bereitgestellt wird und es uns ermöglicht, Programme zu schreiben und auf das Arduino-Board hochzuladen.

Die Arduino IDE 2.0 ist ein Open-Source-Projekt und ein bedeutender Fortschritt gegenüber ihrem stabilen Vorgänger, der Arduino IDE 1.x. Sie bietet eine modernisierte Benutzeroberfläche, einen verbesserten Board- und Bibliotheksmanager, einen Debugger, eine Autovervollständigungsfunktion und vieles mehr.

In diesem Tutorial zeigen wir, wie Sie die Arduino IDE 2.0 auf einem Windows-, Mac- oder Linux-Computer herunterladen und installieren.

Systemanforderungen
---------------------

* Windows - Windows 10 oder neuer, 64-Bit
* Linux - 64-Bit
* macOS - Version 10.14 „Mojave“ oder neuer, 64-Bit

Arduino IDE 2.0 herunterladen
--------------------------------

#. Besuchen Sie die Seite |link_download_arduino|.

#. Laden Sie die IDE für Ihr Betriebssystem herunter.

    .. image:: img/sp_001.png

Installation
------------------------------

Windows
^^^^^^^^^^^^^

#. Doppelklicken Sie auf die Datei ``arduino-ide_xxxx.exe``, um die heruntergeladene Datei auszuführen.

#. Lesen Sie die Lizenzvereinbarung und akzeptieren Sie sie.

    .. image:: img/sp_002.png

#. Wählen Sie die Installationsoptionen.

    .. image:: img/sp_003.png

#. Wählen Sie das Installationsverzeichnis. Es wird empfohlen, die Software auf einem anderen Laufwerk als dem Systemlaufwerk zu installieren.

    .. image:: img/sp_004.png

#. Abschließend auf **Fertigstellen** klicken.

    .. image:: img/sp_005.png

macOS
^^^^^^^^^^^^^^^^

Doppelklicken Sie auf die heruntergeladene Datei ``arduino_ide_xxxx.dmg`` und folgen Sie den Anweisungen, um die **Arduino IDE.app** in den **Programme**-Ordner zu kopieren. Nach wenigen Sekunden wird die Arduino IDE erfolgreich installiert sein.

.. image:: img/macos_install_ide.png
    :width: 800

Linux
^^^^^^^^^^^^

Für eine Anleitung zur Installation der Arduino IDE 2.0 unter Linux besuchen Sie bitte:
https://docs.arduino.cc/software/ide-v2/tutorials/getting-started/ide-v2-downloading-and-installing#linux

Die IDE öffnen
--------------

#. Beim ersten Start der Arduino IDE 2.0 werden automatisch die Arduino AVR Boards, integrierte Bibliotheken und andere erforderliche Dateien installiert.

    .. image:: img/sp_901.png

#. Zudem kann es sein, dass Ihre Firewall oder Ihr Sicherheitscenter mehrmals fragt, ob Gerätetreiber installiert werden sollen. Bitte akzeptieren und alle Treiber installieren.

    .. image:: img/sp_104.png

#. Jetzt ist die Arduino IDE einsatzbereit!

    .. note::
        Falls einige Installationen aufgrund von Netzwerkproblemen oder anderen Gründen nicht abgeschlossen wurden, können Sie die Arduino IDE erneut starten, um den Installationsprozess fortzusetzen. Das **Ausgabe-Fenster** öffnet sich nach der vollständigen Installation nicht automatisch, es sei denn, Sie klicken auf Überprüfen oder Hochladen.
