class Spike :
    def __init__(self, world_x, world_y, height = 50, width = 50) :
        self.world_x = world_x
        self.world_y = world_y
        self.height = height
        self.width = width
    
    def is_colliding(self, block_x, block_y, block_size):
        bottom_left  = (block_x - block_size//2, block_y + block_size//2)
        bottom_right = (block_x + block_size//2, block_y + block_size//2)

        top    = (self.world_x, self.world_y - self.height)
        left   = (self.world_x - self.width // 2, self.world_y)
        right  = (self.world_x + self.width // 2, self.world_y)

        def ccw(a, b, c): return (c[1]-a[1])*(b[0]-a[0]) >= (b[1]-a[1])*(c[0]-a[0])
        def intersect(p1, p2, q1, q2):
            return ccw(p1,q1,q2) != ccw(p2,q1,q2) and ccw(p1,p2,q1) != ccw(p1,p2,q2)

        if intersect(bottom_left, bottom_right, left, top): return True
        if intersect(bottom_left, bottom_right, right, top): return True

        return False
    
    def visible(self, screen_world_x, screen_width) :
        if (self.world_x + self.width//2 >= screen_world_x or self.world_x <= screen_world_x + screen_width) :    
            return [self.world_x, self.world_y, self.height, self.width]
        return None
    

class Level :
    def __init__(self) :
        self.spikes = []
    
    def add_spike(self, world_x, floor, height = 50, width = 50) :
        newSpike = Spike(world_x, floor, height, width) 
        self.spikes.append(newSpike)
    
    def floor(self) :
        return self.floor
    
    def update_spikes(self, screen_world_x, SCREEN_WIDTH,) :
        spike_coordinates = []
        for spike in self.spikes :
            coordinates = spike.visible(screen_world_x, SCREEN_WIDTH) 
            if (coordinates != None) :
                coordinates[0] -= screen_world_x
                spike_coordinates.append(coordinates)
        return spike_coordinates
    
    def possible_collision(self, players_world_x, players_size) :
        possible_collisions = []
        for spike in self.spikes :
            if (spike.world_x + spike.width//2 >= players_world_x - players_size//2 and spike.world_x - spike.width//2 <= players_world_x + players_size//2) :
                possible_collisions.append(spike)
        
        return possible_collisions
            
    def is_colliding(self, possible_collisions, player) :
        for spike in possible_collisions :
            if (spike.is_colliding(player.world_x, player.world_y, player.size)) :
                return True
        return False
                
            
        