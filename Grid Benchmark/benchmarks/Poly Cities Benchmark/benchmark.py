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
os.chdir('images')
main_back1 = pygame.image.load("main_backround1.jpg")
menu1_img = pygame.image.load("menu.png")
mouse = pygame.image.load("mouse.png")
mouse2 = pygame.image.load("mouse2.png")
menu2_img = pygame.image.load("menuBack.png")
checked_img = pygame.image.load("checked.png")
unchecked_img = pygame.image.load("unchecked.png")
grass1_img = pygame.image.load("grass1.png")
logo = pygame.image.load('logo.png')
GUIbar = pygame.image.load('GUIbar.png')
roadGUI_img = pygame.image.load('roadGUI.png')
roadGUI2_img = pygame.image.load('roadGUI2.png')
road_img = pygame.image.load('road.png')
backGUI_img = pygame.image.load('backGUI.png')
outline_img = pygame.image.load('outline.png')
roadTurnGUI_img = pygame.image.load('roadTurnGUI.png')
roadTurn_img = pygame.image.load('roadTurn.png')
terraformGUI_img = pygame.image.load('terraformGUI.png')
waterGUI_img = pygame.image.load('waterGUI.png')
water_img = pygame.image.load('water.png')
grassGUI_img = pygame.image.load('grassGUI.png')
topGuiBar_img = pygame.image.load('topGuiBar.png')
topGuiBarData_img = pygame.image.load('topGuiData.png')
topGuiBarMoney_img = pygame.image.load('topGuiLogoMoney.png')
tree1_img = pygame.image.load('tree1.png')
tree2_img = pygame.image.load('tree2.png')
grass2_img = pygame.image.load('grass2.png')
grass3_img = pygame.image.load('grass3.png')
midwest_img = pygame.image.load('theMidwest.png')
west_img = pygame.image.load('theWest.png')
notheast_img = pygame.image.load('theNortheast.png')
south_img = pygame.image.load('theSouth.png')
midwestHover_img = pygame.image.load('theMidwestHover.png')
westHover_img = pygame.image.load('theWestHover.png')
notheastHover_img = pygame.image.load('theNortheastHover.png')
southHover_img = pygame.image.load('theSouthHover.png')
sand_img = pygame.image.load('sand.png')
buildingsGUI = pygame.image.load('buildingsGUI.png')
smallHouseGUI_img = pygame.image.load('smallHouseGUI.png')
smallHouse_img = pygame.image.load('smallHouse.png')
logo1_img = pygame.image.load('logo1.png')
logo2_img = pygame.image.load('logo2.png')
AButton_img = pygame.image.load('A_Button.png')
BButton_img = pygame.image.load('B_Button.png')
XButton_img = pygame.image.load('X_Button.png')
YButton_img = pygame.image.load('Y_Button.png')
os.chdir('..')


#setup
clock = pygame.time.Clock()

