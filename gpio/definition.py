from enum import Enum

TAG = "Hygrometry"

class GPIOCommands(Enum):
    READ_HUMIDITY = 1
    SET_PUMP = 2