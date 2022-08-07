
def getMoves(board, piece):
    role = piece.role
    if role == "rook":
        return rookMoves(board, piece)
    elif role == "knight":
        return knightMoves(board, piece)
    elif role == "bishop":
        return bishopMoves(board, piece)
    elif role == "queen":
        return queenMoves(board, piece)
    elif role == "king":
        return kingMoves(board, piece)
    elif role == "pawn":
        return pawnMoves(board, piece)
    

def rookMoves(board, piece):
    # returns a list of coordinates that the rook can move to, including position where it takes another piece
    
    moves = []
    for i in range(4):
        space = piece.coords[:]
        contin = True
        
        while contin:
            if i == 0:
                space[0] += 1
            elif i == 1:
                space[0] -= 1
            elif i == 2:
                space[1] += 1
            else:
                space[1] -= 1
            if not (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                break
            if len(board[space[0]][space[1]]) == 0:
                moves.append(space[:])
            else:
                contin = False
                if board[space[0]][space[1]][0].color != piece.color:
                    moves.append(space[:])
    return moves
def knightMoves(board, piece):
    moves = []
    for i in range(4):
        space = piece.coords[:]
        if i == 0:
            space[1] -= 2
            space[0] += 1
            for ii in range(2):
                
                if ii:
                    space[0] -= 2

                if 0<=space[0]<=7 and 0<=space[1]<=7:
                    if len(board[space[0]][space[1]]) == 0:
                        moves.append(space[:])

                    elif board[space[0]][space[1]][0].color != piece.color:
                        moves.append(space[:])
        elif i == 1:
            space[1] += 2
            space[0] += 1
            for ii in range(2):
                
                if ii:
                    space[0] -= 2

                if 0<=space[0]<=7 and 0<=space[1]<=7:
                    if len(board[space[0]][space[1]]) == 0:
                        moves.append(space[:])

                    elif board[space[0]][space[1]][0].color != piece.color:
                        moves.append(space[:])
        elif i == 2:
            space[0] -= 2
            space[1] += 1
            for ii in range(2):
                
                if ii:
                    space[1] -= 2

                if 0<=space[0]<=7 and 0<=space[1]<=7:
                    if len(board[space[0]][space[1]]) == 0:
                        moves.append(space[:])

                    elif board[space[0]][space[1]][0].color != piece.color:
                        moves.append(space[:])
        elif i == 3:
            space[0] += 2
            space[1] += 1
            for ii in range(2):
                
                if ii:
                    space[1] -= 2

                if 0<=space[0]<=7 and 0<=space[1]<=7:
                    if len(board[space[0]][space[1]]) == 0:
                        moves.append(space[:])

                    elif board[space[0]][space[1]][0].color != piece.color:
                        moves.append(space[:])
    
    return moves
            
def bishopMoves(board, piece):
    moves = []
    for i in range(4):
        space = piece.coords[:]
        contin = True
        
        while contin:
            if i == 0:
                space[0] += 1
                space[1] += 1
            elif i == 1:
                space[0] -= 1
                space[1] -= 1
            elif i == 2:
                space[0] += 1
                space[1] -= 1
            else:
                space[0] -= 1
                space[1] += 1
            if not (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                break
            if len(board[space[0]][space[1]]) == 0:
                moves.append(space[:])
            else:
                contin = False
                if board[space[0]][space[1]][0].color != piece.color:
                    moves.append(space[:])
    return moves
def queenMoves(board, piece):
    moves = []
    for i in range(8):
        space = piece.coords[:]
        contin = True
        
        while contin:
            if i == 0:
                space[0] += 1
            elif i == 1:
                space[0] -= 1
            elif i == 2:
                space[1] += 1
            elif i == 3:
                space[1] -= 1
            elif i == 4:
                space[0] += 1
                space[1] += 1
            elif i == 5:
                space[0] -= 1
                space[1] -= 1
            elif i == 6:
                space[0] += 1
                space[1] -= 1
            else:
                space[0] -= 1
                space[1] += 1
            if not (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                break
            if len(board[space[0]][space[1]]) == 0:
                moves.append(space[:])
            else:
                contin = False
                if board[space[0]][space[1]][0].color != piece.color:
                    moves.append(space[:])
    return moves
def kingMoves(board, piece):
    moves = []
    for i in range(8):
        space = piece.coords[:]
        space[0] += -1+i%3
        space[1] += -1+i//3
        if space == piece.coords:
            space[0] += 1
            space[1] += 1
        if 0<=space[0]<=7 and 0<=space[1]<=7:
            if len(board[space[0]][space[1]]) == 0:
                moves.append(space[:])
            elif board[space[0]][space[1]][0].color != piece.color:
                moves.append(space[:])
    if not piece.moved:
        if len(board[1][piece.coords[1]]) == 0 and len(board[2][piece.coords[1]]) == 0 and len(board[3][piece.coords[1]]) == 0 and len(board[0][piece.coords[1]]) == 1:
            if not board[0][piece.coords[1]][0].moved:
                moves.append([0, piece.coords[1]])
        if len(board[6][piece.coords[1]]) == 0 and len(board[5][piece.coords[1]]) == 0 and len(board[7][piece.coords[1]]) == 1:
            if not board[7][piece.coords[1]][0].moved:
                moves.append([7, piece.coords[1]])
    return moves
        
def pawnMoves(board, piece):
    moves = []
    if piece.direction == 1:
        space = piece.coords[:]
        if piece.coords[1] == 6:
            
            for i in range(2):
                space[1] -= 1
                if len(board[space[0]][space[1]]) == 0:
                    moves.append(space[:])
                else:
                    break
            space = piece.coords[:]
            space[1] -= 1
            if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                
                space[0] -= 1
                for i in range(2):
                    space[0] += 2*i
                    if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                        if len(board[space[0]][space[1]]) == 1:
                            if board[space[0]][space[1]][0].color != piece.color:
                                moves.append(space[:])
        else:
            space[1] -= 1
            if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                if len(board[space[0]][space[1]]) == 0:
                    moves.append(space[:])
                space[0] -= 1
                for i in range(2):
                    space[0] += 2*i
                    if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                        if len(board[space[0]][space[1]]) == 1:
                            if board[space[0]][space[1]][0].color != piece.color:
                                moves.append(space[:])
                
    elif piece.direction == -1:
        space = piece.coords[:]
        if piece.coords[1] == 1:
            
            for i in range(2):
                space[1] += 1
                if len(board[space[0]][space[1]]) == 0:
                    moves.append(space[:])
                else:
                    break
            space = piece.coords[:]
            space[1] += 1
            if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                
                space[0] -= 1
                for i in range(2):
                    space[0] += 2*i
                    if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                        if len(board[space[0]][space[1]]) == 1:
                            if board[space[0]][space[1]][0].color != piece.color:
                                moves.append(space[:])
        else:
            space[1] += 1
            if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                if len(board[space[0]][space[1]]) == 0:
                    moves.append(space[:])
                space[0] -= 1
                for i in range(2):
                    space[0] += 2*i
                    if (0 <= space[0] <= 7 and 0 <= space[1] <= 7):
                        if len(board[space[0]][space[1]]) == 1:
                            if board[space[0]][space[1]][0].color != piece.color:
                                moves.append(space[:])
    return moves
                        
                        
