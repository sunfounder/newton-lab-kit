.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_water:

2.14 Water Level Detection
============================

In this lesson, we will learn how to use a **water sensor** with the Raspberry Pi Pico to detect the presence of water or measure the water level. This sensor is commonly used in projects related to rainfall detection, water level monitoring, and liquid leakage alerts.

**How the Water Sensor Works**

The water sensor has a series of exposed parallel wire traces that detect water droplets or measure the volume of water. As water comes into contact with these traces, the sensor outputs an analog signal. The more water that comes into contact with the sensor, the higher the output value, which can be read by the Raspberry Pi Pico's analog-to-digital converter (ADC).

|img_water_sensor|

* Do not fully submerge the sensor in water. Only the area with the exposed traces should come into contact with water.
* Using the sensor in a humid environment while powered may cause the probe to corrode faster, so it is recommended to power the sensor only when taking readings.

**Components Needed**

* Raspberry Pi Pico 2
* Water sensor
* Breadboard
* Jumper wires

**Circuit Diagram**

|sch_water|


**Wiring Diagram**


|wiring_water|


**Writing the Code**

We'll write a simple MicroPython program to read the analog value from the water sensor and print it to the console. As the water sensor is submerged, the value read by GP28 will increase.

.. note::

    * Open the ``2.14_feel_the_water_level.py`` file under the path of ``newton-lab-kit/micropython`` or copy this code into Thonny IDE, then click "Run Current Script" or simply press F5 to run it.

    * Don't forget to click on the "MicroPython (Raspberry Pi Pico).COMxx" interpreter in the bottom right corner. 

    * For detailed tutorials, please refer to :ref:`open_run_code_py`.


.. code-block:: python

    import machine
    import utime

    # Initialize ADC on GP28
    sensor = machine.ADC(28)

    while True:
        # Read the analog value from the sensor
        value = sensor.read_u16()
        print("Water level reading:", value)
        utime.sleep(0.2)  # Delay to avoid flooding the console with data


When the code is running, slowly submerge the water sensor into water, watching the values printed to the console. As the sensor detects more water, the printed value will increase.

**Learn More: Using the Sensor for Leak Detection**

We can also use the water sensor to detect liquid leakage by treating it like a digital sensor. Here's how:

#. Measure the Baseline Value:

   * First, take a reading from the water sensor in a completely dry environment. Record this value to use as a threshold.
   * If the sensor's reading goes above the baseline threshold, we can assume that the sensor is in contact with water, indicating a potential leak.

#. Leak Detection Code:

   In this example, we'll check if the sensor's reading exceeds the threshold value (which you'll need to set based on your environment).

   .. code-block:: python

      import machine
      import utime
  
      # Initialize ADC on GP28
      sensor = machine.ADC(28)
  
      # Set a threshold value based on dry readings (adjust as needed)
      threshold = 30000
  
      while True:
          # Read the analog value from the sensor
          value = sensor.read_u16()
          
          # Check if the value exceeds the threshold, indicating water exposure
          if value > threshold:
              print("Liquid leakage detected!")
          
          utime.sleep(0.2)  # Delay for readability
    

   The program checks if the sensor's value exceeds a predefined threshold. If the value is higher, it prints a message indicating water or liquid leakage.

**Practical Applications**

* **Leak Detection**: Place the sensor near water pipes, and it can alert you if a pipe starts leaking.
* **Water Level Monitoring**: Use the sensor in tanks or containers to monitor the water level and trigger alerts or actions.
* **Rain Detection**: Install the sensor outdoors (with appropriate protection) to detect rainfall.

**Conclusion**

The water sensor is a simple yet powerful tool for detecting water levels or potential liquid leakage. By integrating it with the Raspberry Pi Pico, you can create responsive and useful water detection systems for a variety of applications.

