import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 24
cell_size = 5
random_cells = 2000

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def getHeight():
    return screen.get_height() // cell_size

def getWidth():
    return screen.get_width() // cell_size



pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Life")
clock = pygame.time.Clock()

cells = [[False for i in range(getHeight() + 1)] for j in range(getWidth() + 1)]
neighbors = [[0 for i in range(getHeight())] for j in range(getWidth())]

for i in range(random_cells):
    cells[random.randint(0, getWidth() - 1)][random.randint(0, getHeight() - 1)] = True

def setCell(x,y):

    x = x // cell_size
    y = y // cell_size
    cells[x][y] = not cells[x][y]

def game():

    area = (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)
    for i, ni in enumerate(neighbors):
        for j in range(len(ni)):
            counter = 0
            for a in area:
                if cells[i + a[0]][j + a[1]]:
                    counter += 1
                neighbors[i][j] = counter



    for i, ni in enumerate(neighbors):
        for j, nj in enumerate(ni):
            if cells[i][j]:
                if nj not in (2,3):
                    cells[i][j] = False
            else:
                if neighbors[i][j] == 3:
                    cells[i][j] = True

running = True
pause = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            setCell(x,y)



    screen.fill(BLACK)

    for i in range(getWidth()):
        pygame.draw.line(screen, BLUE, (i * cell_size, 0),
                         (i * cell_size, screen.get_height()))
    for j in range(getHeight()):
        pygame.draw.line(screen, BLUE, (0 , j * cell_size),
                         (screen.get_width(), j * cell_size))

    for i in range(getWidth()):
        for j in range(getHeight()):
            if cells[i][j] == True:
                pygame.draw.rect(screen, GREEN, pygame.Rect(1 + i * cell_size,
                                 1 + j * cell_size, cell_size, cell_size))


    pygame.display.flip()
    if not pause:
        game()
