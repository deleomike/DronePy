from .Device import Device
from pyLMS7002Soapy import pyLMS7002Soapy

class LimeSDR(Device):

    def __init__(self):
        print("Lime SDR Initialized")
        self.soapy = pyLMS7002Soapy.pyLMS7002Soapy(verbose=1)