# **PiRacer AI Racer Kit Documentation**

## Introduction

This document is to show the flow of information from the controller provided by the kit to the actual python program implemented.
</br>

## Hardware Setup

We refered to the Jetrace Assembly Manual in the Waveshare Wiki (https://www.waveshare.com/wiki/JetRacer_Assembly_Manual) for the physical setup of the kit.
</br>

## Software Setup

For the software setup, we have used the piracer python library (https://github.com/SEA-ME/piracer_py) for interfacing with the Jetracer Expansion Board. 
</br>

## Flow of Information

From the Waveshare Wiki (https://www.waveshare.com/wiki/JetRacer_AI_Kit), a [wiring diagram](https://files.waveshare.com/upload/4/4a/JetRacer_Schematic.pdf) is provided with respect to the connections between the modules in the Jetracer Expansion Board.

From the PiRacer Github Page from [SEA:ME](https://github.com/SEA-ME/piracer_py/tree/master) or from [twyleg](https://github.com/twyleg/piracer_py/tree/master), the interface of the software with respect to the hardware is provided (https://github.com/twyleg/piracer_py/blob/master/doc/architecture/export/piracer_overview.drawio.svg)

From the available Python script, the control flow is as follows:

- The robot vehicle is initialized by vehicles.py and uses the interfaces required for controlling the Jetracer Expansion Board (with I2C). 
- The gamepad is initialized and accessed from the linux subsystem via ioctl command and returned as accessible values (button name, button state, axis name, axis state). The poll() method checks the immediate state of the
- The controller.py makes use of the gamepad.py and vehicles.py to give user control to the JetRacer (depending on the choice of buttons/axis for control).

![alt-text](https://github.com/SkySom13/DES_PiRacer-Assembly/blob/main/Diagrams/InformationFlow_PiRacer.drawio.svg)

</br>
