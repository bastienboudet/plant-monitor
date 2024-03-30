from threading import Thread
import time

from .soil_humidity_regulation_statemachine import SoilHumidityRegulationStateMachine

class StatemachineThread(Thread):

    def __init__(self, timeout=1):
        Thread.__init__(self)
        self.soil_humidity_regulation_statemachine = SoilHumidityRegulationStateMachine()
    
    def run(self):

        while True:
            self.soil_humidity_regulation_statemachine.step()
            time.sleep(self.timeout)