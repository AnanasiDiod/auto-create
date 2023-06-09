import ezdxf as dxf
from point import *


def sidewall(width, heigh, quantity, np, sp, actuator, Belimo, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(102.96, 0)
    p.go_line(0, - heigh + 8.6)
    p.go_line(-102.96, 0)
    p.go_init()

    p.circle(7.5, -18, 4.9 / 2)
    p.circle(87.96, 0, 4.9 / 2)
    p.circle(0, -heigh + 44.6, 4.9 / 2)
    p.circle(-87.96, 0, 4.9 / 2)

    d = 11
    if actuator:
        d = 18
    p.circle(43.98, ((heigh - 5) - (np - 1) * sp) / 2 - 18, d / 2)

    for i in range(np - 1):
        p.circle(0, sp, 11 / 2)
    
    if actuator:
        if Belimo:
            p.set_xy(0, 0)
            p.circle(6.8, -heigh + 130.67, 6 / 2)
            p.circle(89.36, 0, 6 / 2)
        doc.saveas(path+"Боковина под привод "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        doc.saveas(path+"Боковина "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, np, sp, Belimo, path=str()):
    sidewall(width, heigh, quantity, np, sp, True, Belimo, path)
    sidewall(width, heigh, quantity, np, sp, False, Belimo, path)
