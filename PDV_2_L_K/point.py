from asyncio.windows_events import NULL
from math import sin, cos, radians


class point:
    x, y = 0, 0
    msp = NULL

    def go_line(self, x, y):
        self.msp.add_line((self.x, self.y), (self.x + x, self.y + y))
        self.x += x
        self.y += y

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def go_angle(self, angle, length):
        self.msp.add_line((self.x, self.y), (self.x + length *
                          cos(radians(angle)), self.y + length*sin(radians(angle))))
        self.x += length*cos(radians(angle))
        self.y += length*sin(radians(angle))

    def go_init(self):
        self.msp.add_line((self.x, self.y), (0, 0))
        self.set_xy(0, 0)

    def circle(self, x, y, radius):
        self.msp.add_circle((self.x + x, self.y + y), radius)
        self.set_xy(self.x + x, self.y + y)

    def go_arc(self, direction, radius, clockwise=True):
        if clockwise:
            self.msp.add_arc((self.x + radius*cos(radians(45*(direction - 2))),
                              self.y + radius*sin(radians(45 * (direction - 2)))),
                             radius, 45*(direction + 1), 45 * (direction + 2))
            s = 2 * radius * cos(radians(67.5))
            self.x += s * cos(radians(67.5 + (direction - 2) * 45))
            self.y += s * sin(radians(67.5 + (direction - 2) * 45))
