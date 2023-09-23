import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, -(width - 4))
    p.go_line(-137.96, 0)
    p.go_init()
    p.circle(8.1, -14.1, 6 / 2)
    p.circle(0, -(width - 32.2), 6 / 2)
    p.circle(33.78, -7.3, 4.9 / 2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, width - 17.6, 4.9 / 2)
    p.circle(-54.2, 0, 4.9 / 2)

    doc.saveas(path + "Греющий гор " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity * 2) + 'шт.dxf')
