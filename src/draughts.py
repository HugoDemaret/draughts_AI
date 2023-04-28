import pygame

import board.board as board

def main():
    pygame.init()
    screen = pygame.display.set_mode((board.WIDTH, board.HEIGHT))
    pygame.display.set_caption("Draughts")
    draughts_board = board.Board()


    running = True
    while(running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                #get position
                pos = pygame.mouse.get_pos()
                #get row and column
                row = pos[1] // board.SQUARE_SIZE
                col = pos[0] // board.SQUARE_SIZE
                #select the piece
                draughts_board.select_piece(row, col)
                if draughts_board.turn % 2 == draughts_board.selected_piece[0] % 2:
                    #add the possible moves
                    draughts_board.add_possible_moves()
                #print the board to the console



        #draughts_board.print_console()
        draughts_board.draw_board(screen)
        pygame.display.update()



if __name__ == "__main__":
    main()