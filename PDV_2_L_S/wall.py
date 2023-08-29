import ezdxf as dxf
from point import *


def main(width, heigh, quantity, nh, np, sp, Belimo, path=str()):
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
    p.go_line(0, -heigh + 12.44)
    p.go_line(-139, 0)
    p.go_line(0, -20.56)
    p.go_line(-174.16, 0)
    p.go_line(0, 20.56)
    p.go_line(-20.56, 0)
    p.go_init()

    p.circle(37.64, 12.46, 4.9 / 2)
    p.circle(70, 0, 4.9 / 2)
    p.circle(70, 0, 4.9 / 2)
    p.circle(0, -heigh - 12.48, 4.9 / 2)
    p.circle(-70, 0, 4.9 / 2)
    p.circle(-70, 0, 4.9 / 2)

    p.circle(25.6, 28.54, 4.9 / 2)
    p.circle(58.6, 0, 4.9 / 2)
    p.circle(0, heigh - 44.6, 4.9 / 2)
    p.circle(-58.6, 0, 4.9 / 2)

    p.circle(262.38, 1.08, 4.9 / 2)
    dh = (heigh - 42.44)/(nh - 1)
    for i in range(nh - 1):
        p.circle(0, -dh, 4.9 /2)
        
    p.set_xy(0, 0)
    drive = 'Китай '
    if Belimo:
        p.set_xy(62.54, -heigh + ((heigh - 8.6) - (np - 1) * sp) / 2 + 40.52)
        p.circle(0, 0, 6 / 2)
        p.circle(60, 0, 6 / 2)
        p.circle(-30, -30, 17 / 2)
        drive = 'Belimo '
    else:
        p.set_xy(52.54, -heigh + ((heigh - 8.6) - (np - 1) * sp) / 2 + 28.52)
        p.circle(0, 0, 6 / 2)
        p.circle(80, 0, 6 / 2)
        p.circle(-40, -18, 17 / 2)

    doc.saveas(path+"Стенка " + drive +str(width)+'x'+str(heigh) +
               ' 0,8мм ' + str(quantity)+'шт.dxf')



