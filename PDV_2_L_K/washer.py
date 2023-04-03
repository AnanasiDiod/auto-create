import ezdxf as dxf
import pylab as p

from point import *


def main(width, heigh, quantity, np, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.circle(0, 0, 11.5 / 2)
    p.circle(0, 0, 19 / 2)

    doc.saveas(path+"Шайба "+str(width)+'x'+str(heigh) +
               ' 2мм ' + str(quantity * 3 * 2 * np)+'шт.dxf')
