def getMoves(board, piece, moves):
    if piece.element == "red":
        graveyard = []
        for move in moves:
            if board[move[0]][move[1]]:
                if board[move[0]][move[1]][0].color != piece.color and board[move[0]][move[1]][0].element == "blue":
                    graveyard.append(move)
        for thing in graveyard:
            moves.remove(thing)
        return moves
    if piece.element == "green":
        graveyard = []
        for move in moves:
            if board[move[0]][move[1]]:
                if board[move[0]][move[1]][0].color != piece.color and board[move[0]][move[1]][0].element == "red":
                    graveyard.append(move)
        for thing in graveyard:
            moves.remove(thing)
        return moves
    if piece.element == "blue":
        graveyard = []
        for move in moves:
            if board[move[0]][move[1]]:
                if board[move[0]][move[1]][0].color != piece.color and board[move[0]][move[1]][0].element == "green":
                    graveyard.append(move)
        for thing in graveyard:
            moves.remove(thing)
        return moves
