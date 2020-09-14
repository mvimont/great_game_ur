from Piece import Piece
from Player import Player

class UrBoard:
    def __init__(self):
        self.safe_square_left = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False} 
        self.safe_square_right = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False}
        self.combat_square = {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
        self.rosette=3
        self.player_left=Player('left')
        self.plaery_right=Player('right')

            
