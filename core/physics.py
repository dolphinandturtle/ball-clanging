from numpy import sqrt as root
from core.definitions import *


class System:

    def __init__(self, bodies):

        self.bodies = bodies
        self.bodies.sort(reverse=True, key=lambda x : x.radius)

        self.magic_body = Body(100, 30, (0, 0), (0, 0), '', GREY, True, True, 0)

        self.scale_quantities()

    def update(self):

        for body in self.bodies:
            body.interact(self)

    def scale_quantities(self):

        for body in self.bodies:
            body.mass *= SCALE
            body.radius *= SCALE
            body.x *= SCALE
            body.y *= SCALE
            body.xdot *= SCALE
            body.ydot *= SCALE


class Body:

    def __init__(self, mass, radius,
                 position=(0, 0), velocity=(0, 0),
                 name="", color=BLACK,
                 unmovable=False, invincible=True,
                 cache_trajectory=DEFAULT_TAIL):

        self.name = name
        self.color = color
        self.mass = mass
        self.radius = radius
        self.unmovable = unmovable
        self.invincible = invincible
        self.cache_trajectory = cache_trajectory
        self.x, self.y = position
        self.xdot, self.ydot = velocity
        self.xforce, self.yforce = 0, 0
        self.__trajectory = [position]

    def interact(self, system):

        for source in system.bodies:

            if source == self:
                continue

            dr = self.distance_from(source)

            if not source.invincible \
               and dr < self.radius \
               and source.mass < self.mass*2:
                system.bodies.remove(source)

            if not self.invincible \
               and dr < self.radius \
               and self.mass < source.mass*2:
                system.bodies.remove(self)
                return None

            if not source.invincible \
               and dr < self.radius \
               and source.mass < self.mass*2:
                self.mass += source.mass

            if not self.invincible \
               and dr < self.radius \
               and self.mass < source.mass*2:
                source.mass += self.mass
                return None

            if self.unmovable:
                return None

            dr = self.distance_from(source)
            dx = self.x-source.x
            dy = self.y-source.y

            force = self.attraction_from(source, BIG_G)
            self.force_x = force*dx/dr
            self.force_y = force*dy/dr
            
            self.update_motion()

    def update_motion(self):

        self.xdot += UNIT_OF_MOTION * self.force_x / self.mass
        self.ydot += UNIT_OF_MOTION * self.force_y / self.mass
        self.x += UNIT_OF_MOTION * self.xdot
        self.y += UNIT_OF_MOTION * self.ydot
        self.__trajectory.append((self.x, self.y))
        if len(self.__trajectory) > self.cache_trajectory:
            self.__trajectory.pop(0)

    def distance_from(self, reference):

        return root((self.x-reference.x)**2 + \
                    (self.y-reference.y)**2)

    def attraction_from(self, source, factor):

        gap = source.radius + self.radius
        distance = max(self.distance_from(source), gap)
        force = -factor*(source.mass*self.mass)/(distance**2)
        return force

    def get_trajectory(self):

        return self.__trajectory
