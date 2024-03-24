from threading import Thread
from logging import getLogger

from .sensor import Sensor
from .definition import TAG


class HygrometryThread(Thread):
    def __init__(self, sensor: Sensor):
        Thread.__init__(self)
        self.logger = getLogger(TAG)
        self.sensor = sensor

    def run(self):
        # initialize sensor
        self.sensor.setup()

        while True:
            # read sensor
            value = self.sensor.read()
            