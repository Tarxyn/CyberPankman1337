import pygame
import sys

def main():

    size = width, height = 800, 600
    map_tile_size = map_tile_width, map_tile_height = 30, 50
    black = 0, 0, 0

    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False

    tiles = [
        pygame.image.load("sprites/default_tile.png")
    ]

    posx = 600
    posy = -300

    vectorx = 0
    vectory = 0

    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameover = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    vectory = -1
                elif event.key == pygame.K_DOWN:
                    vectory = 1
                elif event.key == pygame.K_LEFT:
                    vectorx = -1
                elif event.key == pygame.K_RIGHT:
                    vectorx = 1
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_UP, pygame.K_DOWN]:
                    vectory = 0
                elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    vectorx = 0

        screen.fill(black)

        for i in range(map_tile_height):
            for j in range(map_tile_width):

                tile = tiles[0]
                tilerect = tile.get_rect()

                tilerect.x = j * 69 + i * 69 - posx
                tilerect.y = j * 39 - i * 39 - posy

                screen.blit(tile, tilerect)

        posx += vectorx * 10
        posy += vectory * 10

        pygame.display.flip()
        pygame.time.wait(5)

    sys.exit()

if __name__ == '__main__':
    main()