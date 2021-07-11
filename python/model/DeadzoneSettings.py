class DeadzoneSettings:
    def __init__(self, deadzone_shape, deadzone, dodge_deadzone, aerial_sensitivity, steering_sensitivity,
                 last_updated):
        self.deadzone_shape = deadzone_shape
        self.deadzone = deadzone
        self.dodge_deadzone = dodge_deadzone
        self.aerial_sensitivity = aerial_sensitivity
        self.steering_sensitivity = steering_sensitivity
        self.last_updated = last_updated
