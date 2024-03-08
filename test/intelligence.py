"""Class for the intelligence of the \"AI\""""

import dice
import random


class Intelligence:
    """Handles the simplistic AI needed for the game."""
    score = 0
    die = dice

    def __init__(self):
        self.die = dice.Dice()
        self.score = 0

    def play_turn(self, is_turn):
        rolls = []
        while is_turn:
            i = 0
            if i == 0:
                """Throw dice"""
                self.die.throw()
                print(f"AI rolled {self.die.current_number}")
                rolls.append(self.die.current_number)
                if self.die.current_number != 1:
                    self.score += self.die.current_number
                    i += 1
                else:
                    is_turn = False
                    break
            while i > 0:
                """Check if AI should just switch turn"""
                choice = random.randint(1, 2)
                # if choice is 1 then continue throwing else just switch turn
                if choice == 2:
                    print(f"AI scored {self.score}")
                    is_turn = False
                    break
                self.die.throw()
                print(f"AI rolled {self.die.current_number}")
                rolls.append(self.die.current_number)
                if self.die.current_number != 1:
                    self.score += self.die.current_number
                    i += 1
                else:
                    is_turn = False
                    print(f"AI scored {self.score}")
                    break
        return rolls
