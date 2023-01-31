import pygame as pg
from core.graphics import *
from core.physics import *


# Constants are defined in core/definitions.py

# Defining Quantities
ALPHA_MASS = 2000
ALPHA_RADIUS = 40
ALPHA_POSITION = (0, 0)
ALPHA_VELOCITY = (-0.6, 0.3)

BETA_MASS = 80
BETA_RADIUS = 20
BETA_POSITION = (150, -300)
BETA_VELOCITY = (0.0, -2.2)

GAMMA_MASS = 300
GAMMA_RADIUS = 15
GAMMA_POSITION = (-400, 300)
GAMMA_VELOCITY = (1, 1.5)

DELTA_MASS = 15000
DELTA_RADIUS = 70
DELTA_POSITION = (-11000, -7000)
DELTA_VELOCITY = (1, 0.07)

EPSILON_MASS = 1000
EPSILON_RADIUS = 20
EPSILON_POSITION = (3000, 1000)
EPSILON_VELOCITY = (-0.7, -0.2)


# Creating bodies
alpha = Body(ALPHA_MASS, ALPHA_RADIUS,
             ALPHA_POSITION, ALPHA_VELOCITY,
             name="Alpha", color=PINK,
             unmovable=False, invincible=False)

beta = Body(BETA_MASS, BETA_RADIUS,
            BETA_POSITION, BETA_VELOCITY,
            name="Beta", color=BLACK,
            unmovable=False, invincible=False)

gamma = Body(GAMMA_MASS, GAMMA_RADIUS,
             GAMMA_POSITION, GAMMA_VELOCITY,
             name="Gamma", color=ORANGE,
             unmovable=False, invincible=False)

delta = Body(DELTA_MASS, DELTA_RADIUS,
             DELTA_POSITION, DELTA_VELOCITY,
             name="Delta", color=ORANGE,
             unmovable=False, invincible=False)

epsilon = Body(EPSILON_MASS, EPSILON_RADIUS,
               EPSILON_POSITION, EPSILON_VELOCITY,
               name="Epsilon", color=BLACK,
               unmovable=False, invincible=False)

# Creating System
system = System([alpha, beta, gamma, delta, epsilon])

# Visualizing System
application = SystemVisualizer(system)
application.camera.zoom_out(10)
application.run()
