import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    # perimeter
    p.go_line(198.29, 0)
    p.go_line(0, -(width - 123))
    p.go_line(-198.29, 0)
    p.go_init()
    # screw
    p.circle(11, -20, 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)

    p.circle(-176.289, -(width/2 - 81.5), 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)

    p.circle(-176.289, -(width/2 - 81.5), 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)

    # ears
    if width > 500:
        # upper
        p.set_xy(123.14, -145.9)
        p.go_line(0, -29.1)
        p.go_line(20, 0)
        p.go_line(0, 29.1)
        p.set_xy(143.14, -(145.9 + 12.48))
        p.go_arc(6, 10)
        p.go_arc(5, 10)
        p.go_arc(4, 10)
        p.go_arc(3, 10)
        p.set_xy(133.14, -(145.9 + 12.48 + 1.5))
        p.circle(0, 0, 4.9/2)
        # lower
        p.set_xy(123.14, -width + 268.9)
        p.go_line(0, 29.1)
        p.go_line(20, 0)
        p.go_line(0, -29.1)
        p.set_xy(123.14, -width + 268.9 + 12.48)
        p.go_arc(2, 10)
        p.go_arc(1, 10)
        p.go_arc(8, 10)
        p.go_arc(7, 10)
        p.set_xy(133.14, -width + 268.9 + 12.48 + 1.5)
        p.circle(0, 0, 4.9/2)
    else:
        p.set_xy(123.14, -width/2 + 64.3)
        p.go_line(0, -29.1)
        p.go_line(20, 0)
        p.go_line(0, 29.1)
        p.set_xy(143.14, -width/2 + 64.3 - 12.48)
        p.go_arc(6, 10)
        p.go_arc(5, 10)
        p.go_arc(4, 10)
        p.go_arc(3, 10)
        p.set_xy(133.14, -width/2 + 64.3 - 12.48 - 1.5)
        p.circle(0, 0, 4.9/2)

    doc.saveas(path+"Ребро "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
