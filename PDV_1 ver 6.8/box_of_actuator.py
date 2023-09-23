import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.19, 0)
    p.go_line(0, -19.88)
    p.go_line(19.88, 0)
    p.go_line(0, -224.19)
    p.go_line(-19.88, 0)
    p.go_line(0, -19.88)
    p.go_line(-137.19, 0)
    p.go_line(0, 19.88)
    p.go_line(-19.88, 0)
    p.go_line(0, 224.19)
    p.go_line(19.88, 0)
    p.go_init()
    p.circle(-10.93, -31.97, 3 / 2)
    p.circle(0, -100, 3 / 2)
    p.circle(0, -100, 3 / 2)
    p.circle(159.04, 0, 3 / 2)
    p.circle(0, 100, 3 / 2)
    p.circle(0, 100, 3 / 2)
    p.set_xy(0, 0)
    p.circle(23.49, -8.95, 3 / 2)
    p.circle(90.2, 0, 3 / 2)
    p.circle(0, -246.04, 3 / 2)
    p.circle(-90.2, 0, 3 / 2)

    doc.saveas(path + "Коробка привода " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity) + 'шт.dxf')
