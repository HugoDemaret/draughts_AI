import pygame

# Define some constants for the game board
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 720
HEIGHT = 720
ROWS = 8
COLUMNS = 8
SQUARE_SIZE = WIDTH // COLUMNS

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.selected_piece = None
        self.turn = 0
        #add the pieces to the board
        for row in range(ROWS):
            for col in range(COLUMNS):
                if row < 3 and (row + col) % 2 == 1:
                    self.board[row][col] = 1
                elif row > 4 and (row + col) % 2 == 1:
                    self.board[row][col] = 2

    def draw_board(self, screen):
        # Draw the board background
        for row in range(ROWS):
            for col in range(row % 2, COLUMNS, 2):
                pygame.draw.rect(screen, WHITE, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            for col in range((row + 1) % 2, COLUMNS, 2):
                pygame.draw.rect(screen, GRAY, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

        # Draw the pieces on the board
        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board[row][col] == 1:
                    pygame.draw.circle(screen, RED, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
                elif self.board[row][col] == 2:
                    pygame.draw.circle(screen, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

        # Draw the outline of the selected piece
        if self.selected_piece is not None:
            row, col = self.selected_piece
            pygame.draw.rect(screen, GREEN, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)
            # Draw the possible moves
            if self.board[row][col] == 1 and self.turn % 2 == 0:
                if self.valid_move(row + 1, col - 1):
                    pygame.draw.circle(screen, GREEN, ((col - 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
                if self.valid_move(row + 1, col + 1):
                    pygame.draw.circle(screen, GREEN, ((col + 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row + 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)

            elif self.board[row][col] == 2 and self.turn % 2 == 1:
                if self.valid_move(row - 1, col - 1):
                    pygame.draw.circle(screen, GREEN, ((col - 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)
                if self.valid_move(row - 1, col + 1):
                    pygame.draw.circle(screen, GREEN, ((col + 1) * SQUARE_SIZE + SQUARE_SIZE // 2, (row - 1) * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 2 - 5)



    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, value):
        self.board[row][col] = value

    def select_piece(self, row, col):
        self.selected_piece = (row, col)

    def clear_selection(self):
        self.selected_piece = None


    def print_console(self):
        for row in range(ROWS):
            print(self.board[row])
        print()



    #this function is used to check if the move is valid
    def valid_move(self, row, col):
        #check if the move is within the board
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        #check if the move is to an empty square
        if self.board[row][col] != 0:
            return False
        #check if the move is diagonal
        if row == self.selected_piece[0] or col == self.selected_piece[1]:
            return False
        #check if the move is one square away
        if abs(row - self.selected_piece[0]) != 1 or abs(col - self.selected_piece[1]) != 1:
            return False
        #check if the move is in the right direction
        if self.board[self.selected_piece[0]][self.selected_piece[1]] == 1 and row < self.selected_piece[0]:
            return False
        if self.board[self.selected_piece[0]][self.selected_piece[1]] == 2 and row > self.selected_piece[0]:
            return False
        return True

    #this function is used to check if the move is a jump
    def valid_jump(self, row, col):
        #check if the move is within the board
        if row < 0 or row > 7 or col < 0 or col > 7:
            return False
        #check if the move is to an empty square
        if self.board[row][col] != 0:
            return False
        #check if the move is diagonal
        if row == self.selected_piece[0] or col == self.selected_piece[1]:
            return False
        #check if the move is two squares away
        if abs(row - self.selected_piece[0]) != 2 or abs(col - self.selected_piece[1]) != 2:
            return False
        #check if the move is in the right direction
        if self.board[self.selected_piece[0]][self.selected_piece[1]] == 1 and row < self.selected_piece[0]:
            return False
        if self.board[self.selected_piece[0]][self.selected_piece[1]] == 2 and row > self.selected_piece[0]:
            return False
        #check if the piece being jumped is the opposite color
        if self.board[(row + self.selected_piece[0]) // 2][(col + self.selected_piece[1]) // 2] == self.board[self.selected_piece[0]][self.selected_piece[1]]:
            return False
        return True

    #this function show the pieces on the board

    #this function is used to move the piece
    def move_piece(self, row, col):
        self.board[row][col] = self.board[self.selected_piece[0]][self.selected_piece[1]]
        self.board[self.selected_piece[0]][self.selected_piece[1]] = 0
        self.clear_selection()
