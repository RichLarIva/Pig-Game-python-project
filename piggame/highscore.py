class Highscore:
    """Class to manage high scores for a Pig dice game."""

    def __init__(self):
        """Initialize the high score list."""
        self.scores = []

    def add_score(self, player_name, score):
        """Add a new score to the high score list."""
        self.scores.append((player_name, score))

    def get_top_scores(self, num_scores=5):
        """Get the top scores from the high score list."""
        sorted_scores = sorted(self.scores, key=lambda x: x[1], reverse=True)
        return sorted_scores[:num_scores]

    def reset_scores(self):
        """Reset the high score list."""
        self.scores = []
