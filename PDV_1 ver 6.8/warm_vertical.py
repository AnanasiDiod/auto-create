import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, -(heigh - 4))
    p.go_line(-137.96, 0)
    p.go_init()
    p.circle(7.5, -18, 4.9/2)
    p.circle(122.96, 0, 4.9 / 2)
    p.circle(0, -(heigh - 40), 4.9 / 2)
    p.circle(-122.96, 0, 4.9 / 2)
    p.circle(34.38, -11.2, 4.9 / 2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, heigh - 17.6, 4.9 / 2)
    p.circle(-54.2, 0, 4.9 / 2)

    doc.saveas(path + "Греющий верт " + str(width) + 'x'+str(heigh) +
               ' 0,8мм ' + str(quantity) + 'шт.dxf')
