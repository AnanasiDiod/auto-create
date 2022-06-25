import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(250.26 + (width - 300), 0)
    p.go_line(0, -18.51)
    p.go_line(18.51, 0)
    p.go_line(0, -(206.33 + (heigh - 300)))
    p.go_angle(-45, 14.14)
    p.go_line(0, -20)
    p.go_angle(-135, 14.14)
    p.go_line(0, -17.93)
    p.go_line(-18.51, 0)
    p.go_line(0, -18.51)
    p.go_line(-(250.26 + (width - 300)), 0)
    p.go_line(0, 18.51)
    p.go_line(-18.51, 0)
    p.go_line(0, 17.93)
    p.go_angle(135, 14.14)
    p.go_line(0, 20)
    p.go_angle(45, 14.14)
    p.go_line(0, 206.33 + (heigh - 300))
    p.go_line(18.51, 0)
    p.go_line(0, 18.51)
    p.go_init()

    p.circle(11.03, -30.64, 4.9/2)
    p.circle(0, -(85 + (heigh - 300)/2), 4.9/2)
    p.circle(0, -(85 + (heigh - 300)/2), 4.9/2)

    p.set_xy(31.03, -30.64)
    p.circle(0, 0, 4.9/2)
    p.circle(94.102 + (width - 300)/2, 0, 4.9/2)
    p.circle(94.102 + (width - 300)/2, 0, 4.9/2)

    p.circle(20, 0, 4.9/2)
    p.circle(0, -(85 + (heigh - 300)/2), 4.9/2)
    p.circle(0, -(85 + (heigh - 300)/2), 4.9/2)

    p.set_xy(74.13, -86.74)
    p.circle(0, 0, 4.9/2)
    p.circle(102 + (width - 300), 0, 4.9/2)

    p.set_xy(-17.51, -(244.84 + (heigh - 300)))
    p.circle(0, 0, 5.5)
    p.circle(285.28 + (width - 300), 0, 5.5)

    doc.saveas(path+"лопатка "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
