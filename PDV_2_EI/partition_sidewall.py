import ezdxf as dxf
from point import *


def vertical(width, heigh, quantity, nh, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(16.22, 15)
    p.go_line(23.25, 0)
    p.go_line(16.22, -15)
    p.go_line(0, -(heigh - 73))
    p.go_line(-16.22, -15)
    p.go_line(-23.25, 0)
    p.go_line(-16.22, 15)
    p.go_line(0, heigh - 73)
    p.go_init()

    p.set_xy(6.1, -5)
    dh = (-83 + heigh) / (nh - 1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(43.48, 0, 4.9/2)
        p.set_xy(6.1, -(5 + (i + 1) * dh))

    p.set_xy(27.845, -23.4)
    p.circle(0, 0, 5.65)

    doc.saveas(path+"Боковина лопатки вертикальая"+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity * 2)+'шт.dxf')


def horisontal(width, heigh, quantity, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(14.35, 14)
    p.go_line(26.99, 0)
    p.go_line(14.35, -14)
    p.go_line(0, -(width - 121))
    p.go_line(-14.35, -14)
    p.go_line(-26.99, 0)
    p.go_line(-14.35, 14)
    p.go_line(0, width - 121)
    p.go_init()

    p.set_xy(6.1, -16)
    dw = (-153 + width) / (nw - 1)
    for i in range(nw):
        p.circle(0, 0, 4.9 / 2)
        p.circle(43.48, 0, 4.9/2)
        p.set_xy(6.1, -(16 + (i + 1) * dw))

    doc.saveas(path+"Боковина лопатки горизонтальная "+str(width) +
               'x'+str(heigh)+' 0,8мм ' + str(quantity * 2)+'шт.dxf')

