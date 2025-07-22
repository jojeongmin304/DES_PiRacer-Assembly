import time
from vehicles import PiRacerStandard
from gamepads import ShanWanGamepad

# setting control values
THROTTLE_MAX = 0.6

# initailize gamepad object
try:
    gamepad = ShanWanGamepad()
    print("initialized gamepad")
except FileNotFoundError:
    print("error: can't find gamepad (/dev/input/js0)")
    exit()

car = PiRacerStandard()

#main loop
try:
    while True:
        pad_state = gamepad.read_data()

        # 1. steering control (left analog stick)
        steering_input = pad_state.analog_stick_left.x
        if steering_input is not None:
            car.set_steering_percent(steering_input)

        # 2. forward/stop control (A button)
        a_button_pressed_value = pad_state.button_a or 0.0
        throttle_value = a_button_pressed_value * THROTTLE_MAX
        car.set_throttle_percent(throttle_value)
        
        # for debugging
        print(f"Steering: {steering_input:.2f}, Throttle: {throttle_value:.2f}")
        

except KeyboardInterrupt:
    print("\nprogrem stopped by user.")
finally:
    # safe stop and reset steering
    print("safe stop and reset steering")
    car.set_throttle_percent(0.0)
    car.set_steering_percent(0.0)