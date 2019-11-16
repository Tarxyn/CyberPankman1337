import pygame
import sys

def main():

    sys.stdin = open('map_pattern.txt', 'r')

    size = width, height = 800, 600
    map_tile_size = map_tile_width, map_tile_height = 15, 30
    black = 0, 0, 0

    terrain = [list(map(int, input().split())) for i in range(map_tile_height)]

    tile_size = tile_width, tile_height = 48, 28
    coef = 2

    pygame.init()
    screen = pygame.display.set_mode(size)
    gameover = False

    tiles = [
        pygame.image.load("sprites/default_tile.png"),
        pygame.image.load("sprites/wall_tile.png")
    ]
    tile_sizes = [
        {"w": 48, "h": 28},
        {"w": 48, "h": 38}
    ]
    tile_positions = [
        {"x": 0, "y": 0},
        {"x": 0, "y": -10}
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
                tile = pygame.transform.scale(tile, (tile_width * coef, tile_height * coef))
                tilerect = tile.get_rect()

                tilerect.x = j * (tile_width * coef // 2 - coef) + i * (tile_width * coef // 2 - coef) - posx
                tilerect.y = j * (tile_height * coef // 2 - coef) - i * (tile_height * coef // 2 - coef) - posy

                screen.blit(tile, tilerect)

        for i in range(map_tile_height - 1, -1, -1):
            for j in range(0, map_tile_width):

                tile = tiles[terrain[i][j]]
                tile = pygame.transform.scale(tile, (tile_sizes[terrain[i][j]]["w"] * coef, tile_sizes[terrain[i][j]]["h"] * coef))
                tilerect = tile.get_rect()

                tilerect.x = j * (tile_width * coef // 2 - coef) + i * (tile_width * coef // 2 - coef) - posx + tile_positions[terrain[i][j]]["x"] * coef
                tilerect.y = j * (tile_height * coef // 2 - coef) - i * (tile_height * coef // 2 - coef) - posy + tile_positions[terrain[i][j]]["y"] * coef

                screen.blit(tile, tilerect)

        posx += vectorx * 10
        posy += vectory * 10

        pygame.display.flip()
        pygame.time.wait(5)

    sys.exit()

if __name__ == '__main__':
    main()