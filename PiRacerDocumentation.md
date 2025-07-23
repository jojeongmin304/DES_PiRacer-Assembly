# **PiRacer AI Racer Kit Documentation**

## Introduction

This document is to show the flow of information from the controller provided by the kit to the actual python program implemented.
</br>

## Hardware Setup

We refered to the Jetrace Assembly Manual in the Waveshare Wiki (https://www.waveshare.com/wiki/JetRacer_Assembly_Manual) for the physical setup of the kit.</br>
[Raspberrypi 4 B with Rasbian OS](https://www.raspberrypi.com/documentation/computers/getting-started.html)</br>

[2 Channel CAN BUS FD Shield](https://wiki.seeedstudio.com/2-Channel-CAN-BUS-FD-Shield-for-Raspberry-Pi/)</br>

[7.9inch Captive Touch Screen](https://www.waveshare.com/7.9inch-hdmi-lcd.htm)</br>
</br>

## Software Setup

For the software setup, we have used the piracer python library (https://github.com/SEA-ME/piracer_py) for interfacing with the Jetracer Expansion Board. 
</br>

## Flow of Information

From the Waveshare Wiki (https://www.waveshare.com/wiki/JetRacer_AI_Kit), a [wiring diagram](https://files.waveshare.com/upload/4/4a/JetRacer_Schematic.pdf) is provided with respect to the connections between the modules in the Jetracer Expansion Board.

From the PiRacer Github Page from [SEA:ME](https://github.com/SEA-ME/piracer_py/tree/master) or from [twyleg](https://github.com/twyleg/piracer_py/tree/master), the interface of the software with respect to the hardware is provided (https://github.com/twyleg/piracer_py/blob/master/doc/architecture/export/piracer_overview.drawio.svg)

From the available Python script, the control flow is as follows:

- When a button is pressed, a specific circuit is closed, allowing current to flow, and the gamepad's MCU detects this flow.
- The gamepad's MCU creates an HID (Human Interface Device) data packet from the button input and transmits this packet to the USB dongle via 2.4GHz radio waves.
- A chip inside the dongle converts the radio waves back into a USB data signal and sends it to the USB port.
    - More detail: The Linux kernel directly receives the signal from the USB dongle (at the Kernel Level). 
    A device driver within the kernel interprets this signal and creates a special device file, /dev/input/js0, to allow programs to communicate with the device. 
    Then, back at the User Level, when a function like open('/dev/input/js0') in controller.py is called, it triggers a System Call. 
    The kernel receives this call and instructs the js driver to check if there is any incoming data for that device.
- The main Python functions, located in gamepads.py and controller.py, continuously read new event data from the joystick's device file (/dev/input/js0). 
This raw data is parsed into a Python object, making the joystick's state (e.g., axis position, button status) available as variables.
- Based on these variables, a corresponding method in the vehicles.py hardware library is called. This library converts a high-level command (e.g., "60% throttle") into a low-level hardware value. This calculation is performed by the Raspberry Pi's CPU and the result is stored in memory (RAM).
- To actuate the motors, the calculated value must be sent from the Raspberry Pi's main chip to the specialized chips on the motor  driver board. This chip-to-chip communication is handled by the I2C (Inter-Integrated Circuit) protocol.
    - In this setup, the I2C Master is Raspberry Pi's SoC, while chips on the motor driver board, such as the PCA9685, are I2C Slaves.
- The communication occurs with the SCL(clock) and SDA(data) lines. 
An I2C data packet includes both a data and an id of data. 
The master sends this packet onto the bus.  
While all slave devices see the signal, only the chip whose id matches will process the accompanying data.
- The chip on the motor driver board converts data packet into an appopriate PWM signal.
- The corresponding hardware operates.


![alt-text](https://github.com/SkySom13/DES_PiRacer-Assembly/blob/main/Diagrams/InformationFlow_PiRacer.drawio.svg)

</br>
