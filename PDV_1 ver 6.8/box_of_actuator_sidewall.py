import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(259.24, 0)
    p.go_line(0, -111)
    p.go_line(-259.24, 0)
    p.go_init()

    p.circle(29.62, -8.1, 3 / 2)
    p.circle(100, 0, 3 / 2)
    p.circle(100, 0, 3 / 2)
    p.circle(0, -93.95, 3 / 2)
    p.circle(-100, 0, 3 / 2)
    p.circle(-100, 0, 3 / 2)
    p.set_xy(0, 0)

    p.circle(8.95, -25, 3 / 2)
    p.circle(241.34, 0, 3 / 2)
    p.circle(0, -61, 3 / 2)
    p.circle(-241.34, 0, 3 / 2)


    doc.saveas(path+"коробка привода_бок "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
