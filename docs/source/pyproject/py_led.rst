.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_led:

2.1 Hello, LED!
=================

Welcome to your first hardware project with the Raspberry Pi Pico 2! In this lesson, we'll learn how to make an LED blink using MicroPython. This simple project is a great way to get started with physical computing and understand how to control hardware with code.

* :ref:`cpn_led`

**What You'll Need**

* Raspberry Pi Pico 2 2
* LED (any color)
* 220Ω resistor (red, red, black, black, brown color bands)
* Breadboard
* Jumper wires

**Circuit Diagram**

|sch_led|

By setting the GPIO pin high or low, you're controlling the voltage output of that pin. When the pin is high, current flows through the LED (limited by the resistor), causing it to light up. When the pin is low, no current flows, and the LED turns off.

**Wiring Diagram**

|wiring_led|


**Writing the Code**

.. note::

    * Open the ``2.1_hello_led.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.
    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 
    * For detailed tutorials, please refer to :ref:`open_run_code_py`.

.. code-block:: python

    import machine
    import utime

    led = machine.Pin(15, machine.Pin.OUT)

    while True:
        led.value(1)      # Turn the LED on
        utime.sleep(1)    # Wait for 1 second
        led.value(0)      # Turn the LED off
        utime.sleep(1)    # Wait for 1 second

When the code is running, the LED is turn on for 1 second and turn off for 1 second.

**Understanding the Code**

#. Importing Libraries:

   * ``machine``: Provides access to the hardware components.
   * ``utime``: Allows us to use time-related functions like delays.

#. Setting Up the LED Pin:

   * ``led = machine.Pin(15, machine.Pin.OUT)``: Initializes GP15 as an output pin and assigns it to the variable led.


#. Creating an Infinite Loop:

   * ``while True``: Starts an endless loop to continuously run the code inside it.

#. Controlling the LED:

   * ``led.value(1)``: Sets the pin output to high (3.3V), turning the LED on.
   * ``utime.sleep(1)``: Pauses the program for 1 second.
   * ``led.value(0)``: Sets the pin output to low (0V), turning the LED off.
   * ``utime.sleep(1)``: Pauses the program for another second.

**Experimenting Further**

* **Change Blink Rate**: Modify the ``utime.sleep(1)`` values to make the LED blink faster or slower.
* **Use Different Pins**: Try connecting the LED to a different GPIO pin and update the code accordingly.
* **Multiple LEDs**: Add more LEDs to different pins and control them in your code.

**Troubleshooting**

* LED Not Lighting Up:

  * Check the orientation of the LED. Ensure the anode and cathode are connected correctly.
  * Verify all connections are secure.
  * Ensure the resistor is connected in series with the LED.

* Error Messages in Thonny:

  * Make sure you have selected the correct interpreter.
  * Check for typos in your code.

**Conclusion**

Congratulations! You've successfully made an LED blink using the Raspberry Pi Pico 2 and MicroPython. This foundational project introduces you to controlling hardware with code, setting the stage for more complex projects.


**References**

* |link_mpython_machine_pin|
* |link_mpython_machine|
* |link_mpython_utime|
* |link_python_while|