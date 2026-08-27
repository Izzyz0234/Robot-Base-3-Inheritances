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


    # @abstractmethod
    def report_status(self):
        """Report the current status of the robot.
        
        Returns:
            A string containing robot name, battery level, moving status, and sensor readings.
        """
        return (f"Robot Name: {self._name!r}\n"
                f"Battery Level: {Battery}\n"
                f"Is Moving: {Motor!r}\n"
                f"Sensor Readings: {Sensor!r}")


    def __str__(self):
        return f"RobotBase('{self._name!r}', {self._battery.get_percentage()}, {self._battery.current_level()!r}, {self._motor.is_running!r}, {Sensor!r})"
    
    def __repr__(self):
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


# Add 3 IS-A class
class Arm(RobotBase):
    def __init__(self, name, type):
        super().__init__(name)
        self._battery = Battery(100, 50)
        self._motor = Motor(40, True)
        self._sensor = Sensor("object")
        self.type = type

    def report_status(self):
        return (f"Robot Name: {self._name!r}\n"
                f"Battery Level: {Battery}\n"
                f"Is Moving: {Motor!r}\n"
                f"Sensor Readings: {Sensor!r}"
                f"Type: {self.type!r}")



print("Initial Robot Settings:")
robot = RobotBase("Bob")
handRobot = Arm("Sandy", "Hand")

# Battery
robot._battery = Battery(100, 80)
robot._battery.drain(50)

# Motor
robot._motor = Motor(5, True)
# robot._motor.forward(20)
# robot._motor.stop()
robot._motor.set_speed(50)

# Sensor
robot._sensor = Sensor("object")

print(robot.report_status)

print(handRobot.report_status)
