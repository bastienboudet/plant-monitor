import RPi.GPIO as GPIO

class Actuator:

    def __init_(self, pin_number:int):
        self.pin_number = pin_number

    def setup(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_number, GPIO.OUT)

    def set_state(self, state:bool):
        GPIO.output(self.pin_number, state)
