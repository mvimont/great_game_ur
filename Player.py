from Piece import Piece

class Player:
    def __init__(self, name, side):
        self.name=name
        self.side=side
        self.pieces={1: Piece(), 2: Piece(), 3: Piece(), 4: Piece(), 5: Piece(), 6: Piece(), 7: Piece()}
        self.alive=True

    def check_alive():
        if not sum([piece.alive for piece in self.pieces.values()]):
            self.alive=False
        self.alive=True



