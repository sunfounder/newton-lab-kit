.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_pump:


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
    *   - 8
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

We'll write a simple MicroPython program to start the pump. The pump will run continuously once the code is executed.

.. note::

    * Open the ``3.6_pumping.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    


.. code-block:: python

    import machine
    import utime

    # Define the control pins connected to the L293D
    pump_in1 = machine.Pin(14, machine.Pin.OUT)
    pump_in2 = machine.Pin(15, machine.Pin.OUT)

    # Start the pump by setting IN1 high and IN2 low
    pump_in1.high()
    pump_in2.low()

    # Keep the pump running indefinitely
    while True:
        utime.sleep(1)

When the code is running, the pump should start running, and water should flow through the tubing.

**Understanding the Code**

#. Import Modules:

   * ``machine``: Access to hardware-related functions.
   * ``utime``: Time-related functions for delays.

#. Initialize Control Pins:

   ``pump_in1`` and ``pump_in2`` control the pump via the L293D.

   .. code-block:: python

      pump_in1 = machine.Pin(14, machine.Pin.OUT)
      pump_in2 = machine.Pin(15, machine.Pin.OUT)

#. Start the Pump:

   Sets the pump to run in one direction by applying a high signal to IN1 and a low signal to IN2.

   .. code-block:: python

      pump_in1.high()
      pump_in2.low()

#. Keep the Pump Running: 

   An infinite loop keeps the program running.

   .. code-block:: python

      while True:
          utime.sleep(1)


**Troubleshooting Tips**

* Pump Doesn't Start:

  * Check all wiring connections.
  * Ensure the power supply module is set to 5V and turned on.
  * Make sure the pump is submerged in water.

* Pico Becomes Unresponsive:

  * If the Pico disconnects or the program stops, you may need to reset it.
  * Use the reset connection by momentarily connecting the RUN pin to GND.

* Pump Continues Running After Stopping the Script:

  * The last state of the GPIO pins remains unchanged after stopping the script.
  * Reset the Pico to stop the pump by connecting RUN to GND.

  |wiring_run_reset|

**Safety Precautions**

* Electrical Safety:

  * Be cautious when working with water and electronics.
  * Keep the Pico and other electronic components away from water to prevent damage or injury.

* Pump Care:

  * Do not let the pump run dry.
  * Clean the pump regularly if using it with water that may contain particles.

**Conclusion**

In this lesson, you've learned how to control a small water pump using the Raspberry Pi Pico 2 and an L293D motor driver. This setup can be the foundation for projects like automated plant watering systems or miniature fountains.
