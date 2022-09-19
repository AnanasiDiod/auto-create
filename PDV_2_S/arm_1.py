import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(156.13, 0)
    p.go_arc(8, 16)
    p.go_arc(7, 16)
    p.go_arc(6, 16)
    p.go_arc(5, 16)
    p.go_line(-156.13, 0)
    p.go_arc(4, 16)
    p.go_arc(3, 16)
    p.go_arc(2, 16)
    p.go_arc(1, 16)
    p.go_init()

    p.circle(-8, -16, 6.5/2)

    p.set_xy(115.22, -12)
    p.go_line(31.2, 0)
    p.set_xy(115.22, -20)
    p.go_line(31.2, 0)

    p.set_xy(108, -16)
    p.circle(0, 0, 16.5/2)
    p.circle(45.63, 0, 16.5/2)

    doc.saveas(path+"Рычаг 1 "+str(width)+'x'+str(heigh)+' 2мм '+ str(quantity * 2)+'шт.dxf')