
# GPIO
from gpio.loop import GPIOThread
from gpio.sensor import Sensor
from gpio.definition import TAG

if __name__ == "__main__":
    humidity_sensor = Sensor(4, 0, 1)
    gpio_thread = GPIOThread(humidity_sensor, 0.5, 0.1)
    gpio_thread.daemon = True
    gpio_thread.start()

    # start qt app


    