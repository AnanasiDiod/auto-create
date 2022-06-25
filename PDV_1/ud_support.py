import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(259 + (width - 300), 0)
    p.go_line(0, -55.28)
    p.go_line(-(259 + (width - 300)), 0)
    p.go_line(0, 55.28)

    doc.saveas(path+"уголок верх_низ "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity * 2)+'шт.dxf')
    