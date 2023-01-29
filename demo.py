from core.graphics import *
from core.physics import *

# Some parameters can be modified in core/definitions.py

# Defining a body
mass = 1500
radius = 40
position = (0, 0)
velocity = (0, 0)
unmovable = True  # Great for testing and stability
invincible = True  # This parameter can cause problems in chaotic systems
name = "Sun"
color = PINK
cache_trajectory = 0  # Trajectory memory

# Creating a body
sun = Body(mass, radius, position, velocity, name, color, unmovable, invincible, cache_trajectory)

# Lets create quickly some planets that orbits around it
planet = Body(10, 10, (400, 0), (0, 2.5), "Laura", BLACK, False, True, 1000)
planet2 = Body(10, 10, (700, 0), (0, 1.77), "Laura-2", ORANGE, False, True, 1000)

# Creating a physical system
system = System([sun, planet, planet2])

# Visualizing our system
application = SystemVisualizer(system)
application.run()


'''
ASDW or UPDOWNLEFTRIGHT to move the viewport
- and = keys to zoom in and out
'''
