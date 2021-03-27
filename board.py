import pygame as pg


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


# Simple demonstration of squares
def example_squares(pygame_surface, board_info):
    for i in range(10):
        for j in range(10):
            # Create a rect with board_info.get_pixels_from_grid(x, y, width, height)
            rect = pg.Rect(board_info.get_pixels_from_grid(i, j, 1, 1))

            # Draw it onto the surface
            pg.draw.rect(pygame_surface, "blue", rect)  # fill
            pg.draw.rect(pygame_surface, "black", rect, width=1)  # outline


def main():
    pg.init()
    running = True
    pg.display.set_caption("HooHacks")
    screen_width, screen_height = pg.display.Info().current_w, pg.display.Info().current_h
    min_dimension = min(screen_width, screen_height)
    surf = pg.display.set_mode((int(min_dimension / 1.5), int(min_dimension / 1.5)), pg.RESIZABLE, pg.SCALED)

    board = BoardInfo(pg.display.Info().current_w, pg.display.Info().current_h, 10)

    while running:
        surf.fill('white')
        for ev in pg.event.get():
            if ev.type == pg.QUIT:  # x clicked
                running = False
            elif ev.type == pg.VIDEORESIZE:  # window resized
                board = BoardInfo(pg.display.Info().current_w, pg.display.Info().current_h, 10)
            elif ev.type == pg.MOUSEBUTTONUP:  # click detected
                clicked_x, clicked_y = pg.mouse.get_pos()  # gets raw pixels from click
                grid_space_clicked = board.get_grid_from_pixels(clicked_x, clicked_y)  # convert to grid spaces
                print(grid_space_clicked)

        example_squares(surf, board)
        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()
