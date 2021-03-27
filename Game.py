import pygame
import sys
import logging as log
import testMiniGame

pygame.init()

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
min_dimension = min(screen_width, screen_height)

# STATIC VARIABLES
DEFAULT_SCREEN_SIZE = (int(min_dimension / 1.5), int(min_dimension / 1.5))
DEFAULT_SCREEN_BACKGROUND = 'white'
DEFAULT_MINIGAME = testMiniGame.minigame



# Simple demonstration of squares
def example_squares(pygame_surface, board_info):
    for i in range(10):
        for j in range(10):
            # Create a rect with board_info.get_pixels_from_grid(x, y, width, height)
            rect = pygame.Rect(board_info.get_pixels_from_grid(i, j, 1, 1))

            # Draw it onto the surface
            pygame.draw.rect(pygame_surface, "blue", rect)  # fill
            pygame.draw.rect(pygame_surface, "black", rect, width=1)  # outline

class BoardInfo:
    # __init__ function = constructor
    # self. = this. in Java
    def __init__(self, screen_width, screen_height, num_of_squares):
        self.num_of_squares = num_of_squares
        self.grid_length = min(screen_width, screen_height) / num_of_squares

        if screen_width > screen_height:  # landscape window -> center horizontally
            self.x_offset = (screen_width - screen_height) / 2
            self.y_offset = 0
        else:  # portrait window -> center vertically
            self.x_offset = 0
            self.y_offset = (screen_height - screen_width) / 2

    def get_pixels_from_grid(self, start_x, start_y, width, height):
        return (start_x * self.grid_length + self.x_offset, start_y * self.grid_length + self.y_offset,
                width * self.grid_length, height * self.grid_length)

    def get_grid_from_pixels(self, x_pos, y_pos):
        if x_pos < self.x_offset or x_pos > self.x_offset + self.grid_length * self.num_of_squares:
            return None  # outside of grid
        if y_pos < self.y_offset or y_pos > self.y_offset + self.grid_length * self.num_of_squares:
            return None  # outside of grid
        grid_coords = ((x_pos - self.x_offset) // self.grid_length,
                       (y_pos - self.y_offset) // self.grid_length)
        return grid_coords

class GameObject:

    def __init__(self):
        self.visible = True

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

    def render(self, screen):
        #TODO verify screen is of correct type (couldnt figure out what type was called)
        #if(isinstance(screen, pygame.{SOMETHING})):
        #   log.error("Invalid screen type passed")
        pass

class testObject(GameObject):

    def __init__(self):
        super().__init__()

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(50, 50, 50, 50))

class Game:

    def __init__(self):

        self.objects = {"Layer1":[],"Layer2":[],"Layer3":[],"Layer4":[],"Layer5":[],"Layer6":[],"Layer7":[],"Layer8":[],"Layer9":[],"Hidden":[]}
        self.events = {"OnClick":[]}

        self.screen = pygame.display.set_mode(DEFAULT_SCREEN_SIZE, pygame.RESIZABLE, pygame.SCALED)
        self.board = BoardInfo(pygame.display.Info().current_w, pygame.display.Info().current_h, 10)

        self.background = DEFAULT_SCREEN_BACKGROUND

        if(DEFAULT_MINIGAME != 0):
            self.loadMinigame(DEFAULT_MINIGAME)

        #self.addObject(testObject())

        self.gameLoop()

    def gameLoop(self):
        while True:
            self.eventManager()
            self.render()

    def render(self):
        self.screen.fill(self.background)

        #example_squares(self.screen, self.board)

        for key in self.objects:
            if key == "Hidden":
                continue

            for value in self.objects[key]:
                value.render(self.screen)

        

        pygame.display.update()

    def renderTick(self):
        pass

    def eventManager(self):
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:  # x clicked
                self.exitGame()

            elif event.type == pygame.VIDEORESIZE:  # window resized
                self.board = BoardInfo(pygame.display.Info().current_w, pygame.display.Info().current_h, 10)

            elif event.type == pygame.MOUSEBUTTONUP:  # click detected
                clicked_x, clicked_y = pygame.mouse.get_pos()  # gets raw pixels from click
                grid_space_clicked = self.board.get_grid_from_pixels(clicked_x, clicked_y)  # convert to grid spaces
                print(grid_space_clicked)

    def addObject(self, obj, layer="Layer1", isMinigame=True):
        self.objects[layer].append(obj)
        self.updateLayer(obj, layer)
        obj.isMinigame = isMinigame

    def updateLayer(self, obj, layer="Layer1"):
        obj.layer = layer
        if(obj.layer == "Hidden"):
            obj.visible = False
        else:
            obj.visible = True

    def exitGame(self):
        pygame.quit()
        sys.exit()

    def removeObject(self, obj):
        self.objects[obj.layer].remove(obj)

    def loadMinigame(self, minigame):
        for key in self.objects:
            if(key == "Hidden"):
                for obj in self.objects["Hidden"]:
                    obj.alreadyHidden = True
                    continue

            for obj in self.objects[key]:
                obj.set_visible(False)

        self.minigame = minigame(self).start()

    def exitMinigame(self):
        self.minigame.exitGame()
        del self.minigame

        for key in self.objects:

            for obj in self.objects[key]:
                
                if(obj.isMinigame):
                    self.removeObject(obj)
                else:
                    if(obj.alreadyHidden):
                        obj.alreadyHidden = False
                    else:
                        obj.set_visible(True)

if __name__ == "__main__":
    Game()