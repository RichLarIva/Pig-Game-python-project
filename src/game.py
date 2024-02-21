# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig dice src."""

import dice
import player


class Game:

    def __init__(self, target_score=100):
        """Initializes the Game."""
        self.target_score = target_score
        self.dice = dice.Dice()

    def start(self):
        print("You will throw the dice now!")
