import ezdxf as dxf
from point import *

def variants(width, heigh, quantity, nh, path = str(), drive = False):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(16.22, 15)
    p.go_line(23.25, 0)
    p.go_line(16.22, -15)
    p.go_line(0, -(352 + (heigh - 400)))
    p.go_line(-16.22, -15)
    p.go_line(-23.25, 0)
    p.go_line(-16.22, 15)
    p.go_line(0, 352 + (heigh - 400))
    p.go_init()
    
    p.set_xy(6.1, -5)
    dh = (388 - 23 * 2 + (heigh - 400)) / (nh - 1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(43.48, 0, 4.9/2)
        p.set_xy(6.1, -(5 + (i + 1) * dh))
    if drive:
        p.set_xy(27.84, -(176 + (heigh - 400)/2))
        p.circle(0,0,11.3/2)
        doc.saveas(path+"Боковина лопатки "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
    else:
        p.set_xy(21.69, -(169.85 + (heigh - 400)/2))
        p.go_line(12.3,0)
        p.go_line(0,-12.3)
        p.go_line(-12.3,0)
        p.go_line(0,12.3)
        doc.saveas(path+"Боковина лопатки под привод "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')

def main(width, heigh, quantity, nh, path = str()):
    variants(width, heigh, quantity, nh, path, False)
    variants(width, heigh, quantity, nh, path, True)