from core.definitions.colors import *
from core.definitions.defaults import *
from core.body import Body
from core.system import System
from core.visualizer import Visualizer

earth = Body("Earth", BLUE, 1000, 30, [[800, 500], [0, 0], [0, 0]], True)
moon = Body("Moon", BLACK, 100, 7, [[1000, 500], [0, 2], [0, 0]], False)
system = System([earth, moon])
app = Visualizer(system)
app.run()
