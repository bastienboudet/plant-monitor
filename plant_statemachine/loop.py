from threading import Thread
import time
from statemachine.exceptions import TransitionNotAllowed

from .soil_humidity_regulation_statemachine import SoilHumidityRegulationStateMachine

class StatemachineThread(Thread):

    def __init__(self, timeout=1):
        Thread.__init__(self)
        self.timeout = timeout
        self.soil_humidity_regulation_statemachine = SoilHumidityRegulationStateMachine()
    
    def run(self):

        while True:
            try:
                self.soil_humidity_regulation_statemachine.step()
            except TransitionNotAllowed:
                pass            
            time.sleep(self.timeout)