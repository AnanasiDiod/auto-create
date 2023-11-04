import ezdxf as dxf
from point import *


def main(width, heigh, quantity, np, hp, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(hp - 1, 0)
    p.go_arc(8, 3)
    p.go_arc(7, 3)
    p.go_line(0, -width + 60.4)
    p.go_arc(6, 3)
    p.go_arc(5, 3)
    p.go_line(-hp + 1, 0)
    p.go_arc(4, 3)
    p.go_arc(3, 3)
    p.go_line(0, width - 60.4)
    p.go_arc(2, 3)
    p.go_arc(1, 3)
    p.go_init()

    p.circle(25, -6.1, 4.9 / 2)
    p.circle(hp - 46, 0, 4.9 / 2)
    p.circle(0, -width + 66.6, 4.9 / 2)
    p.circle(- hp + 46, 0, 4.9 / 2)

    dw = (width - 114.4)/(nw - 1)
    for i in range(nw):
        p.set_xy(13.9, -(30 + i * dw))
        p.circle(0, 0, 4.9 / 2)
        p.circle(hp - 23.8, 0, 4.9 / 2)

    doc.saveas(path+"Половина лопатки "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str((np - 1) * quantity)+'шт.dxf')

    p.set_xy(hp/2 - 15, -38.2)
    p.circle(0, 0, 4.9 / 2)
    p.circle(34, 0, 4.9 / 2)

    doc.saveas(path+"Половина лопатки под привод "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
