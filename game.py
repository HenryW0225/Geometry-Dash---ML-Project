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

# GAME
FRAME_UNIT = 8
GAME_FLOOR = SCREEN_HEIGHT - 250

#VARIABLES
#GAMES
screen_world_x = 0
clock = pygame.time.Clock()
running = True
jumping = False

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")

font = pygame.font.Font(None, 48)


def initialize() :
    clock = pygame.time.Clock()
    running = True
    jumping = False
    screen_world_x = 0

def createLevel() :
    level = Level()
    level.add_spike(1000, GAME_FLOOR)
    level.add_spike(2000, GAME_FLOOR)
    level.add_spike(2500, GAME_FLOOR)
    level.add_spike(3250, GAME_FLOOR)
    level.add_spike(3300, GAME_FLOOR)
    level.add_spike(4000, GAME_FLOOR)
    level.add_spike(4050, GAME_FLOOR)
    level.add_spike(4100, GAME_FLOOR)
    level.add_spike(4250, GAME_FLOOR)
    level.add_spike(4550, GAME_FLOOR)
    level.add_spike(4950, GAME_FLOOR)
    level.add_spike(5350, GAME_FLOOR)
    level.add_spike(5040, GAME_FLOOR)
    level.add_spike(5400, GAME_FLOOR)
    level.add_spike(5900, GAME_FLOOR)
    level.add_spike(5950, GAME_FLOOR)
    level.add_spike(6000, GAME_FLOOR)
    level.add_spike(6150, GAME_FLOOR)
    level.add_spike(6600, GAME_FLOOR)
    level.add_spike(6675, GAME_FLOOR)
    level.add_spike(7000, GAME_FLOOR)
    level.add_spike(7300, GAME_FLOOR)
    level.add_spike(7350, GAME_FLOOR)
    level.add_spike(7700, GAME_FLOOR)
    level.add_spike(7750, GAME_FLOOR)
    level.add_spike(8000, GAME_FLOOR)
    level.add_spike(8050, GAME_FLOOR)
    level.add_spike(8550, GAME_FLOOR)
    level.add_spike(8750, GAME_FLOOR)
    level.add_spike(9000, GAME_FLOOR)
    level.add_spike(9400, GAME_FLOOR)
    level.add_spike(9450, GAME_FLOOR)
    level.add_spike(9700, GAME_FLOOR)
    level.add_spike(9750, GAME_FLOOR)
    level.add_spike(9800, GAME_FLOOR)
    level.add_spike(10000, GAME_FLOOR)
    level.add_spike(10050, GAME_FLOOR)
    level.add_spike(10100, GAME_FLOOR)
    level.add_spike(10400, GAME_FLOOR)
    return level
    

initialize()

level = createLevel()

player = Block(450, GAME_FLOOR, 50)



"""while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                jumping = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                jumping = False
                
    if (jumping) :
        player.space_jump()


    #Updating screen
    screen.fill(WHITE)
    screen_world_x += FRAME_UNIT
    
    #Updating and drawing player
    player.update(GAME_FLOOR, FRAME_UNIT)
    [player_world_x, player_world_y, player_size] = player.coordinates()
    pygame.draw.rect(screen, RED, (player_world_x - screen_world_x - player_size/2, player_world_y - player_size/2, player_size, player_size))
    
    #Drawing floor of the game
    pygame.draw.rect(screen, GREY, (0, GAME_FLOOR, SCREEN_WIDTH, SCREEN_HEIGHT - GAME_FLOOR))
    
    #Drawing spikes
    spike_coordinates = level.update_spikes(screen_world_x, SCREEN_WIDTH, player_world_x, player_world_y, player_size)
    if (spike_coordinates == False) :
        running = False
    else :
        for spike in spike_coordinates :
            pygame.draw.polygon(screen, BLACK, [(spike[0] - spike[3]/2, spike[1]), (spike[0] + spike[3]/2, spike[1]), (spike[0], spike[1] - spike[2])])
    
    #Displaying score
    text_surface = font.render(f"Distance: {screen_world_x}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    screen.blit(text_surface, text_rect)
    
    
    pygame.display.flip()
    clock.tick(60)  

pygame.quit()"""



