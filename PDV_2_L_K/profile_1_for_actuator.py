import ezdxf as dxf
import pylab as p

from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(212.4, 0)
    p.go_line(0, -31.44)
    p.go_line(34.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -382.4)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-34.08, 0)
    p.go_line(0, -31.44)
    p.go_line(-212.4, 0)
    p.go_line(0, 31.44)
    p.go_line(-34.08, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 382.4)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(34.08, 0)
    p.go_init()

    p.circle(35, -14, 4.9 / 2)
    p.circle(71.2, 0, 4.9 / 2)
    p.circle(71.2, 0, 4.9 / 2)
    p.circle(0, -427.28, 4.9 / 2)
    p.circle(-71.2, 0, 4.9 / 2)
    p.circle(-71.2, 0, 4.9 / 2)

    p.circle(-51.44, 27.44, 4.9 / 2)
    p.circle(0, 27, 4.9 / 2)
    p.circle(0, 318.4, 4.9 / 2)
    p.circle(0, 27, 4.9 / 2)
    p.circle(245.28, 0, 4.9 / 2)
    p.circle(0, -27, 4.9 / 2)
    p.circle(0, -318.4, 4.9 / 2)
    p.circle(0, -27, 4.9 / 2)

    p.circle(-93.34, 6.7, 4.9 / 2)
    p.circle(-58.6, 0, 4.9 / 2)
    p.circle(0, 359, 4.9 / 2)
    p.circle(58.6, 0, 4.9 / 2)

    p.circle(15.7, -31.18, 6.5 / 2)
    p.circle(0, -240.4, 6.5 / 2)
    p.circle(-90, 0, 6.5 / 2)
    p.circle(0, 240.4, 6.5 / 2)

    p.circle(45, -50.2, 18 / 2)
    doc.saveas(path+"Профиль 1 под привод "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

