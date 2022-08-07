import ERBasic
import ERElemental
import ERStructure
class Piece(object):
    def __init__(self, role, color, coords, direction):
        self.role = role
        self.color = color
        self.coords = coords
        self.direction = direction
        self.moved = False
        self.element = "none"
        self.mods = []
    def getMoves(self, board):
        moves = ERBasic.getMoves(board, self)
        if "elemental" in self.mods:
            moves = ERElemental.getMoves(board, self, moves)
        if "structure" in self.mods:
            moves = ERStructure.getMoves(board, self, moves)

        return moves
