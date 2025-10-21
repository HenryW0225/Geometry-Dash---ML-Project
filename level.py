class Spike:
    def __init__(self, worldX, worldY, height=50, width=50):
        self.worldX = worldX
        self.worldY = worldY
        self.height = height
        self.width = width
    
    def isColliding(self, blockX, blockY, blockSize): 
        bottomLeft  = (blockX - blockSize // 2, blockY + blockSize // 2)
        bottomRight = (blockX + blockSize // 2, blockY + blockSize // 2)

        top    = (self.worldX, self.worldY - self.height)
        left   = (self.worldX - self.width // 2, self.worldY)
        right  = (self.worldX + self.width // 2, self.worldY)

        def ccw(a, b, c): 
            return (c[1] - a[1]) * (b[0] - a[0]) >= (b[1] - a[1]) * (c[0] - a[0])
        
        def intersect(p1, p2, q1, q2):
            return ccw(p1, q1, q2) != ccw(p2, q1, q2) and ccw(p1, p2, q1) != ccw(p1, p2, q2)

        if intersect(bottomLeft, bottomRight, left, top): 
            return True
        if intersect(bottomLeft, bottomRight, right, top): 
            return True

        return False
    
    def visible(self, screenWorldX, SCREEN_WIDTH):
        if (self.worldX + self.width // 2 >= screenWorldX or self.worldX <= screenWorldX + SCREEN_WIDTH):    
            return [self.worldX, self.worldY, self.height, self.width]
        return None
    

class Level:
    def __init__(self):
        self.spikes = []
    
    def addSpike(self, worldX, floor, height=50, width=50):
        newSpike = Spike(worldX, floor, height, width) 
        self.spikes.append(newSpike)
    
    def floor(self):
        return self.floor
    
    def updateSpikes(self, screenWorldX, SCREEN_WIDTH):
        spikeCoordinates = []
        for spike in self.spikes:
            coordinates = spike.visible(screenWorldX, SCREEN_WIDTH) 
            if coordinates is not None:
                coordinates[0] -= screenWorldX
                spikeCoordinates.append(coordinates)
        return spikeCoordinates
    
    def possibleCollision(self, playerWorldX, playerSize):
        possibleCollisions = []
        for spike in self.spikes:
            if (spike.worldX + spike.width // 2 >= playerWorldX - playerSize // 2 
                and spike.worldX - spike.width // 2 <= playerWorldX + playerSize // 2):
                possibleCollisions.append(spike)
        
        return possibleCollisions
            
    def isColliding(self, possibleCollisions, player):
        for spike in possibleCollisions:
            if spike.isColliding(player.worldX, player.worldY, player.size):
                return True
        return False
