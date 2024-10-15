.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_pump:

3.6 Controlling a Water Pump
=============================

In this lesson, we'll learn how to control a **small water pump** using the Raspberry Pi Pico 2 and an **L293D motor driver**. A small centrifugal pump can be used for projects like automatic plant watering systems or creating miniature water features. Controlling the pump is similar to controlling a DC motor, as it uses the same principles.

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
        - :ref:`cpn_l293d`
        - 1
        - 
    *   - 6
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 7
        - 9V Battery
        - 1
        -  
    *   - 9
        - :ref:`cpn_pump`
        - 1
        -  

**Important Notes Before You Begin**

* **Pump Setup**: Connect the tubing to the pump's outlet. Submerge the pump in water before powering it on.
* **Avoid Dry Running**: Ensure the pump is always submerged. Running the pump dry can cause overheating and damage the motor.
* **Prevent Clogging**: If you're using the pump for watering plants, make sure the water is free of debris to prevent clogging.
* **Priming the Pump**: If water doesn't come out initially, there might be air trapped in the tubing. You may need to prime the pump by allowing water to flow through to remove air bubbles.

**Circuit Diagram**

|sch_pump|

L293D is a motor driver chip, EN is connected to 5V to make L293D work. 1A and 2A are the inputs connected to GP15 and GP14 respectively; 1Y and 2Y are the outputs connected to the two ends of the motor.

Y (output) is in phase with A (input), so if GP15 and GP14 are given different levels respectively, the direction of motor rotation can be changed.


**Wiring Diagram**

|wiring_pump|

In this circuit, you will see that the button is connected to the RUN pin. This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer, and the button needs to be pressed (for the Pico's **RUN** pin to receive a low level) to reset.


**Writing the Code**

.. note::

   * You can open the file ``3.6_pumping.ino`` from ``newton-lab-kit/arduino/3.6_pumping``. 
   * Or copy this code into **Arduino IDE**.
   * Select the **Raspberry Pi Pico 2** board and the correct port, then click "Upload".

.. code-block:: arduino

    const int IN1 = 15; // GPIO pin connected to Input 1A
    const int IN2 = 14; // GPIO pin connected to Input 2A

    void setup() {
      pinMode(IN1, OUTPUT);
      pinMode(IN2, OUTPUT);
    }

    void loop() {
      // Turn the pump on
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      delay(5000); // Run for 5 seconds

      // Stop the pump
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(5000); // Stop for 5 seconds
    }

After uploading the code:

* The pump should run for 5 seconds, pumping water through the tubing.
* Then, it will stop for 5 seconds.
* This cycle repeats indefinitely.
* If water doesn't flow initially, make sure the pump is submerged, and there are no air bubbles in the tubing.

**Safety Precautions**

* Water and Electricity:

  * Be extremely careful to keep water away from the Pico and other electronic components.
  * Ensure all connections are secure and insulated if necessary.

* Power Supply:

  * Use a power supply that matches the pump's voltage requirements (typically 3V-6V).
  * Do not power the pump directly from the Pico's 3.3V pin.

* Current Draw:

  * Pumps can draw significant current.
  * Ensure your power source can handle the pump's current requirements.

* Resetting the Pico:

  If you encounter issues uploading code after running the pump, you can manually reset the Pico by connecting the RUN pin to GND momentarily.

  |wiring_run_reset|

**Further Exploration**

* Automated Plant Watering:

  Incorporate soil moisture sensors to automate the watering process based on soil dryness.

* PWM Speed Control:

  Use Pulse Width Modulation (PWM) to control the pump's speed by varying the voltage.

* Timing and Scheduling:

  Implement more complex timing using real-time clocks or schedulers.

**Conclusion**

In this lesson, you've learned how to control a small water pump using the Raspberry Pi Pico and the L293D motor driver. This technique can be used in various projects like automated plant watering systems, fountains, or hydroponic setups.


