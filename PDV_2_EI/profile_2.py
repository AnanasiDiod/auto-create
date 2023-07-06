import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    # perimeter
    p.go_line(188.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -55.43)
    p.go_arc(6, 5)
    p.go_angle(-135, 2.22)
    p.set_xy(188.58, -69.07)
    p.go_arc(2, 5)
    p.set_xy(188.58, -69.07)
    p.go_line(0, 143.14 - width)
    p.set_xy(190.05, 70.54 - width)
    p.go_arc(3, 5)
    p.set_xy(190.05, 70.54 - width)
    p.go_angle(-45, 2.22)
    p.go_arc(7, 5)
    p.go_line(0, -55.43)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-188.08, 0)
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
    # screw
    p.circle(29.44, -6.6, 2.45)
    p.circle(117.79, 0, 2.45)
    p.circle(38.15, 0, 2.45)
    p.circle(0, 18.2 - width, 2.45)
    p.circle(-38.15, 0, 2.45)
    p.circle(-117.79, 0, 2.45)
    # screw in ears
    p.set_xy(-26.2, 13)
    p.circle(0, 0, 4.5)
    p.circle(0, -21 - width, 4.5)

    doc.saveas(path+"Профиль 2 "+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')

