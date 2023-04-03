import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(width - 38, 0)
    p.go_line(0, -8.6)
    p.go_line(-11, 0)
    p.go_line(0, -19.04)
    p.go_line(-width + 60, 0)
    p.go_line(0, 19.04)
    p.go_line(-11, 0)
    p.go_init()

    p.circle(30, -19.54, 4.9 / 2)
    p.circle(width/2 - 49, 0, 4.9 / 2)
    p.circle(width/2 - 49, 0, 4.9 / 2)

    doc.saveas(path+"Уголок верх низ "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity * 2)+'шт.dxf')
