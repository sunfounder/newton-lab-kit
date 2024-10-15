.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_motor:

3.5 Controlling a Small Fan (DC Motor)
======================================

In this lesson, we'll learn how to control a **DC motor** (like a small fan) using the Raspberry Pi Pico 2 and an **L293D motor driver**. The L293D allows us to control the direction of the motor rotation—both clockwise and counterclockwise. Since DC motors require more current than the Pico can provide directly, we'll use an external power supply to safely power the motor.

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
        - :ref:`cpn_motor`
        - 1
        - |link_motor_buy| 
    *   - 7
        - :ref:`cpn_power_module`
        - 1
        -  
    *   - 8
        - 9V Battery
        - 1
        - 
 
**Circuit Diagram**

|sch_motor|


L293D is a motor driver chip, EN is connected to 5V to make L293D work. 1A and 2A are the inputs connected to GP15 and GP14 respectively; 1Y and 2Y are the outputs connected to the two ends of the motor.

Y (output) is in phase with A (input), so if GP15 and GP14 are given different levels respectively, the direction of motor rotation can be changed.


**Wiring Diagram**

|wiring_motor|

In this circuit, you will see that the button is connected to the RUN pin. This is because the motor is operating with too much current, which may cause the Pico to disconnect from the computer, and the button needs to be pressed (for the Pico's **RUN** pin to receive a low level) to reset.

Since DC motors require a high current, we use a power supply module to power the motor here for safety reasons.


**Writing the Code**

.. note::

   * You can open the file ``3.5_small_fan.ino`` from ``newton-lab-kit/arduino/3.5_small_fan``. 
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
      // Rotate motor clockwise
      digitalWrite(IN1, HIGH);
      digitalWrite(IN2, LOW);
      delay(2000); // Run for 2 seconds

      // Stop motor
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // Stop for 1 second

      // Rotate motor counterclockwise
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, HIGH);
      delay(2000); // Run for 2 seconds

      // Stop motor
      digitalWrite(IN1, LOW);
      digitalWrite(IN2, LOW);
      delay(1000); // Stop for 1 second
    }

After uploading the code:

* The motor should rotate in one direction for 2 seconds.
* Then, it will stop for 1 second.
* Then, it will rotate in the opposite direction for 2 seconds.
* This cycle repeats indefinitely.

**Understanding the Code**

#. Defining Control Pins:

   .. code-block:: arduino

        const int IN1 = 15; // Connected to Input 1A
        const int IN2 = 14; // Connected to Input 2A

#. Setting Pin Modes:

   .. code-block:: arduino

        void setup() {
          pinMode(IN1, OUTPUT);
          pinMode(IN2, OUTPUT);
        }

#. Controlling Motor Direction:

   * **Clockwise Rotation**: Sets IN1 HIGH and IN2 LOW, causing the motor to rotate in one direction.

   .. code-block:: arduino

        digitalWrite(IN1, HIGH);
        digitalWrite(IN2, LOW);

   * **Counterclockwise Rotation**: Sets IN1 LOW and IN2 HIGH, causing the motor to rotate in the opposite direction.

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, HIGH);


#. Stopping the Motor:

   Sets both inputs LOW, stopping the motor.

   .. code-block:: arduino

        digitalWrite(IN1, LOW);
        digitalWrite(IN2, LOW);

**Further Exploration**

* Speed Control:

  Use Pulse Width Modulation (PWM) to control the speed of the motor by connecting the EN1 pin to a PWM-capable GPIO pin and varying the duty cycle.

* Controlling Multiple Motors:

  The L293D can control two motors. Try adding a second motor and controlling it independently.

* Sensor Integration:

  Incorporate sensors (e.g., limit switches, encoders) to create more advanced motor control systems.


**Safety Precautions**

* Power Supply:

  * Ensure that the external power supply voltage matches the motor's voltage rating.
  * Do not power the motor directly from the Pico's 3.3V pin.

* Current Draw:

  * Motors can draw significant current, especially during startup or when stalled.
  * Ensure that your power supply can handle the motor's current requirements.

* Resetting the Pico:

  * In some cases, the motor's current draw may cause voltage dips, leading the Pico to reset or disconnect.
  * If you encounter issues uploading code after running the motor, you can manually reset the Pico by connecting the RUN pin to GND momentarily.

  |wiring_run_reset|


**Conclusion**

In this lesson, you've learned how to control a DC motor using the Raspberry Pi Pico and the L293D motor driver. By controlling the inputs to the L293D, you can change the direction of the motor's rotation. This fundamental concept is essential in robotics, automation, and many other applications involving motors.

