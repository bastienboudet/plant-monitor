from threading import Thread
from logging import getLogger
import time

from .sensor import Sensor
from .definition import TAG

class HygrometryThread(Thread):
    # TODO: Add muliple sensor support and refactor
    def __init__(self, sensor: Sensor, read_interval: int, timeout: int):
        Thread.__init__(self)
        self.logger = getLogger(TAG)
        self.sensor = sensor
        self.read_interval = read_interval
        self.last_read_time = 0
        self.timeout = timeout
        self.read_value = None

    def run(self):
        # initialize sensor
        self.sensor.setup()

        while True:
            # read sensor
            current_time = time.time()
            if current_time - self.last_read_time >= self.read_interval:
                self.last_read_time = current_time
                self.read_value = self.sensor.read()

            time.sleep(self.timeout)
