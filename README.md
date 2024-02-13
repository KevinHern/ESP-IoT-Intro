# Introduction

This repository contains a small amount of basic examples of how to use MicroPython to program a microcontroller, in this case, ESP8266 or ESP32.

## Requirements

### Hardware
- ESP device (either 8266 or 32)

### Hardware Firmware
- [ESP32](https://micropython.org/download/?port=esp32) or [ESP8266](https://micropython.org/download/?port=esp8266) Firmware

# Flash Device
We suggest an easier way using the [Thonny Software Method](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/thony_flashing_method.md), or in case you need full control over the device when flashing it, we also have a [From-Scratch Flashing Method](https://github.com/KevinHern/ESP-IoT-Intro/blob/main/docs/flashing_from_scratch_method.md).

# File System
The ESP Microchips are very robust and have an integrated memory to save files.
In order words, it is possible to manage the file sytem of the microchips. This is useful because in some applications, you may need the help of libraries to accomplish your goal. 

However, the ESP does not have a strong OS compared to Windows, Linux or even MacOS. It requires the use of external tools to have a better control of the files.

This is the reason why its recommended to download Ampy, because it is the tool used to manipulate the ESP's internal file system.

## Ampy

It is a software used to communicate between a microchip and your computer through serial connection. In this sense, it is mandatory you have the proper drivers of the microchip you wish you utilize. 
Ampy is the version of cmd of Windows or Linux. With Ampy, you can do the following:
- Check the microchip's saved files
- Write a file onto the microchip
- Obtain a file from the microchip
- Manage directories and files saved in the microchip

**Ampy is the recommended way to save files onto the microchip and not ESPlorer. Ampy does not suffer from format errors while ESPLorer does**

## Ampy Operations

The syntax is very similar to a Linux command prompt: very simple and concise/

- Check the current saved files and directories:
`ampy -pCOMzz ls`
- Write a file onto the ESP:
`ampy -pCOMzz put [file_1] [file_2] ... [file_n]`
- Obtain a file from the ESP and save it with a custom name:
`ampy -pCOMzz get [file] > [new_file_name]`
- Remove a file from the ESP:
`ampy -pCOMzz rm [file]`
- Create directory:
`ampy -pCOMzz mkdir [directory]`
- Delete directory:
`ampy -pCOMzz rmdir [directory]`

**Note: remember to replace the 'z' with your actual COM port**

# Execute Program on Boot

When it is time to deploy a ESP microchip with a predefined program, it is necessary to modify the **boot.py** file that it possesses.
If you want to check the current contents of boot.py, retrieve it using ampy and save it as boot.py. It is mandatory to keep its name because, on boot, the ESP microchip will search for a file named 'boot.py' and execute all the code found inside said file.

On said file, you will find some commented lines (it may vary depending on your ESP model) and then a blank space.
You will think that all of your code must be in the boot.py file, but IT IS NOT THE CASE.

The program you want to execute on boot, you have to save it as a different file and on boot.py, the only thing you have to do is import the file that contains the code.
Once you reboot your ESP, it will execute the code.

Now, there may be situations you want to modify the code to adjust some parameters or fix some bugs. Basically, repeat the process.

Summary:
1. Write your code in some file and save it to the ESP using Ampy
2. Retrieve 'boot.py' file from your ESP or create an empty 'boot.py' file
3. On boot.py, only import the file that contains your code
4. Save boot.py on your ESP
5. REBOOT your ESP, don't reset
6. Enjoy!

# Documentation
- [Installation visualized](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/Instalando_MicroPython.md)
- [File System Manipulation](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/Sistema_de_archivos.md)
- [More Examples + ESP32 and ESP8266 Diagrams](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/ejemplos.md)
- [Interruptions](https://randomnerdtutorials.com/micropython-interrupts-esp32-esp8266/)
