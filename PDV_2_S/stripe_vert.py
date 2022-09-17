import ezdxf as dxf
from point import *

def main(width, heigh, quantity, nh, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(322 + (heigh - 400), 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -32.5)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-(322 + (heigh - 400)), 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 32.5)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    dh = (270 + (heigh - 400))/nh
    for i in range(nh + 1):
        p.set_xy(26 + i * dh, -8.1)
        p.circle(0, 0, 4.9/2)

    doc.saveas(path+"Полоска вертикальная "+str(width)+'x'+str(heigh)+' 1мм '+ str(quantity * 2)+'шт.dxf')