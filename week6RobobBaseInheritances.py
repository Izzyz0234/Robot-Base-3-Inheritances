from abc import ABC, abstractmethod

from battery import Battery
from motor import Motor
from sensor import Sensor


class RobotBase(ABC):
    """Provide shared components and the required robot interface."""

    def __init__(self, name):
        """Initialize a robot with shared components."""
        self._name = name
        self._battery = Battery(100, 50)
        self._motor = Motor(1, True)
        self._sensor = Sensor("object")

    @property
    def name(self):
        """Return the robot's name."""
        return self._name

    @property
    def sensor_reading(self):
        """Return the current sensor reading from the base interface."""
        return self.get_reading()

    def get_reading(self):
        """Read the current sensor value through the shared interface."""
        if hasattr(self._sensor, "get_reading"):
            return self._sensor.get_reading()
        return None

    @abstractmethod
    def read_sensor(self):
        """Return the sensor data in a robot-specific format."""

    @abstractmethod
    def perform_task(self):
        """Carry out the robot's specialised behaviour."""

    @abstractmethod
    def report_status(self):
        """Return the current status message for this robot."""

    def __str__(self):
        """Return the robot's current status summary."""
        return self.report_status()

    def __repr__(self):
        """Return a detailed view of the robot state."""
        return (
            f"Robot Name: {self._name!r}\n"
            "Battery: \n"
            f"Battery Level: {self._battery.current_level}\n"
            f"Battery Charge: {self._battery.charge()}\n"
            f"Battery Percentage: {self._battery.get_percentage()}\n"
            f"Battery depleted: {self._battery.is_depleted()}\n"
            "\nMotor: \n"
            f"Speed: {self._motor._speed!r}\n"
            f"Is Moving: {self._motor.is_running!r}\n"
            "\nSensor: \n"
            f"Sensor Reading: {self.get_reading()!r}\n"
        )


class Vacume(RobotBase):
    """Represent a robot that can vacuum."""

    def __init__(self, name, sucking):
        super().__init__(name)
        self._battery = Battery(100, 50)
        self._motor = Motor(20, True)
        self._sensor = Sensor("object")
        self.sucking = bool(sucking)

    def read_sensor(self):
        """Return the vacuum's room-reading information."""
        reading = self.get_reading()
        return f"Vacuum sensor reading: {reading}" if reading is not None else "Vacuum sensor reading: no data"

    def perform_task(self):
        """Activate the vacuum's cleaning behaviour."""
        self.sucking = True
        return "Vacuuming the floor"

    def report_status(self):
        """Report the vacuum robot's status."""
        return (
            f"Name: {self._name!r}\nBattery Level: {self._battery.current_level}\n"
            f"Motor Speed: {self._motor._speed}\nVacuming: {self.sucking}\n"
            f"Sensor Reading: {self.read_sensor()}\n"
        )


class SecurityCamera(RobotBase):
    """Represent a stationary robot with a security camera sensor."""

    def __init__(self, name):
        super().__init__(name)
        self._battery = Battery(100, 100)
        self._motor = Motor(0, False)
        self._sensor = Sensor("object")

    def read_sensor(self):
        """Return the camera's monitored scene information."""
        reading = self.get_reading()
        return f"Camera view status: {reading}" if reading is not None else "Camera view status: no movement detected"

    def perform_task(self):
        """Monitor the area for motion or movement."""
        return "Monitoring the area for movement"

    def report_status(self):
        """Report the security camera robot's status."""
        return (
            f"Name: {self._name!r}\nBattery Level: {self._battery.current_level}\n"
            f"Motor Running: {self._motor.is_running}\n"
            f"Status: {self.read_sensor()}\n"
        )


class PickupAndPutdown(RobotBase):
    """Represent a robot that can pick up and put down objects."""

    def __init__(self, name, is_holding):
        super().__init__(name)
        self._battery = Battery(100, 40)
        self._motor = Motor(10, True)
        self._sensor = Sensor("object")
        self.is_holding = bool(is_holding)

    def read_sensor(self):
        """Return the pickup robot's object-detection message."""
        reading = self.get_reading()
        return f"Object detected: {reading}" if reading is not None else "No object detected"

    def perform_task(self):
        """Pick up or set down an item depending on current state."""
        self.is_holding = not self.is_holding
        return "Picking up object" if self.is_holding else "Placing object down"

    def report_status(self):
        """Report the pickup robot's status."""
        return (
            f"Name: {self._name!r}\nBattery Level: {self._battery.current_level}\n"
            f"Object Held: {self.is_holding}\n"
            f"Sensor Reading: {self.read_sensor()}\n"
        )


if __name__ == "__main__":
    vacume = Vacume("Vacume", True)
    securityCamera = SecurityCamera("Security Camera")
    pickupAndPutDown = PickupAndPutdown("Pickup & Putdown", True)

    print(vacume.report_status())
    print(securityCamera.report_status())
    print(pickupAndPutDown.report_status())
