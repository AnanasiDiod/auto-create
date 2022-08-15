import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(198.29, 0)
    p.go_line(0, -(315.6 + (width - 400)))
    p.go_line(-198.29, 0)
    p.go_init()
    p.circle(11, -20, 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(-176.289, -(137.8 + (width - 400)/2), 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(88.14, 0, 4.9/2)
    p.circle(-176.289, -(137.8 + (width - 400)/2), 4.9/2)
    p.circle(176.289, 0, 4.9/2)
    p.set_xy(73.144, -(279.4 + (width - 400)))
    p.go_line(52, 0)
    p.go_line(0, -16.2)
    p.go_line(-52, 0)
    p.go_line(0, 16.2)

    doc.saveas(path+"Ребро "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')