.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_micro:

2.8 Press Gently
==========================

In this lesson, we'll learn how to use a **micro switch** (also known as a limit switch) with the Raspberry Pi Pico to detect when it's pressed or released. Micro switches are commonly used in devices like microwave oven doors, printer covers, or as end stops in 3D printers because they are reliable and can handle frequent activation.

**Components Needed**

* Raspberry Pi Pico 2
* Micro switch (3-pin)
* 10 kΩ resistor (color bands: brown, black, orange, gold)
* 0.1 µF ceramic capacitor (marked as 104)
* Breadboard
* Jumper wires

**Understanding the Micro Switch**

A micro switch typically has three pins:

|img_micro_switch|

- **Common (C)**: The middle pin.
- **Normally Open (NO)**: Connected to the common pin when the switch is **pressed**.
- **Normally Closed (NC)**: Connected to the common pin when the switch is **not pressed**.

By connecting the switch appropriately, we can detect when it's pressed by reading the voltage level on a GPIO pin.

**Circuit Diagram**

|sch_limit_sw|

By default, GP14 is low and when pressed, GP14 is high.

The purpose of the 10K resistor is to keep the GP14 low during pressing.

When you press a mechanical switch, the contacts may bounce, causing multiple rapid transitions between open and closed states. The capacitor connected between GP14 and GND helps filter out this noise.

* **Switch Not Pressed**:

  * The **Common (C)** pin is connected to the **NC** pin, which is connected to **GND**.
  * **GP14** reads **LOW** (0V).

* **Switch Pressed**:

  * The **Common (C)** pin is connected to the **NO** pin, which is connected to **3.3V**.
  * **GP14** reads **HIGH** (3.3V).

**Wiring Diagram**

|wiring_limit_sw|


**Writing the Code**

We'll write a MicroPython program that detects when the micro switch is pressed and prints a message accordingly.

.. note::

  * Open the ``2.8_micro_switch.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

  * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

  * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    switch = machine.Pin(14, machine.Pin.IN)

    while True:
        if switch.value() == 1:
            print("The switch is pressed!")
            utime.sleep(0.5)  # Debounce delay

When the code is running, you will observe the following phenomenon:

* **Not Pressed**: No message should appear.
* **Pressed**: "The switch is pressed!" should appear in the console each time you press the switch.

**Understanding the Code**

#. Import Modules:

   * ``import machine``: Access to hardware functions.
   * ``import utime``: Time-related functions.

#. Initialize the Switch Pin:

   * ``switch = machine.Pin(14, machine.Pin.IN)``: Sets up GP14 as an input pin.

#. Main Loop:

   * ``while True``: Starts an infinite loop.
   * ``if switch.value() == 1``: Checks if the switch is pressed (GP14 reads HIGH).
   * ``print("The switch is pressed!")``: Outputs a message to the console.
   * ``utime.sleep(0.5)``: Adds a delay to debounce the switch and prevent multiple detections from a single press.


**Alternative Wiring: Using Internal Pull-Down Resistor**

If you prefer to simplify the wiring even further, you can rely solely on the internal pull-down resistor:

* Modify the Circuit:

  Remove the external 10 kΩ resistor and 0.1 µF capacitor.

* Modified Code:

  .. code-block:: python

      import machine
      import utime

      # Initialize GP14 as an input pin with an internal pull-down resistor
      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

      while True:
          if switch.value() == 1:
              print("The switch is pressed!")
              utime.sleep(0.5)  # Debounce delay
    

**Practical Applications**

* **Limit Detection**: Use the micro switch as an end stop in CNC machines or 3D printers to detect the limit of movement.
* **Safety Interlocks**: Ensure a device operates only when certain conditions are met (e.g., a door is closed).
* **User Input**: Incorporate into projects where a robust and reliable button is needed.

**Experimenting Further**

* Control an LED:

  Connect an LED to another GPIO pin (e.g., GP15) with a suitable resistor. Modify the code to turn the LED on when the switch is pressed.
  
  .. code-block:: python
    
    import machine
    import utime

    switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        if switch.value() == 1:
            led.value(1)  # Turn on the LED
            print("The switch is pressed!")
            utime.sleep(0.5)
        else:
            led.value(0)  # Turn off the LED

* Counting Presses:

  Modify the code to count how many times the switch has been pressed.

  * Control an LED:

   .. code-block:: python

      import machine
      import utime

      switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
      count = 0

      while True:
          if switch.value() == 1:
              count += 1
              print("Switch pressed {} times".format(count))
              utime.sleep(0.5)

**Conclusion**

Using a micro switch with the Raspberry Pi Pico allows you to detect physical interactions reliably. Understanding how to wire the switch and read its state in your code is essential for creating responsive and interactive projects.

