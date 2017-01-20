try:
    import pygame 
    from pygame import *
    from pygame.locals import *
    import random
    import sys
    import pickle
    import time
    import os
    import pyError
    import gbAPI
except:
    try:
        import pyError
        pyError.newError('City Driver 2 Error', 'There was an error on start', 'there was an issue importing something, make sure to use exe', 20, 20)
    except:
        print 'ERROR: pyError does not exist'

#colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 150, 200)
blue2 = (44, 157, 201)
blue3 = (8, 140, 196)
blue4 = (40, 181, 166)
red = (255, 0, 0)
green = (0, 255, 0)
green2 = (0, 153, 0)
green3 = (0,100,0)
gray = (158, 156, 166)
gray2 = (69, 67, 68)

#images

#setup
clock = pygame.time.Clock()

#vars
clock = pygame.time.Clock()
currentTest = 'draw objects'
fps = []

#draw object vars
box1x = 0
box1y = 0
box2x = 0
box2y = 0
drawObjectFps = 0

#pygame start
try:
    from win32api import GetSystemMetrics
except:
    pyError.newError('City Driver 2 Error', 'There was an error on start', 'there was an issue importing win32api(pywin32), make sure to use exe', 20, 20)   
try:  
    print "Width =", GetSystemMetrics(0)
    print "Height =", GetSystemMetrics(1)
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % ( GetSystemMetrics(0) / 4, 1)
    pygame.init()
    fx = GetSystemMetrics(0)
    fy = GetSystemMetrics(1)
    mode = FULLSCREEN
    screen = pygame.display.set_mode([fx,fy], mode)
    sx, sy = screen.get_size()
except:
    pyError.newError('City Driver 2 Error', 'There was an error on start', 'We dont know what happened', 20, 20)   

if sx < 500:
    pyError.newError('window to small', 'your screen may be to small to use this app correctly', '' , 20, 20)

if sy < 720:
    pyError.newError('window to small', 'your screen may be to small to use this app correctly', '' , 20, 20)

#fonts
menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)

#window settings
#pygame.display.set_icon(logo_img)
pygame.display.set_caption("Grid Benchmark")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()

    screen.fill(black)

    clock.tick(((9^9)^9)^9)

    if currentTest == 'draw objects':
        pygame.draw.rect(screen, blue2, [0,0,box1x, box1y])
        box1x = box1x + 2
        box1y = box1y + 2
        pygame.draw.rect(screen, blue3, [0,0,box2x, box2y])
        box2x = box2x + 1
        box2y = box2y + 1
        fps.append(clock.get_fps())
        if box1x > 3000:
            currentTest = 'calculate 1'

    if currentTest == 'calculate 1':
        gbAPI.calculate(fps)
        pickle_out = open('update.run', 'w')
        pickle.dump(True, pickle_out)
        pickle_out.close()
        sys.exit()

    gbAPI.main(screen, sx, sy, clock.get_fps(), currentTest)
    pygame.display.update()