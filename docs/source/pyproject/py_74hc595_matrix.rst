.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_74hc_788bs:

5.4 Displaying Graphics on an 8x8 LED Matrix
===================================================================

In this lesson, we'll learn how to control an **8x8 LED matrix** using the Raspberry Pi Pico 2 and two **74HC595 shift registers**. We'll display patterns and simple graphics by controlling individual LEDs on the matrix.

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
        - :ref:`cpn_dot_matrix`
        - 1
        - 
    *   - 6
        - :ref:`cpn_74hc595`
        - 2
        - |link_74hc595_buy|

**Understanding the 8x8 LED Matrix**

An 8x8 LED matrix consists of 64 LEDs arranged in 8 rows and 8 columns. Each LED can be individually controlled by applying voltage across its row and column. By controlling the current through each pair of rows and columns, we can control each LED to display characters or patterns.

In this setup, we'll use two 74HC595 shift registers to control the rows and columns of the LED matrix, effectively expanding the number of outputs from the Raspberry Pi Pico 2 while using only a few GPIO pins.

**Circuit Diagram**

|sch_ledmatrix|

The 8x8 LED dot matrix is controlled by two **74HC595** shift registers: one controls the rows, and the other controls the columns. These two chips share the Pico's GPIO pins **GP18**, **GP19**, and **GP20**, greatly conserving the Pico's I/O ports.

The Pico outputs a 16-bit binary number at a time. The first 8 bits are sent to the 74HC595 controlling the rows, and the last 8 bits are sent to the 74HC595 controlling the columns. This allows the dot matrix to display specific patterns.

**Q7' (Pin 9)**: This serial data output pin of the first 74HC595 connects to the **DS (Pin 14)** of the second 74HC595, enabling you to chain multiple 74HC595 chips together.

**Wiring Diagram**

Building the circuit can be complex, so let's proceed step by step.


**Step 1:**  First, insert the pico, the LED dot matrix
and two 74HC595 chips into breadboard. Connect the 3.3V and GND of the
pico to holes on the two sides of the board, then hook up pin16 and
10 of the two 74HC595 chips to VCC, pin 13 and pin 8 to GND.

.. note::
   In the Fritzing image above, the side with label is at the bottom.

|wiring_ledmatrix_4|

**Step 2:** Connect pin 11 of the two 74HC595 together, and then to
GP20; then pin 12 of the two chips, and to GP19; next, pin 14 of the
74HC595 on the left side to GP18 and pin 9 to pin 14 of the second
74HC595.

|wiring_ledmatrix_3|

**Step 3:** The 74HC595 on the right side is to control columns of the
LED dot matrix. See the table below for the mapping. Therefore, Q0-Q7
pins of the 74HC595 are mapped with pin 13, 3, 4, 10, 6, 11, 15, and 16
respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **13** | **3**  | **4**  | **10** | **6**  | **11** | **15** | **16** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_2|

**Step 4:** Now connect the ROWs of the LED dot matrix. The 74HC595 on
the left controls ROW of the LED dot matrix. See the table below for the
mapping. We can see, Q0-Q7 of the 74HC595 on the left are mapped with
pin 9, 14, 8, 12, 1, 7, 2, and 5 respectively.

+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **74HC595**        | **Q0** | **Q1** | **Q2** | **Q3** | **Q4** | **Q5** | **Q6** | **Q7** |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+
| **LED Dot Matrix** | **9**  | **14** | **8**  | **12** | **1**  | **7**  | **2**  | **5**  |
+--------------------+--------+--------+--------+--------+--------+--------+--------+--------+

|wiring_ledmatrix_1|


**Writing the Code**

We'll write a MicroPython program to display a pattern on the LED matrix.

.. note::

    * Open the ``5.4_8x8_pixel_graphics.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    

