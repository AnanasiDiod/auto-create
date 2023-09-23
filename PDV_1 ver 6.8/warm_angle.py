import ezdxf as dxf
from point import *


def regular(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(17.65, 0)
    p.go_line(16.54, -16.54)
    p.go_line(16.54, 16.54)
    p.go_line(17.65, 0)
    p.go_line(0, -105.04)
    p.go_line(-17.65, 0)
    p.go_line(-16.54, 16.54)
    p.go_line(-16.54, -16.54)
    p.go_line(-17.65, 0)
    p.go_init()
    p.circle(6, -25.37, 4.9 / 2)
    p.circle(56.37, 0, 4.9 / 2)
    p.circle(0, -54.3, 4.9 / 2)
    p.circle(-56.37, 0, 4.9 / 2)

    doc.saveas(path + "Греющий угол " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity * 4) + 'шт.dxf')


def irregular_150(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    doc.saveas(path + "Греющий угол " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity * 4) + 'шт.dxf')


def irregular_200(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    doc.saveas(path + "Греющий угол " + str(width) + 'x' + str(heigh) +
               ' 0,8мм ' + str(quantity) + 'шт.dxf')


def main(width, heigh, quantity, path=str()):
    if heigh <= 150:
        irregular_150(width, heigh, quantity, path)
        regular(width, heigh, quantity * 3, path)
    elif heigh <= 200:
        irregular_200(width, heigh, quantity, path)
        regular(width, heigh, quantity * 3, path)
    else:
        regular(width, heigh, quantity * 4, path)
