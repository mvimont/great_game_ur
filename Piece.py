class Piece:
    def __init__(self):
        self.position=0
        self.alive=True
        self.finished=False

        def captured():
            self.alive=False

        def finished():
            self.finished=True
            
