import pygame as pg


# Presets

BODY_DEFAULT = ("Generic", BLACK, 100, 10, [[0, 0], [0, 0], [0, 0]], False)

pg.init()
pg.font.init()
pg.display.set_caption("Ball Clanging")

WINDOW_SIZE = WIN_WIDTH, WIN_HEIGHT = 1280, 960
FPS = 60
SCALE = 10**-10
DEFAULT_INTERVAL = 1
DEFAULT_TAIL = 2000

SCREEN = pg.display.set_mode(WINDOW_SIZE)
CLOCK = pg.time.Clock()
SMALL_FONT = pg.font.SysFont("Arial", 16)
BIG_FONT = pg.font.SysFont("Arial", 36)

BACKGROUND = "#FFFFFF"
TEXT = "#333333"
BLACK = "#000000"
GREEN = "#AAFF00"
RED = "#AA3333"
ORANGE = "#DD5500"
MAGENTA = "#BB00BB"
PINK = "#FFCCCC"
BLUE= "#00AAFF"
GREY= "#999999"

# kg, km
UNIT_OF_MOTION = 1
BIG_G = 6.67430 * 10**-11
SUN_MASS = 1.989 * 10**30
SUN_RADIUS = 696340 * 10**3
DISTANCE_SUN_EARTH = 14733 * 10**9
EARTH_MASS = 5.972 * 10**24
EARTH_RADIUS = 6371 * 10*3
DISTANCE_SUN_EARTH = 14733 * 10**9

# My definitions
BIG_G = 3
SCALE = 1
