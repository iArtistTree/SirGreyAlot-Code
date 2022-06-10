#imports pygame & time
from multiprocessing.connection import wait
import pygame,time
pygame.init()

#character
char = pygame.image.load(r'C:\Users\eddyg\OneDrive\Bureau\Projects\SirGreyAlot\images\Character.png')
pace = 0.1
posX = 0
posY = 0

#sets window settings
size = width, height = 1920, 1080
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Project SirGreyAlot")
bgrndclr = (50,168,66)


#game loop
running = True

while running:
    screen.fill(bgrndclr)
    screen.blit(char,(posX,posY))

    #MOVEMENT
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_w]:
        posY -= pace

    if keyPressed[pygame.K_a]:
        posX -= pace 
        
    if keyPressed[pygame.K_s]:
        posY += pace

    if keyPressed[pygame.K_d]:
        posX += pace 

    #for loop through the event queue
    for event in pygame.event.get():        
        #check for QUIT event
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update() 

pygame.quit()