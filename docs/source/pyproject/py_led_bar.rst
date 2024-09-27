.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_led_bar:

2.2 Display the Level
=============================

In this lesson, we'll learn how to control an LED Bar Graph using the Raspberry Pi Pico 2. An LED Bar Graph consists of 10 LEDs arranged in a line, typically used to display levels such as volume, signal strength, or other measurements. We'll light up the LEDs sequentially to create a level display effect.

|img_led_bar_pin|

* :ref:`cpn_led_bar`

**Components Needed**

- Raspberry Pi Pico
- LED Bar Graph
- 10 x 220Ω resistors (color bands: red, red, black, black, brown)
- Breadboard and jumper wires

**Circuit Diagram**

|sch_ledbar|

In this project, each of the 10 LEDs in the LED Bar Graph is connected to the Raspberry Pi Pico 2. The anodes (positive terminals) of the LEDs are connected to GPIO pins GP6 through GP15. The cathodes (negative terminals) are connected through 220Ω resistors to the GND (ground) pin.

**Wiring Diagram**

|wiring_ledbar|

**Writing the Code**

.. note::

  * Open the ``2.2_display_the_level.py`` file under the path ``newton-lab-kit/micropython`` or copy the code below into Thonny. Then click "Run Current Script" or press **F5** to execute it.
  * Make sure the "MicroPython (Raspberry Pi Pico).COMxx" interpreter is selected in the bottom right corner of Thonny.
  * For detailed instructions on running code, refer to :ref:`open_run_code_py`.

.. code-block:: python

  import machine
  import utime

  # Define the GPIO pins connected to the LEDs
  pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
  leds = []

  # Initialize each pin as an output and store it in the leds list
  for pin_number in pins:
      led = machine.Pin(pin_number, machine.Pin.OUT)
      leds.append(led)

  while True:
      # Turn on LEDs one by one to simulate increasing level
      for led in leds:
          led.value(1)  # Turn the LED on
          utime.sleep(0.2)
      # Turn off LEDs one by one to simulate decreasing level
      for led in leds:
          led.value(0)  # Turn the LED off
          utime.sleep(0.2)

When you run the program, the LEDs on the LED Bar Graph will light up sequentially from the first to the last, creating an increasing level effect. Then, they will turn off one by one, simulating a decreasing level.

**Understanding the Code**

In this project, we control multiple LEDs using lists and loops in MicroPython, which makes the code efficient and easy to read.

Let's break down the key parts of the code:

1. Importing Modules:

   * ``import machine``: Provides access to the Raspberry Pi Pico's hardware functionalities.
   * ``import utime``: Allows us to use time-related functions like delays.

2. Defining Pins and Initializing LEDs:

   * We create a list ``pins`` containing the GPIO pin numbers connected to the LEDs and initialize an empty list ``leds`` to store the LED objects.

     .. code-block:: python

      # Define the GPIO pins connected to the LEDs
      pins = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
      leds = []
     
   * Using a ``for`` loop, we iterate over each pin number, set it as an output pin, and append the corresponding ``Pin`` object to the ``leds`` list.
     
     .. code-block:: python

       for pin_number in pins:
         led = machine.Pin(pin_number, machine.Pin.OUT)
         leds.append(led)
     
3. Creating the Level Display Effect:

   * The ``while True:`` loop runs indefinitely.
   * Increasing Level:

     * Use a ``for`` loop to iterate over each ``led`` in the ``leds`` list.
     * ``led.value(1)`` turns the LED on.
     * ``utime.sleep(0.2)`` adds a 200ms delay before the next LED turns on.
     
     .. code-block:: python

        for led in leds:
            led.value(1)
            utime.sleep(0.2)
     
   * Decreasing Level:

     * Turn off each LED one by one using another ``for`` loop.
     * ``led.value(0)`` turns the LED off.

     .. code-block:: python

      for led in leds:
          led.value(0)
          utime.sleep(0.2)
  
**Modifying the Code**

Feel free to experiment with the code:

* Change the Speed:

  * Adjust the delay in ``utime.sleep(0.2)`` to make the LEDs light up faster or slower.

* Reverse the Order:

  * Use ``reversed(leds)`` to reverse the sequence of the LEDs.

    .. code-block:: python

        for led in reversed(leds):
            led.value(1)
            utime.sleep(0.2)
    
* Create a Ping-Pong Effect:

  * Make the LEDs light up from left to right and then back from right to left.

    .. code-block:: python

        while True:
            for led in leds:
                led.value(1)
                utime.sleep(0.1)
            for led in reversed(leds):
                led.value(0)
                utime.sleep(0.1)
    
**Conclusion**

By controlling each LED individually, we've created a simple yet effective level display using the Raspberry Pi Pico. This project demonstrates the power of lists and loops in Python, allowing us to manage multiple outputs efficiently.

Understanding how to work with multiple GPIO pins and using programming structures like lists and loops is essential for more complex projects, such as creating animations, controlling multiple sensors, or building interactive devices.

**References**

* |link_python_for|
* |link_python_list|
