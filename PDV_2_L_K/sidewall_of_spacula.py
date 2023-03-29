import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(23.25, 0)
    p.go_line(16.22, -15)
    p.go_line(0, -152.75)
    p.go_line(-16.22, -15)
    p.go_line(-23.25, 0)
    p.go_line(-16.22, 15)
    p.go_line(0, 152.75)
    p.go_init()

    p.circle(-10.12, -20, 4.9 / 2)
    p.circle(43.5, 0, 4.9 / 2)
    p.circle(0, -142.75, 4.9 / 2)
    p.circle(-43.5, 0, 4.9 / 2)

    p.circle(21.74, 71.38, 11.3 / 2)

    doc.saveas(path+"Боковина лопатки "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')

