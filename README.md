# DronePy
Open Source Drone Command Library

The purpose of this library is to provide hobbyists with an interface to connect specific drone models with their own equipment. A nice sample sample drone you can buy is the DX-2, and you can use the LimeSDR as the equipment.

## Installation

```bash
pip install DronePy
```

## Usage

Implementing your own drone model
```python
from DronePy.Models.DroneModel import DroneModel

class myDroneModel(DroneModel):

    def __init(self):
        ....

model = myDroneModel()
```

Implementing your own Device
```python
from DronePy.Devices.Device import Device

class myDevice(Device):

    def __init(self):
        print("My Transciever")
        
        ....

dev = myDevice()

```

Controller your model with your device

```python

from DronePy.Controller import Controller

comp = Controller(device=dev, droneModel=model)

comp.changeAltitude(10)

...

```

## What DronePy Will Do

DronePy will allow a programmer to select their drone model, and their preferred SDR, and send comands to their drone in real time.

It is being considered whether to add functionality to sample signals and auto-generate models.

## Supported Devices

<ol>
<li>LimeSDR</li>
<i>LimeSDR Mini</li>
</ol>

## Supported Drones

<ol>
<li>DX-2</li>
</ol>

NOT STABLE YET
For Updates.... [Link](https://github.com/deleomike/DronePy)
