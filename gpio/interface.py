
from .definition import GPIOCommands
from .queues import rx_queue, tx_queue

class GPIOInterface:

    def get_humidity():
        rx_queue.put((GPIOCommands.READ_HUMIDITY, None))
        return tx_queue.get()
    
    def set_pump(state: bool):
        rx_queue.put((GPIOCommands.SET_PUMP, state))