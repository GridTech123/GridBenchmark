#gbAPI is grid benchmark's API to communicate with the main app
#created by GridTech

import pygame
import pickle

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

pygame.init()

menu_font = pygame.font.SysFont('Calibri', 40)
hud_font = pygame.font.SysFont('Calibri', 40)
hud_font2 = pygame.font.SysFont('Calibri', 20)
big_font = pygame.font.SysFont('Calibri', 80)

def main(screen, sx, sy, FPS, curTest):
    pygame.draw.rect(screen, blue, [0, sy - 100, sx, 100])
    screen.blit(menu_font.render('FPS:' +str(FPS), True, white), (10, sy - 90))
    screen.blit(menu_font.render('testing: '+str(curTest), True, white), (sx / 2 - 100, sy - 90))

def calculate(fps):
        avgClock = 0
        drawObjectFps = 0
        try:
            while True:
                drawObjectFps = drawObjectFps + fps[avgClock]
                avgClock = avgClock + 1
        except:
            drawObjectFps = drawObjectFps/len(fps)
            pickle_out = open('last.sav', 'w')
            pickle.dump(drawObjectFps, pickle_out)
            pickle_out.close()
            try:
                pickle_in = open('best.sav', 'r')
                best = pickle.load(pickle_in)
                if best < drawObjectFps:
                    pickle_out = open('best.sav', 'w')
                    pickle.dump(drawObjectFps, pickle_out)
                    pickle_out.close()                      
            except:
                pickle_out = open('best.sav', 'w')
                pickle.dump(drawObjectFps, pickle_out)
                pickle_out.close()              