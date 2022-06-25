import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(280.26 + (width - 300), 0)

    p.go_line(0, -15.51)
    p.go_line(15.51, 0)
    p.go_line(0, -(277.13 + (heigh - 300)))
    p.go_line(-14.64, 0)
    p.go_line(0, -34.04)

    p.go_line(-(282 + (width - 300)), 0)

    p.go_line(0, 34.04)
    p.go_line(-14.64, 0)
    p.go_line(0, (277.13 + (heigh - 300)))
    p.go_line(15.51, 0)
    p.go_line(0, 15.51)
    p.go_init()

    p.circle(19.13, -(153.24 + (heigh - 300)/2), 3.5)
    p.circle(40, 0, 3.5)

    doc.saveas(path+"лопатка "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity*2)+'шт.dxf')

# main(400, 300, 1)