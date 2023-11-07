import ezdxf as dxf
from point import *


def spacula_new(width, heigh, quantity, np, hp, nw, drive, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(5, 0)
    p.go_line(0, 30.685)
    p.go_line(18.33, 17.7)
    p.go_line(hp - 43.2, 0)
    p.go_line(20.03, -21.44)
    p.go_line(0, -24.01)
    p.go_line(24.01, 0)
    p.go_line(21.44, -20.03)
    p.go_line(0, -width + 247.6)
    p.go_line(-21.44, -20.03)
    p.go_line(-24.01, 0)
    p.go_line(0, -24.01)
    p.go_line(-20.03, -21.44)
    p.go_line(-hp + 43.2, 0)
    p.go_line(-18.33, 17.7)
    p.go_line(0, 30.685)
    p.go_line(-5, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, width - 217.4)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    p.circle(25, 40.28, 4.9 / 2)
    p.circle(hp - 44.84, 0, 4.9 / 2)
    p.circle(0, -width + 132.85, 4.9 / 2)
    p.circle(- hp + 44.84, 0, 4.9 / 2)

    dw = (width - 273.4)/(nw - 1)
    for i in range(nw):
        p.set_xy(16.05, -(30 + i * dw))
        p.circle(0, 0, 4.9 / 2)
        p.circle(hp + 21.43, 0, 4.9 / 2)

    if not drive:
        p.set_xy(hp/2 + 2.565, 16.09)
        p.circle(0, 0, 5.75)
        p.circle(0, -width + 181.22, 5.75)
        doc.saveas(path+"Половина лопатки "+str(width)+'x'+str(heigh) +
                ' 0,8мм ' + str((np - 1) * quantity)+'шт.dxf')
    else:
        p.set_xy(hp/2 - 14, -38.2)
        p.circle(0, 0, 4.9 / 2)
        p.circle(34, 0, 4.9 / 2)
        p.set_xy(hp/2 + 2.565, 16.09)
        p.circle(0, -width + 181.22, 5.75)
        p.set_xy(hp/2 - 3.585, 9.94)
        p.go_line(0, 12.3)
        p.go_line(12.3, 0)
        p.go_line(0, -12.3)
        p.go_line(-12.3, 0)

        doc.saveas(path+"Половина лопатки под привод "+str(width)+'x'+str(heigh) +
                ' 0,8мм ' + str(quantity)+'шт.dxf')

def main(width, heigh, quantity, np, hp, nw, path=str()):
    spacula_new(width, heigh, quantity, np, hp, nw, True, path)
    spacula_new(width, heigh, quantity, np, hp, nw, False, path)