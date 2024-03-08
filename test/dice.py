# !/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Dice handling."""

import random
import time


class Dice:
    """Class which handles the dice in game."""


    LOW_NUMBER = 1
    MAX_NUMBER = 6

    current_number = None

    def __init__(self):
        """Init the dice class."""
        random.seed(time.time())

    def throw(self):
        """Handles the throw function by generation
        random number by default between 1 and 6."""
        self.current_number = random.randint(self.LOW_NUMBER, self.MAX_NUMBER)
