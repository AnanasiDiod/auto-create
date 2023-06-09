import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(303, 0)
    p.go_line(0, -27.64)
    p.go_line(-303, 0)
    p.go_line(0, 27.64)
    p.circle(20, -19.54, 4.9 / 2)
    p.circle(131.5, 0, 4.9 / 2)
    p.circle(131.5, 0, 4.9 / 2)
    doc.saveas(path+"Уголок верх низ "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity * 2)+'шт.dxf')
main(1,1,1)