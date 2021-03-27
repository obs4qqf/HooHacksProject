import Game
import logging as log
import sys
import pygame

class testObject(Game.GameObject):

    playerSpeed = 100

    def __init__(self, game):
        super().__init__()

        self.pos = [50, 50]
        self.velocity = [0, 0]
        self.game = game

        game.subscribeToEvent(self.onKeyDown, "OnKeyDown")
        game.subscribeToEvent(self.onKeyUp, "OnKeyUp")
        game.subscribeToEvent(self.onTick, "OnRenderTick")

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], 50, 50))

    def onKeyDown(self, key):
        print("KeyPressed")
        print(key)

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