.. code-block:: python

    import machine
    import utime

    # Define the GPIO pins connected to the shift registers
    SDI = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
    SRCLK = machine.Pin(19, machine.Pin.OUT) # Shift Register Clock
    RCLK = machine.Pin(20, machine.Pin.OUT)  # Storage Register Clock (Latch)

    # Function to send data to the shift registers
    def shift_out(data1, data2):
        data = (data1 << 8) | data2  # Combine two bytes of data
        for bit in range(16):
            SRCLK.low()
            SDI.value((data >> (15 - bit)) & 0x01)
            SRCLK.high()
        RCLK.high()
        utime.sleep_us(10)
        RCLK.low()

    # Define the pattern to display (an 'X' shape)
    pattern = [
        0b10000001,  # Row 0
        0b01000010,  # Row 1
        0b00100100,  # Row 2
        0b00011000,  # Row 3
        0b00011000,  # Row 4
        0b00100100,  # Row 5
        0b01000010,  # Row 6
        0b10000001   # Row 7
    ]

    while True:
        for row in range(8):
            # Activate one row at a time
            row_data = 1 << row
            # The columns data is the pattern for that row
            col_data = pattern[row]
            # Send data to shift registers
            shift_out(~col_data & 0xFF, row_data)
            # Small delay to create persistence of vision
            utime.sleep_us(1000)

When you run this code, the 8x8 LED matrix will display an 'X' shape, with the LEDs lighting up to form the pattern of the letter 'X' across the matrix.

**Understanding the Code**

#. Initialize Control Pins:

   .. code-block:: python

        SDI = machine.Pin(18, machine.Pin.OUT)
        SRCLK = machine.Pin(19, machine.Pin.OUT)
        RCLK = machine.Pin(20, machine.Pin.OUT)

#. Shift Out Function:

   * Combines two bytes of data (data1 and data2) into a 16-bit integer.
   * Shifts out the data bit by bit, starting from the most significant bit.
   * Uses SRCLK to clock in the data and RCLK to latch the data to the outputs.

   .. code-block:: python

        def shift_out(data1, data2):
            data = (data1 << 8) | data2
            for bit in range(16):
                SRCLK.low()
                SDI.value((data >> (15 - bit)) & 0x01)
                SRCLK.high()
            RCLK.high()
            utime.sleep_us(10)
            RCLK.low()


#. Define the Pattern:

   * Each element in the pattern list represents a row in the LED matrix.
   * Each bit in a byte represents a column in that row.
   * The pattern creates an 'X' shape on the matrix.

   .. code-block:: python

        pattern = [
            0b10000001,
            0b01000010,
            0b00100100,
            0b00011000,
            0b00011000,
            0b00100100,
            0b01000010,
            0b10000001
        ]

#. Main Loop:

   * Loops through each row to refresh the display.
   * Activates one row at a time by setting the corresponding bit in ``row_data``.
   * Sends the column data (``col_data``) for that row.
   * Uses a short delay to allow the human eye to perceive the image due to persistence of vision.

   .. code-block:: python

        while True:
            for row in range(8):
                row_data = 1 << row
                col_data = pattern[row]
                shift_out(~col_data & 0xFF, row_data)
                utime.sleep_us(1000)

**Experimenting Further**

* Changing the Pattern

  Try replacing the pattern list with the following arrays to display different graphics. Replace pattern in your code with ``pattern_heart`` or ``pattern_smile`` to see different images.

  .. code-block:: python

        # Heart shape
        pattern_heart = [
            0b00000000,
            0b01100110,
            0b11111111,
            0b11111111,
            0b11111111,
            0b01111110,
            0b00111100,
            0b00011000
        ]

        # Smile face
        pattern_smile = [
            0b00111100,
            0b01000010,
            0b10100101,
            0b10000001,
            0b10100101,
            0b10011001,
            0b01000010,
            0b00111100
        ]


* Animating the Display

  Create multiple patterns and cycle through them to create animations:

  .. code-block:: python

        patterns = [pattern1, pattern2, pattern3, pattern4]

        while True:
            for pattern in patterns:
                for _ in range(50):  # Display each pattern for a short time
                    for row in range(8):
                        row_data = 1 << row
                        col_data = pattern[row]
                        shift_out(~col_data & 0xFF, row_data)
                        utime.sleep_us(1000)

* Design Your Own Patterns

  Each byte represents a row; bits set to 1 turn on the LED in that column. Create custom patterns by defining your own pattern list.

**Conclusion**

In this lesson, you've learned how to control an 8x8 LED matrix using the Raspberry Pi Pico 2 and two 74HC595 shift registers. By understanding how to manipulate bits and use shift registers, you can display patterns and graphics on the LED matrix.