import numpy as np
import pygame as pg
import sys
from settings import *
from map import *
from raycasting import *
from object_renderer import *
from player import *







# Define the Sphere class
class Game:
    def __init__(self):

        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
        self.delta_time  = 1

 

    def new_game(self):
        self.player = Player(self)
        self.raycasting = RayCasting(self)
        self.object_renderer = ObjectRenderer(self)
        self.map = Map(self)


    def update(self):
        self.player.update()
        self.raycasting.update()

        pg.display.flip()
        self.delta_time  = 1
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.screen.fill("gray")
        self.object_renderer.draw()
        self.map.draw()
        self.player.draw()

    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.type == pg.K_ESCAPE ):
                pg.quit()
                sys.exit()




    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


 
if __name__ == "__main__":
    game = Game(    )
    game.run()

 
 

 
