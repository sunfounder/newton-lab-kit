.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_788bs:

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

.. note::

   * You can open the file ``5.4_8x8_pixel_graphics.ino`` from ``newton-lab-kit/arduino/5.4_8x8_pixel_graphics``. 
   * Or copy this code into **Arduino IDE**.
   * Select the Raspberry Pi Pico 2 board and the correct port, then click "Upload".

// Define the GPIO pins connected to the 74HC595 shift registers
const int DS = 18;    // GPIO 18 -> DS (Pin 14) of first 74HC595
const int SHCP = 20;  // GPIO 20 -> SHCP (Pin 11) of both 74HC595s
const int STCP = 19;  // GPIO 19 -> STCP (Pin 12) of both 74HC595s

// Array to hold the 'X' pattern for the 8x8 LED matrix
const byte pattern[] = {
  0b10000001, // Row 0
  0b01000010, // Row 1
  0b00100100, // Row 2
  0b00011000, // Row 3
  0b00011000, // Row 4
  0b00100100, // Row 5
  0b01000010, // Row 6
  0b10000001  // Row 7
};

void setup() {
  // Initialize the control pins as outputs
  pinMode(DS, OUTPUT);
  pinMode(SHCP, OUTPUT);
  pinMode(STCP, OUTPUT);
}

void loop() {
  for (int i = 0; i < 8; i++) {
    // Set STCP to LOW to prepare for data
    digitalWrite(STCP, LOW);
    
    // Shift out the row data
    shiftOut(DS, SHCP, MSBFIRST, pattern[i]);
    
    // Shift out the column data (activating one column at a time)
    shiftOut(DS, SHCP, MSBFIRST, 0x80 >> i);
    
    // Set STCP to HIGH to latch the data to the output pins
    digitalWrite(STCP, HIGH);
    
    delay(2); // Short delay for persistence of vision
  }
}
Uploading the Code
Connect Your Pico:

Ensure your Raspberry Pi Pico is connected to your computer via the micro USB cable.
Open the Arduino IDE:

Launch the Arduino IDE on your computer.
Create a New Sketch:

Copy and paste the above code into a new sketch.
Select the Board and Port:

Go to Tools > Board and select Raspberry Pi Pico.
Go to Tools > Port and select the correct COM port for your Pico.
Upload the Code:

Click the Upload button to program the Pico.
Understanding the Code
Defining Control Pins:

cpp
Copy code
const int DS = 18;    // GPIO 18 -> DS (Pin 14) of first 74HC595
const int SHCP = 20;  // GPIO 20 -> SHCP (Pin 11) of both 74HC595s
const int STCP = 19;  // GPIO 19 -> STCP (Pin 12) of both 74HC595s
DS (Data Serial Input): Receives serial data to be shifted into the first 74HC595.
SHCP (Shift Register Clock Input): Controls the shifting of data into the shift registers.
STCP (Storage Register Clock Input): Controls the latching of data from the shift registers to the output pins.
Creating the 'X' Pattern:

cpp
Copy code
const byte pattern[] = {
  0b10000001, // Row 0
  0b01000010, // Row 1
  0b00100100, // Row 2
  0b00011000, // Row 3
  0b00011000, // Row 4
  0b00100100, // Row 5
  0b01000010, // Row 6
  0b10000001  // Row 7
};
Each byte in the pattern array represents a row in the LED matrix.
A 1 in a bit position turns on the corresponding LED in that row.
This specific pattern creates an 'X' across the 8x8 matrix.
Setup Function:

cpp
Copy code
void setup() {
  // Initialize the control pins as outputs
  pinMode(DS, OUTPUT);
  pinMode(SHCP, OUTPUT);
  pinMode(STCP, OUTPUT);
}
Sets the DS, SHCP, and STCP pins as outputs to send data to the shift registers.
Loop Function:

cpp
Copy code
void loop() {
  for (int i = 0; i < 8; i++) {
    // Set STCP to LOW to prepare for data
    digitalWrite(STCP, LOW);
    
    // Shift out the row data
    shiftOut(DS, SHCP, MSBFIRST, pattern[i]);
    
    // Shift out the column data (activating one column at a time)
    shiftOut(DS, SHCP, MSBFIRST, 0x80 >> i);
    
    // Set STCP to HIGH to latch the data to the output pins
    digitalWrite(STCP, HIGH);
    
    delay(2); // Short delay for persistence of vision
  }
}
Iterating Through Rows and Columns:
The for loop cycles through each of the 8 rows.
For each iteration:
Row Data: Sends the pattern for the current row.
Column Data: Activates one column at a time by shifting out 0x80 >> i, which shifts a single 1 bit across the 8 columns.
Latching Data:
Setting STCP LOW prepares the shift registers to receive new data.
After shifting out both row and column data, setting STCP HIGH latches the data, updating the LED states.
Persistence of Vision:
A short delay(2) ensures that the human eye perceives the LEDs as steadily lit without flickering.
Testing the Circuit
Power Up the Circuit:

Ensure all connections are secure.
Power the Raspberry Pi Pico via the micro USB cable.
Observe the LED Matrix:

The LED matrix should display an 'X' pattern by lighting up the appropriate LEDs.
If the pattern is not visible, try adjusting the timing or check the wiring connections.
Troubleshooting:

No LEDs Lighting Up:
Verify all power connections.
Ensure that the shift registers are properly connected to the Pico.
Check that the resistors are correctly placed to limit current to the LEDs.
Incorrect Patterns:
Double-check the pattern array to ensure the correct binary values.
Ensure that the rows and columns are correctly wired to the shift registers.
Flickering or Unstable Display:
Adjust the delay value in the loop to find a balance between performance and visual stability.
Ensure that power supply is stable and sufficient for the number of LEDs being used.
Conclusion
In this lesson, you've learned how to control an 8x8 LED matrix using the Raspberry Pi Pico and two 74HC595 shift registers. By leveraging shift registers, you can efficiently manage multiple LEDs with minimal GPIO usage, allowing for more complex and interactive projects. Understanding how to send serial data and latch it into parallel outputs enables you to create dynamic patterns and graphics on the LED matrix.

Further Exploration
Creating Animations:
Develop more complex patterns and animations by modifying the pattern array or adding multiple pattern arrays.
Implementing Scrolling Text:
Use shift registers to create scrolling text across the LED matrix by shifting the display patterns over time.
Interactive Displays:
Combine the LED matrix with input devices like buttons or sensors to create interactive displays that respond to user input.
Expanding with More Shift Registers:
Chain additional 74HC595 shift registers to control larger LED matrices or other peripherals.
Adding Colors:
Use RGB LED matrices to display colorful patterns by controlling multiple color channels for each LED.