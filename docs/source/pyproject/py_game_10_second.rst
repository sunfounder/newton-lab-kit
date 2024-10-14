.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_10_second:

7.5 Creating a "10 Second" Game
======================================================

In this engaging project, we'll build a fun game called **"10 Second"** using the Raspberry Pi Pico 2, a tilt switch, and a 4-digit 7-segment display. The objective of the game is to shake a magic wand (simulated using the tilt switch attached to a stick) to start a timer, and then shake it again to stop the timer as close to **10.00 seconds** as possible. It's a great way to test your timing skills and challenge friends to see who is the true time wizard!

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
        - 5(4-220Ω, 1-10KΩ)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|
    *   - 8
        - :ref:`cpn_tilt`
        - 1
        - 

**Understanding the Components**

* **Tilt Switch**: A sensor that detects orientation or movement. When tilted, it completes or breaks a circuit, allowing us to detect shaking or movement.
* **4-Digit 7-Segment Display**: Displays numbers from 0000 to 9999. We'll use shift registers to control the display using fewer GPIO pins.
* **74HC595 Shift Register**: 8-bit serial-in, parallel-out shift register that allow us to control multiple outputs with just a few GPIO pins.


**Circuit Diagram**

|sch_10_second|


* This circuit is based on :ref:`py_74hc_4dig` with the addition of a tilt switch.
* GP16 is high when the tilt switch is upright; low when tilted.

**Wiring Diagram**

|wiring_game_10_second| 

**Writing the Code**

We'll write a MicroPython script that:

* Detects shaking using the tilt switch.
* Starts and stops a timer based on the tilt switch.
* Displays the elapsed time on the 4-digit 7-segment display.
* Uses multiplexing and shift registers to control the display.

.. code-block:: python

    from machine import Pin
    import utime

    # Define GPIO pins for the shift registers
    SDI = Pin(18, Pin.OUT)   # Serial Data Input
    SRCLK = Pin(19, Pin.OUT) # Shift Register Clock
    RCLK = Pin(20, Pin.OUT)  # Storage Register Clock (Latch)

    # 7-segment display segment codes for digits 0-9 (common cathode)
    SEGMENT_CODES = [0x3F,  # 0
                    0x06,  # 1
                    0x5B,  # 2
                    0x4F,  # 3
                    0x66,  # 4
                    0x6D,  # 5
                    0x7D,  # 6
                    0x07,  # 7
                    0x7F,  # 8
                    0x6F]  # 9

    # Define digit selection codes (active LOW for common cathode)
    DIGIT_CODES = [0xE,  # Digit 1 (leftmost)
                0xD,  # Digit 2
                0xB,  # Digit 3
                0x7]  # Digit 4 (rightmost)

    # Initialize the tilt switch
    tilt_switch = Pin(16, Pin.IN, Pin.PULL_DOWN)

    # Variables for timing
    start_time = 0
    elapsed_time = 0
    counting = False

    # Function to shift out data to the shift registers
    def shift_out(data):
        for bit in range(15, -1, -1):
            SRCLK.low()
            SDI.value((data >> bit) & 0x01)
            SRCLK.high()
        RCLK.low()
        RCLK.high()

    # Function to display the elapsed time
    def display_time(time_ms):
        # Convert time to centiseconds (hundredths of a second)
        centiseconds = int(time_ms / 10)
        # Limit to 9999 to fit the display
        if centiseconds > 9999:
            centiseconds = 9999

        # Split the time into individual digits
        digits = [centiseconds // 1000 % 10,
                centiseconds // 100 % 10,
                centiseconds // 10 % 10,
                centiseconds % 10]

        # Multiplexing: rapidly display each digit
        for i in range(4):
            # Prepare the data for shift registers
            segment_data = SEGMENT_CODES[digits[i]]
            # Add decimal point after the second digit
            if i == 1:
                segment_data |= 0x80  # Set DP segment
            digit_data = DIGIT_CODES[i]
            data = (segment_data << 8) | digit_data
            shift_out(data)
            utime.sleep_ms(2)  # Small delay for persistence of vision

    # Interrupt handler for the tilt switch
    def tilt_handler(pin):
        global counting, start_time, elapsed_time
        if not counting:
            # Start counting
            counting = True
            start_time = utime.ticks_ms()
        else:
            # Stop counting
            counting = False
            elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

    # Set up tilt switch interrupt
    tilt_switch.irq(trigger=Pin.IRQ_RISING, handler=tilt_handler)

    # Main loop
    while True:
        if counting:
            # Calculate elapsed time
            current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
            display_time(current_time)
        else:
            # Display the final time
            display_time(elapsed_time)


When the code is running, the 4-digit 7-segment display should initialize and show 00.00.

* Start the Timer:

  * Shake the wand or tilt the tilt switch to trigger the interrupt.
  * The timer will start counting up from 00.00.

* Stop the Timer:

  * Shake the wand or tilt the switch again.
  * The timer will stop, displaying the final time.

* Objective:

  * Try to stop the timer as close to 10.00 seconds as possible.
  * Challenge friends to see who can get the closest!


**Understanding the Code**

