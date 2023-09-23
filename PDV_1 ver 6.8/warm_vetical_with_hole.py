import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(137.96, 0)
    p.go_line(0, -132)
    p.go_line(-15, 0)
    p.go_line(0, -132)
    p.go_line(15, 0)
    p.go_line(0, -132)
    p.go_line(-137.96, 0)
    p.go_line(0, 132)
    p.go_line(15, 0)
    p.go_line(0, 132)
    p.go_line(-15, 0)
    p.go_init()
    p.circle(7.5, -18, 4.9/2)
    p.circle(122.96, 0, 4.9 / 2)
    p.circle(0, -360, 4.9 / 2)
    p.circle(-122.96, 0, 4.9 / 2)
    p.circle(34.38, -11.2, 4.9 / 2)
    p.circle(54.2, 0, 4.9 / 2)
    p.circle(0, 382.4, 4.9 / 2)
    p.circle(-54.2, 0, 4.9 / 2)
    p.set_xy(0, 0)
    p.circle(68.98, -198, 18 / 2)
    p.circle(0, -80, 22 / 2)


    doc.saveas(path+"греющий верт с отверстием "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
