import Game
import logging as log
import os


class minigame:

    def __init__(self, game):

        if(!(isinstance(game, Game.Game))):
            log.error("Minigame passed invalid game object")
            os.exit()
        this.game = game