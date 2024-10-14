.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_74hc_4dig:

5.3 Creating a Time Counter with a 4-Digit 7-Segment Display
============================================================

In this lesson, we'll learn how to use a **4-digit 7-segment display** with the Raspberry Pi Pico 2 to create a simple time counter. The display will count up every second, showing the elapsed time in seconds.

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
        - 4(220Ω)
        - |link_resistor_buy|
    *   - 6
        - :ref:`cpn_4_dit_7_segment`
        - 1
        - 
    *   - 7
        - :ref:`cpn_74hc595`
        - 1
        - |link_74hc595_buy|


**Understanding the 4-Digit 7-Segment Display**

A 4-digit 7-segment display consists of four individual 7-segment displays combined into a single module. Each digit shares the same segment control lines (**a** to **g** and **dp**), but each digit has its own **common cathode** control. This configuration allows us to control which digit is active at any given time.

To display different numbers on each digit using shared segment lines, we use a technique called **multiplexing**. We rapidly switch between digits, updating one digit at a time, but so quickly that it appears as if all digits are displayed simultaneously due to the persistence of vision.

|4digit_control_pins|

**Circuit Diagram**

|sch_4dig|

Here the wiring principle is basically the same as :ref:`py_74hc_led`, the only difference is that Q0-Q7 are connected to the a ~ g pins of the 4-digit 7-segment display.

Then G10 ~ G13 will select which 7-segment display to work.

**Wiring Diagram**

|wiring_4dig|

* **Segment Connections (through 220 Ω resistors):**

  * **Q0** → Segment **a**
  * **Q1** → Segment **b**
  * **Q2** → Segment **c**
  * **Q3** → Segment **d**
  * **Q4** → Segment **e**
  * **Q5** → Segment **f**
  * **Q6** → Segment **g**
  * **Q7** → Segment **dp** (decimal point)

* **Common Cathode Connections (Digit Select Pins):**

  * **Digit 1 (Leftmost Digit):** Connect to **GP10** on the Pico
  * **Digit 2:** Connect to **GP11**
  * **Digit 3:** Connect to **GP12**
  * **Digit 4 (Rightmost Digit):** Connect to **GP13**

**Writing the Code**

.. note::

   * You can open the file ``5.3_time_counter.ino`` from ``newton-lab-kit/arduino/5.3_time_counter``. 
   * Or copy this code into **Arduino IDE**.


   * Select the Raspberry Pi Pico 2 board and the correct port, then click "Upload".

Below is the C++ code for the Arduino IDE that controls the 4-digit 7-segment display using a shift register and implements a time counter without using the `delay()` function.

```cpp
// Define the connection pins for the shift register
#define DATA_PIN   11  // DS (Serial Data Input)
#define LATCH_PIN  12  // STCP (Storage Register Clock)
#define CLOCK_PIN  13  // SHCP (Shift Register Clock)

// Define the digit control pins for the 4-digit 7-segment display
const int digitPins[4] = {2, 3, 4, 5}; // DIG1, DIG2, DIG3, DIG4

// Segment byte maps for numbers 0-9
const byte digitCodes[10] = {
  // Pgfedcba
  0b00111111, // 0
  0b00000110, // 1
  0b01011011, // 2
  0b01001111, // 3
  0b01100110, // 4
  0b01101101, // 5
  0b01111101, // 6
  0b00000111, // 7
  0b01111111, // 8
  0b01101111  // 9
};

unsigned long previousMillis = 0; // Stores the last time the display was updated
unsigned int counter = 0;         // Counter value

void setup() {
  // Initialize the shift register pins
  pinMode(DATA_PIN, OUTPUT);
  pinMode(LATCH_PIN, OUTPUT);
  pinMode(CLOCK_PIN, OUTPUT);

  // Initialize the digit control pins
  for (int i = 0; i < 4; i++) {
    pinMode(digitPins[i], OUTPUT);
    digitalWrite(digitPins[i], HIGH); // Turn off all digits
  }
}

void loop() {
  unsigned long currentMillis = millis();

  // Update the counter every 1000 milliseconds (1 second)
  if (currentMillis - previousMillis >= 1000) {
    previousMillis = currentMillis;
    counter++; // Increment the counter
    if (counter > 9999) {
      counter = 0; // Reset counter after 9999
    }
  }

  // Display the counter value
  displayNumber(counter);
}

void displayNumber(int num) {
  // Break the number into digits
  int digits[4];
  digits[0] = num / 1000;         // Thousands
  digits[1] = (num / 100) % 10;   // Hundreds
  digits[2] = (num / 10) % 10;    // Tens
  digits[3] = num % 10;           // Units

  // Display each digit
  for (int i = 0; i < 4; i++) {
    digitalWrite(digitPins[i], LOW); // Activate digit
    shiftOutDigit(digitCodes[digits[i]]);
    delay(5);                        // Small delay for multiplexing
    digitalWrite(digitPins[i], HIGH); // Deactivate digit
  }
}

void shiftOutDigit(byte data) {
  // Send data to the shift register
  digitalWrite(LATCH_PIN, LOW);
  shiftOut(DATA_PIN, CLOCK_PIN, MSBFIRST, data);
  digitalWrite(LATCH_PIN, HIGH);
}

*Understanding the Code
Multiplexing the Display:

Only one digit of the 7-segment display is illuminated at a time.
The displayNumber() function rapidly cycles through each digit, updating its segments according to the current counter value.
Persistence of vision makes it appear as if all digits are lit simultaneously.
Using millis() for Timing:

Instead of using delay(), we use millis() to track elapsed time without blocking the program.
This allows the display to continue multiplexing smoothly while updating the counter every second.
Shift Register Control:

The shiftOutDigit() function sends the segment data to the 74HC595 shift register.
We use shiftOut() function to transfer the byte representing the segments that should be lit for each digit.
Running the Program
Upload the Code:

Open the Arduino IDE.
Copy and paste the code into a new sketch.
Select the correct board (e.g., Arduino Uno, Raspberry Pi Pico with Arduino core) and the appropriate COM port.
Upload the code to your board.
Observe the Display:

The 4-digit 7-segment display should start counting up from 0000, incrementing by 1 every second.
The display should be clear and stable, without flickering.
Additional Notes
Avoiding delay():

Using delay() would pause the entire program, disrupting the multiplexing required for the display.
By using millis(), we can perform non-blocking timing, allowing the display to update smoothly.
Expanding Functionality:

You can modify the code to count down, display different information, or add buttons to control the counter.
Conclusion
This project demonstrates how to control a 4-digit 7-segment display using a shift register and multiplexing techniques. By efficiently managing timing with millis(), we create a responsive and accurate time counter without hindering the display's performance.