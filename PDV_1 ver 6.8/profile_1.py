import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(312.4, 0)
    p.go_line(0, -31.44)
    p.go_line(34.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -(382.4 + (heigh - 400)))
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-34.08, 0)
    p.go_line(0, -31.44)
    p.go_line(-312.4, 0)
    p.go_line(0, 31.44)
    p.go_line(-34.08, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 382.4 + (heigh - 400))
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(34.08, 0)
    p.go_line(0, 31.44)
    p.go_init()

    # Крепления к профилю 2 верхние
    p.circle(35, -13.1, 4.9/2)
    p.circle(242.4, 0, 4.9/2)
    # Отверстия под уголки верхние
    p.circle(-293.84, -28.34, 4.9/2)
    p.circle(0, -27, 4.9/2)
    p.circle(345.28, 0, 4.9/2)
    p.circle(0, 27, 4.9/2)
    # Отверстия под боковины
    p.circle(-218.34, -6.2, 4.9/2)
    p.circle(-58.6, 0, 4.9/2)
    p.circle(0, -(360 + (heigh - 400)), 4.9/2)
    p.circle(58.6, 0, 4.9/2)
    # Крепления к профилю 2 нижние
    p.circle(-75.5, -34.54, 4.9/2)
    p.circle(242.4, 0, 4.9/2)
    # Отверстия под уголки нижние
    p.circle(51.44, 28.34, 4.9/2)
    p.circle(0, 27, 4.9/2)
    p.circle(-345.28, 0, 4.9/2)
    p.circle(0, -27, 4.9/2)

    # p.circle(68.34, 6.2, 4.9/2)
    # p.circle(58.6, 0, 4.9/2)

    doc.saveas(path+"Профиль 1 "+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')

    p.set_xy(31, -(182.64 + (heigh - 400) / 2))
    p.circle(0, 0, 3.25)
    p.circle(240.4, 0, 3.25)
    p.circle(0, -90, 3.25)
    p.circle(-240.4, 0, 3.25)
    p.circle(50.2, 45, 9)

    doc.saveas(path+"Профиль 1 под привод "+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
