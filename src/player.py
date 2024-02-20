class Player:
    """Class to represent a player in a Pig dice game."""

    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_to_score(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0