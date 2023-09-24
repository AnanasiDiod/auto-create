import ezdxf as dxf
from point import *


def regular(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, - heigh / 2 + 68)
    p.go_line(-15, 0)
    p.go_line(0, - 132)
    p.go_line(15, 0)
    p.go_line(0, - heigh / 2 + 68)
    p.go_line(-137.96, 0)
    p.go_line(0, heigh / 2 - 68)
    p.go_line(15, 0)
    p.go_line(0, 132)
    p.go_line(-15, 0)
    p.go_init()
    p.circle(7.5, -18, 4.9 / 2)
    p.circle(122.96, 0, 4.9 / 2)
    p.circle(0, -(heigh - 40), 4.9 / 2)
    p.circle(-122.96, 0, 4.9 / 2)
    p.circle(34.38, -11.2, 4.9 / 2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, heigh - 17.6, 4.9 / 2)
    p.circle(-54.2, 0, 4.9 / 2)
    p.set_xy(0, 0)
    p.circle(68.98, - heigh / 2 + 2, 18 / 2)
    p.circle(0, -80, 22 / 2)

    doc.saveas(path + "Греющий верт с отверстием " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')


def irregular_150(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, -7)
    p.go_line(-15, 0)
    p.go_line(0, -132)
    p.go_line(15, 0)
    p.go_line(0, -7)
    p.go_line(-60.5, 0)
    p.go_line(-3.3, 4)
    p.go_line(-10.37, 0)
    p.go_line(-3.3, -4)
    p.go_line(-60.5, 0)
    p.go_line(0, 7)
    p.go_line(15, 0)
    p.go_line(0, 132)
    p.go_line(-15, 0)
    p.go_init()
    p.circle(41.88, -6.8, 4.9/2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, -132.4, 4.9/2)
    p.circle(-54.2, 0, 4.9 / 2)
    p.set_xy(68.98, -73)
    p.circle(0, 0, 9)

    doc.saveas(path + "Греющий верт с отверстием " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity) + 'шт.dxf')


def main(width, heigh, quantity, path=str()):
    if heigh <= 150:
        irregular_150(width, heigh, quantity, path)
    else:
        regular(width, heigh, quantity, path)
