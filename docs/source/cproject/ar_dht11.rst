.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_dht11:

6.2 Measuring Temperature and Humidity with DHT11
=======================================================

In this lesson, we'll learn how to use a **DHT11 temperature and humidity sensor** with the Raspberry Pi Pico 2. The DHT11 is a basic, low-cost digital sensor that can measure ambient temperature and humidity, providing a calibrated digital output.

**What You'll Need**

In this project, we need the following components. 

It's definitely convenient to buy a whole kit, here's the link: 

.. list-table::
    :widths: 20 20 20
    :header-rows: 1

    *   - Name	
        - ITEMS IN THIS KIT
        - LINK
    *   - Newton Lab Kit	
        - 450+
        - |link_newton_lab_kit|

You can also buy them separately from the links below.


.. list-table::
    :widths: 5 20 5 20
    :header-rows: 1

    *   - SN
        - COMPONENT	
        - QUANTITY
        - LINK

    *   - 1
        - :ref:`cpn_pico_2`
        - 1
        - |link_pico2_buy|
    *   - 2
        - Micro USB Cable
        - 1
        - 
    *   - 3
        - :ref:`cpn_breadboard`
        - 1
        - |link_breadboard_buy|
    *   - 4
        - :ref:`cpn_wire`
        - Several
        - |link_wires_buy|
    *   - 5
        - :ref:`cpn_dht11`
        - 1
        - |link_dht22_buy|


**Understanding the DHT11 Sensor**

The **DHT11** sensor uses a capacitive humidity sensor and a thermistor to measure the surrounding air. It outputs a digital signal on the data pin, and it's fairly simple to use, but requires precise timing to read data.

* Temperature Range: 0–50 °C with ±2 °C accuracy
* Humidity Range: 20–80% RH with ±5% accuracy
* Sampling Rate: 1 Hz (once every second)

**Circuit Diagram**

|sch_dht11|

**Wiring Diagram**

|wiring_dht11|

**Writing the Code**

.. note::

    * You can open the file ``6.2_dht11.ino`` from ``newton-lab-kit/arduino/6.2_dht11``. 
    * Or copy this code into **Arduino IDE**.
    * Select the Raspberry Pi Pico 2 board and the correct port, then click "Upload".
    * The ``DHT sensor library`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_dht.png

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/b9e96e99-59d4-48ca-b41f-c03577acfb8f/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>

Once the code is running, you will see the Serial Monitor continuously print out the temperature and humidity, and as the program runs steadily, these two values will become more and more accurate.

**Understanding the Code**

#. Inclusion of necessary libraries and definition of constants.
   This part of the code includes the DHT sensor library and defines the pin number and sensor type used in this project.

   .. code-block:: arduino
    
      #include <DHT.h>
      #define DHTPIN 16       // Define the pin used to connect the sensor
      #define DHTTYPE DHT11  // Define the sensor type

#. Creation of DHT object.
   Here we create a DHT object using the defined pin number and sensor type.

   .. code-block:: arduino

      DHT dht(DHTPIN, DHTTYPE);  // Create a DHT object

#. This function is executed once when the Arduino starts. We initialize the serial communication and the DHT sensor in this function.

   .. code-block:: arduino

      void setup() {
        Serial.begin(115200);
        Serial.println(F("DHT11 test!"));
        dht.begin();  // Initialize the DHT sensor
      }

#. Main loop.
   The ``loop()`` function runs continuously after the setup function. Here, we read the humidity and temperature values, calculate the heat index, and print these values to the serial monitor.  If the sensor read fails (returns NaN), it prints an error message.

   .. note::
    
      The |link_heat_index| is a way to measure how hot it feels outside by combining the air temperature and the humidity. It is also called the "felt air temperature" or "apparent temperature".

   .. code-block:: arduino

      void loop() {
        delay(2000);
        float h = dht.readHumidity();
        float t = dht.readTemperature();
        float f = dht.readTemperature(true);
        if (isnan(h) || isnan(t) || isnan(f)) {
          Serial.println(F("Failed to read from DHT sensor!"));
          return;
        }
        float hif = dht.computeHeatIndex(f, h);
        float hic = dht.computeHeatIndex(t, h, false);
        Serial.print(F("Humidity: "));
        Serial.print(h);
        Serial.print(F("%  Temperature: "));
        Serial.print(t);
        Serial.print(F("°C "));
        Serial.print(f);
        Serial.print(F("°F  Heat index: "));
        Serial.print(hic);
        Serial.print(F("°C "));
        Serial.print(hif);
        Serial.println(F("°F"));
      }