#vars
clock = pygame.time.Clock()
currentTest = 'Poly Cities Benchmark'
fps = []
scale = 0
rendermode = 'load sandbox'
renderer = 'r2'
place = 'none'
placeSav = 'none'
saveLoad = 0
guiMenu = 'home'
angle = 0
cityName = ''
ver = 'alpha 1.1.4'
renderer = 'r2'
renderTrees = True
selected = False
OpenMessage = False
benchmark = 'loading screens'
loadingPer = 0
loading = ''
loadingList = []
alphaMenu = True
customizeTrees = 50
customizeWater = 50
fpsMessage = True
mousex = 100
mousey = 100
gamex = -3750
gamey = -3750
frames = 0

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

    if currentTest == 'Poly Cities Benchmark':
        if rendermode == 'load sandbox':
            size = 900
            renderClock = 0
            loading_animation = 1
            loading_back_x = 0
            world = ['']
            worldSav = ['']
            worldSavAngle = ['']
            rendermode = 'load'
            population = 0
            money = 'unlimited'
            selected = 'midwest'
        if rendermode == 'load':
            if selected == 'midwest':
                if renderClock < size:
                    loadRandom = random.randint(0,4)
                    if loadRandom == 0:
                        world.append(grass1_img)
                        loading = 'grass1_img'
                        worldSav.append('grass1_img')
                        worldSavAngle.append(0)
                    if loadRandom == 1:
                        world.append(grass2_img)
                        loading = 'grass2_img'
                        worldSav.append('grass2_img')
                        worldSavAngle.append(0)
                    if loadRandom == 2:
                        world.append(grass3_img)
                        loading = 'grass3_img'
                        worldSav.append('grass3_img')
                        worldSavAngle.append(0)
                    if loadRandom == 3:
                        world.append(grass3_img)
                        loading = 'grass3_img'
                        worldSav.append('grass3_img')
                        worldSavAngle.append(0)
                    if loadRandom == 4:
                        world.append(water_img)
                        loading = 'water_img'
                        worldSav.append('water_img')
                        worldSavAngle.append(0)
                    renderClock = renderClock + 1
                else:
                    rendermode = 'load 2'
        if rendermode == 'load 2':
                loading = 'starting load 2'
                trees = ['']
                treeOffsetY = [0]
                treeOffsetX = [0]
                rendermode = 'load 3'
        if rendermode == 'load 3':
            if selected == 'midwest':
                if renderClock < size * 2:
                    loadRandom = random.randint(0,3)
                    if loadRandom == 0:
                        trees.append('none')
                        treeOffsetX.append((random.randint(0,50)))
                        treeOffsetY.append((random.randint(0,100)))
                        loading = 'tree_none'
        #                worldSavTree.append('tree1')
                    if loadRandom == 1:
                        trees.append(tree1_img)
                        treeOffsetX.append((random.randint(0,50)))
                        treeOffsetY.append((random.randint(0,100)))
                        loading = 'tree1'
        #                worldSavTree.append('tree1')
                    if loadRandom == 2:
                        trees.append(tree1_img)
                        treeOffsetX.append((random.randint(0,50)))
                        treeOffsetY.append((random.randint(0,100)))
                        loading = 'tree1'
        #                worldSavTree.append('tree1')
                    if loadRandom == 3:
                        trees.append(tree1_img)
                        treeOffsetX.append((random.randint(0,50)))
                        treeOffsetY.append((random.randint(0,100)))
                        loading = 'tree1'
        #                worldSavTree.append('tree1')
                    renderClock = renderClock + 1
                else:
                    rendermode = 'game'
        if rendermode == 'load' or rendermode == 'load 2' or rendermode == 'load 3':
            screen.fill(blue2)
            screen.blit(logo2_img,(sx/2 - 200, sy/2 - 300))
            pygame.draw.rect(screen, gray2, [100, sy - 270, 620, 60])
            pygame.draw.rect(screen, blue2, [110, sy - 260, renderClock/3, 40])     
            pygame.draw.rect(screen, gray2, [100, sy - 200, 620, 60])
            screen.blit(menu_font.render('Creating map tiles: '+str(loading), True, blue2),(110, sy - 190))
        if rendermode == 'game':
            if renderer == 'r2':
                render = True
                renderX = 0
                xClock = 0
                renderY = 0
                renderClock = 1
                while render == True:
                    try:
                        if renderX + gamex > 0 - 250 and renderX + gamex < sx and renderY + gamey > 0 - 250 and renderY + gamey < sy:
                            screen.blit(world[renderClock], (renderX + gamex, renderY + gamey))
                            if not trees[renderClock] == 'none':
                                if renderTrees == True:
                                    if world[renderClock] == grass1_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass2_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                                    elif world[renderClock] == grass3_img:
                                        if (renderX + gamex)+treeOffsetX[renderClock] > 0 - 250 and (renderX + gamex)+treeOffsetX[renderClock] < sx and (renderY + gamey)+treeOffsetY[renderClock] > 0 - 250 and (renderY + gamey)+treeOffsetY[renderClock] < sy:
                                            screen.blit(trees[renderClock], ((renderX + gamex)+treeOffsetX[renderClock], (renderY + gamey)+treeOffsetY[renderClock]))
                            if not place == 'none':
                                if mx > renderX + gamex and mx < renderX + gamex + 250 and my > renderY + gamey and my < renderY + gamey + 250:
                                    screen.blit(outline_img,(renderX + gamex, renderY + gamey))
                                    if event.type == MOUSEBUTTONDOWN and event.button == 1:   
                                        if not my > sy - 100:
                                            if selected == 'road_img':
                                                if money > 99 or money == 'unlimited':
                                                    money = money - 100
                                                    world[renderClock] = place
                                                    worldSav[renderClock] = ''+str(placeSav)
                                                    worldSavAngle[renderClock] = angle    
                        world[renderClock]
                        renderX = renderX + 250
                        xClock = xClock + 1
                        renderClock = renderClock + 1
                        if xClock == 30:
                            renderX = 0
                            xClock = 0
                            renderY = renderY + 250
                    except:
                        render = False
            gamex = gamex + 1
            gamey = gamey + 1
            frames = frames + 1
            if frames > 500:
                gbAPI.calculate(fps)
                pickle_out = open('update.run', 'w')
                pickle.dump(True, pickle_out)
                pickle_out.close()
                sys.exit()
        fps.append(clock.get_fps())

    if currentTest == 'calculate 1':
        gbAPI.calculate(fps)
        pickle_out = open('update.run', 'w')
        pickle.dump(True, pickle_out)
        pickle_out.close()
        sys.exit()

    gbAPI.main(screen, sx, sy, clock.get_fps(), currentTest)
    pygame.display.update()