import pygame as pg
from src.gamemanager import GameManager
from src.menu import Menu
from project_od.screen import SmartScreen
from option import *


pg.init()

screen = SmartScreen(WIDTH, HEIGHT, caption="Welcome to Panic city")

clock = pg.time.Clock()

gameManager = GameManager(screen)
menu = Menu(gameManager)

# Skip menu

# gameManager.set_level(1)
# gameManager.in_game = False


while not gameManager.shutdown:
    dt = clock.tick(30) / 1000

    for event in pg.event.get():
        if event.type == pg.QUIT:
           gameManager.quit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                if gameManager.in_game:
                    if gameManager.paused:
                        gameManager.resume()
                    else:
                        gameManager.pause()

    screen.draw_background()

    if gameManager.in_game:
        if gameManager.paused:
            menu.pause(screen)
        else:
            gameManager.update(screen, dt)
    else:
        if gameManager.selecting:
            menu.menu_selector(screen)
        else:
            menu.home(screen)

    screen.display_update()


pg.quit()
