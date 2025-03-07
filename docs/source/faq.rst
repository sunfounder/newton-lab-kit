.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauche tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein – gemeinsam mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Erhalte Hilfe bei technischen Herausforderungen und nach dem Kauf auftretenden Problemen durch unsere Community und unser Team.
    - **Lernen & Teilen**: Tausche Tipps und Tutorials aus, um deine Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalte frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Profitiere von exklusiven Preisnachlässen auf unsere neuesten Produkte.
    - **Feierliche Aktionen und Gewinnspiele**: Nimm an Verlosungen und saisonalen Aktionen teil.

    👉 Bereit, mit uns zu entdecken und zu kreieren? Klicke auf [|link_sf_facebook|] und werde Teil unserer Community!

FAQ
=========

Arduino
---------------------

#. Code-Upload im Arduino IDE fehlgeschlagen?
    * Überprüfe, ob dein Pico vom Arduino IDE korrekt erkannt wird. Der Port sollte als COMXX (Raspberry Pi Pico 2) angezeigt werden. Eine Anleitung dazu findest du unter :ref:`setup_pico_arduino`.
    * Stelle sicher, dass das richtige Board (Raspberry Pi Pico 2) und der korrekte Port (COMXX (Raspberry Pi Pico 2)) ausgewählt sind.
    * Falls dein Code korrekt ist und du das richtige Board sowie den richtigen Port ausgewählt hast, der Upload aber dennoch fehlschlägt, versuche Folgendes: Klicke erneut auf das **Upload**-Symbol, und sobald in der Statusleiste „Upload...“ angezeigt wird, ziehe das USB-Kabel ab. Halte dann die **BOOTSEL**-Taste gedrückt, während du das Kabel wieder einsteckst. Der Code sollte nun erfolgreich hochgeladen werden.

MicroPython
------------------

#. Wie öffne und starte ich den Code?
    Eine detaillierte Anleitung findest du unter :ref:`open_run_code_py`.

#. Wie lade ich eine Bibliothek auf den Raspberry Pi Pico 2 hoch?
    Eine detaillierte Anleitung findest du unter :ref:`add_libraries_py`.

#. Keine MicroPython (Raspberry Pi Pico) Interpreter-Option in Thonny IDE?
    * Überprüfe, ob dein Pico über ein USB-Kabel mit dem Computer verbunden ist.
    * Stelle sicher, dass MicroPython für den Pico installiert ist (:ref:`install_micropython_on_pico`).
    * Der MicroPython-Interpreter für den Raspberry Pi Pico 2 ist erst ab Version 3.3.3 oder höher von Thonny verfügbar. Falls du eine ältere Version verwendest, aktualisiere sie bitte (:ref:`thonny_ide`).
    * Versuche, das USB-Kabel mehrmals ein- und auszustecken.

#. Kann den Pico-Code in Thonny IDE nicht öffnen oder darauf speichern?
    * Überprüfe, ob dein Pico über ein USB-Kabel mit dem Computer verbunden ist.
    * Stelle sicher, dass der Interpreter als **MicroPython (Raspberry Pi Pico).COMxx** ausgewählt ist.

#. Kann der Raspberry Pi Pico 2 gleichzeitig mit Thonny und Arduino verwendet werden?
    Nein, unterschiedliche Vorbereitungen sind erforderlich.

    * Falls du den Pico zuerst mit Arduino genutzt hast und ihn nun mit Thonny IDE verwenden möchtest, installiere :ref:`install_micropython_on_pico` darauf.
    * Falls du ihn zuerst mit Thonny verwendet hast und ihn nun mit Arduino IDE nutzen möchtest, richte ihn entsprechend unter :ref:`setup_pico_arduino` ein.

#. Mein Computer verwendet Windows 7 und der Pico wird nicht erkannt.
    * Lade den USB-CDC-Treiber von http://aem-origin.microchip.com/en-us/mindi-sw-library?swsearch=Atmel%2520USB%2520CDC%2520Virtual%2520COM%2520Driver herunter.
    * Entpacke die Datei ``amtel_devices_cdc.inf`` in einen Ordner namens ``pico-serial``.
    * Benenne die Datei ``amtel_devices_cdc.inf`` in ``pico-serial.inf`` um.
    * Öffne/bearbeite die Datei ``pico-serial.inf`` in einem einfachen Texteditor wie Notepad.
    * Ersetze die Zeilen unter den folgenden Abschnitten:

    .. code-block::

        [DeviceList]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTAMD64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NTIA64]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [DeviceList.NT]
        %PI_CDC_PICO%=DriverInstall, USB\VID_2E8A&PID_0005&MI_00

        [Strings]
        Manufacturer = "ATMEL, Inc."
        PI_CDC_PICO = "Pi Pico Serial Port"
        Serial.SvcDesc = "Pi Pico Serial Driver"

    #. Speichere die Datei unter dem Namen ``pico-serial.inf``.
    #. Öffne die Geräteverwaltung deines PCs, suche unter „Ports“ nach dem Pico (vermutlich als „CDC Device“ gekennzeichnet). Falls ein gelbes Ausrufezeichen angezeigt wird, bedeutet dies, dass ein Treiberproblem vorliegt.
    #. Klicke mit der rechten Maustaste auf das CDC-Gerät und wähle „Treiber aktualisieren“ oder „Treiber installieren“, und wähle anschließend die zuvor gespeicherte Datei aus.

.. Piper Make
.. ------------------

.. #. Wie richte ich den Pico auf Piper Make ein?
..     Eine detaillierte Anleitung findest du unter :ref:`per_setup_pico`.

.. #. Wie lade oder importiere ich Code?
..     Eine detaillierte Anleitung findest du unter :ref:`per_save_import`.

.. #. Wie verbinde ich mich mit dem Pico?
..     Eine detaillierte Anleitung findest du unter :ref:`connect_pico_per`.
