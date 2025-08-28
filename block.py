import random

random.seed(42)

class Block:
    def __init__ (self, start_x, start_y, size, instructions) :
        self.world_x = start_x
        self.world_y = start_y - size//2
        self.size = size
        self.jump = -15
        self.gravity = 1
        self.grounded = True
        self.vertical_velocity = 0
        self.instructions = instructions
    
    def space_jump(self) :
        if (self.grounded) :
            self.vertical_velocity = self.jump
            self.grounded = False
            
    def update(self, floor, FRAME_UNIT, frame) :
        if (self.instructions[frame] == 1) :
            self.space_jump()
        self.world_x += FRAME_UNIT
        self.world_y += self.vertical_velocity
        if (self.world_y + self.size//2 >= floor) :
            self.vertical_velocity = 0
            self.world_y = floor - self.size//2
            self.grounded = True
        else :
            self.vertical_velocity += self.gravity
    
    def coordinates(self) :
        return [self.world_x, self.world_y, self.size]
    
    def adapt(self, NUM_OF_ADAPTATIONS, NUM_OF_INSTRUCTIONS) :
        for i in range(NUM_OF_ADAPTATIONS) :
            index = random.randint(0, NUM_OF_INSTRUCTIONS - 1)
            self.instructions[index] = (self.instructions[index] + 1) % 2
    
    def reset(self, START_X, GAME_FLOOR) :
        self.world_x = START_X
        self.vertical_velocity = 0
        self.grounded = True
        self.world_y = GAME_FLOOR - self.size//2
    

