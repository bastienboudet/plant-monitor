from logging import getLogger, INFO
import sys
import time
from PySide6.QtWidgets import QApplication

# GPIO
from gpio.loop import GPIOThread
from gpio.sensor import AnalogSensor
from gpio.actuator import Actuator
from gpio.definition import TAG as TAG_GPIO
from gpio.interface import GPIOInterface
import RPi.GPIO as GPIO

import adafruit_ads1x15.ads1015 as ADS
import board
import busio

# statemachine
from plant_statemachine.loop import StatemachineThread

# qt
from qt.link_main_window import MainWindow

if __name__ == "__main__":
    # initialize logger
    gpio_logger = getLogger(TAG_GPIO)
    gpio_logger.setLevel(INFO)

    # Create the I2C bus
    i2c = busio.I2C(board.SCL, board.SDA)

    # Create the ADC object using the I2C bus
    ads = ADS.ADS1015(i2c)

    humidity_sensor = AnalogSensor(adc=ads, 
                                   channel=ADS.P0,
                                   slope=-1/2.2, intercept=3.3/2.2)
    pump_actuator = Actuator(17)

    gpio_thread = GPIOThread(humidity_sensor, pump_actuator)
    gpio_thread.daemon = True
    gpio_thread.start()

    statemachine_thread = StatemachineThread(timeout=1)
    statemachine_thread.daemon = True
    statemachine_thread.start()

    # for i in range(12):
    #     time.sleep(1)
    #     print(GPIOInterface.get_humidity(), flush=True)
    #     GPIOInterface.set_pump(i%2 == 0)

    # await ctrl-c
    try:
        while True:
            time.sleep(2)
            # monitoring
            print(GPIOInterface.get_humidity(), flush=True)
    except:
        GPIOInterface.set_pump(False)
        GPIO.cleanup()

    finally:
        sys.exit()

    # start qt app
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()
    # sys.exit()



    