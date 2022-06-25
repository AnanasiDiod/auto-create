import ezdxf as dxf
from point import *

def main(width, heigh, quantity = 1, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(293.26 + (heigh - 300), 0)
    p.go_line(0, -36.6)
    p.go_angle(-135.921, 23)
    p.go_line(-(293.26 + (heigh - 300)), 0)
    p.go_line(0, 36.6)
    p.go_angle(44.079, 23)
    p.go_init()
    p.circle(138.37 + (heigh - 300)/2, -26.3, 5.5)

    doc.saveas(path+"полоска "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
    p.circle(0, 0, 9)

    doc.saveas(path+"полоска под привод "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')