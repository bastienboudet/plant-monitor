import RPi.GPIO as GPIO
import time
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn


class DigitalSensor:

    def __init__(self, pin_number):
        self.pin_number = pin_number


    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.IN)
    
    def read(self):
        return GPIO.input(self.pin_number)
    

class AnalogSensor:

    def __init__(self, adc, channel:int, slope:float, intercept:float):
        self.adc = adc
        self.channel = channel
        self.analog_in = None
        self.slope = slope
        self.intercept = intercept
    
    def setup(self):
        self.analog_in = AnalogIn(self.adc, self.channel)
    
    def read(self):
        if self.analog_in:
            return self.analog_in.voltage * self.slope + self.intercept
        return None