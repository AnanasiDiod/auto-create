Simport ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(109.5, 0)
    p.go_arc(8, 10)
    p.go_arc(7, 10)
    p.go_line(0, -2)
    p.go_arc(6, 10)
    p.go_arc(5, 10)
    p.go_line(-109.5, 0)
    p.go_arc(4, 10)
    p.go_arc(3, 10)
    p.go_line(0, 2)
    p.go_arc(2, 10)
    p.go_arc(1, 10)
    p.go_init()

    p.circle(-2, -11, 6.5/2)
    p.circle(114, 0, 6.5/2)

    mul = 2
    if width < 500:
        mul = 1
    doc.saveas(path+"Рычаг 2 "+str(width)+'x'+str(heigh) +
               ' 2мм ' + str(quantity * mul)+'шт.dxf')
