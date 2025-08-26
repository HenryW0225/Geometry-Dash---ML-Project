import pygame
from block import Block
from level import Level



# CONSTANTS
# COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREY = (200, 200, 200)
BLACK = (0, 0, 0)

# SCREEN
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 750

#VARIABLES
#GAMES
gameFloor = SCREEN_HEIGHT - 250
screenWorldX = 0
clock = pygame.time.Clock()
running = True
screenWorldX = 0


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")


def initialize() :
    clock = pygame.time.Clock()
    running = True
    screenWorldX = 0

def createLevel() :
    Level1 = Level(gameFloor)
    Level1.add_spike(1000)
    Level1.add_spike(2000)
    Level1.add_spike(2500)
    return Level1
    

initialize()
Level1 = createLevel()
player = Block(450, gameFloor, 50)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.space_jump()
                
    #Updating screen
    screen.fill(WHITE)
    screenWorldX += 5
    
    #Updating and drawing player
    player.update(gameFloor)
    coordinates = player.coordinates()
    playerSize = coordinates[2]
    pygame.draw.rect(screen, RED, (coordinates[0] - playerSize/2, coordinates[1] - playerSize/2, playerSize, playerSize))
    
    #Drawing floor of the game
    pygame.draw.rect(screen, GREY, (0, gameFloor, SCREEN_WIDTH, SCREEN_HEIGHT - gameFloor))
    
    #Drawing spikes
    spikeCoordinates = Level1.update_spikes(screenWorldX, SCREEN_WIDTH, coordinates[0], coordinates[1], playerSize)
    if (spikeCoordinates == False) :
        running = False
    else :
        for spike in spikeCoordinates :
            pygame.draw.polygon(screen, BLACK, [(spike[0] - spike[3]/2, spike[1]), (spike[0] + spike[3]/2, spike[1]), (spike[0], spike[1] - spike[2])])
    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()
