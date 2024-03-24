import RPi.GPIO as GPIO
import time

class Sensor:

    def __init__(self, pin_number, bias, scale):
        self.pin_number = pin_number
        self.bias = bias
        self.scale = scale

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN)
    
    def read(self):
        return self.bias + GPIO.input(self.pin_number) * self.scale
    