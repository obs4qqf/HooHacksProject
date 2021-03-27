import Game
import GameObject
import logging as log
import sys
import pygame

pygame.font.init()

bullets = []
healthLength = 100
introText = pygame.font.SysFont('Arial', 25)
introTextRender = introText.render('Don\'t touch the walls!', False, (0, 0, 0))

class testObject(GameObject.PhysicsObject):

    global introText
    global introTextRender

    playerSpeed = 100
    playerHealth = 100

    def __init__(self, game):
        super().__init__((25,50), [50,50])

        self.velocity = [0, 0]
        self.game = game

        game.subscribeToEvent(self.onKeyDown, "OnKeyDown")
        game.subscribeToEvent(self.onKeyUp, "OnKeyUp")
        game.subscribeToEvent(self.onTick, "OnRenderTick")

    def render(self, screen, camera):
        pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.pos[0], self.pos[1], 50, 50))
        screen.blit(introTextRender, (170, 230))

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

        global healthLength

        self.pos[0] += self.velocity[0] * self.game.deltaTime
        self.pos[1] += self.velocity[1] * self.game.deltaTime

        for obj in bullets:
            if(self.isColliding(obj)):
                print("Colliding")
                healthLength = healthLength - 0.03

class healthBar(GameObject.PhysicsObject):

    def __init__(self, game):
        super().__init__((250,20), [100,10])
        self.game = game

    def render(self, screen, camera):
        global healthLength
        text = pygame.font.SysFont('Arial', 25)
        textRender = text.render('Health:', False, (0, 0, 0))
        screen.blit(textRender, (150,10))
        pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(self.pos[0], self.pos[1], healthLength, 10))

class collisionObject(GameObject.PhysicsObject):

    def __init__(self, game, xpos, ypos, xsize, ysize):
        super().__init__((xpos,ypos), [xsize, ysize])
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

        bullet1 = collisionObject(self.game, 0, 0, 10, 500)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 100, 0, 10, 400)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 100, 400, 100, 10)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 190, 300, 100, 10)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 100, 200, 100, 10)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 190, 100, 100, 10)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 290, 100, 10, 400)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 390, 0, 10, 400)
        bullets.append(bullet1)
        self.game.addObject(bullet1)
        bullet1 = collisionObject(self.game, 470, 0, 10, 400)
        bullets.append(bullet1)
        self.game.addObject(bullet1)

        self.game.addObject(healthBar(self.game))

        self.game.addObject(testObject(self.game))