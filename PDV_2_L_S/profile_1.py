import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(16.15, 0)
    p.go_line(0, 16.15)
    p.go_line(213.59, 0)
    p.go_line(0, -18.44)
    p.go_line(5.24, 0)
    p.go_line(0, 43.8)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(24.13, 0)
    p.go_arc(8, 5)
    p.go_line(7.07, -7.07)
    p.go_arc(7, 5)

    p.go_line(0, -heigh - 59.26)

    p.go_arc(6, 5)
    p.go_line(-7.07, -7.07)
    p.go_arc(5, 5)
    p.go_line(-24.13, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 43.8)
    p.go_line(-5.24, 0)
    p.go_line(0, -18.44)
    p.go_line(-213.59, 0)
    p.go_line(0, 16.15)
    p.go_line(-16.15, 0)
    p.go_init()

    p.circle(66.15, 9.55, 4.9 / 2)
    p.circle(113.59, 0, 4.9 / 2)
    p.circle(0, -width - 9.48, 4.9 / 2)
    p.circle(-113.59, 0, 4.9 / 2)


    p.circle(24.29, 27.04, 4.9 / 2)
    p.circle(58.6, 0, 4.9 / 2)
    p.circle(0, width - 44.6, 4.9 / 2)
    p.circle(-58.6, 0, 4.9 / 2)

    p.circle(170.74, 49, 9 / 2)
    p.circle(0, -(width + 53.4), 9 / 2)

    doc.saveas(path+"Профиль 1 "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')



