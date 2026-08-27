from abc import ABC, abstractmethod
from battery import Battery
from sensor import Sensor
from motor import Motor

class RobotBase(ABC):
    """A base class for a robot with basic functionalities."""

    def __init__(self, name):
        self._name = name
        self._battery = Battery(100, 50)
        self._motor = Motor(1, True)
        self._sensor = Sensor("object")

    @property
    def name(self):
        """Get robot name."""
        return self._name

    def report_status(self):
        """Repots __repr__ or __str__ when called"""
        return

    def __str__(self):
        """Returns the robots stats"""
        return (f"RobotBase {self._name!r} {self._battery.current_level} {self._battery.charge()} "
                f"{self._battery.get_percentage()} {self._battery.is_depleted()}"
                f"{self._motor._speed!r} {self._motor.is_running!r}"
                f"{self._sensor.read_data()!r} {self._sensor.detect_obstacle()!r} {self._sensor.get_reading()!r}\n")

    def __repr__(self):
        """Returns the robots stats"""
        return (f"Robot Name: {self._name!r}\n"
                "Battery: \n"
                f"Battery Level: {self._battery.current_level}\n"                
                f"Battery Charge: {self._battery.charge()}\n"
                f"Battery Persentage: {self._battery.get_percentage()}\n"                
                f"Battery depleted: {self._battery.is_depleted()}\n"  

                "\nMotor: \n"
                f"Speed: {self._motor._speed!r}\n"
                f"Is Moving: {self._motor.is_running!r}\n"

                "\nSensor: \n"
                f"Sensor Read Data: {self._sensor.read_data()!r}\n"
                f"Sensor Detect Obstacle: {self._sensor.detect_obstacle()!r}\n"
                f"Sensor Get Reading: {self._sensor.get_reading()!r}\n")


class Vacume(RobotBase):
    def __init__(self, name, sucking):
        super().__init__(name)
        self._battery = Battery(100, 50)
        self._motor = Motor(20, True)
        self._sensor = Sensor("object")
        self.sucking = sucking

    def vacuming(self, vacuming):
        if vacuming == True:
            self.sucking == True

class SecurityCamera(RobotBase):
    def __init__(self, name):
        super().__init__(name)
        self._battery = Battery(100, 100)
        self._motor = Motor(0, False)
        self._sensor = Sensor("object")

class PickupAndPutdown(RobotBase):
    def __init__(self, name, is_holding):
        super().__init__(name)
        self._battery = Battery(100, 40)
        self._motor = Motor(10, True)
        self._sensor = Sensor("object")
        self.is_holding = is_holding

    def grabber(self, grabbing_item):
        if grabbing_item == True:
            self.is_holding == True
        

    
vacume = Vacume("Vacume", True)
securityCamera = SecurityCamera("Security Camera")
pickupAndPutDown = PickupAndPutdown("Pickup & Putdown", True)

print(vacume.report_status)
print(securityCamera.report_status)
print(pickupAndPutDown.report_status)

print(handRobot.report_status)
