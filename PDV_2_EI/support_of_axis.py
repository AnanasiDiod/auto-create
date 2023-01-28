import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(89.5, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -20)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-89.5, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 20)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    p.circle(3, -15, 2.45)
    p.circle(41.74, 0, 8.15)
    p.circle(41.74, 0, 2.45)

    doc.saveas(path+"Поддержка оси "+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
