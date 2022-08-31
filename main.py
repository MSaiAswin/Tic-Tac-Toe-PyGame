import pygame ,sys,time
import numpy as np



pygame.init()

WIDTH = HEIGHT = 600
BG_COL = (255, 191, 0)
LINE_WID = CIRCLE_WID = 15
LINE_COL = (205, 141, 0)
BOARD_ROWS = BOARD_COLS = 3
CIRCLE_RADIUS = 60
CIRCLE_COL = (238,230,201)
CROSS_WIDTH = 25
SPACE = 55
CROSS_COL = (65,67,66)


screen = pygame.display.set_mode((WIDTH,HEIGHT))


pygame.display.set_caption('Tic Tac Toe')


screen.fill(BG_COL)

board = np.zeros((BOARD_ROWS,BOARD_COLS))

def start():
    screen.fill(BG_COL)
    draw_lines()

    font = pygame.font.Font('freesansbold.ttf',80)
    text1 = font.render('TIC', True, LINE_COL)
    tRect1 = text1.get_rect()
    tRect1.center = (WIDTH//6,HEIGHT//3+HEIGHT//6)
    screen.blit(text1,tRect1)

    text2 = font.render('TAC', True, LINE_COL)
    tRect2 = text2.get_rect()
    tRect2.center = (WIDTH//3+WIDTH//6,HEIGHT//3+HEIGHT//6)
    screen.blit(text2,tRect2)

    text3 = font.render('TOE', True, LINE_COL)
    tRect3 = text3.get_rect()
    tRect3.center = (WIDTH-WIDTH//6,HEIGHT//3+HEIGHT//6)
    screen.blit(text3,tRect3)

    pygame.display.update()


def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen,CIRCLE_COL,((int(col*200+100)),(int(row*200+100))), CIRCLE_RADIUS,CIRCLE_WID)
            elif board[row][col] == 2:
                pygame.draw.line(screen, CROSS_COL, (col*200+SPACE,row*200+200-SPACE),(col*200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COL, (col*200+SPACE,row*200+SPACE),(col*200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)


def mark_squares(row,col,player):
    board[row][col] = player

def available_squares(row,col):
    return board[row][col] == 0
    
def is_board_full():
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            if board[i][j] == 0:
                return False
    return True

def draw_lines():
    pygame.draw.line(screen, LINE_COL,(0,200),(600,200),LINE_WID)
    pygame.draw.line(screen, LINE_COL,(0,400),(600,400),LINE_WID)
    pygame.draw.line(screen, LINE_COL,(200,0),(200,600),LINE_WID)
    pygame.draw.line(screen, LINE_COL,(400,0),(400,600),LINE_WID)

draw_lines()

player = 2

def check_win(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col,player)
            return True
    
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row,player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_ascending_win_line(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_descending_win_line(player)
        return True
    return False


def draw_vertical_win_line(col,player):
    posX = col*200+100
    if player == 1:
        color = CIRCLE_COL
    elif player == 2:
        color = CROSS_COL

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)

def draw_horizontal_win_line(row,player):
    posY = row*200+100
    if player == 1:
        color = CIRCLE_COL
    elif player == 2:
        color = CROSS_COL

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

def draw_ascending_win_line(player):
    if player == 1:
        color = CIRCLE_COL
    elif player == 2:
        color = CROSS_COL

    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15, 15),15)

def draw_descending_win_line(player):
    if player == 1:
        color = CIRCLE_COL
    elif player == 2:
        color = CROSS_COL

    pygame.draw.line(screen,color,(15,15),(WIDTH-15, HEIGHT-15),15)

def restart():
    screen.fill((BG_COL))
    draw_lines()
    for i in range(BOARD_ROWS):
        for j in range(BOARD_COLS):
            board[i][j] = 0
    
start()
star = True
running = True
game_over = False
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over and not star:

            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY//200)
            clicked_col = int(mouseX//200)
            
            if available_squares(clicked_row,clicked_col):
                if player == 1:
                    mark_squares(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    mark_squares(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                

                draw_figures()

        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start:
                star = False
                screen.fill(BG_COL)
                draw_lines()
            if event.key == pygame.K_ESCAPE:
                player = 2
                game_over = False
                restart()
                

    
    pygame.display.update()

    # if is_board_full() or game_over:
    #         player = 2
    #         game_over = False
    #         time.sleep(5)
    #         restart()