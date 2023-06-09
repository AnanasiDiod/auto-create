import ezdxf as dxf
from point import *


def sidewall(width, heigh, quantity, np, sp, actuator, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(102.96, 0)
    p.go_line(0, - heigh + 5)
    p.go_line(-102.96, 0)
    p.go_init()

    p.circle(7.5, -18, 4.9 / 2)
    p.circle(87.96, 0, 4.9 / 2)

    p.circle(0, -heigh + 41, 4.9 / 2)
    p.circle(0.7, 104.07, 6 / 2)  # special
    p.circle(-89.36, 0, 6 / 2)  # special
    p.circle(0.7, -104.07, 4.9 / 2)

    d = 11
    if actuator:
        d = 18
    p.circle(43.98, ((heigh - 5) - (np - 1) * sp) / 2 - 18, d / 2)

    for i in range(np - 1):
        p.circle(0, sp, 11 / 2)

    if actuator:
        doc.saveas(path+"Боковина под привод "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        doc.saveas(path+"Боковина "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, np, sp, path=str()):
    sidewall(width, heigh, quantity, np, sp, True, path)
    sidewall(width, heigh, quantity, np, sp, False, path)
