.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Vertiefen Sie sich mit anderen Enthusiasten in die Welt von Raspberry Pi, Arduino und ESP32.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Austausch von Tipps und Anleitungen zur Verbesserung Ihrer Fähigkeiten.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _setup_pico_arduino:

1.3 Einrichtung des Raspberry Pi Pico 2 (Wichtig)
====================================================

1. Installieren des Board-Pakets
---------------------------------------

Um den Raspberry Pi Pico 2 zu programmieren, müssen Sie das entsprechende Board-Paket in der Arduino IDE installieren. Folgen Sie diesen Schritten, um zu beginnen:

#. Öffnen Sie die Arduino IDE und navigieren Sie zu **Datei** -> **Voreinstellungen**.

   .. image:: img/arduino_pico_file.png

#. Geben Sie im angezeigten Dialogfeld die folgende URL in das Feld „Zusätzliche Boardverwalter-URLs“ ein: ``https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json``.

   .. image:: img/arduino_pico_link.png

#. Öffnen Sie den **Boardverwalter** über das Menü und suchen Sie nach **pico**. Klicken Sie auf den **INSTALLIEREN**-Button, um die Installation zu starten. Dadurch wird das Paket **Raspberry Pi Pico 2/RP2040** installiert, einschließlich der Unterstützung für den Raspberry Pi Pico 2.

   .. image:: img/arduino_pico_install.png

#. Während des Installationsprozesses erscheinen möglicherweise mehrere Pop-up-Fenster, die Sie zur Installation spezifischer Gerätetreiber auffordern. Wählen Sie **"Installieren"**.

   .. image:: img/install_pico_sa.png

#. Nach Abschluss der Installation erscheint eine Benachrichtigung zur Bestätigung der erfolgreichen Einrichtung.

2. Auswahl des Boards und Ports
------------------------------------------

#. Halten Sie die **BOOTSEL**-Taste gedrückt, trennen Sie dann den Raspberry Pi Pico 2 vom Computer und stecken Sie ihn schnell wieder ein.

   .. image:: img/led_onboard.png
        :width: 500
        :align: center

   .. warning::
        
      * Dieser Schritt ist entscheidend, insbesondere für Erstnutzer der Arduino IDE. Wird dieser Schritt übersprungen, schlägt das Hochladen fehl.
      * Sobald der Code erfolgreich hochgeladen wurde, wird Ihr Pico vom Computer erkannt. Für zukünftige Uploads reicht es, den Pico einfach ohne gedrückte Taste anzuschließen.

#. Um das passende Board auszuwählen, gehen Sie zu **Werkzeuge** -> **Board** -> **Raspberry Pi Pico 2/RP2040** -> **Raspberry Pi Pico 2**.

   .. image:: img/arduino_pico_board.png
      :width: 800
      :align: center

2. Wählen Sie als Nächstes den richtigen Port aus, indem Sie zu **Werkzeuge** -> **Port** -> **UF2 Board** navigieren.

   .. note::
     
     * Beim ersten Anschluss oder wenn die **BOOTSEL**-Taste gedrückt wird, wählen Sie **UF2 Board**.
     * Nach dem erfolgreichen Hochladen des Codes wird Ihr Pico 2 vom Computer erkannt. Für zukünftige Verwendungen wählen Sie den entsprechenden **COMxx (Raspberry Pi Pico 2)**.

   .. image:: img/arduino_pico_port.png


3. Hochladen des Codes
--------------------------

Nun geht es weiter mit dem Hochladen des Codes auf Ihren Raspberry Pi Pico 2.

#. Öffnen Sie eine ``.ino``-Datei oder verwenden Sie den standardmäßig angezeigten leeren Sketch. Klicken Sie dann auf den **Upload**-Button.

   .. image:: img/install_pico_upload.png

#. Nach dem erfolgreichen Hochladen erscheint eine Bestätigungsmeldung.

   .. image:: img/install_pico_upload_done.png

#. Ihr Computer sollte den Pico 2 nun erfolgreich erkennen.

   .. image:: img/arduino_pico_port_com.png

#. Die Arduino IDE 2.0 bietet eine Schnellwahlfunktion, mit der das richtige Board und der richtige Port einfach eingestellt werden können.

   .. image:: img/install_pico_select.png
