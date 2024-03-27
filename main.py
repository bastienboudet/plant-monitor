from logging import getLogger, INFO
import sys
from PySide6.QtWidgets import QApplication

# GPIO
from gpio.loop import GPIOThread
from gpio.sensor import Sensor
from gpio.definition import TAG as TAG_GPIO

# qt
from qt.link_main_window import MainWindow

if __name__ == "__main__":
    # initialize logger
    gpio_logger = getLogger(TAG_GPIO)
    gpio_logger.setLevel(INFO)

    humidity_sensor = Sensor(4, 0, 1)
    gpio_thread = GPIOThread(humidity_sensor, 0.5, 0.1)
    gpio_thread.daemon = True
    gpio_thread.start()

    # start qt app
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit()



    