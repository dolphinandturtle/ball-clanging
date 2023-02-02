from numpy import sqrt
from core.definitions.physics import *

X, Y = 0, 1
POSITION, VELOCITY, ACCELERATION = 0, 1, 2


class Body:

    def __init__(self, name, color, mass, radius, spacial, is_frozen):
        self.name = name
        self.color = color
        self.mass = mass
        self.radius = radius
        self.spacial = spacial
        self.is_frozen = is_frozen
        self.__trajectory = []
        # Work in progress
        self.elasticity = 1.0  # Normalized value

    def moves(self, dt):
        integrate = lambda const, degree : (const/degree)*dt**degree
        for derivative_order_1, quantity_1 in enumerate(self.spacial):
            for derivative_order_2, quantity_2 in enumerate(self.spacial):
                if derivative_order_2 <= derivative_order_1:
                    continue
                const_x, const_y = quantity_2
                relative_degree = derivative_order_2 - derivative_order_1
                index = derivative_order_1
                self.spacial[index][X] += integrate(const_x, relative_degree)
                self.spacial[index][Y] += integrate(const_y, relative_degree)
            if len(self.__trajectory) > CACHE_SIZE:
                self.__trajectory.append(self.spacial[POSITION])

    def interact(self, bodies):
        pythagoras = lambda p1, p2 : sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        gravitation = lambda m1, m2, r, k : k*(m1*m2)/r**2
        for body in bodies:
            if body == self:
                continue
            p1 = self.spacial[POSITION]
            p2 = body.spacial[POSITION]
            m1 = self.mass
            m2 = body.mass
            r = distance = pythagoras(p1, p2)
            k = BIG_G
            contact_distance = self.radius/2 + body.radius/2
            if distance <= contact_distance:
                self.spacial[VELOCITY] = [0, 0]
                self.spacial[ACCELERATION] = [0, 0]
                continue
            force = gravitation(m1, m2, r, k)
            self.spacial[ACCELERATION][X] = (force*(p2[X]-p1[X])/r)/self.mass
            self.spacial[ACCELERATION][Y] = (force*(p2[Y]-p1[Y])/r)/self.mass

    def get_trajectory(self):
        return self.__trajectory
