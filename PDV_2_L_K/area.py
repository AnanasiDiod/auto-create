import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(202.4, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -16.44)
    p.go_line(34.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -100)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-34.08, 0)
    p.go_line(0, -16.44)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-202.4, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 16.44)
    p.go_line(-34.08, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 100)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(34.08, 0)
    p.go_line(0, 16.44)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    p.circle(-35.08, -31.44, 7 / 2)
    p.circle(272.56, 0, 7 / 2)
    p.circle(0, -90, 7 / 2)
    p.circle(-272.56, 0, 7 / 2)
    p.circle(66.28, 45, 18 / 2)

    doc.saveas(path+"Площадка "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

