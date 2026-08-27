class Sensor():
    def __init__(self, sensor_type):
        self._sensor_type = sensor_type

    def read_data(self):
        """Read environmental data from sensors."""
        pass
    
    def detect_obstacle(self):
        """Detect if obstacle is present."""
        pass
    
    def get_reading(self):
        """Get sensor reading value."""
        pass


#read_data()
#detect_obstacle()
#get_reading()