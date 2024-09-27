.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_keypad:

4.2 4x4 Keypad
========================

The 4x4 keyboard, also known as the matrix keyboard, is a matrix of 16 keys excluded in a single panel.

The keypad can be found on devices that mainly require digital input, such as calculators, TV remote controls, push-button phones, vending machines, ATMs, combination locks, and digital door locks.

In this project, we will learn how to determine which key is pressed and get the related key value.

* :ref:`cpn_keypad`
* `E.161 - Wikipedia <https://en.wikipedia.org/wiki/E.161>`_

**Schematic**

|sch_keypad|

4 pull-down resistors are connected to each of the columns of the matrix keyboard, so that G6 ~ G9 get a stable low level when the keys are not pressed.

The rows of the keyboard (G2 ~ G5) are programmed to go high; if one of G6 ~ G9 is read high, then we know which key is pressed.

For example, if G6 is read high, then numeric key 1 is pressed; this is because the control pins of numeric key 1 are G2 and G6, when numeric key 1 is pressed, G2 and G6 will be connected together and G6 is also high.


**Wiring**

|wiring_keypad|

To make the wiring easier, in the above diagram, the column row of the matrix keyboard and the 10K resistors are inserted into the holes where G6 ~ G9 are located at the same time.


**Code**

.. note::

    * Open the ``4.2_4x4_keypad.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import time

    # Define the characters on the 4x4 keypad, where each row represents a different set of keys.
    characters = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]

    # Define the pin numbers connected to the row lines of the keypad.
    row_pins = [2, 3, 4, 5]
    row = []

    # Initialize each row pin as an output, which will be used to scan the keypad rows.
    for i in range(4):
        row.append(None)  # Add a placeholder to the row list.
        row[i] = machine.Pin(row_pins[i], machine.Pin.OUT)  # Set each row pin as output.

    # Define the pin numbers connected to the column lines of the keypad.
    col_pins = [6, 7, 8, 9]
    col = []

    # Initialize each column pin as an input, which will detect key presses.
    for i in range(4):
        col.append(None)  # Add a placeholder to the column list.
        col[i] = machine.Pin(col_pins[i], machine.Pin.IN)  # Set each column pin as input.

    def readKey():
        """Scans the keypad and returns the key that was pressed."""
        key = []  # List to store the detected key(s).
        
        # Iterate through the rows of the keypad.
        for i in range(4):
            row[i].high()  # Activate the current row.
            
            # Check the state of each column in the active row.
            for j in range(4):
                if col[j].value() == 1:  # If a key is pressed (column reads high), record the key.
                    key.append(characters[i][j])  # Map the key from the character array.
            
            row[i].low()  # Deactivate the current row.
        
        # Return the detected key(s) or None if no key was pressed.
        return None if key == [] else key

    # Variable to store the last detected key for comparison.
    last_key = None

    # Main loop to continuously check the keypad for key presses.
    while True:
        current_key = readKey()  # Read the currently pressed key(s).
        
        # If the same key is being pressed, skip processing (debouncing).
        if current_key == last_key:
            continue
        
        # Update the last_key variable with the current key.
        last_key = current_key
        
        # If a new key press is detected, print the key value(s).
        if current_key is not None:
            print(current_key)
        
        # Delay to prevent rapid polling and reduce CPU usage.
        time.sleep(0.1)



After the program runs, the Shell will print out the keys you pressed on the Keypad.

**How it works**

#. Keypad Layout:

   The keypad's characters are defined in a 2D list, where each row in the array corresponds to a row on the keypad, and each element corresponds to the character of a specific key.

   .. code-block:: python

     characters = [["1", "2", "3", "A"], ["4", "5", "6", "B"], ["7", "8", "9", "C"], ["*", "0", "#", "D"]]

#. Pin Setup:

   * The keypad’s rows and columns are connected to the microcontroller's GPIO pins.
   * The row pins ([2, 3, 4, 5]) are configured as output pins.
   * The column pins ([6, 7, 8, 9]) are configured as input pins.

   .. code-block:: python

      pin = [2, 3, 4, 5]
      row = []
      for i in range(4):
          row.append(None)
          row[i] = machine.Pin(pin[i], machine.Pin.OUT)
      
      pin = [6, 7, 8, 9]
      col = []
      for i in range(4):
          col.append(None)
          col[i] = machine.Pin(pin[i], machine.Pin.IN)
      
#. Key Detection Logic:

   * **Row Scanning**: The code activates one row at a time by setting its corresponding GPIO pin high (``row[i].high()``).
   * **Column Reading**: When a row is active, the code checks each of the column pins (``col[j].value() == 1``) to see if the column is receiving a high signal. If a column is high, it means a key on that row and column intersection is pressed.
   * The pressed key is then appended to the key list.

   .. code-block:: python

      def readKey():
          key = []
          for i in range(4):
              row[i].high()  # Activate the current row
              for j in range(4):
                  if(col[j].value() == 1):  # Check if any column is pressed
                      key.append(characters[i][j])  # Append the corresponding key
              row[i].low()  # Deactivate the current row
          return None if key == [] else key
    
   |img_keypad_pressed|


#. Debouncing:

   * In hardware keypads, when a key is pressed, mechanical "bouncing" can occur, leading to multiple keypress detections for a single press. The program uses a debouncing technique by checking if the currently pressed key is the same as the last detected key.
   * If the same key is being pressed (i.e., ``current_key == last_key``), the program skips printing the key, avoiding repeated outputs for a single press.
   
   .. code-block:: python

      if current_key == last_key:
          continue
    
#. Printing Key Values:

   If a key is pressed and it's different from the last detected key, the code prints the value to the console:
   
   .. code-block:: python

      if current_key != None:
          print(current_key)

#. Polling and Delay:

   The code continuously polls the keypad by looping indefinitely (``while True``). A short delay (``time.sleep(0.1)``) is added at the end of each loop to avoid excessive CPU usage and to allow for a readable pace of key detection.
   
   .. code-block:: python

      time.sleep(0.1)
