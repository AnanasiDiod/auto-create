import ezdxf as dxf
from point import *

#163,75

def main(width, heigh, quantity, np, hp, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(4, 0)
    p.go_line(0, 33.7)
    p.go_arc(2, 9.74)
    p.go_arc(1, 9.74)
    p.go_arc(8, 9.74)
    p.go_angle(315, 57.4)

    p.go_line(hp - 16.635, 0)
    p.go_line(0, -width + 54.4)

    p.go_line(- hp + 16.635, 0)
    p.go_angle(225, 57.4)

    p.go_arc(5, 9.74)
    p.go_arc(4, 9.74)
    p.go_arc(3, 9.74)
    p.go_line(0, 33.7)
    p.go_line(-4, 0)

    p.go_arc(4, 3)
    p.go_arc(3, 3)
    p.go_line(0, width - 60.4)
    p.go_arc(2, 3)
    p.go_arc(1, 3)
    p.go_init()

    p.circle(13.736, 33.7, 5.2 / 2)
    p.circle(0, - width - 13.01, 5.2 / 2)

    p.set_xy(27.8, -8.1)
    p.circle(0, 0, 4.9 / 2)
    p.circle(hp - 47.8, 0, 4.9 / 2)
    p.circle(0, -width + 70.6, 4.9 / 2)
    p.circle(- hp + 47.8, 0, 4.9 / 2)

    dw = (width - 114.4)/(nw - 1)
    for i in range(nw):
        p.set_xy(15.9, -(30 + i * dw))
        p.circle(0, 0, 4.9 / 2)
        p.circle(hp + 19.73, 0, 4.9 / 2)

    doc.saveas(path+"Половина лопатки с отгибами "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str((np - 1) * quantity)+'шт.dxf')

    p.set_xy(hp/2 - 15, -38.2)
    p.circle(0, 0, 4.9 / 2)
    p.circle(34, 0, 4.9 / 2)

    doc.saveas(path+"Половина лопатки с отгибами под привод "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
