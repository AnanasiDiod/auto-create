import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(55.68, 0)
    p.go_line(0, -50)
    p.go_line(-55.68, 0)
    p.go_init()
    p.set_xy(21.69, -18.85)
    p.go_line(12.3, 0)
    p.go_line(0, -12.3)
    p.go_line(-12.3, 0)
    p.go_line(0, 12.3)

    p.circle(-15.59, 10.85, 4.9 / 2)
    p.circle(43.48, 0, 4.9 / 2)
    p.circle(0, -34, 4.9 / 2)
    p.circle(-43.48, 0, 4.9 / 2)

    doc.saveas(path+"Поддержка оси "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')
