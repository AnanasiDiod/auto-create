import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(198.29, 0)
    p.go_line(0, -(315.6 + (width - 400)))
    p.go_line(-198.29, 0)
    p.go_init()

    p.circle(11, -20, 4.9/2)
    p.circle(88.14, -35, 4.9/2)
    p.circle(88.14, 35, 4.9/2)
    p.circle(-176.289, -(137.8 + (width - 400)/2), 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(-176.289, -(137.8 + (width - 400)/2), 4.9/2)
    p.circle(176.289, 0, 4.9/2)
    p.set_xy(99.14, -(260.6 + (width - 400)))
    p.circle(0, 0, 4.9/2)

    p.set_xy(71.644, -(279.4 + (width - 400)))
    p.go_line(55, 0)
    p.go_line(0, -21)
    p.go_line(-55, 0)
    p.go_line(0, 21)

    doc.saveas(path+"Ребро "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
