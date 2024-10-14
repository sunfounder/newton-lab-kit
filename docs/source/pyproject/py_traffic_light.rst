.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_traffic_light:

7.6 Building a Traffic Light Controller
==============================================================

In this project, we'll create a **Traffic Light Controller** using the Raspberry Pi Pico 2, three LEDs (red, yellow, green), and a 4-digit 7-segment display. This system will simulate a real traffic light sequence, displaying the remaining time for each light on the 7-segment display.

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
        - 7(220Ω)
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
        - :ref:`cpn_led`
        - 3
        - |link_led_buy|

**Understanding the Components**

* **LEDs**: Represent the traffic lights. We'll control them to simulate the standard traffic light sequence.
* **4-Digit 7-Segment Display**: Shows the countdown timer for each light.
* **74HC595 Shift Register**: Allow us to control multiple outputs (segments and digits of the display) using fewer GPIO pins on the Pico.


**Circuit Diagram**

|sch_traffic_light|


* This circuit is based on the :ref:`py_74hc_4dig` with the addition of 3 LEDs.
* The 3 red, yellow and green LEDs are connected to GP7~GP9 respectively.

**Wiring Diagram**

|wiring_traffic_light| 

**Writing the Code**

We'll write a MicroPython script that:

* Controls the traffic light sequence.
* Displays the countdown timer on the 7-segment display.
* Uses shift registers to control the display.

.. note::

    * Open the ``7.6_traffic_light.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 

.. code-block:: python

    import machine
    import utime
    from machine import Timer

    # Define the duration for each traffic light color in seconds [Green, Yellow, Red]
    light_time = [30, 5, 30]  # [Green, Yellow, Red]

    # 7-segment display codes for digits 0-9 (common cathode)
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

    # Initialize GPIO pins for shift registers
    SDI = machine.Pin(18, machine.Pin.OUT)    # Serial Data Input
    SRCLK = machine.Pin(19, machine.Pin.OUT)  # Shift Register Clock
    RCLK = machine.Pin(20, machine.Pin.OUT)   # Storage Register Clock (Latch)

    # Initialize list to store 4 digit control pins for the 7-segment display
    digit_pins = [10, 13, 12, 11]  # Adjust according to your wiring
    digit_controls = [machine.Pin(pin, machine.Pin.OUT) for pin in digit_pins]

    # Initialize LED pins
    led_pins = [7, 8, 9]  # Red, Yellow, Green LEDs connected to GP7, GP8, GP9
    leds = [machine.Pin(pin, machine.Pin.OUT) for pin in led_pins]

    # Function to select which digit to display
    def select_digit(digit):
        for i in range(4):
            digit_controls[i].value(1)  # Turn off all digits (assuming common cathode)
        digit_controls[digit].value(0)  # Turn on the selected digit

    # Function to shift out data to the shift registers
    def shift_out(data):
        RCLK.value(0)  # Prepare for data shift
        for bit in range(15, -1, -1):
            SRCLK.value(0)
            SDI.value((data >> bit) & 0x01)
            SRCLK.value(1)
        RCLK.value(1)  # Latch the data

    # Function to display a number on the 7-segment display
    def display_number(num):
        digits = [
            num // 1000 % 10,
            num // 100 % 10,
            num // 10 % 10,
            num % 10
        ]
        for i in range(4):
            select_digit(i)
            segment_data = SEGMENT_CODES[digits[i]]
            # Prepare data for both shift registers (segments and digit controls)
            data = (segment_data << 8) | 0xFF  # Digit controls are managed separately
            shift_out(data)
            utime.sleep_ms(2)

    # Function to update the LEDs based on the current state
    def update_leds(state):
        # States: 0 = Green, 1 = Yellow, 2 = Red
        for i in range(3):
            leds[i].value(0)
        leds[state].value(1)

    # Timer variables
    counter = light_time[0]  # Start with green light duration
    current_state = 0  # 0 = Green, 1 = Yellow, 2 = Red

    # Timer interrupt callback to update the traffic light state and counter
    def timer_callback(t):
        global counter, current_state
        counter -= 1
        if counter <= 0:
            current_state = (current_state + 1) % 3  # Cycle through the states
            counter = light_time[current_state]  # Reset counter for the new state
            update_leds(current_state)

    # Initialize the timer
    timer = Timer(period=1000, mode=Timer.PERIODIC, callback=timer_callback)

    # Initial LED state
    update_leds(current_state)

    # Main loop
    try:
        while True:
            display_number(counter)
    except KeyboardInterrupt:
        timer.deinit()
        print("Program stopped.")

When the code runs, the green LED will light up first, and the display will show a countdown from 30.
After 30 seconds, the yellow LED will light up, and the display will count down from 5.
Then, the red LED will light up, and the display will count down from 30.
The cycle repeats indefinitely.

**Understanding the Code**

#. Imports and Pin Definitions:

   * ``machine, utime, Timer``: Modules for hardware control and timing.
   * ``Define SDI, SRCLK, RCLK``: For controlling the shift registers.
   * ``digit_controls``: List of pins controlling the digits of the display.
   * ``leds``: List of pins controlling the LEDs.

#. Segment Codes:

   * ``SEGMENT_CODES``: Defines which segments to light up for digits 0-9.

#. Display Functions:

   * ``select_digit(digit)``: Activates a specific digit on the display.
   * ``shift_out(data)``: Sends data to the shift registers.
   * ``display_number(num)``: Breaks down the number into digits and displays them using multiplexing.

#. LED Control:

   * ``update_leds(state)``: Turns on the appropriate LED based on the current traffic light state.

#. Timer and State Management:

   * ``counter``: Tracks the remaining time for the current light.
   * ``current_state``: Indicates the current traffic light state.
   * ``timer_callback(t)``: Decrements the counter and switches states when necessary.
   * ``timer``: Initializes a hardware timer to call timer_callback every second.

#. Main Loop:

   * Continuously updates the display to show the remaining time.
   * Uses a try-except block to handle a KeyboardInterrupt gracefully.

**Experimenting Further**

* Adjust Timing:

  Change the light_time list to adjust the durations for each light.

* Add Pedestrian Crossing:

  Implement buttons and additional LEDs to simulate pedestrian crossing signals.

* Improve Display:

  Modify the code to add features like blinking the LED when time is almost up.

* Simulate Real Traffic Lights:

  Add more complex sequences, such as left-turn signals or multiple intersections.

**Conclusion**

You've successfully built a Traffic Light Controller using the Raspberry Pi Pico 2! This project demonstrates how microcontrollers can be used to control hardware components like LEDs and displays, and how timers and interrupts can create real-time applications.

Feel free to expand upon this project, adding new features or integrating it into a larger system.