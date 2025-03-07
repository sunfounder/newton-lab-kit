.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Promotionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _install_micropython_on_pico:

1.3 Installieren Sie MicroPython auf Ihrem Pico2
===================================================

Jetzt geht es darum, MicroPython auf Raspberry Pi Pico 2 zu installieren. Die Thonny IDE bietet eine sehr bequeme Möglichkeit, dies mit einem Klick zu tun.

.. note::
    Wenn Sie Thonny nicht aktualisieren möchten, können Sie die offizielle Methode von Raspberry Pi |link_micropython_method| verwenden, indem Sie eine ``rp2_pico_xxxx.uf2`` Datei auf den Raspberry Pi Pico2 ziehen und ablegen.


#. Öffnen Sie die Thonny IDE.

    .. image:: img/new/set_pico1.png

#. Halten Sie die **BOOTSEL**-Taste gedrückt und verbinden Sie dann den Pico2 über ein Micro USB-Kabel mit dem Computer. Lassen Sie die **BOOTSEL**-Taste los, nachdem Ihr Pico2 als Massenspeichergerät namens **RPI-RP2040** erkannt wurde.

    .. image:: img/new/bootsel_onboard.png

#. Klicken Sie in der unteren rechten Ecke auf den Interpreter-Auswahlknopf und wählen Sie **Install Micropython**.

    .. note::
        Wenn Ihre Thonny-Version diese Option nicht bietet, aktualisieren Sie bitte auf die neueste Version.

    .. image:: img/new/set_pico2.jpg

#. Im Feld **Target volume** erscheint automatisch das Volume des gerade angeschlossenen Pico2 und im Feld **Micropython variant** wählen Sie **Raspberry Pi.Pico 2**.

    .. image:: img/new/set_pico3.jpg

#. Klicken Sie auf den **Install**-Button, warten Sie bis die Installation abgeschlossen ist und schließen Sie dann diese Seite.

    .. image:: img/new/set_pico4.jpg

Herzlichen Glückwunsch, Ihr Raspberry Pi Pico2 ist nun einsatzbereit.
