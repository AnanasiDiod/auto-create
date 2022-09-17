from turtle import width
import ezdxf as dxf
from point import *
import os

heigh, width, quantity = 700, 700, 1
ver, side = False, False
nh = int((270 + (heigh - 400))//120)
nw = int((288.2 + (width - 400))//120)
doc = dxf.new()
path = "C:/Users/vip/Documents/Danila/scripts/test/"
doc.layers.add("FIGURE", color=2) 
msp = doc.modelspace()
p = point()
p.msp = msp

p.go_line(89.49, 0)
p.go_arc(8, 5)
p.go_arc(7, 5)
p.go_line(0, -20)
p.go_arc(6, 5)
p.go_arc(5, 5)
p.go_line(-89.49, 0)
p.go_arc(4, 5)
p.go_arc(3, 5)
p.go_line(0, 20)
p.go_arc(2, 5)
p.go_arc(1, 5)
p.go_init()

p.circle(3, -15, 4.9/2)
p.circle(41.74, 0, 17/2)
p.circle(41.74, 0, 4.9/2)

doc.saveas(path+"test.dxf")