import pygame
import sys

def main():

    size = width, height = 800, 600
    black = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False

    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True

        screen.fill(black)

        pygame.display.flip()
        pygame.time.wait(5)

    sys.exit()

if __name__ == '__main__':
    main()