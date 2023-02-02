from numpy import sqrt
from core.definitions import *


POSITION, VELOCITY, ACCELERATION = 0, 1, 2
X, Y = 0, 1


class System:

    def __init__(self, bodies):
        self.bodies = bodies
        self.bodies.sort(reverse=True, key=lambda x : x.radius)
        self.center_of_mass = [0, 0]

    def update(self):
        for body in self.bodies:
            body.interact(self.bodies)
        self.calculate_center_of_mass()

    def calculate_center_of_mass(self):
        total_mass, weighted_x, weighted_y = 0.0, 0.0, 0.0
        for body in self.bodies:
            total_mass += body.mass
            weighted_x += body.spacial[POSITION][X]*body.mass
            weighted_y += body.spacial[POSITION][Y]*body.mass
        center_of_mass_x = weighted_x / total_mass
        center_of_mass_y = weighted_y / total_mass
        self.center_of_mass = [center_of_mass_x, center_of_mass_y]
