import pygame
import random
from block import Block
from level import Level

random.seed(42)

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


clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")

font = pygame.font.Font(None, 48)

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


# EXPIEREMENT CONSTANTS
NUM_OF_PLAYERS = 100
NUM_OF_GENERATIONS = 100
MAX_DISTANCE = 11000

START_X = 45
PLAYER_SIZE = 50
NUM_OF_ADAPTATIONS = 100
NUM_OF_INSTRUCTIONS = MAX_DISTANCE//FRAME_UNIT


# SETTING UP EXPERIEMENT
# CREATE LEVEL
level = createLevel()

# CREATE PLAYERS
players = []

def random_instructions(length):
    return [random.randint(0, 1) for _ in range(length)]

for i in range(NUM_OF_PLAYERS) :
    instructions = random_instructions(NUM_OF_INSTRUCTIONS)
    player = Block(START_X, GAME_FLOOR, PLAYER_SIZE, instructions)
    players.append(player)

# OTHER VARIABLES
frame = 0
screen_world_x = 0
running = True
remaining_players = NUM_OF_PLAYERS


# EXPIEREMENT
for generation in range(1, NUM_OF_GENERATIONS + 1) :
    # Reset variables
    frame = 0
    screen_world_x = 0
    running = True
    remaining_players = NUM_OF_PLAYERS
    for player in players:
        player.reset(START_X, GAME_FLOOR)
    
    while (running and screen_world_x < MAX_DISTANCE) :
        
        # Enable quiting of pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        # Updating screen
        screen.fill(WHITE)
        screen_world_x += FRAME_UNIT
        
        # Updating players
        for player in players :
            player.update(GAME_FLOOR, FRAME_UNIT, frame)
        
        # Checking for collisions
        possible_collisions = level.possible_collision(screen_world_x + START_X, PLAYER_SIZE)
        surviving_players = []
        for player in players :
            if (level.is_colliding(possible_collisions, player) == False or running == False) :
                surviving_players.append(player)
            else :
                remaining_players -= 1
            if (remaining_players == NUM_OF_PLAYERS//2) :
                running = False
                #break
        players = surviving_players
        
        # Drawing players
        for player in players :
            [player_world_x, player_world_y, player_size] = player.coordinates()
            pygame.draw.rect(screen, RED, (player_world_x - screen_world_x - player_size//2, player_world_y - player_size//2, player_size, player_size))
            
        # Drawing floor of the game
        pygame.draw.rect(screen, GREY, (0, GAME_FLOOR, SCREEN_WIDTH, SCREEN_HEIGHT - GAME_FLOOR))
        
        # Drawing visible spikes
        spike_coordinates = level.update_spikes(screen_world_x, SCREEN_WIDTH)
        for spike in spike_coordinates :
            pygame.draw.polygon(screen, BLACK, [(spike[0] - spike[3]//2, spike[1]), (spike[0] + spike[3]//2, spike[1]), (spike[0], spike[1] - spike[2])])
        
        # Displaying distance
        text_surface = font.render(f"Distance: {screen_world_x}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
        screen.blit(text_surface, text_rect)
        
        # Display generation number
        text_surface = font.render(f"Generation: {generation}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(200, 100))
        screen.blit(text_surface, text_rect)
        
        # Displaying number of remaining players
        text_surface = font.render(f"# of remaining players: {len(players)}", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
        screen.blit(text_surface, text_rect)
        
        # Update variables
        frame += 1
        
        # Displaying screen
        pygame.display.flip()
        clock.tick(100)  

    # Limiting player count
    if (len(surviving_players) > NUM_OF_PLAYERS//2) :
        players = players[0: NUM_OF_PLAYERS//2]
    
    # Adapting players
    new_players = []
    for player in players :
        new_player = Block(player.world_x, player.world_y, player.size, player.instructions)
        new_player.adapt(NUM_OF_ADAPTATIONS, NUM_OF_INSTRUCTIONS)
        new_players.append(new_player)
    for new_player in new_players :
        players.append(new_player)


pygame.quit()






