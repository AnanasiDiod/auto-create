import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, -7)
    p.go_line(-15, 0)
    p.go_line(0, -132)
    p.go_line(15, 0)
    p.go_line(0, -7)
    p.go_line(-60.5, 0)
    p.go_line(-3.3, 4)
    p.go_line(-10.37, 0)
    p.go_line(-3.3, -4)
    p.go_line(-60.5, 0)
    p.go_line(0, 7)
    p.go_line(15, 0)
    p.go_line(0, 132)
    p.go_line(-15, 0)
    p.go_init()
    p.circle(41.88, -6.8, 4.9/2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, -132.4, 4.9/2)
    p.circle(-54.2, 0, 4.9 / 2)

    doc.saveas(path+"греющий верт с отверстием "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
