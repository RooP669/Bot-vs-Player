import pygame
import sys
import time
import random

# Initialize Pygame
pygame.init()
print("\033c")
# Set up the window
WIDTH = 1000
HEIGHT = 1000
CELL_SIZE = 335
LINE_WIDTH = 5
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
X_COLOR = (255, 0, 0)
O_COLOR = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


def draw_board(board):
    screen.fill(BG_COLOR)
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                pygame.draw.line(screen, X_COLOR, (col * CELL_SIZE, row * CELL_SIZE),
                                 ((col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, ((col + 1) * CELL_SIZE, row * CELL_SIZE),
                                 (col * CELL_SIZE, (row + 1) * CELL_SIZE), LINE_WIDTH)
            elif board[row][col] == "O":
                pygame.draw.circle(screen, O_COLOR,
                                   (int((col + 0.5) * CELL_SIZE), int((row + 0.5) * CELL_SIZE)),
                                   int(CELL_SIZE / 2 - LINE_WIDTH), LINE_WIDTH)


def check_winner(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    # No winner
    return None


def bot_move(board):
    # Check if the bot can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "O"
                if check_winner(board) == "O":
                    return row, col
                else:
                    board[row][col] = " "  # Undo the move

    # Check if the player can win in the next move
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = "X"
                if check_winner(board) == "X":
                    return row, col
                else:
                    board[row][col] = " "  # Undo the move

    # If there is no immediate winning move, make a random move
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col


def play_game_1player():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        draw_board(board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and current_player == "X":
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    continue

                if board[row][col] != " ":
                    continue

                board[row][col] = current_player
                winner = check_winner(board)

                if winner:
                    draw_board(board)
                    pygame.display.flip()
                    if winner == "X":
                        print("Red wins (X)!")
                    else:
                        print("Blue wins (0)!")
                    return

                if all(board[i][j] != " " for i in range(3) for j in range(3)):
                    draw_board(board)
                    pygame.display.flip()
                    print("It's a tie!")
                    return

                current_player = "O"
            elif current_player == "O":
                row, col = bot_move(board)

                board[row][col] = current_player
                winner = check_winner(board)

                if winner:
                    draw_board(board)
                    pygame.display.flip()
                    if winner == "X":
                        print("Red wins (X)!")
                    else:
                        print("Blue wins (0)!")
                    return

                if all(board[i][j] != " " for i in range(3) for j in range(3)):
                    draw_board(board)
                    pygame.display.flip()
                    print("It's a tie!")
                    return

                current_player = "X"


def play_game_2players():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        draw_board(board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if not (0 <= row <= 2 and 0 <= col <= 2):
                    continue

                if board[row][col] != " ":
                    continue

                board[row][col] = current_player
                winner = check_winner(board)

                if winner:
                    draw_board(board)
                    pygame.display.flip()
                    if winner == "X":
                        print("Red wins (X)!")
                    else:
                        print("Blue wins (0)!")
                    return

                if all(board[i][j] != " " for i in range(3) for j in range(3)):
                    draw_board(board)
                    pygame.display.flip()
                    print("It's a tie!")
                    return

                current_player = "O" if current_player == "X" else "X"


def draw_buttons():
    pygame.draw.rect(screen, LINE_COLOR, (100, 450, 200, 100), LINE_WIDTH)
    pygame.draw.rect(screen, LINE_COLOR, (700, 450, 200, 100), LINE_WIDTH)

    font = pygame.font.Font(None, 40)
    text_1player = font.render("1 Player", True, LINE_COLOR)
    text_2players = font.render("2 Players", True, LINE_COLOR)
    screen.blit(text_1player, (140, 475))
    screen.blit(text_2players, (730, 475))


# Main program
print("Welcome to Tic-Tac-Toe!")

while True:
    screen.fill(BG_COLOR)
    draw_buttons()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if 100 <= x <= 300 and 450 <= y <= 550:
                play_game_1player()
            elif 700 <= x <= 900 and 450 <= y <= 550:
                play_game_2players()

    print("Thank you for playing!")
    print("Restarting...")
    time.sleep(1.5)
