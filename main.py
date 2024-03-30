from logging import getLogger, INFO
import sys
import time
from PySide6.QtWidgets import QApplication

# GPIO
from gpio.loop import GPIOThread
from gpio.sensor import DigitalSensor
from gpio.actuator import Actuator
from gpio.definition import TAG as TAG_GPIO
from gpio.interface import GPIOInterface

# qt
from qt.link_main_window import MainWindow

if __name__ == "__main__":
    # initialize logger
    gpio_logger = getLogger(TAG_GPIO)
    gpio_logger.setLevel(INFO)

    humidity_sensor = DigitalSensor(4)
    pump_actuator = Actuator(17)

    gpio_thread = GPIOThread(humidity_sensor, pump_actuator, 0.5, 0.1)
    gpio_thread.daemon = True
    gpio_thread.start()

    for i in range(12):
        time.sleep(1)
        print(GPIOInterface.get_humidity(), flush=True)
        GPIOInterface.set_pump(i%2 == 0)

    GPIOInterface.set_pump(False)
    time.sleep(1000)

    # start qt app
    # app = QApplication(sys.argv)
    # window = MainWindow()
    # window.show()
    # app.exec()
    # sys.exit()



    