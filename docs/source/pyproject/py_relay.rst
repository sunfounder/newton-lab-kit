.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_relay:


2.16 Control Another Circuit with a Relay
=========================================

In this lesson, we will learn how to control another circuit using a **relay** and the Raspberry Pi Pico. A relay acts like a switch controlled by a low-voltage circuit (like Pico) to operate a high-voltage circuit. For example, you can use a relay to turn on a lamp or any other device, making it possible to automate electrical appliances.


**Components Needed**

* Raspberry Pi Pico 2
* Relay module
* S8050 NPN Transistor
* Diode (for circuit protection)
* Breadboard and power supply
* Jumper wires


**Circuit Diagram**

|sch_relay_1|

* Relay Activation:

  * The relay's coil is energized by the transistor when the Pico outputs a **high signal** (3.3V) to GP15.
  * The transistor allows current to flow through the relay, activating the switch inside.
  * The relay makes a "click" sound when switching, indicating the control of the load circuit.

* Flyback Diode:

  * The diode is placed across the relay coil to protect the transistor from voltage spikes that occur when the relay is turned off.

**Wiring Diagram**

|wiring_relay_1|

**Writing the Code**

The following code will control the relay, switching the connected circuit on and off every two seconds.

.. note::

    * Open the ``2.16_control_another_circuit.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    # Initialize the relay pin on GP15
    relay = machine.Pin(15, machine.Pin.OUT)

    while True:
        relay.value(1)  # Turn the relay on
        utime.sleep(2)  # Wait for 2 seconds
        relay.value(0)  # Turn the relay off
        utime.sleep(2)  # Wait for 2 seconds

When the code is running, you should hear a "click" sound from the relay every two seconds, indicating the circuit is being switched on and off.

**Experimenting Further**

* **Set a Timer**: Modify the code to turn the relay on for 10 minutes and then automatically turn it off.
* **Control Home Appliances**: With appropriate guidance, you can connect high-voltage devices to the relay for automation tasks such as turning lights or fans on and off.

  * The circuit should look like this: To demonstrate controlling an external circuit safely, we'll add an external 5V power supply (through a breadboard power module) to power an LED. This simulates how you could control higher voltage devices (like home appliances) using the relay. Here's how to modify the circuit:

    |sch_relay_2|
  
    |wiring_relay_2|

  * Code to Control the Relay:

    .. code-block:: python

        import machine
        import utime

        # Initialize the relay pin on GP15
        relay = machine.Pin(15, machine.Pin.OUT)

        while True:
            relay.value(1)  # Turn the relay on
            utime.sleep(2)  # Wait for 2 seconds
            relay.value(0)  # Turn the relay off
            utime.sleep(2)  # Wait for 2 seconds

    When the relay is activated (GP15 outputs high), the Normally Open (NO) and Common (C) pins of the relay connect, allowing the external 5V power to flow through the LED. The LED will light up, simulating how a relay can control an external appliance.

    When the relay is deactivated (GP15 outputs low), the Normally Open (NO) pin disconnects from the Common (C) pin, cutting off the external power, and the LED turns off.

**Safety Considerations for Controlling Real Appliances**

This example uses an LED and a 5V power source to demonstrate relay control. If you are controlling higher voltage devices (like household appliances), ensure:

* **Proper Voltage Rating**: Use a relay rated for the appropriate voltage and current for your appliance.
* **Isolation**: For safety, ensure proper isolation between the low-voltage control circuit (like the Pico) and the high-voltage appliance circuit.
* **Fuse Protection**: Consider adding fuses or circuit breakers to protect against short circuits or overloads.
* **Professional Guidance**: When working with high-voltage circuits, always seek professional guidance to ensure safe operation.

This project can serve as the basis for home automation, such as controlling lamps, fans, or other devices based on timers or sensors connected to the Raspberry Pi Pico.


**Conclusion**

By using the relay to control an external circuit, you've learned how to switch on and off external devices, such as LEDs or even higher voltage appliances. This opens the door to creating automated smart devices that can be controlled through code, offering endless possibilities for home automation and other projects.
