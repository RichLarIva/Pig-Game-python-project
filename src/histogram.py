class Histogram:
    """Class to manage a histogram of dice rolls."""

    def __init__(self):
        """Initialize the histogram."""
        self.histogram = {}

    def record_roll(self, roll):
        """Record a dice roll in the histogram."""
        if roll in self.histogram:
            self.histogram[roll] += 1
        else:
            self.histogram[roll] = 1

    def display(self):
        """Display the histogram."""
        print("Dice Roll Histogram:")
        for roll, frequency in sorted(self.histogram.items()):
            print(f"{roll}: {'*' * frequency}")
