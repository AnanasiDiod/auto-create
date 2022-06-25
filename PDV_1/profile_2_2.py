import ezdxf as dxf
from point import *

def main(width, heigh, quantity = 1, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(146.56, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -(289 + (width - 300)))
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-146.56, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 289 + (width - 300))
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    p.circle(20.64, -65, 4.9/2)
    p.circle(0, -(169 + (width - 300)), 4.9/2)
    doc.saveas(path+"профиль 2_2 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity*2)+'шт.dxf')