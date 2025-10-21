import pygame
import random
from block import Block
from level import Level

random.seed(43)

# -------------------------
# CONSTANTS
# -------------------------
# COLORS
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
GREY  = (200, 200, 200)
BLACK = (0, 0, 0)

# SCREEN
SCREEN_WIDTH  = 1500
SCREEN_HEIGHT = 750

# GAME
FRAME_UNIT = 8
GAME_FLOOR = SCREEN_HEIGHT - 250

# EXPERIMENT CONSTANTS
NUM_OF_PLAYERS       = 100
NUM_OF_GENERATIONS   = 100
MAX_DISTANCE         = 11000

START_X                  = 45
PLAYER_SIZE              = 50
NUM_OF_ADAPTATIONS       = 100
MIN_NUM_OF_INSTRUCTIONS  = MAX_DISTANCE//FRAME_UNIT

# You use NUM_OF_INSTRUCTIONS below; map it to your minimum (no behavior change intended)
NUM_OF_INSTRUCTIONS      = MIN_NUM_OF_INSTRUCTIONS

# -------------------------
# PYGAME SETUP
# -------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geometry Dash")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 48)

# -------------------------
# LEVEL
# -------------------------
def createLevel():
    level = Level()
    level.addSpike(1000, GAME_FLOOR)
    level.addSpike(2000, GAME_FLOOR)
    level.addSpike(2500, GAME_FLOOR)
    level.addSpike(3250, GAME_FLOOR)
    level.addSpike(3300, GAME_FLOOR)
    level.addSpike(4000, GAME_FLOOR)
    level.addSpike(4050, GAME_FLOOR)
    level.addSpike(4100, GAME_FLOOR)
    level.addSpike(4250, GAME_FLOOR)
    level.addSpike(4550, GAME_FLOOR)
    level.addSpike(4950, GAME_FLOOR)
    level.addSpike(5350, GAME_FLOOR)
    level.addSpike(5040, GAME_FLOOR)
    level.addSpike(5400, GAME_FLOOR)
    level.addSpike(5900, GAME_FLOOR)
    level.addSpike(5950, GAME_FLOOR)
    level.addSpike(6000, GAME_FLOOR)
    level.addSpike(6150, GAME_FLOOR)
    level.addSpike(6600, GAME_FLOOR)
    level.addSpike(6675, GAME_FLOOR)
    level.addSpike(7000, GAME_FLOOR)
    level.addSpike(7300, GAME_FLOOR)
    level.addSpike(7350, GAME_FLOOR)
    level.addSpike(7700, GAME_FLOOR)
    level.addSpike(7750, GAME_FLOOR)
    level.addSpike(8000, GAME_FLOOR)
    level.addSpike(8050, GAME_FLOOR)
    level.addSpike(8550, GAME_FLOOR)
    level.addSpike(8750, GAME_FLOOR)
    level.addSpike(9000, GAME_FLOOR)
    level.addSpike(9400, GAME_FLOOR)
    level.addSpike(9450, GAME_FLOOR)
    level.addSpike(9700, GAME_FLOOR)
    level.addSpike(9750, GAME_FLOOR)
    level.addSpike(9800, GAME_FLOOR)
    level.addSpike(10000, GAME_FLOOR)
    level.addSpike(10050, GAME_FLOOR)
    level.addSpike(10100, GAME_FLOOR)
    level.addSpike(10400, GAME_FLOOR)
    return level

# -------------------------
# PLAYERS
# -------------------------
def random_instructions(length):
    return [random.randint(0, 1) for _ in range(length)]

level = createLevel()

players = []
for _ in range(NUM_OF_PLAYERS):
    instructions = random_instructions(NUM_OF_INSTRUCTIONS)
    player = Block(START_X, GAME_FLOOR, PLAYER_SIZE, instructions)
    players.append(player)

# -------------------------
# MAIN LOOP (EXPERIMENT)
# -------------------------
frame = 0
screen_world_x = 0
running = True
remaining_players = NUM_OF_PLAYERS

for generation in range(1, NUM_OF_GENERATIONS + 1):
    # Reset variables
    frame = 0
    screen_world_x = 0
    running = True
    remaining_players = NUM_OF_PLAYERS

    for player in players:
        player.reset(START_X, GAME_FLOOR)

    while running and screen_world_x < MAX_DISTANCE:
        # Handle quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # Update background
        screen.fill(WHITE)
        screen_world_x += FRAME_UNIT

        # Update players
        for player in players:
            player.update(GAME_FLOOR, FRAME_UNIT, frame)

        # Collisions
        possible_collisions = level.possibleCollision(screen_world_x + START_X, PLAYER_SIZE)
        surviving_players = []
        for player in players:
            if level.isColliding(possible_collisions, player) is False or running is False:
                surviving_players.append(player)
            else:
                remaining_players -= 1
            if remaining_players == NUM_OF_PLAYERS // 4:
                running = False
        players = surviving_players

        # Draw players
        for player in players:
            player_world_x, player_world_y, player_size = player.coordinates()
            pygame.draw.rect(
                screen,
                RED,
                (
                    player_world_x - screen_world_x - player_size // 2,
                    player_world_y - player_size // 2,
                    player_size,
                    player_size,
                ),
            )

        # Draw floor
        pygame.draw.rect(screen, GREY, (0, GAME_FLOOR, SCREEN_WIDTH, SCREEN_HEIGHT - GAME_FLOOR))

        # Draw visible spikes
        spike_coordinates = level.updateSpikes(screen_world_x, SCREEN_WIDTH)
        for spike in spike_coordinates:
            pygame.draw.polygon(
                screen,
                BLACK,
                [
                    (spike[0] - spike[3] // 2, spike[1]),
                    (spike[0] + spike[3] // 2, spike[1]),
                    (spike[0], spike[1] - spike[2]),
                ],
            )

        # HUD: distance
        text_surface = font.render(f"Distance: {screen_world_x}", True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text_surface, text_rect)

        # HUD: generation
        text_surface = font.render(f"Generation: {generation}", True, BLACK)
        text_rect = text_surface.get_rect(center=(200, 100))
        screen.blit(text_surface, text_rect)

        # HUD: remaining players
        text_surface = font.render(f"# of remaining players: {len(players)}", True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))
        screen.blit(text_surface, text_rect)

        # Tick
        frame += 1
        pygame.display.flip()
        clock.tick(100)

    # Trim to top 25%
    if len(surviving_players) > NUM_OF_PLAYERS // 4:
        players = players[0 : NUM_OF_PLAYERS // 4]

    # Reproduce / adapt
    new_players = []
    for player in players:
        for _ in range(3):
            # NOTE: fields are worldX/worldY in your Block class
            new_player = Block(player.worldX, player.worldY, player.size, player.instructions.copy())
            new_player.adapt(NUM_OF_ADAPTATIONS, NUM_OF_INSTRUCTIONS, frame)
            new_players.append(new_player)

    players.extend(new_players)

pygame.quit()
