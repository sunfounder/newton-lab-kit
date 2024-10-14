.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_74hc_led:

5.1 Using the 74HC595 Shift Register
===========================================================

In this lesson, we'll learn how to use the **74HC595 shift register** to control multiple LEDs with just a few GPIO pins on the Raspberry Pi Pico 2. The 74HC595 is an integrated circuit (IC) that allows you to expand the number of digital outputs using a serial input. This is incredibly useful when you want to control many outputs but have limited GPIO pins available.

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
        - :ref:`cpn_resistor`
        - 8(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_led`
        - 8
        - |link_led_buy|
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|



**Understanding the 74HC595 Shift Register**

The **74HC595** is an 8-bit serial-in, parallel-out shift register with output latches. It has the ability to take serial data input and convert it into parallel output, allowing you to control 8 outputs using only 3 GPIO pins from the Pico.

**Key Pins on the 74HC595:**

|img_74jc595_pin|

* **DS (Pin 14)**: Serial Data Input
* **SHCP (Pin 11)**: Shift Register Clock Input
* **STCP (Pin 12)**: Storage Register Clock Input (Latch Pin)
* **OE (Pin 13)**: Output Enable (Active Low, connect to GND)
* **MR (Pin 10)**: Master Reset (Active Low, connect to 3.3V)
* **Q0-Q7 (Pins 15, 1-7)**: Parallel Outputs
* **VCC (Pin 16)**: Connect to 3.3V
* **GND (Pin 8)**: Connect to GND

**Circuit Diagram**

|sch_74hc_led|

**Wiring Diagram**

|wiring_74hc_led|

**Writing the Code**

Now, let's write a MicroPython program to control the LEDs through the 74HC595 shift register.

.. note::

    * Open the ``5.1_microchip_74hc595.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.

    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

    

.. code-block:: python

    import machine
    import utime

    # Define the pins connected to the 74HC595
    SDI = machine.Pin(0, machine.Pin.OUT)   # Serial Data Input (DS)
    RCLK = machine.Pin(1, machine.Pin.OUT)  # Register Clock (STCP)
    SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Register Clock (SHCP)

    # Function to send data to 74HC595
    def shift_out(data):
        for bit in range(8):
            # Extract the highest bit and send it first
            bit_val = (data & 0x80) >> 7
            SDI.value(bit_val)
            # Pulse the Shift Register Clock
            SRCLK.high()
            utime.sleep_us(1)
            SRCLK.low()
            utime.sleep_us(1)
            # Shift data left by 1 for the next bit
            data = data << 1
        # Pulse the Register Clock to latch the data
        RCLK.high()
        utime.sleep_us(1)
        RCLK.low()
        utime.sleep_us(1)

    # Main loop to demonstrate shifting patterns
    while True:
        # Light up LEDs one by one from Q0 to Q7
        for i in range(8):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # Light up LEDs one by one from Q7 to Q0
        for i in range(7, -1, -1):
            data = 1 << i
            shift_out(data)
            utime.sleep(0.2)
        # Create a moving bar effect
        for i in range(9):
            data = (1 << i) - 1
            shift_out(data)
            utime.sleep(0.2)
        # Turn off all LEDs
        shift_out(0x00)
        utime.sleep(0.5)

When you run the code, the LEDs connected to the 74HC595 shift register will display dynamic light patterns:

* **First Sequence**: LEDs light up one after another from left to right. Each LED turns on in sequence, creating the effect of a light moving across the row.
* **Second Sequence**: LEDs light up one after another from right to left, reversing the direction of the movement.
* **Third Sequence**: LEDs create a growing bar effect, where LEDs turn on cumulatively from left to right until all LEDs are lit.
* **Final Step**: All LEDs turn off briefly before the entire sequence repeats.

This results in an eye-catching display of lights moving back and forth and a bar growing across the LEDs, looping continuously.

**Explanation of the Code**

#. Import Modules:

   * ``machine``: Provides access to GPIO pins.
   * ``utime``: Contains time-related functions.

#. Define Control Pins:

   We define the GPIO pins connected to the 74HC595.

   .. code-block:: python

      SDI = machine.Pin(0, machine.Pin.OUT)   # Data Input
      RCLK = machine.Pin(1, machine.Pin.OUT)  # Latch Clock
      SRCLK = machine.Pin(2, machine.Pin.OUT) # Shift Clock

#. Shift Out Function:

   * This function sends 8 bits of data to the shift register.
   * It sends the most significant bit (MSB) first.
   * Pulses the shift register clock (SRCLK) to shift in each bit.
   * After all bits are shifted in, it pulses the register clock (RCLK) to latch the data to the outputs.

   .. code-block:: python

      def shift_out(data):
          for bit in range(8):
              bit_val = (data & 0x80) >> 7
              SDI.value(bit_val)
              SRCLK.high()
              utime.sleep_us(1)
              SRCLK.low()
              utime.sleep_us(1)
              data = data << 1
          RCLK.high()
          utime.sleep_us(1)
          RCLK.low()
          utime.sleep_us(1)
    

#. Main Loop:

   * Lights up each LED one by one from Q0 to Q7.

   .. code-block:: python

      for i in range(8):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)


   * Lights up each LED one by one from Q7 to Q0.

   .. code-block:: python

      for i in range(7, -1, -1):
          data = 1 << i
          shift_out(data)
          utime.sleep(0.2)

   * Gradually lights up LEDs to create a bar that grows from Q0 to Q7.

   .. code-block:: python

      for i in range(9):
          data = (1 << i) - 1
          shift_out(data)
          utime.sleep(0.2)

   * Sends 0x00 to turn off all LEDs.

   .. code-block:: python

     shift_out(0x00)
     utime.sleep(0.5)


**Understanding *Understanding the Code**

The 74HC595 shift register allows us to control 8 outputs using only 3 GPIO pins.
Data is shifted into the register serially on the rising edge of the Shift Register Clock (SHCP).
The Register Clock (STCP) latches the shifted data to the output pins.
By sending different byte values, we can control which LEDs are on or off.

Example: Controlling LEDs

* Data Byte: 0b00000001 lights up LED connected to Q0.
* Data Byte: 0b10000000 lights up LED connected to Q7.
* Data Byte: 0b11111111 lights up all LEDs.

**Experimenting Further**

* Create Custom Patterns:

  Modify the data sent to create different LED patterns. For example, to blink alternate LEDs:
 
  .. code-block:: python

    shift_out(0b10101010)

* Control More LEDs:

  Chain multiple 74HC595 chips together to control more outputs. Connect the Q7' (Pin 9) of the first chip to DS (Pin 14) of the second chip.

* Integrate with Sensors:

  Use inputs from sensors or buttons to change the LED patterns dynamically.

**Conclusion**

In this lesson, you've learned how to use the 74HC595 shift register to expand the output capabilities of your Raspberry Pi Pico 2. This technique is invaluable when working with projects that require controlling many outputs with limited GPIO pins.

