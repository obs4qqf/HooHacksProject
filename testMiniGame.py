import Game
import GameObject
import logging as log
import sys
import pygame

bullets = []


class testObject(GameObject.PhysicsObject):

    playerSpeed = 100

    def __init__(self, game):
        super().__init__((50,50), [50,50])

        self.velocity = [0, 0]
        self.game = game

        game.subscribeToEvent(self.onKeyDown, "OnKeyDown")
        game.subscribeToEvent(self.onKeyUp, "OnKeyUp")
        game.subscribeToEvent(self.onTick, "OnRenderTick")

    def render(self, screen, camera):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], 50, 50))

    def onKeyDown(self, key):

        if(key == 's'):
            self.velocity[1] -= self.playerSpeed
        elif(key == 'w'):
            self.velocity[1] += self.playerSpeed
        if(key == 'd'):
            self.velocity[0] -= self.playerSpeed
        elif(key == 'a'):
            self.velocity[0] += self.playerSpeed

    def onKeyUp(self, key):
        if(key == 's'):
            self.velocity[1] += self.playerSpeed
        elif(key == 'w'):
            self.velocity[1] -= self.playerSpeed
        if(key == 'd'):
            self.velocity[0] += self.playerSpeed
        elif(key == 'a'):
            self.velocity[0] -= self.playerSpeed

    def onTick(self):
        self.pos[0] += self.velocity[0] * self.game.deltaTime
        self.pos[1] += self.velocity[1] * self.game.deltaTime

        for obj in bullets:
            if(self.isColliding(obj)):
                print("Colliding")

class collisionObject(GameObject.PhysicsObject):

    def __init__(self, game):
        super().__init__((100,100), [50,50])
        self.game = game

    def render(self, screen, camera):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], self.collisionDimensions[0], self.collisionDimensions[1]))

class minigame:

    def __init__(self, game):

        #TODO make this work
        # if(isinstance(game, Game.Game) == False):
        #     log.error("Minigame passed invalid game object")
        #     sys.exit()

        self.game = game

    def start(self):
        self.game.background = (0,255,0)
        self.game.addObject(testObject(self.game))

        bullet = collisionObject(self.game)
        bullets.append(bullet)
        self.game.addObject(bullet)
