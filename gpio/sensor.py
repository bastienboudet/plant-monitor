import RPi.GPIO as GPIO
import time

class DigitalSensor:

    def __init__(self, pin_number):
        self.pin_number = pin_number


    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN)
    
    def read(self):
        return GPIO.input(self.pin_number)