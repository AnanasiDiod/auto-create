import ezdxf as dxf
from point import *


def variants(width, heigh, quantity, axle=False, Drive=False, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    # perimeter
    p.go_line(163.79, 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -16.44)
    p.go_line(5.24, 0)
    p.go_line(0, 43.8)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(24.13, 0)
    p.go_arc(8, 5)
    p.go_angle(-45, 10)
    p.go_arc(7, 5)
    p.go_line(0, -43.06 - heigh)
    p.go_arc(6, 5)
    p.go_angle(-135, 10)
    p.go_arc(5, 5)
    p.go_line(-24.13, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 43.8)
    p.go_line(-5.24, 0)
    p.go_line(0, -16.44)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-163.79, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 14.15)
    p.go_line(-14.15, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, -29.81 + heigh)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_line(14.15, 0)
    p.go_line(0, 14.15)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()
    # Отверстия для крепления к соседним профилям
    p.circle(23, -6.6, 2.45)
    p.circle(117.79, 0, 2.45)
    p.circle(0, 6.72 - heigh, 2.45)
    p.circle(-117.79, 0, 2.45)
    # Отверстия для крепления боковин
    p.set_xy(-11.55, -26.15)
    p.circle(0, 0, 2.45)
    p.circle(0, 45.81 - heigh, 2.45)
    p.circle(55.34, 6.99, 2.45)
    p.circle(0, -59.8 + heigh, 2.45)
    # Отверстия для крепления в ушах
    p.set_xy(197.23, 15.36)
    p.circle(0, 0, 4.5)
    p.circle(0, -37.2 - heigh, 4.5)

    if axle:
        if Drive:
            p.set_xy(89.59, -151.64)
            p.circle(0, 0, 3.5)
            p.circle(60, 0, 3.5)
            doc.saveas(path+"Профиль 1 под привод Belimo "+str(width) +
                       'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
        else:
            p.set_xy(79.59, -139.64)
            p.circle(0, 0, 3.25)
            p.circle(80, 0, 3.25)
            p.circle(-40, -93, 3.25)
            doc.saveas(path+"Профиль 1 под привод Китай "+str(width) +
                       'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        p.set_xy(119.59, 142.16 - heigh)
        p.circle(0, 0, 4.9/2)
        p.circle(0, -54, 4.9/2)
        doc.saveas(path+"Профиль 1 "+str(width)+'x' +
                   str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, path, Belimo=False):
    variants(width, heigh, quantity, False, Belimo, path)
    variants(width, heigh, quantity, True, Belimo, path)
