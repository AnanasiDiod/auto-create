import ezdxf as dxf
from point import *


def main(width, heigh, quantity, nh, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(350.26 + (width - 400), 0)
    p.go_line(0, -18.51)
    p.go_line(18.51, 0)
    p.go_line(0, -(306.33 + (heigh - 400)))
    p.go_line(10, -10)
    p.go_line(0, -20)
    p.go_line(-10, -10)
    p.go_line(0, -17.93)
    p.go_line(-18.51, 0)
    p.go_line(0, -18.51)
    p.go_line(-(350.26 + (width - 400)), 0)
    p.go_line(0, 18.51)
    p.go_line(-18.51, 0)
    p.go_line(0, 17.93)
    p.go_line(-10, 10)
    p.go_line(0, 20)
    p.go_line(10, 10)
    p.go_line(0, 306.33 + (heigh - 400))
    p.go_line(18.51, 0)
    p.go_line(0, 18.51)
    p.go_init()
    # вертикальные отверстия для доп пластин
    dh = (270 + (heigh - 400))/nh
    for i in range(nh + 1):
        p.set_xy(11.03, -(30.64 + i * dh))
        p.circle(0, 0, 4.9/2)
        p.circle(328.2 + (width - 400), 0, 4.9/2)
    # горизонтальные отверстия для доп пластин
    dw = (288.2 + (width - 400))/nw
    for i in range(nw + 1):
        p.set_xy(31.03 + i * dw, -30.64)
        p.circle(0, 0, 4.9/2)
    # отверстия под ребро
    p.set_xy(74.13, -(186.74 + (heigh - 400)))
    p.circle(0, 0, 4.9/2)
    p.circle(202 + (width - 400), 0, 4.9/2)
    # отверстия под ось
    p.set_xy(-17.51, -(344.84 + (heigh - 400)))
    p.circle(0, 0, 5.5)
    p.circle(385.28 + (width - 400), 0, 5.5)

    doc.saveas(path+"Лопатка "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
