import machine
import utime

# Define the control pins connected to the L293D
pump_in1 = machine.Pin(14, machine.Pin.OUT)
pump_in2 = machine.Pin(15, machine.Pin.OUT)

# Start the pump by setting IN1 high and IN2 low
pump_in1.high()
pump_in2.low()

# Keep the pump running indefinitely
while True:
    utime.sleep(1)