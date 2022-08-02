# Introduction

This repository contains a small amount of basic examples of how to use MicroPython to program a microcontroller, in this case, ESP8266 or ESP32.

## Requirements

### Hardware
- ESP device (either 8266 or 32)

### Hardware Firmware
- [ESP32](https://micropython.org/download/?port=esp32) or [ESP8266](https://micropython.org/download/?port=esp8266) Firmware

### Programming Software
- [Python version 3](https://www.python.org/downloads/)
- [Java](https://www.java.com/es/download/)

### Python Libraries
- [ESPtool](https://github.com/espressif/esptool/)
- [Ampy](https://github.com/pycampers/ampy)

### IDEs
- [ESPLorer](https://esp8266.ru/esplorer/)

## Installation and Preparations

### Install Python Libraries
- `pip3 install esptool`
- `pip3 install adafruit-ampy`

### Flash Device
1. Connect ESP by USB port and verify the PORT connectivity
2. Download device Firmware Binary
3. `esptool erase_flash`
4. `esptool --chip ZZZ --port YYY --baud 460800 write_flash -z 0x1000 <binary route>`
   - **ZZZ**: Esp device, either `esp32` or `esp82`
   - **YYY**: The port that the device is connected to (Example: `COM5`)
   - **<binary route\>**: The directory path to the binary

### Configuring ESPLorer
1. En el directorio donde se encuentra el .jar, ejecutar: 
    `java -jar ESPlorer.jar`
2. Settings > Select Firmware > MicroPython
3. Main Tab > Baud Rate > 115200
4. RTS ON
5. Open connection
6. Program!

# Documentation
- [Installation visualized](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/Instalando_MicroPython.md)
- [File System Manipulation](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/Sistema_de_archivos.md)
- [More Examples + ESP32 and ESP8266 Diagrams](https://github.com/FunPythonEC/Python_para_MicroControladores/blob/master/ejemplos.md)
- [Interruptions](https://randomnerdtutorials.com/micropython-interrupts-esp32-esp8266/)
