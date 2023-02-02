from numpy import sqrt
from core.definitions.physics import *
from core.definitions.simulation import *


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

    def move(self, dt):
        if self.is_frozen:
            return None
        primitive = lambda const, degree : (const/degree)*dt**degree
        for degree, _ in enumerate(self.spacial):
            for _degree, _const in enumerate(self.spacial):
                if _degree <= degree:
                    continue
                relative_degree = _degree - degree
                self.spacial[degree][X] += primitive(_const[X], relative_degree)
                self.spacial[degree][Y] += primitive(_const[Y], relative_degree)
        self.__trajectory.append(self.spacial[POSITION])
        if len(self.__trajectory) > TRAJECTORY_LENGHT:
            self.__trajectory.pop(0)

    def interact(self, bodies):
        pythagoras = lambda p1, p2 : sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        gravitation = lambda m1, m2, r, k : -k*(m1*m2)/r**2
        for body in bodies:
            if body == self:
                continue
            p1 = self.spacial[POSITION]
            p2 = body.spacial[POSITION]
            m1 = self.mass
            m2 = body.mass
            r = distance = pythagoras(p1, p2)
            k = BIG_G
            contact_distance = self.radius + body.radius
            # Temporary fix for collision bugs!
            if distance < contact_distance:
                self.spacial[VELOCITY] = [0, 0]
                self.spacial[ACCELERATION] = [0, 0]
                body.spacial[VELOCITY] = [0, 0]
                body.spacial[ACCELERATION] = [0, 0]
                continue
            force = gravitation(m1, m2, r, k)
            self.spacial[ACCELERATION][X] = (force*(p1[X]-p2[X])/r)/self.mass
            self.spacial[ACCELERATION][Y] = (force*(p1[Y]-p2[Y])/r)/self.mass

    def get_trajectory(self):
        return self.__trajectory
