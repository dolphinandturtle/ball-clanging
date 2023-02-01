import pygame as pg
import sys


class Controls:

    def __init__(self, host):
        self.host = host
        self.keyboard_presses = None
        self.mouse_presses = None
        self.mouse_position = None

    def listen(self):
        self.keyboard_presses = pg.key.get_pressed()
        self.mouse_presses = pg.mouse.get_pressed()
        self.mouse_position = pg.mouse.get_pos()
        for event in pg.event.get():
            self.gui_controls(event)
            self.camera_controls(event)
        self.gui_controls()
        self.camera_controls()
        self.super_controls()

    def gui_controls(self, event=None):
        if event and self.event.type == pg.KEYDOWN:
            if self.event.key == pg.K_g:
                self.host.show_gui = not self.host.show_gui
            if self.event.key == pg.K_b:
                self.host.show_bodies = not self.host.show_bodies
            if self.event.key == pg.K_n:
                self.host.show_names = not self.host.show_names
            if self.event.key == pg.K_c:
                self.host.show_coordinates = not self.host.show_coordinates
            if self.event.key == pg.K_t:
                self.host.show_trajectory = not self.host.show_trajectory
            return None

    def camera_controls(self, event=None):
        if event and event.key == pg.K_f:
            self.host.focus += 1
            if self.host.focus == len(self.system.bodies):
                self.host.focus = -1
            return None
        if self.keyboard_presses[pg.K_UP] or self.keyboard_presses[pg.K_w]:
            self.host.camera.move_up()
            self.host.focus = -1
        if self.keyboard_presses[pg.K_DOWN] or self.keyboard_presses[pg.K_s]:
            self.host.camera.move_down()
            self.host.focus = -1
        if self.keyboard_presses[pg.K_LEFT] or self.keyboard_presses[pg.K_a]:
            self.host.camera.move_left()
            self.host.focus = -1
        if self.keyboard_presses[pg.K_RIGHT] or self.keyboard_presses[pg.K_d]:
            self.host.camera.move_right()
            self.host.focus = -1
        if self.keyboard_presses[pg.K_EQUALS]:
            self.host.camera.zoom_in()
        if self.keyboard_presses[pg.K_MINUS]:
            self.host.camera.zoom_out()

    def simulation_controls(self, event=None):
        pass

    def super_controls(self, event=None):
        if self.keyboard_presses[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
