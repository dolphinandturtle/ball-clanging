import pygame as pg
import numpy as np
from core.definitions.display import *
from core.definitions.defaults import *
from core.camera import *


class Graphics:

    def __init__(self, host):
        self.host = host
        self.camera = Camera(*CAMERA_DEFAULT)
        self.major_font = pg.font.SysFont("Arial", 36)
        self.minor_font = pg.font.SysFont("Arial", 16)
        self.screen = self.host.screen
        self.system = self.host.system

    def draw(self):
        self.screen.fill(BLANK)
        self.draw_bodies()
        self.draw_gui()

    def draw_bodies(self):
        for bodies in self.system.bodies:
            pass

    def draw_gui(self):
        pass
