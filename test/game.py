# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig dice game class."""

import dice
import player


class Game:
    """Simple class that handles mainly set up for the program."""
    def __init__(self, target_score=100):
        """Initializes the Game."""
        self.target_score = target_score
        self.dice = dice.Dice()

    def start(self):
        print("You will throw the dice now!")
