from turtle import width
import ezdxf as dxf
from point import *
import os

heigh, width, quantity = 400, 400, 1
ver, side = False, False
nh = (int((384 + (heigh - 400) - 23 * 2) // 140) // 2 + 1) * 2
nw = (((int(341.6) + 1 + (width - 400) - 20 * 2)) // 120) + 2
doc = dxf.new()
path = "C:/Users/vip/Documents/Danila/scripts/test/"
doc.layers.add("FIGURE", color=2) 
msp = doc.modelspace()
p = point()
p.msp = msp


p.go_line(55.68,0)
p.go_line(0, -50)
p.go_line(-55.68, 0)
p.go_init()
p.circle(6.1, -8, 4.9/2)
p.circle(43.48, 0, 4.9/2)
p.circle(0, -34, 4.9/2)
p.circle(-43.48, 0, 4.9/2)

p.set_xy(21.69, -18.85)
p.go_line(12.3, 0)
p.go_line(0, -12.3)
p.go_line(-12.3, 0)
p.go_line(0, 12.3)
doc.saveas(path+"test.dxf")
