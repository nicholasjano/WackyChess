def getMoves(board, piece, moves):
    graveyard = []
    for move in moves:
        if board[move[0]][move[1]]:
            if board[move[0]][move[1]][0].role == "wall":
                graveyard.append(move)
    for thing in graveyard:
        moves.remove(thing)
    return moves
