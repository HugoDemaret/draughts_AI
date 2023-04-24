import pygame

# Define some constants for the game board
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)

WIDTH = 800
HEIGHT = 800
ROWS = 8
COLUMNS = 8
SQUARE_SIZE = WIDTH // COLUMNS

class Board:
    def __init__(self):
        self.board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.selected_piece = None

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

    def get_piece(self, row, col):
        return self.board[row][col]

    def set_piece(self, row, col, value):
        self.board[row][col] = value

    def select_piece(self, row, col):
        self.selected_piece = (row, col)

    def clear_selection(self):
        self.selected_piece = None
