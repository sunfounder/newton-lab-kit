.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_mpu6050:

6.3 6-axis Motion Tracking
=====================================


The MPU-6050 is a 6-axis(combines 3-axis Gyroscope, 3-axis Accelerometer) motion tracking devices.


An accelerometer is a tool that measures proper acceleration.For example, an accelerometer at rest on the surface of the Earth will measure an acceleration due to Earth's gravity, straight upwards[3] (by definition) of g ≈ 9.81 m/s2.

Accelerometers have many uses in industry and science. For example: inertial navigation systems for aircraft and missiles, for keeping images on tablets and digital cameras vertical, etc.

Gyroscopes are used to measure orientation and angular velocity of a device or maintenance.
Applications of gyroscopes include anti-rollover and airbag systems for automobiles, motion sensing systems for smart devices, attitude stabilization systems for drones, and more.

* :ref:`cpn_mpu6050`

**Schematic**

|sch_mpu6050_ar|


**Wiring**


|wiring_mpu6050_ar|

**Code**


.. note::

    * Open the ``6.3_6axis_motion_tracking.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`. 
    
    * Here you need to use the ``imu.py`` and ``vector3d.py``, please check if it has been uploaded to Pico, for a detailed tutorial refer to :ref:`add_libraries_py`.


.. code-block:: python

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


After running the program, you can see the 3-axis accelerometer values and 3-axis gyroscope values cycling through the output.
At this point you rotate the MPU6050 at random, and these values will appear to change accordingly.
To make it easier to see the changes, you can comment out one of the print lines and concentrate on another set of data.

**How it works?**

### Code Analysis

#. **Imports and Setup**: The code starts by importing the required modules.

   .. code-block:: python

      from imu import MPU6050
      from machine import I2C, Pin
      import time

   * ``MPU6050`` is imported from the ``imu`` module, which handles communication with the MPU6050 sensor.
   * ``I2C`` and ``Pin`` are imported from the ``machine`` module for interfacing with hardware pins on the microcontroller.
   * ``time`` is imported to control timing and delays between sensor readings.

#. **I2C Initialization**: The I2C interface is initialized.

   .. code-block:: python

      i2c = I2C(0, sda=Pin(4), scl=Pin(5), freq=400000)

   * The I2C bus is set up on bus 0 using GPIO pins 4 (``SDA``) and 5 (``SCL``), with a clock frequency of 400 kHz.
   * This interface allows communication with the MPU6050 sensor over I2C protocol.

#. **MPU6050 Sensor Initialization**: The MPU6050 object is instantiated.

   .. code-block:: python

      mpu = MPU6050(i2c)

   * The MPU6050 is initialized using the I2C interface, making it ready for reading accelerometer and gyroscope data.

#. **Function Definitions**: Two functions are defined for reading data from the accelerometer and gyroscope.

   .. code-block:: python

      def read_accel():
          return mpu.accel.x, mpu.accel.y, mpu.accel.z

   * `read_accel()` reads the current values from the accelerometer's x, y, and z axes.
   * Similarly, `read_gyro()` returns the gyroscope data:

   .. code-block:: python

      def read_gyro():
          return mpu.gyro.x, mpu.gyro.y, mpu.gyro.z

   * Both functions return the respective x, y, and z-axis data as a tuple for easy handling later.

#. **Main Loop**: The ``main()`` function is responsible for continuously reading and printing the sensor data.

   .. code-block:: python

      def main():
          while True:

   * The ``while True`` loop ensures that the sensor data is read continuously.
   * The accelerometer values are fetched, formatted, and printed:
  
   .. code-block:: python

        accel_x, accel_y, accel_z = read_accel()
        print("Accelerometer - X: {:.6f}, Y: {:.6f}, Z: {:.6f}".format(accel_x, accel_y, accel_z))

   * The values are printed with 6 decimal places using the ``"{:.6f}"`` format string, which provides precision and consistency in the output.
   * After a short delay (``time.sleep(0.5)``), the gyroscope values are fetched and printed in the same manner.

#. **Sleep Delay**: After reading and printing each set of values (accelerometer and gyroscope), the code waits for 0.5 seconds using ``time.sleep(0.5)``.

   .. code-block:: python

      time.sleep(0.5)

   * This introduces a pause between each sensor reading to avoid overwhelming the system and to provide periodic sensor updates.

#. **Main Function Entry**: The script is executed by calling ``main()`` in the typical Pythonic style.

   .. code-block:: python

      if __name__ == "__main__":
          main()

   * This ensures that the main loop is only started when the script is run directly, allowing for better flexibility if the script were to be imported as a module in another program.
