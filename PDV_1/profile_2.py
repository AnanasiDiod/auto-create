import ezdxf as dxf
from point import *

def main(width, heigh, quantity, EI150 = False, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    
    p.go_line(394.56, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -(289 + (width - 300)))
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-394.56, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 289 + (width - 300))
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    if EI150:
        p.circle(24.64, -65, 4.9/2)
        p.circle(0, -(169 + (heigh - 300)), 4.9/2)

    doc.saveas(path+"профиль 2 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity * 2)+'шт.dxf')
# main(300, 500, 1, True)