#. Imports and Pin Definitions:

   * ``machine.Pin``: For controlling GPIO pins.
   * ``utime``: For timing functions.
   * Define SDI, SRCLK, and RCLK pins for controlling the shift registers.
   * Initialize the tilt switch on GP16 with a pull-down resistor.

#. Segment and Digit Codes:

   * ``SEGMENT_CODES``: A list containing the binary codes for displaying digits 0-9 on a 7-segment display.
   * ``DIGIT_CODES``: Codes to select each digit of the display. Active LOW for common cathode displays.

   .. code-block:: python

        SEGMENT_CODES = [0x3F,  # 0
                        0x06,  # 1
                        0x5B,  # 2
                        0x4F,  # 3
                        0x66,  # 4
                        0x6D,  # 5
                        0x7D,  # 6
                        0x07,  # 7
                        0x7F,  # 8
                        0x6F]  # 9

        # Define digit selection codes (active LOW for common cathode)
        DIGIT_CODES = [0xE,  # Digit 1 (leftmost)
                    0xD,  # Digit 2
                    0xB,  # Digit 3
                    0x7]  # Digit 4 (rightmost)

#. Variables for Timing:

   * ``start_time``: Records the time when the timer starts.
   * ``elapsed_time``: Stores the total elapsed time when the timer stops.
   * ``counting``: A boolean flag indicating whether the timer is running.

#. ``shift_out`` Function:

   * Shifts out 16 bits of data to the two shift registers.
   * **Data Format**: Upper 8 bits are segment data, lower 8 bits are digit control data.
   * **Bit Order**: MSB first.

   .. code-block:: python

        def shift_out(data):
            for bit in range(15, -1, -1):
                SRCLK.low()
                SDI.value((data >> bit) & 0x01)
                SRCLK.high()
            RCLK.low()
            RCLK.high()

#. ``display_time`` Function:

   * Converts the elapsed time from milliseconds to centiseconds (hundredths of a second).
   * Splits the time into individual digits.
   * Uses multiplexing to display each digit rapidly.
   * Adds a decimal point after the second digit to display time as XX.XX seconds.

   .. code-block:: python

        def display_time(time_ms):
            # Convert time to centiseconds (hundredths of a second)
            centiseconds = int(time_ms / 10)
            # Limit to 9999 to fit the display
            if centiseconds > 9999:
                centiseconds = 9999
                ...
                shift_out(data)
                utime.sleep_ms(2)  # Small delay for persistence of vision

#. ``tilt_handler`` Function:

   * Triggered by the tilt switch interrupt.
   * Toggles the counting state.
   * Records the ``start_time`` when counting starts.
   * Calculates the ``elapsed_time`` when counting stops.

   .. code-block:: python

        def tilt_handler(pin):
            global counting, start_time, elapsed_time
            if not counting:
                # Start counting
                counting = True
                start_time = utime.ticks_ms()
            else:
                # Stop counting
                counting = False
                elapsed_time = utime.ticks_diff(utime.ticks_ms(), start_time)

#. Main Loop:

   * If counting is ``True``, continuously updates the display with the current elapsed time.
   * If counting is ``False``, displays the final ``elapsed_time``.

   .. code-block:: python

        while True:
            if counting:
                # Calculate elapsed time
                current_time = utime.ticks_diff(utime.ticks_ms(), start_time)
                display_time(current_time)
            else:
                # Display the final time
                display_time(elapsed_time)

**Troubleshooting**

* Display Issues:

  * If the display is not showing numbers correctly, verify the segment and digit codes, and check the wiring connections.
  * Ensure that the shift register is connected properly and that data is being shifted out in the correct order.

* Tilt Switch Sensitivity:

  * If the tilt switch is too sensitive or not sensitive enough, consider adjusting its orientation or replacing it with a different type.
  * Ensure that the pull-down resistor is correctly connected to prevent false triggers.

* Timing Accuracy:

  * The timer relies on the system clock, which is reasonably accurate but may have slight variances.
  * For improved accuracy, use an external real-time clock (RTC) module.

**Extensions and Enhancements**

* Visual Effects:

  * Add LEDs that flash or change color when the timer stops.
  * Use a buzzer to provide audio feedback when starting and stopping the timer.

* High Score Tracking:

  * Modify the code to store the best (closest to 10.00) time achieved.
  * Display a congratulatory message or animation for new high scores.

* Multiplayer Mode:

  * Allow multiple players to take turns, storing each player's time.
  * Display player numbers and their respective times.

* Difficulty Levels:

  * Introduce different target times (e.g., 5.00 seconds, 15.00 seconds) to increase the challenge.
  * Randomize the target time and display it at the beginning of each round.

* Alternate Input Methods:

  * Replace the tilt switch with a button or another sensor for starting and stopping the timer.
  * Use a motion sensor to detect specific gestures.

**Conclusion**

You've successfully built a "10 Second" Game using the Raspberry Pi Pico 2! This project combines sensor input, timing functions, and display control to create an interactive and entertaining game. It's an excellent example of how microcontrollers can be used to create fun and engaging experiences.

Feel free to customize and expand upon this project. Whether it's adding new features, improving the design, or integrating additional components, the possibilities are endless.
