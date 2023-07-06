import ezdxf as dxf
from point import *


def profile(width, heigh, quantity, path=str(), ver=False):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_arc(2, 5)
    p.go_line(7.07, 7.07)
    p.go_arc(1, 5)
    p.go_line(24.13, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -23)
    p.go_line(236.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)

    p.go_line(0, -(width - 15))

    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-236.08, 0)
    p.go_line(0, -23)
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-24.13, 0)
    p.go_arc(4, 5)
    p.go_line(-7.07, 7.07)
    p.go_arc(3, 5)
    p.go_init()

    p.circle(95.64, -22.53, 4.9 / 2)
    p.circle(113.59, 0, 4.9 / 2)
    p.circle(0, -width + 18.2, 4.9 / 2)
    p.circle(-113.59, 0, 4.9 / 2)

    p.circle(-80.64, -19.6, 9 / 2)
    p.circle(0, width + 21, 9 / 2)
    # метка
    if ver:
        p.circle(116.14, -119.8, 22 / 2)
        p.circle(49, 0, 22 / 2)

        p.circle(-79.4, -19.1, 4.9 / 2)
        p.circle(70, 0, 4.9 / 2)
        p.circle(70, 0, 4.9 / 2)

        p.circle(-115, -50.5, 4.9 / 2)
        p.circle(0, 118.5 - width / 2, 4.9 / 2)
        p.circle(0, 118.5 - width / 2, 4.9 / 2)
        doc.saveas(path+"Профиль 2 верх "+str(width)+'x' +
                   str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        p.circle(170.54, -68.6, 4.9 / 2)
        p.circle(0, 118.5 - width / 2, 4.9 / 2)
        p.circle(0, 118.5 - width / 2, 4.9 / 2)
        p.circle(-84.8, -50.5, 4.9 / 2)
        p.circle(70, 0, 4.9 / 2)
        p.circle(70, 0, 4.9 / 2)
        doc.saveas(path+"Профиль 2 низ "+str(width)+'x' +
                   str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, path=str()):
    profile(width, heigh, quantity, path, False)
    profile(width, heigh, quantity, path, True)
