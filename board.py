import pygame as pg


def main():
    pg.init()
    running = True
    pg.display.set_caption("Sorry!")
    screen_width, screen_height = pg.display.Info().current_w, pg.display.Info().current_h
    min_dimension = min(screen_width, screen_height)
    surf = pg.display.set_mode((int(min_dimension / 1.5), int(min_dimension / 1.5)), pg.RESIZABLE, pg.SCALED)

    while running:
        surf.fill('white')
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                running = False

        pg.display.update()

    pg.quit()


if __name__ == "__main__":
    main()






