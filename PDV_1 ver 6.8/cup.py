import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    
    p.go_line(154.46, 0)

    p.go_line(0, -96.2)
    p.go_line(-22.24, 0)
    p.go_line(0, -5.24)
    p.go_line(102.25, 0)
    p.go_line(0, -62.06)
    p.go_arc(6, 10)
    p.go_angle(225, 34.14)
    p.go_arc(5, 10)

    p.go_line(-246.20, 0)

    p.go_arc(4, 10)
    p.go_angle(135, 34.14)
    p.go_arc(3, 10)
    p.go_line(0, 62.06)
    p.go_line(102.25, 0)
    p.go_line(0, 5.24)
    p.go_line(-22.24, 0)
    p.go_line(0, 96.2)
    p.go_init()

    p.circle(-70.01, -119.54, 1.5)
    p.circle(0, -40, 1.5)
    p.circle(294.48, 0, 1.5)
    p.circle(0, 40, 1.5)
    doc.saveas(path+"Крышка привода "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')

# main(400, 300, 1)