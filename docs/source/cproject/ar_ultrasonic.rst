.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_ultrasonic:

6.1 Measuring Distance with an Ultrasonic Sensor
================================================

In this lesson, we'll learn how to use an **ultrasonic sensor module** with the Raspberry Pi Pico 2 to measure the distance to an object. Ultrasonic sensors are commonly used in robotics and automation systems for object detection and distance measurement.

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
        - :ref:`cpn_ultrasonic`
        - 1
        - |link_ultrasonic_buy|

**Understanding the Ultrasonic Sensor**

The ultrasonic sensor works by emitting a short ultrasonic pulse from the **Trig** pin and listening for the echo on the **Echo** pin. By measuring the time it takes for the echo to return, we can calculate the distance to an object using the speed of sound.

|ultrasonic_prin|

* **Trigger Pulse**: A 10-microsecond high pulse on the Trig pin initiates the measurement.
* **Ultrasonic Burst**: The sensor emits an 8-cycle ultrasonic burst at 40 kHz.
* **Echo Reception**: The Echo pin goes high, and stays high until the echo is received back.
* **Time Measurement**: By measuring the time the Echo pin stays high, we can calculate the distance.


**Circuit Diagram**

|sch_ultrasonic|

**Wiring Diagram**

|wiring_ultrasonic|

**Writing the Code**

.. note::

   * You can open the file ``6.1_ultrasonic.ino`` from ``newton-lab-kit/arduino/6.1_ultrasonic``. 
   * Or copy this code into **Arduino IDE**.


   * Select the Raspberry Pi Pico 2 board and the correct port, then click "Upload".

.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/631a1663-ce45-4d46-b8f0-7d10f32097a9/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


Once the program is running, the Serial Monitor will print out the distance of the ultrasonic sensor from the obstacle ahead.


**Understanding the Code**

About the application of ultrasonic sensor, we can directly check the
subfunction.

.. code-block:: arduino

    float readSensorData(){// ...}

``PING`` is triggered by a HIGH pulse of 2 or more microseconds. (Give a
short ``LOW`` pulse beforehand to ensure a clean ``HIGH`` pulse.)

.. code-block:: arduino

    digitalWrite(trigPin, LOW); 
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH); 
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW); 

The echo pin is used to read signal from PING, a ``HIGH`` pulse whose
duration is the time (in microseconds) from the sending of the ping to
the reception of echo of the object.

.. code-block:: arduino

    microsecond=pulseIn(echoPin, HIGH);

The speed of sound is 340 m/s or 29 microseconds per centimeter.

This gives the distance travelled by the ping, outbound and return, so
we divide by 2 to get the distance of the obstacle.

.. code-block:: arduino

    float distance = microsecond / 29.00 / 2;  


Note that the ultrasonic sensor will pause the program when it is working, which may cause some lagging when writing complex projects.

