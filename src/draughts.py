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
        draughts_board.draw_board(screen)
        pygame.display.update()



if __name__ == "__main__":
    main()