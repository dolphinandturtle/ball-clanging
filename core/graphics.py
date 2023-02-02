import pygame as pg
import numpy as np
from core.definitions.display import *
from core.definitions.defaults import *
from core.camera import *

X, Y = 0, 1
POSITION, VELOCITY, ACCELERATION = 0, 1, 2

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
        for body in self.system.bodies:
            x = body.spacial[POSITION][X]
            y = body.spacial[POSITION][Y]
            radius = body.radius
            color = body.color
            if body.color:
                position = self.camera.relative_to_camera(x, y, 0, 0)
                radius = radius*(WIN_WIDTH/self.camera.width)
                pg.draw.circle(self.screen, color, position, radius)

    def draw_gui(self):
        pass
