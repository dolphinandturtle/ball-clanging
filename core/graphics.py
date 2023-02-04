import pygame as pg
import numpy as np
from core.definitions.display import *
from core.definitions.defaults import *
from core.definitions.colors import *
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
        for body in self.system.bodies:
            self.draw_body(body)
            self.draw_tarjectory(body)

    def draw_body(self, body):
        x = body.spacial[POSITION][X]
        y = body.spacial[POSITION][Y]
        if body.color:
            position = self.camera.relative_to_camera(x, y, 0, 0)
            scaled_radius = body.radius*(WIN_WIDTH/self.camera.width)
            pg.draw.circle(self.screen, body.color, position, scaled_radius)

    def draw_tarjectory(self, body):
        if len(body.get_trajectory()) > 1:
            positions = [self.camera.relative_to_camera(_x, _y, 0, 0)
                         for _x, _y in body.get_trajectory()]
            pg.draw.aalines(self.screen, body.color, False, positions, 2)
