import pygame
import chessBoard
pygame.init()
myBoard = chessBoard.Board(1)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
LIGHT_BROWN = (200, 170, 130)
DARK_BROWN = (102, 51, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
VERY_DARK_BROWN = (83, 74, 65)


font = pygame.font.SysFont('arial', 20)


def drawBoard():
    square_x = 50
    square_y = 50
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if j % 2 == 0:
                    pygame.draw.rect(win, LIGHT_BROWN, (square_x, square_y, 100, 100))
                else:
                    pygame.draw.rect(win, DARK_BROWN, (square_x, square_y, 100, 100))
            else:
                if j % 2 == 0:
                    pygame.draw.rect(win, DARK_BROWN, (square_x, square_y, 100, 100))
                else:
                    pygame.draw.rect(win, LIGHT_BROWN, (square_x, square_y, 100, 100))
            piecesToDraw.append((square_x + 9, square_y + 9, j, i))
            if myBoard.portal[1] != [-1, -1]:
                for k in range(2):
                    if [j, i] == myBoard.portal[k]:
                        win.blit(portalIMG, (square_x, square_y))
            if len(squares) != 64:
                squares.append((square_x, square_y, 100, 100))
            square_x += 100
        square_x = 50
        square_y += 100


def drawPieces(piecesToDraw):
    for piece in piecesToDraw:
        drawPiece(piece[0], piece[1], piece[2], piece[3])


def drawPiece(coord_x, coord_y, x, y):
    if len(myBoard.board[x][y]) == 1:
        role = myBoard.board[x][y][0].role
        color = myBoard.board[x][y][0].color
        element = myBoard.board[x][y][0].element
        if role == 'rook':
            if color == 1:
                win.blit(pieces[11], (coord_x, coord_y))
            else:
                win.blit(pieces[10], (coord_x, coord_y))
        elif role == 'knight':
            if color == 1:
                win.blit(pieces[5], (coord_x, coord_y))
            else:
                win.blit(pieces[4], (coord_x, coord_y))
        elif role == 'bishop':
            if color == 1:
                win.blit(pieces[1], (coord_x, coord_y))
            else:
                win.blit(pieces[0], (coord_x, coord_y))
        elif role == 'queen':
            if color == 1:
                win.blit(pieces[9], (coord_x, coord_y))
            else:
                win.blit(pieces[8], (coord_x, coord_y))
        elif role == 'king':
            if color == 1:
                win.blit(pieces[3], (coord_x, coord_y))
            else:
                win.blit(pieces[2], (coord_x, coord_y))
        elif role == 'pawn':
            if color == 1:
                win.blit(pieces[7], (coord_x, coord_y))
            else:
                win.blit(pieces[6], (coord_x, coord_y))
        elif role == 'wall':
            pygame.draw.rect(win, BLACK, (coord_x - 9, coord_y - 9, 100, 100))

        if element == 'red':
            pygame.draw.circle(win, RED, (coord_x + 42, coord_y), 15)
        elif element == 'green':
            pygame.draw.circle(win, GREEN, (coord_x + 42, coord_y), 15)
        elif element == 'blue':
            pygame.draw.circle(win, BLUE, (coord_x + 42, coord_y), 15)


def highlightSquares(clickPos):
    global selected
    movesToHighlight = []
    for i, r in enumerate(squares):
        if pygame.Rect(r).collidepoint(clickPos):
            pygame.draw.rect(win, RED, r)
            x = i % 8
            y = i // 8
            if selected:
                myBoard.move(selected, [x, y])
                selected = []
            if len(myBoard.board[x][y]) == 1 and myBoard.inGame:
                moves = myBoard.getMoves([x, y])
                selected = [x, y]
                if moves:
                    for move in moves:
                        movesToHighlight.append(move[1]*8+move[0])
            else:
                selected = []
    for i, r in enumerate(squares):
        if i in movesToHighlight:
            pygame.draw.rect(win, RED, r)


def loadPieces():
    images = []
    for image in range(12):
        fileName = 'Chess_' + str(image) + '.png'
        images.append(pygame.image.load(fileName))
        # 0 = black bishop
        # 1 = white bishop
        # 2 = black king
        # 3 = white king
        # 4 = black horse
        # 5 = white horse
        # 6 = black pawn
        # 7 = white pawn
        # 8 = black queen
        # 9 = white queen
        # 10 = black rook
        # 11 = white rook
    return images


def blitText(message, fontSize, x, y):
    defaultFont = pygame.font.SysFont('arial', fontSize)
    textSurface = defaultFont.render(message, True, BLACK)
    win.blit(textSurface, (x, y))


def drawButton(win, text, r, bColor, fColor, font):
    pygame.draw.rect(win, bColor, r)
    pygame.draw.rect(win, fColor, r, 3)
    txtSurface = font.render(text, True, fColor)
    win.blit(txtSurface, (r[0] + (r[2] - txtSurface.get_width()) // 2, r[1] + (r[3] - txtSurface.get_height()) // 2))


def drawButtons(win, buttons, categories):
    for i, r in enumerate(buttons):
        drawButton(win, categories[i], r, GREEN, BLACK, font)


def getIndex(bList, mp):
    for i, r in enumerate(bList):
        if pygame.Rect(r).collidepoint(mp):
            return i
    return -1


def redraw_game_window():
    win.fill(VERY_DARK_BROWN)
    blitText('Wacky Chess', 30, 360, 5)
    drawBoard()
    if clickPos != 0:
        highlightSquares(clickPos)
    drawPieces(piecesToDraw)
    blitText('Elemental Alteration', 40, 950, 175)
    blitText('The colored game pieces are immune', 20, 960, 245)
    blitText('to other colors in a cyclic order:', 20, 990, 285)
    blitText('Red > Green > Blue > Red', 20, 1008, 325)
    blitText('Necromancy', 40, 1010, 400)
    blitText("Taking an opponent's piece revives them as your own", 20, 890, 470)
    blitText('Structure Generation', 40, 938, 545)
    blitText('Impassible black pillars are randomly placed', 20, 925, 615)
    blitText('Portal Magic', 40, 1007, 690)
    blitText('Two portals are randomly placed to allow teleportation', 20, 885, 760)
    blitText('Elemental Alteration', 40, 50, 860)
    blitText('Necromancy', 40, 490, 860)
    blitText('Structure Gen.', 40, 810, 860)
    blitText('Portal Magic', 40, 1135, 860)
    pygame.draw.circle(win, RED, (220, 950), 40)
    pygame.draw.circle(win, RED, (602, 950), 40)
    pygame.draw.circle(win, RED, (935, 950), 40)
    pygame.draw.circle(win, RED, (1242, 950), 40)
    for i in range(len(myBoard.activeMods)):
        remainingTurns = str(30 - (myBoard.turn % 10 + (len(myBoard.activeMods) - 1 - i) * 10))
        if myBoard.activeMods[i] == 'elemental':
            pygame.draw.circle(win, GREEN, (220, 950), 40)
            if int(remainingTurns) > 9:
                blitText(remainingTurns, 40, 199, 929)
            else:
                blitText(remainingTurns, 40, 209, 929)
        elif myBoard.activeMods[i] == 'necro':
            pygame.draw.circle(win, GREEN, (602, 950), 40)
            if int(remainingTurns) > 9:
                blitText(remainingTurns, 40, 581, 929)
            else:
                blitText(remainingTurns, 40, 591, 929)
        elif myBoard.activeMods[i] == 'structure':
            pygame.draw.circle(win, GREEN, (935, 950), 40)
            if int(remainingTurns) > 9:
                blitText(remainingTurns, 40, 914, 929)
            else:
                blitText(remainingTurns, 40, 924, 929)
        elif myBoard.activeMods[i] == 'portal':
            pygame.draw.circle(win, GREEN, (1242, 950), 40)
            if int(remainingTurns) > 9:
                blitText(remainingTurns, 40, 1221, 929)
            else:
                blitText(remainingTurns, 40, 1231, 929)
    if myBoard.checkWin() != 0:
        if myBoard.checkWin() == 1:
            blitText('White Wins!', 80, 905, 75)
        else:
            blitText('Black Wins!', 80, 915, 75)
        blitText('Play Again?', 80, 245, 375)
        drawButtons(win, playAgainButtons, playAgainText)

    pygame.display.update()


win = pygame.display.set_mode((1400, 1000))
pieces = loadPieces()
portalIMG = pygame.image.load('Portal.png')
selected = []
squares = []
clickPos = 0
playAgainText = ['Yes', 'No']
playAgainButtons = ((225, 500, 200, 100), (475, 500, 200, 100))
inPlay = True
while inPlay:
    piecesToDraw = []
    redraw_game_window()
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickPos = pygame.mouse.get_pos()
            if myBoard.checkWin() != 0:
                PAIndex = getIndex(playAgainButtons, clickPos)
                if PAIndex == 0:
                    del myBoard
                    myBoard = chessBoard.Board(1)
                elif PAIndex == 1:
                    inPlay = False

pygame.quit()
