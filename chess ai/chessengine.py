import chess
class state:
    def __init__(self):
        self.board = chess.Board()
    def getlegal(self):
        return self.board.legal_moves
    def movepawn(self, move):
        if self.board.push_san(move) in self.getlegal():
            self.board.push_san(move)
        else:
            print("invalid")

    def makemove(self, movefrom, moveto):
        if chess.Move.from_uci(movefrom + moveto) in self.getlegal():
            chess.Move.from_uci(movefrom + moveto)
        else:
            print("invalid")