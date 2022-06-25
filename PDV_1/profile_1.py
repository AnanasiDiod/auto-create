import ezdxf as dxf
from point import *

def main(width, heigh, quantity, EI150 = False, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    
    p.go_line(302.4, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -26.44)
    p.go_line(41.08, 0)
    p.go_arc(8, 5)
    p.go_arc(7, 5)
    p.go_line(0, -(285.6 + (heigh - 300)))
    p.go_arc(6, 5)
    p.go_arc(5, 5)
    p.go_line(-41.08, 0)
    p.go_line(0, -26.44)
    p.go_arc(6, 5)
    p.go_arc(5, 5)

    p.go_line(-302.4, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 26.44)
    p.go_line(-41.08, 0)
    p.go_arc(4, 5)
    p.go_arc(3, 5)
    p.go_line(0, 285.6 + (heigh - 300))
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_line(41.08, 0)
    p.go_line(0, 26.44)
    p.go_arc(2, 5)
    p.go_arc(1, 5)
    p.go_init()

    if EI150:
        p.circle(323.76, -96.44, 4.9/2)
        p.circle(0, -(165.6 + (heigh - 300)), 4.9/2)

    p.set_xy(0, 0)
        
    p.circle(226.2, -(179.24 + (heigh - 300)/2), 4.5)
    doc.saveas(path+"профиль 1 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')

    p.circle(0, 0, 9)
    p.circle(-145.2, 35, 3.5)
    p.circle(200.4, 0, 3.5)
    p.circle(0, -70, 3.5)
    p.circle(-200.4, 0, 3.5)
    doc.saveas(path+"профиль 1 под привод "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
        

# main(300, 500, 1, True)