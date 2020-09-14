from random import randint

class Dice:
    def __init__(self):
        self.die1={0: True, 1: True, 2: False, 3: False}
        self.die2={0: True, 1: True, 2: False, 3: False}
        
        def self.roll():
            die1_result = self.die1[randint(0, 3)]
            die2_result = self.die2[randint(0, 3)]
            return sum([die1_result, die2_result])

            
            


