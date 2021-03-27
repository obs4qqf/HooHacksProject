import Game
import logging as log
import sys
import pygame

class testObject(Game.GameObject):

    def __init__(self):
        super().__init__()

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, 50, 50, 50))
class minigame:

    def __init__(self, game):

        #TODO make this work
        # if(isinstance(game, Game.Game) == False):
        #     log.error("Minigame passed invalid game object")
        #     sys.exit()

        self.game = game

    def start(self):
        self.game.background = (0,255,0)
        self.game.addObject(testObject())