import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(187.38, 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -(391 + (width - 400)))
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-187.38, 0)
    p.go_line(0, -23)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-24.13, 0)
    p.go_arc(4, 5)
    p.go_angle(135, 10)
    p.go_arc(3, 5)
    p.go_line(0, 426.86 + (width - 400))
    p.go_arc(2, 5)
    p.go_angle(45, 10)
    p.go_arc(1, 5)
    p.go_line(24.13, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_init()

    #отверстия в ушах
    p.circle(-26.2, 13, 4.5)
    p.circle(0, -(421 + (width - 400)), 4.5)
    #отверстия для крепления профиля 1
    for i in range(3):
        p.set_xy(29.44 + i * 59.45, -6.6)
        p.circle(0, 0, 4.9/2)
        p.circle(0, -(381.8 + (width - 400)), 4.9/2)

    p.set_xy(26.44, -(348 + (width - 400)))
    p.circle(0, 0, 11)
    p.circle(49, 0, 11)
    doc.saveas(path+"Профиль 3 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')