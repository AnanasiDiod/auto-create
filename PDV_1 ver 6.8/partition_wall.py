import ezdxf as dxf
from point import *

def main(width, heigh, quantity, nh, nw, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(384 + (heigh - 400), 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, -(341.6 + (width - 400)))
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-(384 + (heigh - 400)), 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, 341.6 + (width - 400))
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()
  
    p.set_xy(21, -6.1)
    dh = (388 - 23 * 2 + (heigh - 400)) / (nh - 1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(0,-(333.4 + (width - 400)), 4.9/2)
        p.set_xy(23 + (i + 1) * dh, -6.1)

    p.set_xy(9.9, -20)
    dw = (345.6 - 20 * 2 + (width - 400)) / (nw - 1)
    for i in range(nw):
        p.circle(0, 0, 4.9 / 2)
        p.circle(364.2 + (heigh - 400), 0, 4.9/2)
        p.set_xy(9.9, -(20 + (i + 1) * dw))

    p.set_xy(175 + (heigh - 400) / 2, -41.1)
    p.circle(0, 0, 4.9/2)
    p.circle(34, 0, 4.9/2)
    
    doc.saveas(path+"Половина лопатки "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity * 2)+'шт.dxf')
    

# main(500, 500, 1, 4, 4, "C:/Users/vip/Documents/Danila/scripts/test/Клапан противопожарный ПДВ-1(Пр) 500x500 - 1 шт/резка/0,8мм")