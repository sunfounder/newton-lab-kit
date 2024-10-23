import machine
import utime

# Define the control pins
motor_in1 = machine.Pin(14, machine.Pin.OUT)
motor_in2 = machine.Pin(15, machine.Pin.OUT)

def rotate_clockwise():
    motor_in1.high()
    motor_in2.low()

def rotate_counterclockwise():
    motor_in1.low()
    motor_in2.high()

def stop_motor():
    motor_in1.low()
    motor_in2.low()

while True:
    rotate_clockwise()
    utime.sleep(1)
    stop_motor()
    utime.sleep(1)
    rotate_counterclockwise()
    utime.sleep(1)
    stop_motor()