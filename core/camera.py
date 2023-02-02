from core.definitions.display import *


class Camera:

    def __init__(self, x, y, width, height, move_factor, zoom_factor):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.move_factor = move_factor
        self.zoom_factor = zoom_factor

    def move_up(self, amount):
        self.y -= self.move_factor*amount

    def move_down(self, amount):
        self.y += increment

    def move_left(self, amount):
        self.x -= increment

    def move_right(self, amount):
        self.x += increment

    def zoom_out(self, amount):
        increment = self.zoom_factor*amount
        self.width += increment
        self.height += increment
        self.x -= increment/2
        self.y -= increment/2

    def zoom_in(self, amount):
        if self.width > 2*self.zoom_factor or self.height > 2*self.zoom_factor:
            self.width -= self.zoom_factor*amount
            self.height -= self.zoom_factor*amount
            self.x += self.zoom_factor*amount/2
            self.y += self.zoom_factor*amount/2

    def relative_to_camera(self, source_x, source_y, offset_x, offset_y):
        norm_x = (source_x + offset_x - self.x) / (self.width) * WIN_WIDTH
        norm_y = (source_y + offset_y - self.y) / (self.height) * WIN_HEIGHT
        return (norm_x, norm_y)
