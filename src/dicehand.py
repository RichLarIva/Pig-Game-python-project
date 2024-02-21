#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class DiceHand:
    """Class to represent a hand of dice."""

    def __init__(self, num_dice=1):
        """Initialize the hand of dice."""
        self.num_dice = num_dice
        self.dice = [Dice() for _ in range(num_dice)]

    def roll_all(self):
        """Roll all dice in the hand."""
        for die in self.dice:
            die.throw()

    def roll_individual(self, die_index):
        """Roll a specific die in the hand."""
        if 0 <= die_index < self.num_dice:
            self.dice[die_index].throw()
        else:
            print("Invalid die index")

    def get_values(self):
        """Get the current values of all dice in the hand."""
        return [die.current_number for die in self.dice]

    def get_total(self):
        """Get the total value of all dice in the hand."""
        return sum(self.get_values())
