from .Devices import limeSDR
from .Models import DX2



class Controller:

    def __init__(self, device=None, droneModel=None):
        if device is None:
            self.device = limeSDR.LimeSDR()
        else:
            self.device = device

        if droneModel is None:
            self.droneModel = DX2.DX2()
        else:
            self.droneModel = droneModel


        print("Controller Initialized")

    def __send_command__(self, data):
        #TODO: Send data to the transciever
        print("Sending to Transciever")

    def changeAltitude(self, amount):
        #TOOD: interface with drone model, and send to transciever
        print("Changing Altitude by ", amount)
