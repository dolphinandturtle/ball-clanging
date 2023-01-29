import sys
import pygame as pg
from core.physics import *
from core.definitions import *


class SystemVisualizer:

    def __init__(self, system):

        self.small_font = SMALL_FONT
        self.big_font = BIG_FONT
        self.screen = SCREEN
        self.clock = CLOCK
        self.interval = DEFAULT_INTERVAL

        self.system = system
        self.camera = Camera(-WIN_WIDTH/2, -WIN_HEIGHT/2, WIN_WIDTH, WIN_HEIGHT)

        self.show_gui = True
        self.show_bodies = True
        self.show_names = True
        self.show_coordinates = False
        self.show_trajectory = True
        self.focus = -1

    def run(self):

        while True:
            self.clock.tick(FPS*self.interval)
            self.event_handler()
            self.screen.fill(BACKGROUND)
            self.make_gui()
            self.make_graphics()
            pg.display.update()

    def event_handler(self):

        mouse_buttons = pg.mouse.get_pressed()
        mouse_position = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_g:
                    self.show_gui = not self.show_gui
                if event.key == pg.K_b:
                    self.show_bodies = not self.show_bodies
                if event.key == pg.K_n:
                    self.show_names = not self.show_names
                if event.key == pg.K_c:
                    self.show_coordinates = not self.show_coordinates
                if event.key == pg.K_t:
                    self.show_trajectory = not self.show_trajectory
                if event.key == pg.K_f:
                    self.focus += 1
                    if self.focus == len(self.system.bodies):
                        self.focus = -1
            if event.type == pg.MOUSEWHEEL and not mouse_buttons[0]:
                if event.y > 0:
                    self.system.magic_body.mass *= event.y*1.2
                if event.y < 0:
                    self.system.magic_body.mass /= -event.y*1.2
            if event.type == pg.MOUSEWHEEL and mouse_buttons[0]:
                self.system.magic_body.radius += event.y*10

        if mouse_buttons[0]:
            xratio = self.camera.width/WIN_WIDTH
            yratio = self.camera.height/WIN_HEIGHT
            x = mouse_position[0]*xratio - self.camera.width/2
            y = mouse_position[1]*yratio - self.camera.height/2
            self.system.magic_body.x = x
            self.system.magic_body.y = y
            if self.system.magic_body not in self.system.bodies:
                self.system.bodies.append(self.system.magic_body)
        if not mouse_buttons[0]:
            if self.system.magic_body in self.system.bodies:
                self.system.bodies.remove(self.system.magic_body)

        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.camera.move_up()
            self.focus = -1
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.camera.move_down()
            self.focus = -1
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.camera.move_left()
            self.focus = -1
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.camera.move_right()
            self.focus = -1
        if keys[pg.K_EQUALS]:
            self.camera.zoom_in()
        if keys[pg.K_MINUS]:
            self.camera.zoom_out()
        if keys[pg.K_0]:
            self.interval += 0.1
        if keys[pg.K_9]:
            self.interval = max(self.interval-0.1, 0.1)

    def make_graphics(self):

        for body in self.system.bodies:

            x, y, radius = body.x, body.y, body.radius
            cam_x, cam_y = self.camera.x, self.camera.y
            cam_w, cam_h = self.camera.width, self.camera.height
            name, color = body.name, body.color
            gap = 1.5*radius

            if self.focus > -1 and self.focus < len(self.system.bodies):
                self.camera.x = self.system.bodies[self.focus].x - cam_w/2
                self.camera.y = self.system.bodies[self.focus].y - cam_h/2

            if self.show_bodies and body.color:
                position = self.camera.relative_position(x, y)
                radius = radius*(WIN_WIDTH/self.camera.width)
                pg.draw.circle(self.screen, color, position, radius)

            if self.show_names:
                position = self.camera.relative_position(x, y, 0, gap)
                text_render = self.small_font.render(name, True, TEXT)
                self.screen.blit(text_render, position)

            if self.show_coordinates:
                position = self.camera.relative_position(x, y, gap/2, -gap)
                text = f"({'%.0f' % x}, {'%.0f' % y})"
                text_render = self.small_font.render(text, True, TEXT)
                self.screen.blit(text_render, position)

            if self.show_trajectory and len(body.get_trajectory()) > 1:
                positions = [self.camera.relative_position(_x, _y)
                             for _x, _y in body.get_trajectory()]
                pg.draw.aalines(self.screen, color, False, positions, 2)

        self.system.update()

    def make_gui(self):

        if not self.show_gui:
            return None

        x = self.camera.width/2 + self.camera.x
        y = self.camera.height/2 + self.camera.y
        text = f"({'%.0f' % x}, {'%.0f' % y})"
        text_render = self.big_font.render(text, True, TEXT)
        self.screen.blit(text_render, (20, WIN_HEIGHT-60))

        self.make_show_status("bodies", self.show_bodies, 1)
        self.make_show_status("names", self.show_names, 2)
        self.make_show_status("coordinates", self.show_coordinates, 3)
        self.make_show_status("trajectory", self.show_trajectory, 4)

        self.magic_body_gui()

    def make_show_status(self, status_name, trigger, level=0):

        status_name = "(" + status_name[0] + ")" + status_name[1:]
        text = f"{status_name}: off"
        if trigger:
            text = f"{status_name}: on"
        text_render = self.small_font.render(text, True, TEXT)
        self.screen.blit(text_render, (20, level*30))

    def magic_body_gui(self):

        text = f"{'%.0f' % self.system.magic_body.mass}"
        text_render = self.small_font.render(text, True, TEXT)
        self.screen.blit(text_render, (WIN_WIDTH-60, WIN_HEIGHT-50))


class Camera:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dmove = 5 + (width/WIN_WIDTH*10)
        self.dzoom = 50

    def move_up(self, amount=1):

        self.y -= self.dmove*amount

    def move_down(self, amount=1):

        self.y += self.dmove*amount

    def move_left(self, amount=1):

        self.x -= self.dmove*amount

    def move_right(self, amount=1):

        self.x += self.dmove*amount

    def zoom_out(self, amount=1):

        self.width += self.dzoom*amount
        self.height += self.dzoom*amount
        self.x -= self.dzoom*amount/2
        self.y -= self.dzoom*amount/2

    def zoom_in(self, amount=1):

        if self.width > 2*self.dzoom or self.height > 2*self.dzoom:
            self.width -= self.dzoom*amount
            self.height -= self.dzoom*amount
            self.x += self.dzoom*amount/2
            self.y += self.dzoom*amount/2

    def relative_position(self, source_x, source_y, offset_x=0, offset_y=0):

        norm_x = (source_x + offset_x - self.x) / (self.width) * WIN_WIDTH
        norm_y = (source_y + offset_y - self.y) / (self.height) * WIN_HEIGHT
        return (norm_x, norm_y)
