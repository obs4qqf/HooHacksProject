import Game
import logging as log
import sys
import pygame

class PuzzlePiece(Game.NormalObject):

    def __init__(self, game, x, y, piece_number):
        super().__init__((x, y))

        self.pos = [x, y]
        self.velocity = [0, 0]
        self.game = game
        self.piece_number = piece_number

        game.subscribeToEvent(self.onTick, "OnRenderTick")

    def render(self, screen):
        rect = pygame.Rect(self.x, self.y, 50, 50)
        piece_img = pygame.load("image_puzzle_assets/image_puzzle_" + self.piece_number)
        screen.blit(piece_img, rect)
        # pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], 50, 50))


    def onTick(self):
        pass

class minigame:

    def __init__(self, game):

        #TODO make this work
        # if(isinstance(game, Game.Game) == False):
        #     log.error("Minigame passed invalid game object")
        #     sys.exit()

        self.game = game

    def start(self):
        self.game.background = (0,255,0)
        self.game.addObject(PuzzlePiece(self.game, 1, 1, 1))
        self.game.addObject(PuzzlePiece(self.game, 1, 2, 1))
        self.game.addObject(PuzzlePiece(self.game, 1, 3, 1))
        self.game.addObject(PuzzlePiece(self.game, 1, 2, 1))
