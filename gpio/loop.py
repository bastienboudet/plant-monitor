from threading import Thread
from logging import getLogger, INFO
import time
from queue import Empty

from .sensor import Sensor
from .definition import TAG, GPIOCommands
from .queues import rx_queue, tx_queue

class GPIOThread(Thread):
    # TODO: Add muliple sensor support and refactor
    def __init__(self, humidity_sensor: Sensor, read_interval: int, timeout: int):
        Thread.__init__(self)
        self.humidity_sensor = humidity_sensor
        self.read_interval = read_interval
        self.last_read_time = 0
        self.timeout = timeout
        self.humidity = None

    def run(self):
        # initialize sensor
        self.humidity_sensor.setup()
        print("Humidity sensor initialized", flush=True)

        while True:

            # check for commands
            try:
                command, args = rx_queue.get(block=False)
                self.execute_command(command, args)
            except Empty:
                pass

            # read sensor
            current_time = time.time()
            if current_time - self.last_read_time >= self.read_interval:
                self.last_read_time = current_time
                self.humidity = self.humidity_sensor.read()
                print("Humidity: ", self.humidity, flush=True)

            time.sleep(self.timeout)
    
    def execute_command(self, command: GPIOCommands, args=None):
        if command == GPIOCommands.READ_HUMIDITY:
            tx_queue.put(self.humidity)
        else:
            self.logger.error("Invalid command")