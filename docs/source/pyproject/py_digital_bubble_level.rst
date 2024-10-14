.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_bubble_level:

7.12 Building a Digital Bubble Level
==========================================

In this project, we'll create a **Digital Bubble Level** using the Raspberry Pi Pico 2, an MPU6050 accelerometer and gyroscope module, and an 8x8 LED matrix display controlled by two 74HC595 shift registers. This device functions similarly to a traditional spirit level, indicating the tilt of a surface. As you tilt the MPU6050, a "bubble" represented by LEDs on the matrix will move accordingly, allowing you to visualize the levelness of a surface.

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
    *   - 7
        - :ref:`cpn_mpu6050`
        - 1
        - 

**Understanding the Components**

* **MPU6050 Accelerometer and Gyroscope**: Provides acceleration and angular velocity data along three axes (X, Y, Z), which we'll use to calculate the tilt angles.
* **8x8 LED Matrix Display**: An array of LEDs arranged in 8 rows and 8 columns, allowing us to display patterns or images by controlling individual LEDs.
* **74HC595 Shift Registers**: Allows us to control multiple outputs (in this case, the rows and columns of the LED matrix) using fewer GPIO pins on the Pico.

**Circuit Diagram**

|sch_bubble_level|

The MPU6050 takes the acceleration values in each direction and calculates the attitude angle.

As a result, the program draws a 2x2 dot on the dot matrix based on data from the two 74HC595 chips.

As the attitude angle changes, the program sends different data to the 74HC595 chips, and the position of the dot changes, creating a bubble effect.

**Wiring**

|wiring_digital_bubble_level| 


**Writing the Code**

We'll write a MicroPython script that:

* Reads acceleration data from the MPU6050.
* Calculates the tilt angles along the X and Y axes.
* Maps the tilt angles to positions on the 8x8 LED matrix.
* Displays a "bubble" (a 2x2 pixel representation) that moves according to the tilt.

.. note::

    * Open the ``7.12_digital_bubble_level.py`` from ``newton-lab-kit/micropython`` or copy the code into Thonny, then click "Run" or press F5.
    * Ensure the correct interpreter is selected: MicroPython (Raspberry Pi Pico).COMxx. 
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.

.. code-block:: python

    from imu import MPU6050
    from machine import Pin, I2C
    import utime
    import math

    # Initialize I2C communication for MPU6050
    i2c = I2C(1, scl=Pin(7), sda=Pin(6))
    mpu = MPU6050(i2c)

    # Initialize shift register pins
    SDI = Pin(18, Pin.OUT)    # Serial Data Input
    RCLK = Pin(19, Pin.OUT)   # Register Clock (Latch)
    SRCLK = Pin(20, Pin.OUT)  # Shift Register Clock

    # Function to shift data into the shift registers
    def shift_out(data1, data2):
        for i in range(8):
            SRCLK.value(0)
            # Shift out to first shift register (columns)
            SDI.value((data1 >> (7 - i)) & 1)
            SRCLK.value(1)
        for i in range(8):
            SRCLK.value(0)
            # Shift out to second shift register (rows)
            SDI.value((data2 >> (7 - i)) & 1)
            SRCLK.value(1)
        RCLK.value(0)
        RCLK.value(1)

    # Function to calculate the position of the bubble
    def get_bubble_position():
        accel = mpu.accel
        x_angle = math.degrees(math.atan2(accel.x, math.sqrt(accel.y ** 2 + accel.z ** 2)))
        y_angle = math.degrees(math.atan2(accel.y, math.sqrt(accel.x ** 2 + accel.z ** 2)))

        # Map angles to positions (0 to 7)
        x_pos = int(((x_angle + 90) / 180) * 7)
        y_pos = int(((y_angle + 90) / 180) * 7)

        # Clamp positions to within the matrix
        x_pos = max(0, min(7, x_pos))
        y_pos = max(0, min(7, y_pos))

        return x_pos, y_pos

    # Function to display the bubble on the LED matrix
    def display_bubble(x, y):
        # Create a buffer for the matrix
        matrix = [0x00] * 8

        # Set the bits for the bubble (2x2 pixels)
        for i in range(2):
            if y + i < 8:
                matrix[y + i] |= (0x80 >> x)
                if x + 1 < 8:
                    matrix[y + i] |= (0x80 >> (x + 1))

        # Shift out the data to the shift registers
        for row in range(8):
            cols = matrix[row]
            rows = 1 << row
            shift_out(cols, ~rows & 0xFF)
            utime.sleep_us(1000)  # Small delay to create persistence of vision

    # Main loop
    try:
        while True:
            x_pos, y_pos = get_bubble_position()
            for _ in range(50):  # Refresh the display multiple times for visibility
                display_bubble(x_pos, y_pos)
    except KeyboardInterrupt:
        pass

