import ezdxf as dxf
from point import *


def variants(width, heigh, quantity, path=str(), drive=False):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(102.96, 0)
    p.go_line(0, -(heigh - 4))
    p.go_line(-102.96, 0)
    p.go_line(0, heigh - 4)
    p.go_init()

    p.circle(7.5, -18, 4.9/2)
    p.circle(87.96, 0, 4.9/2)
    p.circle(0, -(360 + heigh - 400), 4.9/2)
    p.circle(-87.96, 0, 4.9/2)
    if drive:
        p.set_xy(51.48, -(198 + (heigh - 400)/2))
        p.circle(0, 0, 5.5)
        doc.saveas(path+"Боковина "+str(width)+'x'+str(heigh) +
                   ' 0,8мм ' + str(quantity)+'шт.dxf')
    else:
        p.set_xy(51.48, -(198 + (heigh - 400)/2))
        p.circle(0, 0, 9)
        doc.saveas(path+"Боковина под привод "+str(width)+'x' +
                   str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')


def main(width, heigh, quantity, path=str()):
    variants(width, heigh, quantity, path, False)
    variants(width, heigh, quantity, path, True)
