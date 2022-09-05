import ezdxf as dxf
from point import *


def wall(width, heigh, quantity, nh, nw, path=str(), side=False):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(384 + (heigh - 400), 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -(341.6 + (width - 400)))
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-(384 + (heigh - 400)), 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 341.6 + (width - 400))
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    p.set_xy(21, -6.1)
    dh = (388 - 23 * 2 + (heigh - 400)) / (nh - 1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(0, -(333.4 + (width - 400)), 4.9/2)
        p.set_xy(21 + (i + 1) * dh, -6.1)

    p.set_xy(9.9, -20)
    dw = (345.6 - 20 * 2 + (width - 400)) / (nw - 1)
    for i in range(nw):
        p.circle(0, 0, 4.9 / 2)
        p.circle(364.2 + (heigh - 400), 0, 4.9/2)
        p.set_xy(9.9, -(20 + (i + 1) * dw))

    p.set_xy(175 + (heigh - 400) / 2, -41.1)
    p.circle(0, 0, 4.9/2)
    p.circle(34, 0, 4.9/2)

    if width < 400 and heigh < 400 or heigh < 200:
        doc.saveas(path+"Половина лопатки "+str(width)+'x' +
                   str(heigh)+' 0,8мм ' + str(quantity * 2)+'шт.dxf')
    else:
        if side:
            p.set_xy(192 + (heigh - 400)/2, -(170.8 + (width - 400)/2))
            p.circle(0, 0, 4.9/2)
            p.circle(0, -(137.8 + (width - 400)/2), 4.9/2)
            p.set_xy(192 + (heigh - 400)/2, -68)
            p.circle(0, 0, 4.9/2)
            doc.saveas(path+"Половина лопатки передняя "+str(width) +
                       'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
        else:
            p.set_xy(128 + (heigh - 400)/2, -33)
            p.circle(0, 0, 4.9/2)
            p.circle(128, 0, 4.9/2)
            p.circle(-128, -(137.8 + (width - 400)/2), 4.9/2)
            p.circle(128, 0, 4.9/2)
            p.circle(-128, -(137.8 + (width - 400)/2), 4.9/2)
            p.circle(128, 0, 4.9/2)
            doc.saveas(path+"Половина лопатки задняя "+str(width) +
                       'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, nh, nw, path=str()):
    wall(width, heigh, quantity, nh, nw, path, False)
    wall(width, heigh, quantity, nh, nw, path, True)
