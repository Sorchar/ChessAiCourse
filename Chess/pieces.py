import chess


# super class is chess.Piece from the chess lib
# att: color: True = upper-case else lower-case
# func: symbol() -> str

class NullPiece(chess.Piece):
    piece_type = 0
    position = -1
    value = 0;

    def __init__(self, alliance, position, value):
        self.alliance = alliance
        self.position = position
        self.value = value


class Bishop(chess.Piece):
    piece_type = chess.BISHOP
    position = -1
    value = 3

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value


class King(chess.Piece):
    piece_type = chess.KING
    position = -1
    value = 100000

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value


class Knight(chess.Piece):
    piece_type = chess.KNIGHT
    position = -1
    value = 3

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value


class Pawn(chess.Piece):
    piece_type = chess.PAWN
    position = -1
    value = 1

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value


class Queen(chess.Piece):
    piece_type = chess.QUEEN
    position = -1
    value = 10

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value


class Rook(chess.Piece):
    piece_type = chess.ROOK
    position = -1
    value = 5

    def __init__(self, color, position, value):
        self.color = color
        self.position = position
        self.value = value
