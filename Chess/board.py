import chess

# Arrays
tile_names = chess.SQUARE.NAMES
columns = chess.FILE_NAMES
rows = chess.RANK_NAMES

class Board(chess.Board):
    # Fields
    gameTiles = {}

    # Constructor
    def __init__(self):
        pass

    # Functions
    def createBoard(self):
        for tile in range(64):
            self.gameTiles[tile] = Tile(tile)




###### help classes ######
class Move(chess.Move):
    from_square = None
    to_square = None
    promotion = None
    drop = None

    def __init__(self, from_square, to_square, promotion, drop):
        super()

    #uci()->str
    #from_uci(uci: str)->chess.Move
    #null()->chess.Move

class Tile():
    tile_index = None
    tile_name = None
    belongsToRow = None
    belongsToColumn = None
    occupiedBy = None

    def __init__(self, index):
        self.tile_index = index
        self.tile_name = tile_names[index]
        self.belongsToRow = rows[index]
        self.belongsToColumn = columns[index]

    def getOccupied(self, piece):
        self.occupiedBy = piece
