import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(222 + (heigh - 300), 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -32.5)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-(222 + (heigh - 300)), 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 32.5)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    p.circle(26, -8.102, 4.9/2)
    p.circle(85 + (heigh - 300)/2, 0, 4.9/2)
    p.circle(85 + (heigh - 300)/2, 0, 4.9/2)

    doc.saveas(path+"полоска вертикальная "+str(width)+'x'+str(heigh)+' 1мм '+ str(quantity * 2)+'шт.dxf')