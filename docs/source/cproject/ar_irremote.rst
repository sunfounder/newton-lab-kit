.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ar_irremote:

6.4 Using an Infrared Remote Control
==========================================================

In this lesson, we'll learn how to use an **infrared (IR) remote control** and an **IR receiver** with the Raspberry Pi Pico 2. This will allow us to receive and decode signals from an IR remote, enabling us to control our projects wirelessly.

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
        - :ref:`cpn_ir_receiver`
        - 1
        - |link_receiver_buy|

**Understanding Infrared Communication**

Infrared communication involves transmitting data wirelessly using infrared light. Common household devices like TVs and DVD players use IR remote controls for operation.

* **IR Transmitter (Remote Control):** Emits modulated infrared light when a button is pressed.
* **IR Receiver:** Detects the modulated IR light and converts it into electrical signals that can be decoded.

**Circuit Diagram**

|sch_irrecv|

**Wiring Diagram**

|wiring_irrecv|


**Writing the Code**

We'll write a program that initializes the IR receiver, listens for incoming IR signals, decodes them, and prints the corresponding button presses to the Serial Monitor.

.. note::

    * You can open the file ``6.4_ir_remote_control.ino`` from ``newton-lab-kit/arduino/6.4_ir_remote_control``. 
    * Or copy this code into **Arduino IDE**.
    * Select the **Raspberry Pi Pico 2** board and the correct port, then click "Upload".
    * The ``IRremote`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_ir.png

.. code-block:: arduino

    #include <IRremote.h>

    // Define the connection pin for the IR receiver
    const int IR_RECEIVE_PIN = 17;

    // Create an IR receiver object
    IRrecv irrecv(IR_RECEIVE_PIN);
    decode_results results;

    void setup() {
      // Initialize serial communication at 115200 baud
      Serial.begin(115200);
      Serial.println("IR Remote Control Test");

      // Initialize the IR receiver
      irrecv.enableIRIn(); // Start the receiver
    }

    void loop() {
      // Check if an IR signal has been received
      if (irrecv.decode(&results)) {
        // Decode the received value
        String key = decodeKeyValue(results.value);
        if (key != "ERROR") {
          Serial.println(key); // Print the decoded key to Serial Monitor
        } else {
          Serial.println("Unknown Command");
        }
        irrecv.resume(); // Receive the next value
      }
    }

    // Function to map received IR signals to corresponding keys
    String decodeKeyValue(unsigned long value) {
      // Each case corresponds to a specific IR command
      switch (value) {
        case 0x16:
          return "0";
        case 0xC:
          return "1";
        case 0x18:
          return "2";
        case 0x5E:
          return "3";
        case 0x8:
          return "4";
        case 0x1C:
          return "5";
        case 0x5A:
          return "6";
        case 0x42:
          return "7";
        case 0x52:
          return "8";
        case 0x4A:
          return "9";
        case 0x9:
          return "+";
        case 0x15:
          return "-";
        case 0x7:
          return "EQ";
        case 0xD:
          return "U/SD";
        case 0x19:
          return "CYCLE";
        case 0x44:
          return "PLAY/PAUSE";
        case 0x43:
          return "FORWARD";
        case 0x40:
          return "BACKWARD";
        case 0x45:
          return "POWER";
        case 0x47:
          return "MUTE";
        case 0x46:
          return "MODE";
        case 0x0:
          return "ERROR";
        default:
          return "ERROR";
      }
    }

After uploading the code, press buttons on the IR remote control. Observe the corresponding key labels printed in the Serial Monitor.

.. code-block:: arduino

  IR Remote Control Test
  1
  2
  PLAY/PAUSE
  5
  Unknown Command

.. note::

  The new remote control may have a plastic piece at the end to isolate the battery. Pull out this plastic piece to activate the remote.


**Understanding the Code**

#. Including Libraries and Defining Constants:

   * ``IRremote.h``: Includes the IRremote library to handle IR signal reception and decoding.
   * ``IR_RECEIVE_PIN``: Specifies the GPIO pin connected to the IR receiver's data pin.
   * ``irrecv``: Creates an IR receiver object to manage incoming IR signals.
   * ``results``: Stores the decoded IR signal data.
  
#. Setup Function:

   * **Serial Communication**: Starts serial communication for debugging and displaying received IR signals.
   * **IR Receiver Initialization**: Enables the IR receiver to start listening for incoming signals.

   .. code-block:: arduino

      void setup() {
        // Initialize serial communication at 115200 baud
        Serial.begin(115200);
        Serial.println("IR Remote Control Test");
      
        // Initialize the IR receiver
        irrecv.enableIRIn(); // Start the receiver
      }

#. Loop Function:

   * **IR Signal Detection**: Checks if the IR receiver has detected a signal.
   * **Signal Decoding**: Uses the ``decodeKeyValue()`` function to map the received IR value to a readable key.
   * **Serial Output**: Prints the decoded key to the Serial Monitor for easy identification.
   * **Prepare for Next Signal**: Resets the IR receiver to listen for the next incoming signal.

   .. code-block:: arduino

      void loop() {
        // Check if an IR signal has been received
        if (irrecv.decode(&results)) {
          // Decode the received value
          String key = decodeKeyValue(results.value);
          if (key != "ERROR") {
            Serial.println(key); // Print the decoded key to Serial Monitor
          } else {
            Serial.println("Unknown Command");
          }
          irrecv.resume(); // Receive the next value
        }
      }


#. Helper Function - Decoding IR Signals:

   * **Purpose**: Maps specific IR codes to corresponding key labels for easier understanding.
   * **Usage**: Converts raw IR codes received from the remote into readable strings that represent button presses.
   * **Error Handling**: Returns "ERROR" for unknown or unmapped IR codes.

   .. code-block:: arduino

      // Function to map received IR signals to corresponding keys
      String decodeKeyValue(unsigned long value) {
        // Each case corresponds to a specific IR command
        switch (value) {
          case 0x16:
            return "0";
          case 0xC:
            return "1";
          ...
          case 0x47:
            return "MUTE";
          case 0x46:
            return "MODE";
          case 0x0:
            return "ERROR";
          default:
            return "ERROR";
        }
      }


**Troubleshooting**

* No Readings Displayed:

  * Ensure the IR receiver is properly connected to GPIO 17.
  * Verify that the IR receiver is receiving power (VCC and GND connections).
  * Check that the correct GPIO pin is defined in the code (``IR_RECEIVE_PIN``).

* Incorrect Readings:

  * Confirm that the remote control is compatible with the IR receiver.
  * Check that the ``decodeKeyValue()`` function correctly maps the IR codes from your specific remote.
  * Use a universal remote to ensure compatibility.

* Unknown Commands:

  * Update the ``decodeKeyValue()`` function to include the IR codes specific to your remote control.
  * Use an IR decoding tool or reference to find the correct codes emitted by your remote.

* Signal Interference:

  * Ensure there are no obstructions between the remote and the IR receiver.
  * Avoid placing the sensor near other IR-emitting devices that might cause interference.

**Further Exploration**

* Controlling Devices with IR Signals:

  Use decoded IR signals to control LEDs, motors, servos, or other actuators based on remote inputs.

* Creating a Universal Remote:

  Expand the ``decodeKeyValue()`` function to support multiple remotes by mapping a broader range of IR codes.

* Adding Feedback Mechanisms:

  Implement LCD or OLED displays to show the current state or received commands.

**Conclusion**

In this lesson, you've learned how to use an infrared (IR) remote control and an IR receiver with the Raspberry Pi Pico to receive and decode IR signals. By integrating the IRremote library, you can easily interpret remote control inputs and use them to interact with your projects wirelessly. This setup is foundational for creating remote-controlled devices, automated systems, and user-friendly interfaces in various applications.

