import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    
    p.go_line(152.48, 0)
    p.go_line(0, -(282 + (width - 300)))
    p.go_line(-152.48, 0)
    p.go_line(0, 282 + (width - 300))
    p.go_init()

    p.circle(76.24, -(222 + (width - 300)), 3)
    p.circle(0, -40, 3)

    doc.saveas(path+"ребро_2 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')