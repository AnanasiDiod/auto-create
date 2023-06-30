import ezdxf as dxf
from point import *

def main(width, heigh, quantity, path = str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2) 
    msp = doc.modelspace()
    p = point()
    p.msp = msp

    p.go_line(100.29, 0)
    p.go_line(0, -(302 + (width-400)))
    p.go_line(-100.29, 0)
    p.go_line(0, 302 + (width-400))
    p.go_init()
    #отверстия для крепления
    p.circle(8.1, -50, 4.9/2)
    p.circle(0, -(202 + (width - 400)), 4.9/2)
    #отверстия для рычагов
    p.set_xy(50.14, -101.37)
    p.circle(0, 0, 5.2/2)
    p.circle(0, -(121 + (width - 400)), 5.2/2)
    #вырезы для ушей
    p.set_xy(39.14, -87)
    p.go_line(0, -25)
    p.go_line(22, 0)
    p.go_line(0, 25)
    p.set_xy(61.114, -102.37)
    p.go_arc(6, 8)
    p.go_arc(5, 8)
    p.go_line(-6, 0)
    p.go_arc(4, 8)
    p.go_arc(3, 8)

    p.set_xy(39.14, -(208 + (width - 400)))
    p.go_line(0, -25)
    p.go_line(22, 0)
    p.go_line(0, 25)
    p.set_xy(61.114, -(223.37 + (width - 400)))
    p.go_arc(6, 8)
    p.go_arc(5, 8)
    p.go_line(-6, 0)
    p.go_arc(4, 8)
    p.go_arc(3, 8)

    doc.saveas(path+"Ребро_3 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
