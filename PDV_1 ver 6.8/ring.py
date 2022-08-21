import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.circle(0, 0, 5.75)
    p.circle(0, 0, 9.5)

    doc.saveas(path+"Шайба "+str(width)+'x' +
               str(heigh)+' 2мм ' + str(quantity * 2)+'шт.dxf')