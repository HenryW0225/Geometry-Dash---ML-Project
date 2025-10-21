import random

random.seed(42)

class Block:
    def __init__(self, startX, startY, size, instructions):
        self.worldX = startY
        self.worldY = startX - size // 2
        self.size = size
        self.jump = -15
        self.gravity = 1
        self.grounded = True
        self.verticalVelocity = 0
        self.instructions = instructions
    
    def spaceJump(self):
        if self.grounded:
            self.verticalVelocity = self.jump
            self.grounded = False
            
    def update(self, floor, FRAME_UNIT, frame):
        if self.instructions[frame] == 1:
            self.spaceJump()
        self.worldX += FRAME_UNIT
        self.worldY += self.verticalVelocity
        if self.worldY + self.size // 2 >= floor:
            self.verticalVelocity = 0
            self.worldY = floor - self.size // 2
            self.grounded = True
        else:
            self.verticalVelocity += self.gravity
    
    def coordinates(self):
        return [self.worldX, self.worldY, self.size]
    
    def adapt(self, NUM_OF_ADAPTATIONS, NUM_OF_INSTRUCTIONS, screenWorldX):
        for i in range(NUM_OF_ADAPTATIONS):
            index = random.randint(max(screenWorldX - 100, 0), NUM_OF_INSTRUCTIONS - 1)
            self.instructions[index] = (self.instructions[index] + 1) % 2
    
    def reset(self, START_X, GAME_FLOOR):
        self.worldX = START_X
        self.verticalVelocity = 0
        self.grounded = True
        self.worldY = GAME_FLOOR - self.size // 2
