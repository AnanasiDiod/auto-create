import ezdxf as dxf
from point import *


def main(width, heigh, quantity, np, sp, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    length = (np - 1) * sp

    p.go_arc(2, 10)
    p.go_arc(1, 10)
    p.go_line(2, 0)
    p.go_arc(8, 10)
    p.go_arc(7, 10)
    p.go_line(0, -length)
    p.go_arc(6, 10)
    p.go_arc(5, 10)
    p.go_line(-2, 0)
    p.go_arc(4, 10)
    p.go_arc(3, 10)
    p.go_init()

    p.set_xy(11, 0)
    p.circle(0, 0, 6.5 / 2)
    for i in range(np-1):
        p.circle(0, -sp, 6.5 / 2)

    doc.saveas(path+"Ребро "+str(width)+'x'+str(heigh) +
               ' 2мм ' + str(quantity * 2)+'шт.dxf')
