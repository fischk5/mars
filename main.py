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

def quitGame():
    pygame.quit()
    sys.exit()

def handleEvents(eventQueue):
    for event in eventQueue:
        if event.type == QUIT:
            quitGame()

def drawCanvas():
    # need instructions for how to draw the canvas... a scene?
    # perhaps the currentImageList populates based on the scene
    # using a loadScene function
    currentImageList = ["dirt1.png"]
    currentImages = []
    for image in currentImageList:
        currentImages.append(getImage(image))
    # also need instructions for what to do with the images once loaded
    screen = pygame.display.get_surface()
    screen.fill(WHITE)
    for image in currentImages:
        screen.blit(image, (screen.get_width()/2,screen.get_height()/2))
    pygame.display.update()

    

def initGameLoop():
    
    while True:
        drawCanvas()
        handleEvents(pygame.event.get())
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()