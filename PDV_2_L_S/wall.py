import ezdxf as dxf
from point import *


def main(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(20.56, 0)
    p.go_line(0, 20.56)
    p.go_line(174.16, 0)
    p.go_line(0, -20.56)
    p.go_line(139, 0)
    p.go_line(0, -537.56)
    p.go_line(-139, 0)
    p.go_line(0, -20.56)
    p.go_line(-174.16, 0)
    p.go_line(0, 20.56)
    p.go_line(-20.56, 0)
    p.go_init()

    p.circle(37.64, 12.46, 4.9 / 2)
    p.circle(70, 0, 4.9 / 2)
    p.circle(70, 0, 4.9 / 2)
    p.circle(0, -562.48, 4.9 / 2)
    p.circle(-70, 0, 4.9 / 2)
    p.circle(-70, 0, 4.9 / 2)

    p.circle(25.6, 28.54, 4.9 / 2)
    p.circle(58.6, 0, 4.9 / 2)
    p.circle(0, 505.4, 4.9 / 2)
    p.circle(-58.6, 0, 4.9 / 2)

    p.circle(262.38, 1.08, 4.9 / 2)
    p.circle(0, -126.89, 4.9 / 2)
    p.circle(0, -126.89, 4.9 / 2)
    p.circle(0, -126.89, 4.9 / 2)
    p.circle(0, -126.89, 4.9 / 2)

    p.set_xy(0, 0)
    p.circle(62.54, -417.41, 6 / 2)
    p.circle(60, 0, 6 / 2)
    p.circle(-30, -30, 17 / 2)

    doc.saveas(path+"Стенка БЕЛИМО "+str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')



