class Motor():
    def __init__(self, speed, is_running):
        self._speed = speed
        self._is_running = is_running

    @property
    def is_running(self):
        """Get moving status."""
        return self._is_running

    @is_running.setter
    def is_running(self, value):
        """Set moving status.

        Args:
            value: New moving status (bool)
        """

        self._is_running = value

    def forward(self, distance):
        if self._is_running == True:
            if distance > 0:
                self._is_running = True
                return (f"Moving Forward: {distance}")
            if distance == 0:
                self._is_running = False
                return (f"Moving Forward: {distance}")
            else:
                raise ValueError("Speed cant be negative")
        else:
            self._speed = 0


    def backward(self, distance):
        if self._is_running == True:
            if distance > 0:
                self._is_running = True
                return (f"Moving Backwards: {distance}")
            if distance == 0:
                self._is_running = False
                return (f"Moving Backwards: {distance}")
            else:
                raise ValueError("Speed cant be negative")
        else:
            self._speed = 0

        
    def stop(self):
        """Stop the robot."""
        self._is_running = False
        self._speed = 0

        return ("Robot Stopped")

    def set_speed(self, speed):
        if speed < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = speed

#forward(distance)
#backward(distance)
#stop()
#set_speed(speed)