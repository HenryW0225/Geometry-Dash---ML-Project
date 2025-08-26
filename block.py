class Block:
    def __init__ (self, start_x, start_y, size) :
        self.world_x = start_x
        self.world_y = start_y - size/2
        self.size = size
        self.jump = -15
        self.gravity = 1
        self.grounded = True
        self.vertical_velocity = 0
    
    def space_jump(self) :
        if (self.grounded) :
            self.vertical_velocity = self.jump
            self.grounded = False
            
    def update(self, floor) :
        self.world_y += self.vertical_velocity
        if (self.world_y + self.size/2 >= floor) :
            self.vertical_velocity = 0
            self.world_y = floor - self.size/2
            self.grounded = True
        else :
            self.vertical_velocity += self.gravity
    
    
    def coordinates(self) :
        return [self.world_x, self.world_y, self.size]
