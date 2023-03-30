import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(26.99, 0)
    p.go_line(14.35, -14)
    p.go_line(0, -317.6)
    p.go_line(-14.35, -14)
    p.go_line(-26.99, 0)
    p.go_line(-14.35, 14)
    p.go_line(0, 317.6)
    p.go_init()

    p.circle(-8.25, -30, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)
    p.circle(0, -95.2, 4.9 / 2)

    p.circle(43.48, 0, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)
    p.circle(0, 95.2, 4.9 / 2)


    doc.saveas(path+"Боковина лопатки горизонтальная "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

