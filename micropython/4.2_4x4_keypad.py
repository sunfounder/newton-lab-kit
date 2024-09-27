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
