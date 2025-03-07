
    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Community auf Facebook! Tauchen Sie tiefer ein in Raspberry Pi, Arduino und ESP32 mit Gleichgesinnten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Kauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezielle Rabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie [|link_sf_facebook|] und treten Sie heute bei!

.. _py_mpr121:

4.3 Elektroden-Tastatur mit MPR121
========================================================

In dieser Lektion lernen wir, wie man den **MPR121 kapazitiven Berührungssensor** verwendet, um eine berührungsempfindliche Tastatur mit dem Raspberry Pi Pico 2 zu erstellen. Der MPR121 ermöglicht die Erfassung von Berührungen auf bis zu 12 Elektroden, die mit leitfähigen Materialien wie Drähten, Folie oder sogar Früchten wie Bananen verbunden werden können!

**Was Sie benötigen**

Für dieses Projekt benötigen wir die folgenden Komponenten.

Es ist definitiv praktisch, ein ganzes Kit zu kaufen, hier ist der Link:

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ARTIKEL IN DIESEM KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

Sie können sie auch einzeln über die untenstehenden Links kaufen.

.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - KOMPONENTE	
        - MENGE
        - LINK

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - Micro-USB-Kabel
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Mehrere
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_mpr121`
        - 1
        - 

**Verständnis des MPR121-Sensors**

Der **MPR121** ist ein kapazitiver Berührungssensor-Controller, der über die I2C-Schnittstelle kommuniziert. Er kann bis zu 12 Berührungseingaben verarbeiten, was ihn ideal für die Erstellung interaktiver Projekte mit mehreren Berührungspunkten macht.

Der MPR121-Sensor erkennt Änderungen der Kapazität an seinen Elektroden. Wenn Sie eine Elektrode berühren, ändert sich die Kapazität und der Sensor registriert eine Berührung. Der Sensor kommuniziert diese Informationen über I2C mit dem Raspberry Pi Pico 2.

**Schaltplan**

|sch_mpr121_ar|


**Verdrahtungsdiagramm**

|wiring_mpr121_ar|

* Verbinden Sie Drähte oder leitfähige Materialien mit den Elektrodenpins (gekennzeichnet mit **E0** bis **E11**) am MPR121.
* Sie können die anderen Enden der Drähte mit leitfähigen Objekten wie Früchten, Aluminiumfolienformen oder Touchpads verbinden.

**Code schreiben**

Schreiben wir ein MicroPython-Programm, um Berührungseingaben auf den Elektroden zu erkennen und auszugeben, welche berührt werden.

.. note::

    * Öffnen Sie die Datei ``4.3_electrode_keyboard.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
    * Stellen Sie sicher, dass der richtige Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx. 
    * Hier benötigen Sie die Bibliothek ``mpr121.py``, bitte überprüfen Sie, ob sie auf den Pico hochgeladen wurde, für ein detailliertes Tutorial siehe :ref:`add_libraries_py`.

.. code-block:: python
    
    from mpr121 import MPR121
    from machine import Pin, I2C
    import utime

    i2c = I2C(0, sda=Pin(4), scl=Pin(5))
    mpr = MPR121(i2c)

    # check all keys
    while True:
        value = mpr.get_all_states()
        if len(value) != 0:
            print(value)
        utime.sleep_ms(100)

Nach dem Starten des Programms berühren Sie die verbundenen Elektroden oder leitfähigen Objekte. Beobachten Sie die ausgegebene Druckausgabe in der Thonny Shell. Sie sollten Nachrichten sehen, die anzeigen, welche Elektroden berührt werden.

**Code verstehen**

#. Import-Module:

   * ``machine``: Bietet Zugang zu hardwarebezogenen Funktionen.
   * ``mpr121``: Die Bibliothek zur Anbindung an den MPR121-Sensor.
   * ``utime``: Enthält zeitbezogene Funktionen für Verzögerungen.

#. I2C-Kommunikation initialisieren:

   * ``i2c = I2C(0, sda=Pin(4), scl=Pin(5))``: Richtet die I2C-Kommunikation auf dem I2C0-Bus mit GP4 (SDA) und GP5 (SCL) ein.

#. Ein MPR121-Objekt erstellen:

   * ``mpr = MPR121(i2c)``: Initialisiert den MPR121-Sensor über die eingerichtete I2C-Kommunikation.

#. Hauptschleife zur Erkennung von Berührungseingaben:

   * ``get_all_states()``: Gibt eine Liste der Elektrodennummern zurück, die gerade berührt werden.
   * Wenn Elektroden berührt werden, werden ihre Nummern ausgegeben.
   * Die Schleife läuft kontinuierlich mit einer kurzen Verzögerung von 100 Millisekunden.

   .. code-block:: python

        while True:
            value = mpr.get_all_states()
            if len(value) != 0:
                print(value)
            time.sleep_ms(100)

**Erweiterung der Elektroden**

Sie können Ihr Projekt erweitern, indem Sie die Elektroden mit verschiedenen leitfähigen Materialien verbinden:

* **Früchte**: Verbinden Sie Drähte mit Bananen, Äpfeln oder anderen Früchten, um sie in berührungsempfindliche Eingaben zu verwandeln.
* **Folienformen**: Schneiden Sie Formen aus Aluminiumfolie aus und verbinden Sie sie mit den Elektroden.
* **Leitfähige Farbe**: Zeichnen Sie Muster mit leitfähiger Tinte oder Farbe.

.. note::
    
    Wenn Sie die Elektroden ändern (z. B. verschiedene Materialien anschließen), müssen Sie möglicherweise den Sensor zurücksetzen, um die Basiswerte neu zu kalibrieren.

**Weitere Experimente**

* Bestimmte Elektrode erkennen:

  Wenn Sie eine spezifische Elektrode überwachen möchten, können Sie die Methode ``is_touched(pin)`` verwenden, die True zurückgibt, wenn die angegebene Elektrode (Pin) berührt wird; andernfalls gibt sie False zurück.

  .. code-block:: python
  
        from mpr121 import MPR121
        from machine import Pin, I2C
        import utime

        i2c = I2C(0, sda=Pin(4), scl=Pin(5))
        mpr = MPR121(i2c)

        # check all keys
        while True:
          if mpr.is_touched(0):
              print("Electrode 0 is touched!")
          utime.sleep(0.1)


* **Musikinstrument erstellen**: Ordnen Sie jeder Elektrode eine Musiknote zu und spielen Sie Töne, wenn sie berührt wird.
* **Interaktive Kunst**: Verwenden Sie leitfähige Farbe, um berührungsempfindliche Kunstwerke zu schaffen.
* **Spielcontroller**: Gestalten Sie benutzerdefinierte Touch-Steuerungen für ein Spiel.


**Schlussfolgerung**

In dieser Lektion haben Sie gelernt, wie man den MPR121 kapazitiven Berührungssensor mit dem Raspberry Pi Pico 2 verwendet, um eine berührungsempfindliche Elektroden-Tastatur zu erstellen. Dies eröffnet Möglichkeiten für interaktive Projekte, die auf kreative Weise auf Berührungseingaben reagieren.


