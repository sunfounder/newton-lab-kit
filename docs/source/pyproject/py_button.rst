.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_button:

2.5 Reading Button Value
=============================

In this lesson, we'll learn how to read input from a pushbutton using the Raspberry Pi Pico. So far, we've used the GPIO pins mainly for output, like lighting up LEDs. Now, we'll use a GPIO pin as an input to detect when a button is pressed. This is a fundamental skill for creating interactive projects.

**Components Needed**

* Raspberry Pi Pico 2
* Pushbutton
* 10 kΩ resistor (color bands: brown, black, orange, gold)
* Breadboard
* Jumper wires


**Circuit Diagram**

|sch_button|

As long as one side of the button pin is connected to 3.3v, and the other side pin is connected to GP14, then when the button is pressed, GP14 will be high. However, when the button is not pressed, GP14 is in a suspended state and may be high or low. In order to get a stable low level when the button is not pressed, GP14 needs to be reconnected to GND through a 10K pull-down resistor.

* **Button Not Pressed**: The GP14 pin is connected to GND through the resistor, so it reads **LOW (0)**.
* **Button Pressed**: The GP14 pin is connected to 3.3V through the button, so it reads **HIGH (1)**.

**Wiring Diagram**

A four-pin button is shaped like an H. Its left two pins or right two pins are connected, which means that when it crosses the central gap, it connects two half rows with the same row number. (For example, in my circuit, E23 and F23 are already connected, as are E25 and F25).

Until the button is pressed, the left and right pins are independent of each other and current cannot flow from one side to the other.

|wiring_button|


**Writing the Code**

We'll write a simple program that prints a message when the button is pressed.

.. note::

  * Open the ``2.5_read_button_value.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

  * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

  * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input pin
    button = machine.Pin(14, machine.Pin.IN)

    while True:
        if button.value() == 1:
            print("Button pressed!")
            utime.sleep(0.2)  # Debounce delay

When the code is running, you will observe the following phenomenon:

* **Not Pressed**: No message should appear.
* **Pressed**: "Button pressed!" should appear in the console each time you press the switch.



**Understanding the Code**

#. Import Modules:

   * ``machine``: Provides access to the hardware functions.
   * ``utime``: Allows us to use time-related functions like delays.

#. Set Up the Button Pin:

   * ``button = machine.Pin(14, machine.Pin.IN)``: Initializes GPIO pin 14 as an input.

#. Main Loop:

   * ``while True``: Creates an infinite loop.
   * ``if button.value() == 1``: Checks if the button is pressed.
   * ``button.value()`` returns 1 when the pin reads high (button pressed).
   * ``print("Button pressed!")``: Prints a message to the console.
   * ``utime.sleep(0.2)``: Waits for 200 milliseconds to debounce the button.

**Alternate Wiring: Pull-Up Resistor**

You can also wire the button using a pull-up resistor configuration.

#. Connect a 10kΩ resistor between GP14 and the 3.3V rail. This pulls the pin high when the button is not pressed.

    |sch_button_pullup|

    |wiring_button_pullup|

   * **Button Not Pressed**: The GP14 pin is connected to 3.3V through the resistor, so it reads HIGH (1).
   * **Button Pressed**: The GP14 pin is connected to GND through the button, so it reads LOW (0).

#. Modified Code for Pull-Up Configuration.

   .. code-block:: python
   
       import machine
       import utime
   
       # Initialize GP14 as an input pin
       button = machine.Pin(14, machine.Pin.IN)
   
       while True:
           if button.value() == 0:
               print("Button pressed!")
               utime.sleep(0.2)

**Using Internal Pull-Up/Pull-Down Resistors**

The Raspberry Pi Pico 2 allows you to enable internal pull-up or pull-down resistors, eliminating the need for external resistors.

Using internal resistors simplifies wiring and saves space by eliminating the need for additional external resistors on the breadboard.

* Enabling Internal Pull-Down Resistor:

  .. code-block:: python
  
      import machine
      import utime
  
      # Initialize GP14 as an input with an internal pull-down resistor
      button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
  
      while True:
          if button.value() == 1:
              print("Button pressed!")
              utime.sleep(0.2)

* Enabling Internal Pull-Up Resistor:

  .. code-block:: python

    import machine
    import utime

    # Initialize GP14 as an input with an internal pull-up resistor
    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

    while True:
        if button.value() == 0:
            print("Button pressed!")
            utime.sleep(0.2)

**Experimenting Further**

* **Multiple Buttons**: Connect additional buttons to other GPIO pins and modify the code to handle multiple inputs.
* **LED Control**: Combine button input with LED output to toggle the LED state when the button is pressed.

.. code-block:: python

    import machine
    import utime

    button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
    led = machine.Pin(15, machine.Pin.OUT)
    led_state = False

    while True:
        if button.value() == 1:
            led_state = not led_state  # Toggle LED state
            led.value(led_state)
            utime.sleep(0.2)

**Conclusion**

Reading input from a button is a fundamental skill in microcontroller programming. It allows you to make your projects interactive and responsive to user input. Understanding how to use pull-up and pull-down resistors ensures reliable and stable readings from your input devices.
