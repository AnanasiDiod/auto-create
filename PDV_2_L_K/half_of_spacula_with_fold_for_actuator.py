import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(2, 0)
    p.go_line(0, 33.7)
    p.go_arc(2, 9.74)
    p.go_arc(1, 9.74)
    p.go_arc(8, 9.74)
    p.go_angle(315, 57.4)

    p.go_line(128.53, 0)
    p.go_arc(8, 3)
    p.go_arc(7, 3)
    p.go_line(0, -339.6)
    p.go_arc(6, 3)
    p.go_arc(5, 3)

    p.go_line(-128.53, 0)
    p.go_angle(225, 57.4)

    p.go_arc(5, 9.74)
    p.go_arc(4, 9.74)
    p.go_arc(3, 9.74)
    p.go_line(0, 33.7)
    p.go_line(-2, 0)

    p.go_arc(4, 3)
    p.go_arc(3, 3)
    p.go_line(0, 339.6)
    p.go_arc(2, 3)
    p.go_arc(1, 3)
    p.go_init()

    p.circle(25, -6.1, 4.9 / 2)
    p.circle(142.75, 0, 4.9 / 2)
    p.circle(0, -333.4, 4.9 / 2)
    p.circle(-142.75, 0, 4.9 / 2)

    p.circle(-11.1, 23.9, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)
    p.circle(164.95, 0, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)

    p.circle(-167.11, -63.7, 6.2 / 2)
    p.circle(0, 413.01, 6.2 / 2)

    p.circle(67.64, -72.5, 4.9 / 2)
    p.circle(34, 0, 4.9 / 2)

    doc.saveas(path+"Половина лопатки с отгибами под привод "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

