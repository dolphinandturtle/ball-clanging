import sys
import pygame as pg
from core.definitions.colors import *
from core.definitions.display import *
from core.graphics import Graphics
from core.controls import Controls


class Visualizer:

    def __init__(self, system):
        pg.init()
        pg.font.init()
        self.system = system
        self.screen = pg.display.set_mode(WINDOW_SIZE)
        self.clock = pg.time.Clock()
        self.graphics = Graphics(self)
        self.controls = Controls(self)

    def run(self):
        while True:
            self.clock.tick(FPS)
            self.controls.listen()
            self.graphics.draw()
            self.system.update()
            pg.display.update()
