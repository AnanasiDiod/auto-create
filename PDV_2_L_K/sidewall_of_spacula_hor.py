import ezdxf as dxf
from point import *


def main(width, heigh, quantity, nw, np, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(14.35, 14)
    p.go_line(26.99, 0)
    p.go_line(14.35, -14)
    p.go_line(0, -(width - 82.4))
    p.go_line(-14.35, -14)
    p.go_line(-26.99, 0)
    p.go_line(-14.35, 14)
    p.go_init()

    if width > 100:
        p.set_xy(6.1, -16)
        dw = (width - 114.4)/(nw - 1)
        for i in range(nw):
            p.circle(0, 0, 4.9 / 2)
            p.circle(43.48, 0, 4.9/2)
            p.set_xy(6.1, -(6 + (i + 1) * dw))
    else:
        p.set_xy(6.1, -2.14)
        p.circle(0, 0, 2.45)
        p.circle(43.48, 0,  2.45)
        p.circle(0, -14, 2.45)
        p.circle(-43.48, 0,  2.45)

    doc.saveas(path+"Боковина лопатки горизонтальная " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity * 2 * np)+'шт.dxf')
