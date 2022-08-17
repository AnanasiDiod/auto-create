import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(362 + (width - 400), 0)
    p.go_line(0, -8.595)
    p.go_line(-11, 0)
    p.go_line(0, -19.04)
    p.go_line(-(340 + (width - 400)), 0)
    p.go_line(0, 19.04)
    p.go_line(-11, 0)
    p.go_line(0, 8.595)
    p.go_init()

    p.circle(30, -24.54, 4.9/2)
    p.circle(151 + (width - 400)/2, 0, 4.9/2)
    p.circle(151 + (width - 400)/2, 0, 4.9/2)

    doc.saveas(path+"Уголок "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity * 2)+'шт.dxf')
