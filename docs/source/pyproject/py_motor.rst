.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_motor:

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

Let's write a MicroPython program to control the motor. 

.. note::

    * Open the ``3.5_small_fan.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Define the control pins
    motor_in1 = machine.Pin(14, machine.Pin.OUT)
    motor_in2 = machine.Pin(15, machine.Pin.OUT)

    def rotate_clockwise():
        motor_in1.high()
        motor_in2.low()

    def rotate_counterclockwise():
        motor_in1.low()
        motor_in2.high()

    def stop_motor():
        motor_in1.low()
        motor_in2.low()

    while True:
        rotate_clockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)
        rotate_counterclockwise()
        utime.sleep(1)
        stop_motor()
        utime.sleep(1)

When the code is running, the motor will rotate clockwise for one second, stop for one second, rotate counterclockwise for one second, and then stop for one second, in a loop.

**Understanding the Code**

#. Initialize the Pins:

   ``motor_in1`` and ``motor_in2`` are connected to GP14 and GP15, controlling the direction of the motor.

   .. code-block:: python

      motor_in1 = machine.Pin(14, machine.Pin.OUT)
      motor_in2 = machine.Pin(15, machine.Pin.OUT)

#. Define Functions:

   * ``rotate_clockwise()``: Sets ``motor_in1`` high and ``motor_in2`` low to rotate the motor clockwise.
   * ``rotate_counterclockwise()``: Sets ``motor_in1`` low and ``motor_in2`` high to rotate counterclockwise.
   * ``stop_motor()``: Sets both ``motor_in1`` and ``motor_in2`` low to stop the motor.

#. Main Loop:

   The motor rotates clockwise, stops, rotates counterclockwise, and stops again, each for one second, repeatedly.

   .. code-block:: python

      while True:
          rotate_clockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)
          rotate_counterclockwise()
          utime.sleep(1)
          stop_motor()
          utime.sleep(1)

**Troubleshooting Tips**

* Motor Keeps Spinning After Stopping the Script:

  If the motor continues to run after stopping the program, you may need to reset the Pico. Use a wire or a button to momentarily connect the RUN pin to GND, which resets the Pico.

  |wiring_run_reset|

* Pico Disconnects or Becomes Unresponsive:

  The motor may draw too much current, causing voltage fluctuations. Ensure you're using a separate power supply for the motor and that all grounds are connected.

**Conclusion**

In this lesson, you've learned how to control a DC motor using the L293D motor driver and the Raspberry Pi Pico 2. You can now control the motor's direction and create projects like a small fan or a motorized device.

**Next Steps**

* **Speed Control**: Try using PWM (Pulse Width Modulation) to control the speed of the motor by connecting the EN1 pin to a PWM-capable GPIO pin.
* **Control Multiple Motors**: Use the other channels of the L293D to control additional motors.
* **Sensor Integration**: Incorporate sensors to control the motor based on input (e.g., temperature, light).
