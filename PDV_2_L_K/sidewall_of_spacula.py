import ezdxf as dxf
from point import *


def sidewall(width, heigh, quantity, np, hp, actuator, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(23.25, 0)
    p.go_line(16.22, -15)
    p.go_line(0, -hp + 36)
    p.go_line(-16.22, -15)
    p.go_line(-23.25, 0)
    p.go_line(-16.22, 15)
    p.go_line(0, hp - 36)
    p.go_init()

    p.circle(-10.12, -20, 4.9 / 2)
    p.circle(43.48, 0, 4.9 / 2)
    p.circle(0, -hp + 46, 4.9 / 2)
    p.circle(-43.48, 0, 4.9 / 2)

    if actuator:
        p.set_xy(5.48, -hp/2 + 9.15)

        p.go_line(12.3, 0)
        p.go_line(0, -12.3)
        p.go_line(-12.3, 0)
        p.go_line(0, 12.3)
        doc.saveas(path+"Боковина лопатки под привод "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        p.set_xy(11.625, -hp/2 + 3)
        p.circle(0, 0, 11.3 / 2)
        doc.saveas(path+"Боковина лопатки "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity * (np * 2 - 1))+'шт.dxf')


def main(width, heigh, quantity, np, hp, path=str()):
    sidewall(width, heigh, quantity, np, hp, True, path)
    sidewall(width, heigh, quantity, np, hp, False, path)
