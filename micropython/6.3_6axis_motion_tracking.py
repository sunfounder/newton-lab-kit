from imu import MPU6050
from machine import I2C, Pin
import time

# Initialize the I2C interface (SDA: Pin 4, SCL: Pin 5) with a frequency of 400kHz
i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

# Initialize the MPU6050 sensor using the I2C interface
mpu = MPU6050(i2c)

def read_accel():
    """Reads and returns accelerometer values (x, y, z)."""
    return mpu.accel.x, mpu.accel.y, mpu.accel.z

def read_gyro():
    """Reads and returns gyroscope values (x, y, z)."""
    return mpu.gyro.x, mpu.gyro.y, mpu.gyro.z

def main():
    """Main loop that continuously reads and prints accelerometer and gyroscope data."""
    while True:
        # Read accelerometer data
        accel_x, accel_y, accel_z = read_accel()
        print("Accelerometer - X: {:.6f}, Y: {:.6f}, Z: {:.6f}".format(accel_x, accel_y, accel_z))
        
        # Wait for 0.5 seconds before reading gyroscope data
        time.sleep(0.5)

        # Read gyroscope data
        gyro_x, gyro_y, gyro_z = read_gyro()
        print("Gyroscope - X: {:.6f}, Y: {:.6f}, Z: {:.6f}".format(gyro_x, gyro_y, gyro_z))
        
        # Wait for 0.5 seconds before the next loop
        time.sleep(0.5)

# Entry point of the script
if __name__ == "__main__":
    main()
