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

In this lesson, we'll learn how to use an **infrared (IR) remote control** and an **IR receiver module** with the Raspberry Pi Pico 2. This will allow us to receive and decode signals from an IR remote, enabling us to control our projects wirelessly.

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
* **IR Receiver Module:** Detects the modulated IR light and converts it into electrical signals that can be decoded.

**Circuit Diagram**

|sch_irrecv|

**Wiring Diagram**

|wiring_irrecv|


**Writing the Code**

.. note::

    * You can open the file ``6.4_ir_remote_control.ino`` from ``newton-lab-kit/arduino/6.4_ir_remote_control``. 
    * Or copy this code into **Arduino IDE**.
    * Select the Raspberry Pi Pico 2 board and the correct port, then click "Upload".
    * The ``IRremote`` library is used here, you can install it from the **Library Manager**.

      .. image:: img/lib_ir.png


.. raw:: html
    
    <iframe src=https://create.arduino.cc/editor/sunfounder01/71f50561-d1ad-4d9e-9db2-8eb7727df0a4/preview?embed style="height:510px;width:100%;margin:10px 0" frameborder=0></iframe>


The new remote control has a plastic piece at the end to isolate the battery inside. You need to pull out this plastic piece to power up the remote when you are using it.
Once the program is running, when you press the remote control, the Serial Monitor will print out the key you pressed.


**Understanding the Code**

This code is designed to work with an infrared (IR) remote control using the ``IRremote`` library. Here's the breakdown:

#. Including the library and defining constants. First, the IRremote library is included, and the pin number for the IR receiver is defined as 2.

   .. code-block:: cpp
 
     #include <IRremote.h>
     const int IR_RECEIVE_PIN = 17;


#. Initializes serial communication at a baud rate of 115200. Initializes the IR receiver on the specified pin (``IR_RECEIVE_PIN``) and enables LED feedback (if applicable).

   .. code-block:: arduino

       void setup() {
           Serial.begin(115200);                                     // Start serial communication at 115200 baud rate
           IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK);  // Start the IR receiver
       }

#. The loop runs continuously to process incoming IR remote signals.

   .. code-block:: arduino

      void loop() {
         if (IrReceiver.decode()) {  // Check if the IR receiver has received a signal
            bool result = 0;
            String key = decodeKeyValue(IrReceiver.decodedIRData.command);
            if (key != "ERROR") {
              Serial.println(key);  // Print the readable command
              delay(100);
            }
         IrReceiver.resume();  // Prepare the IR receiver to receive the next signal
        }
      }
   
   * Checks if an IR signal is received and successfully decoded.
   * Decodes the IR command and stores it in ``decodedValue`` using a custom ``decodeKeyValue()`` function.
   * Prints the decoded IR value to the serial monitor.
   * Resumes IR signal reception for the next signal.

   .. raw:: html

        <br/>

#. Helper function to map received IR signals to corresponding keys

   .. image:: img/ir_key.png
      :align: center
      :width: 80%

   .. code-block:: arduino

      // Function to map received IR signals to corresponding keys
      String decodeKeyValue(long result) {
        // Each case corresponds to a specific IR command
        switch (result) {
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


