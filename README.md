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

Control your model with your device

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

LimeSDR : [Setup](https://wiki.myriadrf.org/LimeSDR-USB) <br>
LimeSDR Mini

## Supported Drones

<ol>
<li>DX-2</li>
</ol>

## Depends on

[SoapySDR](https://github.com/pothosware/SoapySDR/wiki)<br>
[pyLMS7002Soapy](https://github.com/myriadrf/pyLMS7002Soapy/blob/master/pyLMS7002Soapy/__init__.py)

NOT STABLE YET
For Updates.... [Link](https://github.com/deleomike/DronePy)
