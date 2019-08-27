import pygame, sys
from pygame.locals import *

_image_library = {}

def main():
    initGameVars()
    initGameLoop()

def initGameVars():
    global FPS, FPSCLOCK, MDISP
    global BLACK, WHITE, RED, GREEN, BLUE
    pygame.display.set_caption('Stardew Valley')
    FPS = 30
    FPSCLOCK = pygame.time.Clock()
    MDISP = pygame.display.set_mode((300, 300), 0, 32)

    BLACK   =   ( 0, 0, 0)
    WHITE   =   ( 255,255,255)
    RED     =   ( 255,0,0)
    GREEN   =   ( 0,255,0)
    BLUE    =   ( 0,0,255)

    pygame.init()

def getImage(imagePath):
    image = _image_library.get(imagePath)
    if image == None:
        image = pygame.image.load(imagePath)
        _image_library[imagePath] = image
    return image

def getText(text):
    fontObj = pygame.font.SysFont('helvetica', 16)
    return fontObj.render(text, True, BLACK)

def handleEvents(eventQueue):
    for event in eventQueue:
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def initGameLoop():
    while True:
        MDISP.fill(WHITE)

        handleEvents(pygame.event.get())

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()