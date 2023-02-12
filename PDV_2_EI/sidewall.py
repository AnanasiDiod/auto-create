import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    # perimeter
    p.go_line(97.52, 0)
    p.go_line(0, 23.8 - heigh)
    p.go_line(-64.48, 0)
    p.go_line(0, 1)
    p.go_line(-33.04, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, -(28.8 - heigh))
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()
    # screw
    p.circle(4.6, -11, 2.45)
    p.circle(0, 45.81 - heigh, 2.45)
    p.set_xy(90.02, -18)
    p.circle(0, 0, 2.45)
    p.circle(0, 59.8 - heigh, 2.45)
    p.set_xy(44.74, 71.8 - heigh)
    p.circle(0, 0, 5.5)

    doc.saveas(path+'Боковина '+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity * 2)+'шт.dxf')
