# !/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Pig dice game."""

import dice


class Game:

    def __init__(self):
        """Initializes the game"""
        print("initalize")

    def start(self):
        print("You will throw the dice now!")
        Dice.throw()
