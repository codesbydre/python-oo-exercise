"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start = 0):
        """Make a new generator at the start point"""
        self.start = start
        self.current = start

    def __repr__(self):
        """Show representation of Serial Generator"""
        return f"<SerialGenerator start = {self.start} current = {self.current}>"

    def generate(self):
        """Generate the next serial number"""
        result = self.current
        self.current += 1
        return result

    def reset(self):
        """Reset the serial number generator to the initial value"""
        self.current = self.start

