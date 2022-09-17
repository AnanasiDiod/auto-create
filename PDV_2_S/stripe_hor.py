import ezdxf as dxf
from point import *

def main(width, heigh, quantity, nw, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(307 + (width - 400), 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -32.5)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-(307 + (width - 400)), 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 32.5)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    dw = (288.2 + (width - 400))/nw
    for i in range(nw + 1):
        p.set_xy(9.4 + i * dw, -28)
        p.circle(0, 0, 4.9/2)

    doc.saveas(path+"Полоска горизонтальная "+str(width)+'x'+str(heigh)+' 1мм '+ str(quantity)+'шт.dxf')