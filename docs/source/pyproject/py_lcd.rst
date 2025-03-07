.. note:: 

    Hallo, willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community auf Facebook! Tauchen Sie tiefer in die Welt von Raspberry Pi, Arduino und ESP32 mit Gleichgesinnten ein.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Probleme nach dem Verkauf und technische Herausforderungen mit Hilfe unserer Community und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Tutorials aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Giveaways**: Nehmen Sie an Giveaways und Feiertagsaktionen teil.

    👉 Bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_lcd:

3.4 Flüssigkristallanzeige (LCD1602)
======================================

In dieser Lektion lernen wir, wie man ein **1602 LCD** mit dem Raspberry Pi Pico 2 verwendet, um Text anzuzeigen. Das LCD1602 ist ein zeichenbasiertes Flüssigkristalldisplay, das 16 Zeichen auf 2 Linien anzeigen kann, was es ideal für Projekte macht, die Informationen wie Nachrichten, Sensordaten oder Statusaktualisierungen anzeigen müssen.

Das direkte Verbinden eines LCDs mit einem Mikrocontroller erfordert normalerweise viele GPIO-Pins, was die Funktionalität Ihres Projekts einschränken kann. Um dieses Problem zu lösen, können wir ein LCD1602-Modul verwenden, das über eine **I2C-Schnittstelle** verfügt. Das I2C-Protokoll verwendet nur zwei Datenleitungen (SDA und SCL), was Ihnen erlaubt, das LCD mit nur zwei GPIO-Pins zu steuern, wodurch andere Pins für zusätzliche Sensoren oder Geräte frei werden.

**Verständnis von I2C auf dem Raspberry Pi Pico 2**

Der Raspberry Pi Pico 2 unterstützt die I2C-Kommunikation über mehrere GPIO-Pins und bietet Flexibilität für Ihre Projekte. Er verfügt über zwei I2C-Busse, I2C0 und I2C1, die jeweils verschiedenen Pins zugeordnet werden können.

Hier ist eine Übersicht der I2C-fähigen Pins auf dem Pico 2:

|pin_i2c|

Sie können jedes passende Paar von SDA- und SCL-Pins für entweder I2C0 oder I2C1 wählen. Diese Flexibilität ermöglicht es Ihnen, Pin-Konflikte mit anderen Peripheriegeräten in Ihrem Projekt zu vermeiden.

**Was Sie benötigen**

In diesem Projekt benötigen Sie die folgenden Komponenten. 

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

Sie können diese auch einzeln über die untenstehenden Links kaufen.

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
        - :ref:`cpn_i2c_lcd`
        - 1
        - |link_i2clcd1602_buy|

**Schaltplan**

|sch_lcd_ar|

**Verdrahtungsplan**

|wiring_lcd_ar|

**Schreiben des Codes**

Schreiben wir ein MicroPython-Programm, um Nachrichten auf dem LCD1602 anzuzeigen.

.. note::

   * Öffnen Sie ``3.4_liquid_crystal_display.py`` aus ``newton-lab-kit/micropython`` oder kopieren Sie den Code in Thonny, dann klicken Sie auf "Ausführen" oder drücken Sie F5.
   * Stellen Sie sicher, dass der korrekte Interpreter ausgewählt ist: MicroPython (Raspberry Pi Pico).COMxx.  
   * Hier benötigen Sie die Bibliothek ``lcd1602.py``, bitte überprüfen Sie, ob sie auf Pico hochgeladen wurde, für eine detaillierte Anleitung siehe :ref:`add_libraries_py`.

.. code-block:: python

   from machine import I2C, Pin
   from lcd1602 import LCD
   import utime

   # I2C-Kommunikation initialisieren (I2C0)
   i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   # Ein LCD-Objekt erstellen
   lcd = LCD(i2c)

   # Die erste Nachricht anzeigen
   lcd.clear()
   lcd.message("Hello, World!")
   utime.sleep(2)

   # Zur zweiten Zeile wechseln und eine weitere Nachricht anzeigen
   lcd.write(0, 1,"LCD1602 with I2C")  # Spalte 0, Zeile 1
   utime.sleep(5)

   # Das Display löschen
   lcd.clear()

Wenn der Code ausgeführt wird, sehen Sie:

* Das LCD sollte "Hallo, Welt!" in der ersten Zeile anzeigen.
* Nach 2 Sekunden wird die zweite Zeile "LCD1602 mit I2C" anzeigen.
* Nach weiteren 5 Sekunden wird das Display gelöscht.

**Verständnis des Codes**

#. Importieren von Modulen:

   * ``machine``: Bietet Zugang zur Hardware.
   * ``lcd1602``: Eigene Bibliothek zur Steuerung des LCD.
   * ``utime``: Zeitbezogene Funktionen für Verzögerungen.

