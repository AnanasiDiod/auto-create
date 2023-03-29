import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(154.46, 0)
    p.go_line(0, -8.98)
    p.set_xy(154.46, -11.02)
    p.go_arc(3, 1.5)
    p.go_arc(2, 1.5)
    p.set_xy(154.46, -11.02)

    p.go_line(0, -85.18)
    p.go_line(-22.24, 0)
    p.go_line(0, -5.24)
    p.go_line(102.25, 0)
    p.go_line(0, -62.06)
    p.go_arc(6, 10)

    p.go_line(-24.14, -24.14)
    p.go_arc(5, 10)
    p.go_line(-246.2, 0)

    p.go_arc(4, 10)
    p.go_line(-24.14, 24.14)
    p.go_arc(3, 10)
    p.go_line(0, 62.06)
    p.go_line(102.25, 0)
    p.go_line(0, 5.24)
    p.go_line(-22.24, 0)
    p.go_line(0, 85.18)

    p.set_xy(0, -8.98)
    p.go_arc(7, 1.5)
    p.go_arc(6, 1.5)
    p.set_xy(0, -8.98)

    p.go_init()

    p.circle(-70.01, -119.54, 3 / 2)
    p.circle(294.48, 0, 3 / 2)
    p.circle(0, -40, 3 / 2)
    p.circle(-294.48, 0, 3 / 2)
    doc.saveas(path+"Крышка привода "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

