import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(182.9, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, 15 - width)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-182.9, 0)
    p.go_line(0, -23)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-24.13, 0)
    p.go_arc(4, 5)
    p.go_angle(135, 10)
    p.go_arc(3, 5)
    p.go_line(0, 26.86 + width)
    p.go_arc(2, 5)
    p.go_angle(45, 10)
    p.go_arc(1, 5)
    p.go_line(24.13, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_init()

    # отверстия в ушах
    p.circle(-26.2, 13, 4.5)
    p.circle(0, -21 - width, 4.5)
    # отверстия для крепления профиля 1
    p.set_xy(29.44, -6.6)
    p.circle(0, 0, 2.45)
    p.circle(117.79, 0, 2.45)
    p.circle(0, 18.2 - width, 2.45)
    p.circle(-117.79, 0, 2.45)

    p.set_xy(26.44, 52 - width)
    p.circle(0, 0, 11)
    p.circle(49, 0, 11)
    doc.saveas(path+"Профиль 3 "+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
