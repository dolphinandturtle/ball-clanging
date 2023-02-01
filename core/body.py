from numpy import sqrt
from core.definitions import *


class Body:

    def __init__(self, name, color, mass, radius, motion, is_frozen):
        self.name = name
        self.color = color
        self.mass = mass
        self.radius = radius
        self.motion = motion
        self.is_frozen = is_frozen
        self.__trajectory = []

        # Work in progress
        self.elasticity = 1.0  # Normalized value

    def moves(self, dt):
        integrate = lambda const, degree : (const/degree)*dt**degree
        for derivative_order_1, quantity_1 in enumerate(self.motion):
            for derivative_order_2, quantity_2 in enumerate(self.motion):
                if derivative_order_2 <= derivative_order_1:
                    continue
                const_x, const_y = quantity_2
                relative_degree = derivative_order_2 - derivative_order_1
                index = derivative_order_1
                self.motion[index][X] += integrate(const_x, relative_degree)
                self.motion[index][Y] += integrate(const_y, relative_degree)
            if len(self.__trajectory) > CACHE_SIZE:
                self.__trajectory.append(self.motion[POSITION])

    def interact(self, bodies):
        gravitation = lambda m1, m2, r, k : k*(m1*m2)/r**2
        distance = lambda p1, p2 : sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        for body in bodies:
            if body == self:
                continue
            lenght = distance(self.motion[POSITION], body.motion[POSITION])
            contanct_distance = self.radius/2 + body.radius/2
            if lenght <= contanct_distance:
                self.motion[VELOCITY] = [0, 0]
                self.motion[ACCELERATION] = [0, 0]
                continue
            force = gravitation(self.mass, body.mass, lenght, BIG_G)
            self.motion[ACCELERATION][X] = (force*(p2[X]-p1[X])/r)/self.mass
            self.motion[ACCELERATION][Y] = (force*(p2[Y]-p1[Y])/r)/self.mass

    def get_trajectory(self):
        return self.__trajectory
