import chessPieces as P
import random


class Board(object):

    def __init__(self, color):
        # board is a 2d list, [x][y]
        # color dictates which side is at the bottom of the screen.
        # 1 is white, -1 is black
        self.board = []
        for x in range(8):
            self.board.append([])
            for y in range(8):
                self.board[x].append([])
        self.setUp(color)
        self.turn = 0
        self.dead = []
        self.mods = ["elemental", "necro", "structure", "portal"]
        self.activeMods = []
        self.portal = [[-1, -1], [-1, -1]]
        self.step = False
        self.playing = 1
        self.inGame = True

    def setUp(self, color):
        # sets up all the pieces in the right place
        for x, row in enumerate(self.board):
            for y, space in enumerate(row):
                if y == 0 and (x == 0 or x == 7):
                    space.append(P.Piece("rook", -1*color, [x, y], -1))
                if y == 0 and (x == 1 or x == 6):
                    space.append(P.Piece("knight", -1*color, [x, y], -1))
                if y == 0 and (x == 2 or x == 5):
                    space.append(P.Piece("bishop", -1*color, [x, y], -1))
                if y == 0 and x == 3:
                    space.append(P.Piece("queen", -1*color, [x, y], -1))
                if y == 0 and x == 4:
                    space.append(P.Piece("king", -1*color, [x, y], -1))
                if y == 1:
                    space.append(P.Piece("pawn", -1*color, [x, y], -1))
                if y == 7 and (x == 0 or x == 7):
                    space.append(P.Piece("rook", color, [x, y], 1))
                if y == 7 and (x == 1 or x == 6):
                    space.append(P.Piece("knight", color, [x, y], 1))
                if y == 7 and (x == 2 or x == 5):
                    space.append(P.Piece("bishop", color, [x, y], 1))
                if y == 7 and x == 3:
                    space.append(P.Piece("queen", color, [x, y], 1))
                if y == 7 and x == 4:
                    space.append(P.Piece("king", color, [x, y], 1))
                if y == 6:
                    space.append(P.Piece("pawn", color, [x, y], 1))
    def getMoves(self, space):
        # input list: [x, y]
        # outputs a list of multiple [x, y]
        if len(self.board[space[0]][space[1]]) == 1:
            if (self.board[space[0]][space[1]][0].color == 1 and self.turn%2==1) or (self.board[space[0]][space[1]][0].color == -1 and self.turn%2==0) or self.board[space[0]][space[1]][0].role == "wall":
                return []
            return self.board[space[0]][space[1]][0].getMoves(self.board)
    def checkPortal(self, square, color):
        if square:
            if square[0].color == color:
                return False
        return True
    def move(self, target, position):
        # input target as [x, y]
        # input position as [x, y]
        # if possible, moves the chess piece that is at target to position
        # if there is a piece at the new position, it gets killed
        if len(self.board[target[0]][target[1]]) == 1:
            if self.step and ("portal" in self.activeMods):
                self.board[target[0]][target[1]][0].coords = position
                self.board[position[0]][position[1]].append(self.board[target[0]][target[1]].pop(0))       
                if len(self.board[position[0]][position[1]]) > 1:
                    fallen = self.board[position[0]][position[1]].pop(0)
                    self.dead.append(fallen)
                    if "necro" in self.activeMods:
                        self.board[target[0]][target[1]].append(P.Piece(fallen.role, -1*fallen.color, target, -1*fallen.direction))
                        self.board[target[0]][target[1]][0].element = fallen.element
                if self.board[position[0]][position[1]][0].role == "pawn":
                    if (self.board[position[0]][position[1]][0].direction == 1 and position[1] == 0) or (self.board[position[0]][position[1]][0].direction == -1 and position[1] == 7):
                        self.board[position[0]][position[1]][0].role = "queen"
                self.board[position[0]][position[1]][0].moved = True
            elif position in self.getMoves(target):
                thing = 0
                
                if self.board[target[0]][target[1]][0].moved == False and self.board[target[0]][target[1]][0].role == "king" and len(self.board[position[0]][position[1]]) == 1 and (target[0] - position[0] > 1 or position[0] - target[0] > 1):
                    
                    if not self.board[position[0]][position[1]][0].moved:
                        if position[0] > target[0]:
                            self.board[position[0]][position[1]][0].coords = [target[0]+1, target[1]]
                            self.board[target[0]+1][target[1]].append(self.board[position[0]][position[1]].pop(0))
                            self.board[target[0]+1][target[1]][0].moved = True
                            
                            self.board[target[0]][target[1]][0].coords = [target[0]+2, target[1]]
                            self.board[target[0]+2][target[1]].append(self.board[target[0]][target[1]].pop(0))
                            self.board[target[0]+2][target[1]][0].moved = True
                        elif position[0] < target[0]:
                            
                            self.board[position[0]][position[1]][0].coords = [target[0]-1, target[1]]
                            self.board[target[0]-1][target[1]].append(self.board[position[0]][position[1]].pop(0))
                            self.board[target[0]-1][target[1]][0].moved = True
                            
                            self.board[target[0]][target[1]][0].coords = [target[0]-2, target[1]]
                            self.board[target[0]-2][target[1]].append(self.board[target[0]][target[1]].pop(0))
                            self.board[target[0]-2][target[1]][0].moved = True
                            thing = self.board[target[0]-2][target[1]][0]



                else:
                    self.board[target[0]][target[1]][0].coords = position
                    self.board[position[0]][position[1]].append(self.board[target[0]][target[1]].pop(0))       
                    if len(self.board[position[0]][position[1]]) > 1:
                        fallen = self.board[position[0]][position[1]].pop(0)
                        self.dead.append(fallen)
                        if "necro" in self.activeMods:
                            self.board[target[0]][target[1]].append(P.Piece(fallen.role, -1*fallen.color, target, -1*fallen.direction))
                            self.board[target[0]][target[1]][0].element = fallen.element
                    if self.board[position[0]][position[1]][0].role == "pawn":
                        if (self.board[position[0]][position[1]][0].direction == 1 and position[1] == 0) or (self.board[position[0]][position[1]][0].direction == -1 and position[1] == 7):
                            self.board[position[0]][position[1]][0].role = "queen"
                    self.board[position[0]][position[1]][0].moved = True
                    thing = self.board[position[0]][position[1]][0]
                if position in self.portal and self.checkPortal(self.board[self.portal[1-self.portal.index(position)][0]][self.portal[1-self.portal.index(position)][1]], thing.color):
                    self.step = True
                    self.move(position, self.portal[1-self.portal.index(position)])
                self.step = False
                self.turn += 1
                self.playing *= -1
                self.rollMod()
                
            
    def checkWin(self):
        for p in self.dead:
            if p.role == "king":
                
                self.inGame = False
                return p.color * -1
        return 0

    
    def removeMod(self, mod):
        if mod == "elemental":
            for row in self.board:
                for space in row:
                    if space:
                        space[0].element = "none"
    def addMod(self, mod, activeMods):
        for row in self.board:
            for space in row:
                if space:
                    space[0].mods = activeMods[:]
        if mod == "elemental":
            pass
        if mod == "necro":
            pass
        
            
    def elementShuffle(self):
        for row in self.board:
            for space in row:
                if space:
                    space[0].element = random.choice(["red", "green", "blue"])
    def structureBuild(self):
        for row in self.board:
            for space in row:
                if space:
                    if space[0].role == "wall":
                        space.pop(0)
        if "structure" in self.activeMods:
            for i in range(3):
                filled = True
                while filled:
                    x = random.randrange(8)
                    y = random.randrange(8)
                    square = self.board[x][y]
                    filled = bool(square)

                square.append(P.Piece("wall", 0, [x, y], 0))
    def portalBuild(self):
        self.portal = [[-1, -1], [-1, -1]]
        if "portal" in self.activeMods:
            for i in range(2):
                filled = True
                while filled:
                    x = random.randrange(8)
                    y = random.randrange(8)
                    square = self.board[x][y]
                    filled = bool(square)
                    if i == 1:
                        filled = ([x, y] == self.portal[0]) or bool(square)

                self.portal[i] = [x, y]    
    def rollMod(self):
        if self.turn % 10 == 0:
            added = random.choice(list(set(self.mods) - set(self.activeMods)))
            self.activeMods.append(added)
            
            if len(self.activeMods) > 3:
                removed = self.activeMods.pop(0)
                self.removeMod(removed)
            self.addMod(added, self.activeMods)
        if self.turn % 5 == 0 and "elemental" in self.activeMods:
            self.elementShuffle()
        if self.turn % 5 == 0:
            self.structureBuild()
        if self.turn % 10 == 0:
            self.portalBuild()
            

    
    
            
                
                
