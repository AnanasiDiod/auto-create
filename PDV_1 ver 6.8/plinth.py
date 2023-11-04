import ezdxf as dxf
from point import *


def usual(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(202.4, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -16.44)
    p.go_line(34.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -100)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-34.08, 0)
    p.go_line(0, -16.44)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-202.4, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 16.44)
    p.go_line(-34.08, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 100)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(34.08, 0)
    p.go_line(0, 16.44)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    if heigh <= 100:
        p.circle(-35.08, -41.44, 3.5)
        p.circle(0, -70, 3.5)
        p.circle(272.56, 0, 3.5)
        p.circle(0, 70, 3.5)
        p.circle(-206.28, -35, 9)
    else:
        p.circle(-35.08, -31.44, 3.5)
        p.circle(0, -90, 3.5)
        p.circle(272.56, 0, 3.5)
        p.circle(0, 90, 3.5)
        p.circle(-206.28, -45, 9)

    doc.saveas(path+"Площадка "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')


def ms(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(205.8, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -15.47)
    p.go_line(53.84, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -120)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-53.84, 0)
    p.go_line(0, -15.47)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-205.8, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 15.47)
    p.go_line(-53.84, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 120)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(53.84, 0)
    p.go_line(0, 15.47)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    p.circle(-54.84, -40.47, 7 / 2)
    p.circle(0, -90, 7 / 2)
    p.circle(315.48, 0, 7 / 2)
    p.circle(0, 90, 7 / 2)
    p.set_xy(0, 0)

    p.circle(2.9, -8.1, 3 / 2)
    p.circle(100, 0, 3 / 2)
    p.circle(100, 0, 3 / 2)
    p.circle(0, -154.74, 3 / 2)
    p.circle(-100, 0, 3 / 2)
    p.circle(-100, 0, 3 / 2)

    p.set_xy(0, 0)
    p.circle(32.9, -85.47, 18 / 2)

    doc.saveas(path+"Площадка МС "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, ms_trigger, path=str()):
    if ms_trigger:
        ms(width, heigh, quantity, path)
    else:
        usual(width, heigh, quantity, path)
