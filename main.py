from random import *
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
        if (x*w) > screen.get_width() or (y*h) > screen.get_height():
            continue
        pixel(x* w, y * h, w, h,WHITE)

    gridTemp = ()
    vecinos = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    vecinosTemp = ()

    for (x, y) in grid:
        vecinosVivos = 0
        for (i,k) in vecinos:
            if (x+i, y+k) in grid:
                vecinosVivos += 1

            else:
                vecinosTemp = (*vecinosTemp, (x+i, y+k))

        if vecinosVivos == 2 or vecinosVivos == 3:
            gridTemp = (*gridTemp, (x, y))

    vecinosTemp = list(set(vecinosTemp))
    gridTemp = list(set(gridTemp))

    for (x, y) in vecinosTemp:
        vecinosVivos = 0
        for (i,k) in vecinos:
            if (x+i, y+k) in grid:
                vecinosVivos += 1
        if vecinosVivos == 3:
            gridTemp = (*gridTemp, (x, y))
    

    return gridTemp


###################  GRID  ######################
pixel_size = 100

grid = ()

for i in range(80):
    w = screen.get_width() / pixel_size
    h = screen.get_height() / pixel_size

    x = randint(0, pixel_size)
    y = randint(0, pixel_size)

    choice = randint(0, 6)

    if choice == 0: #block
        grid = (*grid, (x, y))
        grid = (*grid, (x+1, y+1))
        grid = (*grid, (x, y+1))
        grid = (*grid, (x+1, y))
    
    elif choice == 1: #blinker
        grid = (*grid, (x, y))
        grid = (*grid, (x, y+1))
        grid = (*grid, (x, y+2))

    elif choice == 2: #spaceship glider
        grid = (*grid, (x, y))
        grid = (*grid, (x+1, y))
        grid = (*grid, (x+2, y+1))
        grid = (*grid, (x+2, y+3))

    elif choice == 3: #toad
        grid = (*grid, (x, y))
        grid = (*grid, (x, y+1))
        grid = (*grid, (x, y+2))
        grid = (*grid, (x+1, y+1))
        grid = (*grid, (x+1, y+2))
        grid = (*grid, (x+1, y+3))

    elif choice == 4: #beehive
        grid = (*grid, (x, y+1))
        grid = (*grid, (x+3, y+1))
        grid = (*grid, (x+1, y))
        grid = (*grid, (x+2, y))
        grid = (*grid, (x+1, y+2))
        grid = (*grid, (x+2, y+2))

    elif choice == 5: #tub
        grid = (*grid, (x, y+1))
        grid = (*grid, (x+2, y+1))
        grid = (*grid, (x+1, y))
        grid = (*grid, (x+1, y+2))

    elif choice == 6: #Gosper glider gun
        grid = (*grid, (x, y+4))
        grid = (*grid, (x, y+5))
        grid = (*grid, (x+1, y+4))
        grid = (*grid, (x+1, y+5))

        grid = (*grid, (x+10, y+3))
        grid = (*grid, (x+10, y+4))
        grid = (*grid, (x+10, y+5))

        grid = (*grid, (x+11, y+2))
        grid = (*grid, (x+11, y+6))

        grid = (*grid, (x+12, y+7))
        grid = (*grid, (x+12, y+1))
        grid = (*grid, (x+13, y+7))
        grid = (*grid, (x+13, y+1))

        grid = (*grid, (x+14, y+4))

        grid = (*grid, (x+15, y+2))
        grid = (*grid, (x+15, y+6))


        grid = (*grid, (x+16, y+3))
        grid = (*grid, (x+16, y+4))
        grid = (*grid, (x+16, y+5))

        grid = (*grid, (x+17, y+4))

        grid = (*grid, (x+20, y+5))
        grid = (*grid, (x+20, y+6))
        grid = (*grid, (x+20, y+7))

        grid = (*grid, (x+21, y+5))
        grid = (*grid, (x+21, y+6))
        grid = (*grid, (x+21, y+7))

        grid = (*grid, (x+22, y+4))
        grid = (*grid, (x+22, y+8))

        grid = (*grid, (x+24, y+3))
        grid = (*grid, (x+24, y+4))
        grid = (*grid, (x+24, y+8))
        grid = (*grid, (x+24, y+9))

        grid = (*grid, (x+34, y+6))
        grid = (*grid, (x+34, y+7))
        grid = (*grid, (x+35, y+6))
        grid = (*grid, (x+35, y+7))


###################  RAY TRACER  ######################
running = True
while running:
    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT)

    grid = draw(screen, grid, pixel_size)
    pygame.display.flip()

    time.sleep(0.1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False