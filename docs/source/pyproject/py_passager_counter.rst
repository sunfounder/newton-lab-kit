.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_passage_counter:


7.4 Passager Counter
====================

For large shopping malls, shopping centers, chain stores, airports, stations, museums, and public places such as exhibition halls, passenger traffic is an indispensable data.

In airports and stations, for example, the number of people needs to be strictly controlled to ensure safety and smooth flow.
It is also possible to know when there are more visitors in shopping centers and chain stores, how many orders each user can generate, etc.
As a result, we can analyze people's consumption habits and increase turnover.

Passenger counters can help people understand the operation of these public places and organize their operations efficiently.

A simple passager counter is created using a PIR sensor and a 4-digit 7-segment display.


**Schematic**

|sch_passager_counter| 

* This circuit is based on the :ref:`py_74hc_4dig` with the addition of a PIR module.
* The PIR will send a high signal of about 2.8s long when someone passes by.
* The PIR module has two potentiometers: one adjusts sensitivity, the other adjusts detection distance. To make the PIR module work better, you need to turn both of them counterclockwise to the end.

    |img_PIR_TTE|


**Wiring**


|wiring_passager_counter| 


**Code**

.. note::

    * Open the ``7.4_passager_counter.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Initialize PIR sensor on pin 16, configured as an input
    pir_sensor = machine.Pin(16, machine.Pin.IN)

    # 7-segment display codes for digits 0-9, using hexadecimal to represent LED segments
    SEGCODE = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]

    # Define pins for shift register communication (74HC595)
    sdi = machine.Pin(18, machine.Pin.OUT)   # Serial Data Input
    rclk = machine.Pin(19, machine.Pin.OUT)  # Register Clock (Latch)
    srclk = machine.Pin(20, machine.Pin.OUT) # Shift Register Clock

    # Initialize list to store 4 digit control pins
    placePin = []

    # Define control pins for each of the four digits (common anodes)
    pin = [10,13,12,11] # Pin numbers for the 4-digit display
    for i in range(4):
        placePin.append(None)  # Reserve space in list
        placePin[i] = machine.Pin(pin[i], machine.Pin.OUT)  # Initialize pin as output

    # Initialize counter to keep track of detected motion events
    count = 0

    # Function to select which digit (0-3) to display by controlling the common anode pins
    def pickDigit(digit):
        for i in range(4):
            placePin[i].value(1)  # Turn off all digits
        placePin[digit].value(0)  # Turn on the selected digit

    # Function to clear the display by sending '0x00' to the shift register
    def clearDisplay():
        hc595_shift(0x00)

    # Function to send data to the shift register (74HC595)
    def hc595_shift(dat):
        rclk.low()  # Pull latch low to prepare for data shifting
        time.sleep_us(200)  # Small delay for timing stability
        for bit in range(7, -1, -1):  # Loop through each bit (MSB first)
            srclk.low()  # Prepare to send the next bit
            time.sleep_us(200)
            value = 1 & (dat >> bit)  # Extract the current bit from the data
            sdi.value(value)  # Set the data line to the current bit value
            time.sleep_us(200)
            srclk.high()  # Pulse the shift clock to store the bit in the register
            time.sleep_us(200)
        time.sleep_us(200)
        rclk.high()  # Pulse the register clock to move the data to the output

    # Interrupt handler for PIR sensor, triggered on motion detection (rising edge)
    # Increments the motion count each time the sensor is triggered
    def motion_detected(pin):
        global count
        count = count + 1  # Increment the count when motion is detected

    # Set up an interrupt to detect motion using the PIR sensor
    pir_sensor.irq(trigger=machine.Pin.IRQ_RISING, handler=motion_detected)

    # Main loop to continuously update the 7-segment display with the current count
    while True:
        # Update the first digit (units place)
        pickDigit(0)
        hc595_shift(SEGCODE[count % 10])

        # Update the second digit (tens place)
        pickDigit(1)
        hc595_shift(SEGCODE[count % 100 // 10])

        # Update the third digit (hundreds place)
        pickDigit(2)
        hc595_shift(SEGCODE[count % 1000 // 100])

        # Update the fourth digit (thousands place)
        pickDigit(3)
        hc595_shift(SEGCODE[count % 10000 // 1000])


When the code is run, the number on the 4-digit 7-segment display will be added by one if someone passes in front of the PIR module.

