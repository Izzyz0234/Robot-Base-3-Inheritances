class Battery():
    def __init__(self, capacity, current_level):
        self._capacity = capacity
        self._current_level = current_level

    @property
    def current_level(self):
        """Get battery level."""
        return self._current_level

    @current_level.setter
    def current_level(self, value):
        """Set battery level with validation.

        Args:
            value: New battery level percentage (float, 0-100)
        Raises:
            ValueError: If battery level is not in valid range
        """
        if not (0 <= value <= 100):
            raise ValueError("Battery level must be between 0 and 100")
        self._current_level = value

    def drain(self, amount):
        if self._current_level < amount:
            raise ValueError("Battery drain level must be lower or equal to current level")
        self.current_level = self.current_level - amount

    def charge(self):
        if self.current_level == self._capacity:
            return (f"Battery level is charged")
        else:
            return (f"Battery level is not charged")

    def get_percentage(self):
        return (f"{self.current_level / self._capacity}")

    def is_depleted(self):
        if self._current_level == 0:
            return (f"Battery level is depleted")
        else:
            return (f"Battery level is not depleted")
        
        
#drain(amount)
#charge()
#get_percentage()
#is_depleted()