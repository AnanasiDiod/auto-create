import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(17.65, 0)
    p.go_line(16.54, -16.54)
    p.go_line(16.54, 16.54)
    p.go_line(17.65, 0)
    p.go_line(0, -105.04)
    p.go_line(-17.65, 0)
    p.go_line(-16.54, 16.54)
    p.go_line(-16.54, -16.54)
    p.go_line(-17.65, 0)
    p.go_init()
    p.circle(6, -25.37, 4.9 / 2)
    p.circle(56.37, 0, 4.9 / 2)
    p.circle(0, -54.3, 4.9 / 2)
    p.circle(-56.37, 0, 4.9 / 2)
    p.set_xy(0, 0)
    p.circle(48.57, -52.47, 22 / 2)


    doc.saveas(path+"греющий угол "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity*4)+'шт.dxf')
