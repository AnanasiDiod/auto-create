from turtle import width
import ezdxf as dxf
from point import *

heigh, width, quantity = 300, 300, 1
doc = dxf.new()
path = "C:/Users/vip/Documents/Danila/scripts/test/"
doc.layers.add("FIGURE", color=2) 
msp = doc.modelspace()
p = point()
p.msp = msp

p.go_line(72, 0)
p.go_arc(8, 3)
p.go_arc(7, 3)
p.go_line(0, -19)
p.go_arc(6, 3)
p.go_arc(5, 3)
p.go_line(-47, 0)
p.set_xy(20, -30)
p.go_arc(2, 5)
p.go_arc(1, 5)
doc.saveas(path+"полоска "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity*2)+'шт.dxf')

