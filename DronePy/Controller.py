import Transcievers
import Models

class Controller:

    def __init__(self, transciever, droneModel):
        self.transciever = transciever
        self.droneModel = droneModel

    def __send_command__(self, data):
        #TODO: Send data to the transciever
        print("Sending to Transciever")

    def changeAltitude(self, amount):
        #TOOD: interface with drone model, and send to transciever
        print("Changing Altitude by ", amount)
