# Detailed ESP Setup

Contents:
- Install MicroPython into an ESP
- How to manipulate the ESP's File System
- Run Program
- IMPORTANT NOTES
- FAQ

Software:
- [Thonny](https://thonny.org)
- [adafruit-ampy](https://pypi.org/project/adafruit-ampy/) Python Library

# Flash ESP Microcontroller
1. After you installed **Thonny**, **connect the ESP Microcontroller** to your computer and open the program and you will see a terminal like this one:

![Thonny Terminal](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/imgs/thonny_1.png)

2. Go to the bottom right corner and click on it. You will see a menu pop on your screen

![Thonny Menu](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/imgs/thonny_2.png)

3. Go to **Interpreter** Tab and do the following modifications:

* Select your interpreter as:
   * MicroPython (ESP32) **(If you are using an ESP32)**
   * MicroPython (ESP8266) **(If you are using an ESP8266)**
* Select the Port that the ESP is connected to
* Make sure all 4 checkboxes are **marked**

Once you are all done, click on **"Install or update MicroPython"**

![Thonny Interpreter](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/imgs/thonny_3.png)

5. Select the Port once again
6. Browse for the Flash File contained in the [flash_files](https://github.com/KevinHern/ESP-IoT-Intro/tree/main/flash_files) directory.

![Flash Files](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/imgs/thonny_5.png)

7. Select the **correct** Flash File for your device
8. Make sure Flash Mode is set to **"From image file (keep)"**

![Flash Final Option](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/imgs/thonny_4.png)

9. Click **Install**
