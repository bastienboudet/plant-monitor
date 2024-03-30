from threading import Thread
from logging import getLogger, INFO
import time
from queue import Empty

from .sensor import DigitalSensor
from .actuator import Actuator
from .definition import TAG, GPIOCommands
from .queues import rx_queue, tx_queue

class GPIOThread(Thread):
    # TODO: Add muliple sensor support and refactor
    def __init__(self, humidity_sensor: DigitalSensor, pump_actuator: Actuator):
        Thread.__init__(self)
        self.humidity_sensor = humidity_sensor
        self.pump_actuator = pump_actuator
        self.humidity = None

    def run(self):
        # initialize sensor
        self.humidity_sensor.setup()

        # initialize actuator
        self.pump_actuator.setup()

        while True:

            # check for commands
            try:
                command, args = rx_queue.get(block=True)
                self.execute_command(command, args)
            except Empty:
                pass

            # time.sleep(self.timeout)
    
    def execute_command(self, command: GPIOCommands, args=None):
        if command == GPIOCommands.READ_HUMIDITY:
            self.humidity = self.humidity_sensor.read()
            tx_queue.put(self.humidity)
        elif command == GPIOCommands.SET_PUMP:
            self.pump_actuator.set_state(args)
        else:
            print("Unknown command", flush=True)