#. I2C-Kommunikation initialisieren:

   .. code-block:: python
   
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)
   
   * ``I2C(0, ...)``: Verwendet den I2C0-Bus.
   * ``sda=Pin(4)``: Setzt GP4 als SDA.
   * ``scl=Pin(5)``: Setzt GP5 als SCL.
   * ``freq=400000``: Stellt die I2C-Frequenz auf 400kHz ein.

#. Ein LCD-Objekt erstellen:

   * ``lcd = LCD(i2c)``: Erstellt eine Instanz der LCD-Klasse und übergibt das I2C-Objekt.

#. Nachrichten anzeigen:

   * ``lcd.clear()``: Löscht jeglichen vorhandenen Text auf dem Display.
   * ``lcd.message("Hello, World!")``: Zeigt die Zeichenkette "Hallo, Welt!" auf dem LCD an.
   * ``utime.sleep(2)``: Wartet 2 Sekunden, bevor der nächste Befehl ausgeführt wird.

#. Cursor bewegen und weiteren Text anzeigen:

   * ``lcd.write(0, 1,"LCD1602 with I2C")``: Bewegt den Cursor zur ersten Spalte der zweiten Zeile und zeigt die Zeichenkette in der zweiten Zeile an.

#. Letzte Verzögerung und Löschen:

   * ``utime.sleep(5)``: Wartet 5 Sekunden
   * ``lcd.clear()``: Löscht das Display.

**Weitere Experimente**

* **Benutzerdefinierte Nachrichten anzeigen**: Ändern Sie die Zeichenketten in ``lcd.message()``, um Ihre eigenen Nachrichten anzuzeigen.
* **Zeilenumbrüche verwenden**: Da das LCD1602 zwei Zeilen hat, können Sie den Cursor mit ``(0, 1, message[i:i+16])`` in die zweite Zeile verschieben.
* **Scrolltext erstellen**: Sie können einen Scroll-Effekt erzeugen, indem Sie die Anzeige innerhalb einer Schleife aktualisieren.

  .. code-block:: python

      from machine import I2C, Pin
      from lcd1602 import LCD
      import utime

      # I2C-Kommunikation initialisieren (I2C0)
      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

      # Ein LCD-Objekt erstellen
      lcd = LCD(i2c)

      message = "Scrolling Text Demo "
      lcd.clear()
      while True:
         for i in range(len(message)):
            lcd.write(0, 0, message[i:i+16])  # Zeige jeweils 16 Zeichen
            utime.sleep(0.3)

**Tipps zur Fehlerbehebung**

* Falsche Zeichen oder keine Anzeige:

  * Stellen Sie sicher, dass die Verdrahtung korrekt ist, insbesondere die SDA- und SCL-Verbindungen.
  * Überprüfen Sie, ob die I2C-Adresse in der lcd1602-Bibliothek mit der Adresse Ihres LCD übereinstimmt. Häufig sind 0x27 oder 0x3F voreingestellt.

* Kontrast einstellen:

  Einige LCD-Module haben ein Kontraststellpotentiometer. Wenn nichts auf dem Bildschirm erscheint, versuchen Sie, es einzustellen.

* Stromversorgung:

  Stellen Sie sicher, dass das LCD ausreichend mit Strom versorgt wird. Wenn Sie 5V verwenden, schließen Sie es an den VSYS-Pin des Pico an (wenn über USB gespeist) oder an eine externe 5V-Stromquelle.

* Verständnis der I2C-Adressen

  Wenn Ihr LCD keinen Text anzeigt, ist es möglich, dass es eine andere I2C-Adresse verwendet. Sie können Geräte auf dem I2C-Bus scannen:

  .. code-block:: python
  
      from machine import I2C, Pin
      i2c = I2C(0, sda=Pin(4), scl=Pin(5))
      devices = i2c.scan()

      # Die I2C-Adressen im Hexadezimalformat ausgeben
      print("I2C addresses found:", [hex(device) for device in devices])

  Dies zeigt die Adressen von Geräten an, die an den I2C-Bus angeschlossen sind. Aktualisieren Sie die lcd1602.py-Bibliothek oder Ihren Code, um die korrekte Adresse zu verwenden.

**Fazit**

Sie haben erfolgreich gelernt, wie man ein LCD1602-Display über die I2C-Schnittstelle mit Ihrem Raspberry Pi Pico 2 steuert! Diese Fähigkeit ermöglicht es Ihnen, Ihren Projekten eine visuelle Ausgabe hinzuzufügen, was sie interaktiver und informativer macht.
