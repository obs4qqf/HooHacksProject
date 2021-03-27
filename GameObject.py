class GameObject:

    def __init__(self, pos=(0,0)):
        self.visible = True
        self.pos = [pos[0], pos[1]]

    def getRelativePos(self, camera):
        relativePos = self.pos
        relativePos[0] -= camera.x
        relativePos[1] -= camera.y
        return relativePos

    def set_visible(self, value):

        if(self.visible == value):
            return

        if(value == False):
            self.savedLayer = self.layer
            self.game.updateLayer(self, layer="Hidden")

        if(value == True):
            self.game.updateLayer(self, layer=savedLayer)

    def get_visible(self):
        return self.visible

    def render(self, screen, camera):
        #TODO verify screen is of correct type (couldnt figure out what type was called)
        #if(isinstance(screen, pygame.{SOMETHING})):
        #   log.error("Invalid screen type passed")
        pass

class PhysicsObject(GameObject):

    '''
    Collision dimensions in form [width, height]
    Position in form [x, y]
    '''


    def __init__(self, pos=(0,0), collisionDimensions=[10,10]):
        super().__init__(pos)
        self.collisionDimensions = collisionDimensions

    def isColliding(self, otherObj):
        if(self.pos[0] < otherObj.pos[0] + otherObj.collisionDimensions[0] and self.pos[0] + self.collisionDimensions[0] > otherObj.pos[0] and self.pos[1] < otherObj.pos[1] + otherObj.collisionDimensions[1] and self.pos[1] + self.collisionDimensions[1] > otherObj.pos[1]):
            return True
        return False