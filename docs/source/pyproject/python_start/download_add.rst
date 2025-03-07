.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _download_upload:

1.4 Code herunterladen und hochladen
===============================================

**Code herunterladen**

Laden Sie den relevanten Code von untenstehendem Link herunter.


* :download:`SunFounder Newton Lab Kit Beispiel <https://github.com/sunfounder/newton-lab-kit/archive/refs/heads/main.zip>`

* Oder sehen Sie sich den Code auf `Newton Lab Kit - GitHub <https://github.com/sunfounder/newton-lab-kit>`_ an

.. _add_libraries_py:

Bibliotheken auf den Pico hochladen
---------------------------------------

In einigen Projekten benötigen Sie zusätzliche Bibliotheken. Hier werden wir zuerst diese Bibliotheken auf den Raspberry Pi Pico 2 hochladen, damit wir später den Code direkt ausführen können.

#. Verbinden Sie den Raspberry Pi Pico 2 mit einem Micro USB-Kabel mit Ihrem Computer. (Drücken Sie nicht **BOOTSEL**; Sie haben bereits die MicroPython-Firmware auf Pico 2 im vorherigen Schritt gezogen, also stecken Sie es direkt ein.)

#. Öffnen Sie die Thonny IDE und wählen Sie "MicroPython (Raspberry Pi Pico).COMxx.COMxx" über den Interpreter-Auswahlknopf in der unteren rechten Ecke.

   .. image:: img/th_select_com.png

#. Klicken Sie in der oberen Navigationsleiste der Thonny IDE auf **Ansicht** -> **Dateien**.

   .. image:: img/th_open_files.png

#. Navigieren Sie zu dem Ordner, in dem Sie zuvor das Codepaket heruntergeladen haben, und gehen Sie dann in den Ordner ``newton-lab-kit-main/libs``.

   .. image:: img/th_open_code.png

#. Wählen Sie nun alle Dateien im Ordner ``libs\`` aus und laden Sie sie auf den Raspberry Pi Pico 2 hoch. Das Hochladen der Dateien wird eine Weile dauern.

   .. image:: img/th_upload_libs.png

#. Nun werden Sie die Dateien, die Sie gerade hochgeladen haben, auf Ihrem Laufwerk mit der Bezeichnung ``Raspberry Pi Pico 2`` sehen.

   .. image:: img/th_pico_libs.png