When the code runs, place the setup on a level surface.
The bubble (a 2x2 pixel area) should appear at the center of the LED matrix.
Tilt the breadboard or the MPU6050 module.
Observe the bubble moving on the LED matrix in the direction of the tilt, simulating a real bubble level.

**Understanding the Code**

#. Initialization:

   * I2C Communication: Set up to read data from the MPU6050.
   * Shift Register Pins: Initialized for controlling the 74HC595 shift registers.

#. Shift Register Control (``shift_out`` function):

   * Sends data to the shift registers controlling the columns and rows of the LED matrix.
   * The function first shifts out the column data, then the row data, and then latches the data to update the outputs.

   .. code-block:: python

        def shift_out(data1, data2):
            for i in range(8):
                SRCLK.value(0)
                # Shift out to first shift register (columns)
                SDI.value((data1 >> (7 - i)) & 1)
                SRCLK.value(1)
            for i in range(8):
                SRCLK.value(0)
                # Shift out to second shift register (rows)
                SDI.value((data2 >> (7 - i)) & 1)
                SRCLK.value(1)
            RCLK.value(0)
            RCLK.value(1)

#. Calculating Bubble Position (``get_bubble_position`` function):

   * Reads acceleration data from the MPU6050.
   * Calculates tilt angles along the X and Y axes.
   * Maps these angles to positions on the 8x8 grid (values from 0 to 7).
   * Uses ``math.atan2`` to calculate the tilt angle in degrees.

   .. code-block:: python

        # Function to calculate the position of the bubble
        def get_bubble_position():
            accel = mpu.accel
            x_angle = math.degrees(math.atan2(accel.x, math.sqrt(accel.y ** 2 + accel.z ** 2)))
            y_angle = math.degrees(math.atan2(accel.y, math.sqrt(accel.x ** 2 + accel.z ** 2)))

            # Map angles to positions (0 to 7)
            x_pos = int(((x_angle + 90) / 180) * 7)
            y_pos = int(((y_angle + 90) / 180) * 7)

            # Clamp positions to within the matrix
            x_pos = max(0, min(7, x_pos))
            y_pos = max(0, min(7, y_pos))

            return x_pos, y_pos

#. Displaying the Bubble (``display_bubble`` function):

   * Creates a buffer representing the LED matrix.
   * Sets bits in the buffer to represent a 2x2 pixel bubble at the calculated position.
   * Shifts out the data to the shift registers to update the LED matrix.
   * Uses multiplexing to refresh the display for persistence of vision.

   .. code-block:: python

        # Function to display the bubble on the LED matrix
        def display_bubble(x, y):
            # Create a buffer for the matrix
            matrix = [0x00] * 8

            # Set the bits for the bubble (2x2 pixels)
            for i in range(2):
                if y + i < 8:
                    matrix[y + i] |= (0x80 >> x)
                    if x + 1 < 8:
                        matrix[y + i] |= (0x80 >> (x + 1))

            # Shift out the data to the shift registers
            for row in range(8):
                cols = matrix[row]
                rows = 1 << row
                shift_out(cols, ~rows & 0xFF)
                utime.sleep_us(1000)  # Small delay to create persistence of vision

#. Main Loop:

   * Continuously updates the bubble position based on the MPU6050 readings.
   * Refreshes the display multiple times to ensure the bubble is visible.

   .. code-block:: python

       # Main loop
        try:
            while True:
                x_pos, y_pos = get_bubble_position()
                for _ in range(50):  # Refresh the display multiple times for visibility
                    display_bubble(x_pos, y_pos)
        except KeyboardInterrupt:
            pass

**Troubleshooting**

* LED Matrix Not Displaying Correctly:

  * Check all wiring connections between the shift registers and the LED matrix.
  * Ensure that the shift registers are connected properly to the Pico.
  * Verify that the common anode or cathode configuration of your LED matrix matches the code logic.

* Incorrect Bubble Movement:

  * Ensure the MPU6050 is properly connected and functioning.
  * Check that the MPU6050 is correctly oriented.

* Program Errors:

  * Ensure that ``imu.py`` and ``vector3d.py`` are correctly uploaded.
  * Check for typos or indentation errors in the code.

**Experimenting Further**

* Adjust Sensitivity:

  Modify the mapping of angles to positions to change the sensitivity of the bubble movement.

* Display Enhancements:

  * Change the size or shape of the bubble.
  * Add visual effects, such as trails or different patterns.

* Calibration:

  Implement a calibration routine to set the zero point when the device is placed on an uneven surface.

* Alternative Displays:

  Use an OLED or LCD display to show numerical angle values in addition to the visual bubble.

**Conclusion**

You've successfully built a Digital Bubble Level using the Raspberry Pi Pico 2! This project demonstrates how accelerometer data can be used to visualize orientation and tilt, and how to control an LED matrix display using shift registers.

Feel free to expand upon this project by adding new features or integrating it into larger systems.

