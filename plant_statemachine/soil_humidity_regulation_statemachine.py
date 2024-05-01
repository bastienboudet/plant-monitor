from statemachine import StateMachine, State
from datetime import datetime, timedelta

# gpio
from gpio.interface import GPIOInterface

class SoilHumidityRegulationStateMachine(StateMachine):
    
    # states
    off = State(initial=True)
    waiting = State()
    watering = State()
    awaiting_feedback = State()

    # transitions
    off_to_waiting = off.to(waiting, unless="is_system_halted")
    waiting_to_watering = waiting.to(watering, cond="is_humidity_low")
    watering_to_awaiting_feedback = watering.to(awaiting_feedback, cond="is_watering_done")
    awaiting_feedback_to_waiting = awaiting_feedback.to(waiting, cond="is_feedback_received")
    waiting_to_off = waiting.to(off, cond="is_system_halted")

    # logic loop
    step = off_to_waiting\
        | waiting_to_watering\
        | watering_to_awaiting_feedback\
        | awaiting_feedback_to_waiting\
        | waiting_to_off


    def __init__(self):
        self.waiting_time = datetime.now()
        self.watering_time = timedelta(seconds=1)
        self.cooldown_time = timedelta(seconds=1500)
        self.humidity_low_threshold = 0.5
        super().__init__()

    # conditions
    def is_system_halted(self):
        return False
    
    def is_humidity_low(self):
        return GPIOInterface.get_humidity() < self.humidity_low_threshold

    def is_watering_done(self):
        return datetime.now() - self.waiting_time > self.watering_time
    
    def is_feedback_received(self):
        # print remaining time
        print("Remaining time before humidity check: ", (self.cooldown_time - (datetime.now() - self.waiting_time)).seconds, "s", flush=True)
        return datetime.now() - self.waiting_time > self.cooldown_time
    
    # actions
    def on_enter_watering(self):
        GPIOInterface.set_pump(True)
        self.waiting_time = datetime.now()
        print("Entering watering state", flush=True)
    
    def on_enter_awaiting_feedback(self):
        GPIOInterface.set_pump(False)
        self.waiting_time = datetime.now()
        print("Entering awaiting feedback state", flush=True)