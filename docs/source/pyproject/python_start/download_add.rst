
.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _download_upload:

1.4 Download and Upload the Code
===============================================

**Download the Code**

Download the relevant code from the link below.


* :download:`SunFounder Newton Lab Kit Example <https://github.com/sunfounder/newton-lab-kit/archive/refs/heads/main.zip>`

* Or check out the code at `Newton Lab Kit - GitHub <https://github.com/sunfounder/newton-lab-kit>`_

.. _add_libraries_py:

Upload the Libraries to Pico
----------------------------------
In some projects, you will need additional libraries. Here, we will first upload these libraries to the Raspberry Pi Pico, and then we can run the code directly later.

#. Use a Micro USB cable to connect the Raspberry Pi Pico 2 to your computer. (Do not hold down **BOOTSEL**; you already dragged the MicroPython firmware to Pico 2 in the previous step, so just plug it in directly.)

#. Open the Thonny IDE and select "MicroPython (Raspberry Pi Pico).COMxx.COMxx" from the interpreter selection button in the bottom right corner.

   .. image:: img/th_select_com.png

#. Click **View** -> **Files** in the top navigation bar of the Thonny IDE.

   .. image:: img/th_open_files.png

#. Navigate to the folder where you previously downloaded the code package, and then go to the ``newton-lab-kit-main/libs`` folder.

   .. image:: img/th_open_code.png

#. Now, select all the files in the ``libs\`` folder and upload them to the Raspberry Pi Pico 2. It will take a while for the files to upload.

   .. image:: img/th_upload_libs.png

#. Now you will see the files you just uploaded inside your drive labeled ``Raspberry Pi Pico``.

   .. image:: img/th_pico_libs.png
