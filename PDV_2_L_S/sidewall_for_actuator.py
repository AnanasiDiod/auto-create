import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(102.96, 0)
    p.go_line(0, -541.4)
    p.go_line(-102.96, 0)
    p.go_init()
    p.circle(7.5, -18, 4.9 / 2)
    p.circle(87.96, 0, 4.9 / 2)
    p.circle(0, -505.4, 4.9 / 2)
    p.circle(-87.96, 0, 4.9 / 2)

    p.set_xy(0, 0)
    p.circle(51.48, -92.07, 11 / 2)
    p.circle(0, -178.63, 11 / 2)

    p.set_xy(0, 0)
    p.circle(6.8, -419.33, 6 / 2)
    p.circle(89.36, 0, 6 / 2)
    p.circle(-44.68, -30, 18 / 2)

    doc.saveas(path+"Боковина под привод БЕЛИМО "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
