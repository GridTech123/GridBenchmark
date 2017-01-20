def update():
    rendermode = 'loading'

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
rendermode = 'loading'
backgroundColor1 = 0
backgroundColor2 = 150
backgroundColor3 = 201
benchmarks = []
updates = 0
currentBenchmark = 0

#images
left = pygame.image.load('left.png')
right = pygame.image.load('right.png')

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
    mode = RESIZABLE
    screen = pygame.display.set_mode([fx - 100,fy - 100], mode)
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

#program
#program
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==VIDEORESIZE:
            screen=pygame.display.set_mode(event.dict['size'], mode)
            sx, sy = screen.get_size()


    #settings
    screen.fill((backgroundColor1, backgroundColor2, backgroundColor3))
    clock.tick(200)
    mx, my = pygame.mouse.get_pos()

    fps_text = menu_font.render('FPS:' +str (clock.get_fps()), True, white)

    pygame.draw.rect(screen, blue, [100, 100, sx - 200, sy - 200])
    pygame.draw.rect(screen, blue2, [(sx / 2) - ((sx - 400) / 2), 200, sx - 400, 600])

    backgroundColor1 = backgroundColor1 + .1
    backgroundColor2 = backgroundColor2 + .1
    backgroundColor3 = backgroundColor3 + .1
    if backgroundColor1 > 254:
        backgroundColor1 = 0
    if backgroundColor2 > 254:
        backgroundColor2 = 150
    if backgroundColor3 > 254:
        backgroundColor3 = 200

    if rendermode == 'loading':
        screen.blit(big_font.render('Loading your data', True, blue3), (sx/2 - 300, 200))
        pygame.display.update()
        os.chdir('benchmarks')
        benchmarks = os.listdir(os.getcwd())
        os.chdir('..')
        numBenchmarks = len(benchmarks)
        cwd = os.getcwd()
        rendermode = 'newDir'

    if rendermode == 'newDir':
        currentDir = benchmarks[currentBenchmark]
        os.chdir('benchmarks')
        os.chdir(currentDir)
        cover = pygame.image.load('cover.png')
        try:
            pickle_in = open('best.sav', 'r')
            best = pickle.load(pickle_in)    
        except:
            best = '--'    
        try:
            pickle_in = open('last.sav', 'r')
            last = pickle.load(pickle_in)      
        except:
            last = '--'
        rendermode = 'menu'

    if rendermode == 'menu':
        cover = pygame.transform.scale(cover, (sx - 400, 300))
        screen.blit(cover, (200, 200))    
        screen.blit(big_font.render(currentDir, True, blue3), (200, 510))  
        if mx > (sx / 2) - 150 and mx < (sx / 2) - 150 + 300 and my > 600 and my < 700:
            pygame.draw.rect(screen, blue, [(sx / 2) - 150, 600, 300, 100]) 
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                try:
                    os.startfile('benchmark.exe')
                except:
                    os.startfile('benchmark.py')
        else:
            pygame.draw.rect(screen, blue3, [(sx / 2) - 150, 600, 300, 100])         
        screen.blit(big_font.render('RUN', True, blue2), ((sx / 2) - 75, 600))
        screen.blit(menu_font.render('Last Run: '+str(last)+str(' fps'), True, blue3), (210, 720))       
        screen.blit(menu_font.render('Best Run: '+str(best)+str(' fps'), True, blue3), (210, 750)) 
   
        screen.blit(left, (sx - 200, sy / 2 - 45))
        if mx > sx - 200 and mx < sx - 200 + 90 and my > sy / 2 - 45 and my < sy / 2 - 45 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if currentBenchmark < len(benchmarks) - 1:
                    currentBenchmark = currentBenchmark + 1
                    rendermode = 'load'
        screen.blit(right, (110, sy / 2 - 45))
        if mx > 110 and mx < 110 + 90 and my > sy / 2 - 45 and my < sy / 2 - 45 + 90:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if currentBenchmark > 0:
                    currentBenchmark = currentBenchmark - 1
                    rendermode = 'load'
                
        


        pickle_in = open('update.run', 'r')
        update = pickle.load(pickle_in)
        if update == True:
            rendermode = 'loading'
            pickle_out = open('update.run', 'w')
            pickle.dump(False, pickle_out)
            pickle_out.close()
            os.chdir('..')
            os.chdir('..')
            update = False
            

    pygame.display.update()