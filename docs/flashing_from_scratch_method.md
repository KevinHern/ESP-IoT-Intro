# Detailed ESP setup from Scratch 

## Programming Software
- [Python version 3](https://www.python.org/downloads/)
- [Java](https://www.java.com/es/download/)

## Python Libraries
- [ESPtool](https://github.com/espressif/esptool/)
- [Ampy](https://github.com/pycampers/ampy)

## IDEs
- [ESPLorer](https://esp8266.ru/esplorer/)

# Installation and Preparations

## Install Python Libraries
- `pip3 install esptool`
- `pip3 install adafruit-ampy`

## Flash Device
1. Connect ESP by USB port and verify the PORT connectivity
2. Download device Firmware Binary or select the correct firmware in the [flash_files](https://github.com/KevinHern/ESP-IoT-Intro/tree/main/flash_files) directory
3. Open a CMD and execute `esptool erase_flash` o `esptool.py erase_flash` (depending on the esptool library's version, either has to work)
4. Execute the following command, replacing the respective parameters:

`esptool --chip ZZZ --port YYY --baud 460800 write_flash -z 0x1000 <binary route>`

or

`esptool.py --chip ZZZ --port YYY --baud 460800 write_flash -z 0x1000 <binary route>`
   - **ZZZ**: Esp device, either `esp32` or `esp8266`
   - **YYY**: The port that the device is connected to (Example: `COM5`)
   - **<binary route\>**: The directory path to the flash file (binary file)

## Configuring ESPLorer
1. En el directorio donde se encuentra el .jar de ESPlorer, ejecutar: 
    `java -jar ESPlorer.jar`
2. Settings > Select Firmware > MicroPython
3. Main Tab > Baud Rate > 115200
4. RTS ON
5. Open connection
6. Program!
