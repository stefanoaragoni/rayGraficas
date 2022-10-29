import pygame   
from OpenGL.GL import *
import time

pygame.init()
screen = pygame.display.set_mode((600, 400), pygame.OPENGL | pygame.DOUBLEBUF)

WHITE = (255,255,255)
BLACK = (0,0,0)

###################  PIXEL DRAW ######################

def pixel(x, y, width, height,color):
    glEnable(GL_SCISSOR_TEST)
    glScissor(int(x),int(y),int(width),int(height))
    glClearColor(color[0],color[1],color[2],1.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glDisable(GL_SCISSOR_TEST)

###################  Conway’s Game Of Life  ######################

def draw(screen, grid, size):
    w = screen.get_width() / size
    h = screen.get_height() / size
    
    for (x, y) in grid:
        pixel(x* w, y * h, w, h,(255,0,0))

    gridTemp = ()
    vecinos = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    posiblesVecinos = ()

    for (x, y) in grid:
        vecinosVivos = 0
        for (i,k) in vecinos:
            if (x+i, y+k) in grid:
                vecinosVivos += 1

            else:
                posiblesVecinos = (*posiblesVecinos, (x+i, y+k))

        if vecinosVivos == 2 or vecinosVivos == 3:
            gridTemp = (*gridTemp, (x, y))

    posiblesVecinos = list(set(posiblesVecinos))
    gridTemp = list(set(gridTemp))

    for (x, y) in posiblesVecinos:
        vecinosVivos = 0
        for (i,k) in vecinos:
            if (x+i, y+k) in grid:
                vecinosVivos += 1
        if vecinosVivos == 3:
            gridTemp = (*gridTemp, (x, y))
    

    return gridTemp


###################  GRID  ######################
grid = [(49,49),(20,20),(20,21),(20,22),(22, 8), (12, 7), (36, 7), (17, 9), (11, 8), (1, 9), (25, 4), (2, 8), (16, 7),
                                   (25, 10), (21, 6), (23, 9), (14, 6), (36, 6), (22, 7), (14, 12), (17, 8), (11, 10),
                                   (25, 9), (35, 7), (1, 8), (18, 9), (22, 6), (21, 8), (23, 5), (12, 11), (17, 10),
                                   (11, 9), (35, 6), (25, 5), (2, 9), (13, 6), (13, 12), (15, 9), (16, 11), (21, 7)]

pixel_size = 50

###################  RAY TRACER  ######################
running = True
while running:
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)

    grid = draw(screen, grid, pixel_size)
    pygame.display.flip()

    time.sleep(0.2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False