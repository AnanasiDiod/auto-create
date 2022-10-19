import ezdxf as dxf
from point import *
from math import floor


def main(width, heigh, quantity, rib = 30.0, circles = False, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(width - 3.414, 0)
    l = 0.0
    if rib != 0.0:
        l = rib - 0.95
    p.go_line(0, -l)
    p.go_line(l, 0)
    p.go_line(0, -(heigh - 3.414))
    p.go_line(-l, 0)
    p.go_line(0, -l)
    p.go_line(-(width - 3.414), 0)
    p.go_line(0, l)
    p.go_line(-l, 0)
    p.go_line(0, heigh - 3.414)
    p.go_line(l, 0)
    p.go_line(0, l)

    if circles:
        p.circle(17.29, -(l + 17.29), 3.5)
        p.circle(width - 38, 0, 3.5)
        p.circle(0, -(heigh - 38), 3.5)
        p.circle(-(width - 38), 0, 3.5)

    n = floor((heigh - 153.414)/80)
    delta = l + (heigh - 3.414 - ((n + 1)*50 + n * 30))/2
    for i in range(n + 1):
        p.set_xy(width - 71.71, -(delta + i * 80))
        p.go_line(0, -45)
        p.go_arc(6, 5)
        p.go_arc(5, 5)
        p.go_line(-(width - 150), 0)
        p.go_arc(4, 5)
        p.go_arc(3, 5)
        p.go_line(0, 45)
        
    doc.saveas(path+"Решётка оц "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
