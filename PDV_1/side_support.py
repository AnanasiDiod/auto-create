import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    
    p.go_line(103.7 + (heigh - 300)/2, 0)
    p.go_line(0, -55.28)
    p.go_line(-(121.7 + (heigh - 300)/2), 0)
    p.go_line(0, 39.08)
    p.go_line(18, 0)
    p.go_line(0, 16.2)
    p.go_init()

    doc.saveas(path+"уголок боковой "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity * 4)+'шт.dxf')
