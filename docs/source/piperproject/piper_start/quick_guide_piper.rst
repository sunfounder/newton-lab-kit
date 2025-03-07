.. note:: 

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 ein, gemeinsam mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie nach dem Kauf aufgetretene Probleme und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu kreieren? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _quick_guide_piper:

1.2 Schnellstartanleitung für Piper Make
=============================================

1. Neues Projekt erstellen
------------------------------

Nachdem Sie das Pico W eingerichtet haben, ist es nun an der Zeit zu lernen, wie man es programmiert.
Lassen Sie uns jetzt die an Bord befindliche LED zum Leuchten bringen.


Wechseln Sie in den ``CREATIVE MODE`` und klicken Sie auf den **Neues Projekt**-Button,
dann erscheint ein neues Projekt im Abschnitt **MEINE PROJEKTE** und 
es wird ein zufälliger Name zugewiesen, der auf der Programmierseite geändert werden kann.

|media9-s|

Öffnen Sie dann das gerade erstellte neue Projekt.

|media11-s|

Gehen Sie nun zur Piper Make Programmierseite.

|piper_intro1|

* **START**: Wird verwendet, um den Code auszuführen; wenn er grau ist, ist er derzeit nicht mit dem Pico W verbunden.
* **Blockpalette**: enthält verschiedene Arten von Blöcken.
* **VERBINDEN**: Dient zum Verbinden mit dem Pico W; es ist grün, wenn es nicht mit dem Pico W verbunden ist, und wird zu **TRENNEN (rot)**, wenn die Verbindung hergestellt ist.
* **Programmierbereich**: Ziehen Sie Blöcke hierher, um das Programmieren durch Stapeln abzuschließen.
* **Werkzeugbereich**: Sie können **DIGITALE ANSICHT** klicken, um die Pin-Verteilung des Pico W zu sehen; Sie können die Druckinformationen in **KONSOLE** einsehen; Sie können Daten aus **DATEN** lesen, und Sie können **Python** klicken, um den Python-Quellcode einzusehen.
* **Projektname und -beschreibung**: Sie können den Projektnamen und die Beschreibung ändern.
* **DOWNLOAD**: Sie können auf den **DOWNLOAD**-Button klicken, um ihn lokal zu speichern, normalerweise im **|**-Format. Beim nächsten Mal können Sie ihn über den **Projekt importieren**-Button auf der Startseite importieren.

Klicken Sie auf die **Chip**-Palette und ziehen Sie den [start]-Block in den **Programmierbereich**.

|media12|

Ziehen Sie dann den [Schleife]-Block aus der **Schleifen**-Palette an das Ende des [start]-Blocks und stellen Sie das Schleifenintervall auf 1 Sekunde ein.

|media14|

Die an Bord befindliche LED des Raspberry Pi Pico 2 befindet sich an Pin25, also verwenden wir den [Pin () EIN/AUS schalten]-Block aus der **Chip**-Palette, um sie zu steuern.

|media15|

.. _connect_pico_per:

2. Mit dem Pico W verbinden
------------------------------

Klicken Sie jetzt auf den **VERBINDEN**-Button, um eine Verbindung zum Pico W herzustellen, nachdem Sie darauf geklickt haben, erscheint ein neues Popup.

|media16|

Wählen Sie den erkannten **CircuitPython CDC-Steuerung (COMXX)**-Port, dann klicken Sie auf **Verbinden**. 

|pico_port|

Wenn die Verbindung erfolgreich ist, wird das grüne **VERBINDEN** in der unteren linken Ecke zu einem roten **TRENNEN**.

|disconnect_per|

3. Den Code ausführen
------------------------

Klicken Sie nun auf den **START**-Button, um diesen Code auszuführen, und Sie werden sehen, dass die LED auf dem Pico W aufleuchtet. Wenn es grau ist, bedeutet das, dass das Pico W nicht verbunden ist, bitte verbinden Sie es erneut.

|media166|

Schalten Sie dann jeden Sekunde im Zyklus den Pin25 aus und klicken Sie erneut auf **START** oben links, damit Sie sehen können, wie die an Bord befindliche LED blinkt.

|media17|
