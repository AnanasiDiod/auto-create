import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(491.64, 0)
    p.go_line(0, -111)
    p.go_line(-491.64, 0)
    p.go_init()

    p.circle(21.55, -8.95, 3 / 2)
    p.circle(90.2, 0, 3 / 2)
    p.circle(268.14, 0, 3 / 2)
    p.circle(90.2, 0, 3 / 2)
    p.set_xy(0, 0)

    p.circle(145.82, -8.95, 3 / 2)
    p.circle(100, 0, 3 / 2)
    p.circle(100, 0, 3 / 2)

    p.circle(0, -93.95, 3 / 2)
    p.circle(-100, 0, 3 / 2)
    p.circle(-100, 0, 3 / 2)
    p.set_xy(0, 0)

    p.circle(8.95, -25, 3 / 2)
    p.circle(473.74, 0, 3 / 2)
    p.circle(0, -61, 3 / 2)
    p.circle(-473.74, 0, 3 / 2)
    p.set_xy(0, 0)

    p.circle(424.99, -32, 22 / 2)
    p.circle(-24.5, -30, 22 / 2)
    p.circle(49, 0, 22 / 2)

    doc.saveas(path + "Коробка привода_бок_2 " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity) + 'шт.dxf')
