"""Class for the intelligence of the \"AI\""""

import dice
import random


class Intelligence:
    intelligence_level = 0
    score = 0
    die = dice

    def __init__(self):
        correct_format = False
        self.die = dice.Dice()
        while correct_format == False:
            ai_level = input("What difficulty do you want?\n1 or 2: ")
            if ai_level == "1" or ai_level == "2":
                self.intelligence_level = int(ai_level)
                correct_format = True
                break
            print("Please make sure you made it in the correct format")

    def play_turn(self, is_turn):
        while is_turn:
            i = 0
            if i == 0:
                """Throw dice"""
                die.throw()
                if self.die.current_number != 1:
                    self.score += self.die.current_number
                else:
                    is_turn = False
                    break
            while i > 0:
                """Check if AI should just switch turn"""
                choice = random.randint(1, 2)
                # if choice is 1 then continue throwing else just switch turn

