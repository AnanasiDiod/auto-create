from turtle import width
import ezdxf as dxf
from point import *
import os

heigh, width, quantity = 400, 400, 1
nh = (int((384 + (heigh - 400) - 23 * 2) // 140) // 2 + 1) * 2
nw = (((int(341.6) + 1 + (width - 400) - 20 * 2)) // 120) + 2
doc = dxf.new()
path = "C:/Users/vip/Documents/Danila/scripts/test/"
doc.layers.add("FIGURE", color=2) 
msp = doc.modelspace()
p = point()
p.msp = msp

p.go_line(312.4, 0)
p.go_line(0, -31.44)
p.go_line(41.08, 0)
p.go_arc(8, 5)
p.go_arc(7, 5)
p.go_line(0, -(382.4 + (heigh - 400)))
p.go_arc(6, 5)
p.go_arc(5, 5)
p.go_line(-41.08, 0)
p.go_line(0, -31.44)
p.go_line(-312.4, 0)
p.go_line(0, 31.44)
p.go_line(-41.08, 0)
p.go_arc(4, 5)
p.go_arc(3, 5)
p.go_line(0, 382.4 + (heigh - 400))
p.go_arc(2, 5)
p.go_arc(1, 5)
p.go_line(41.08, 0)
p.go_line(0, 31.44)
p.go_init()

p.circle(35, 13.1, 4.9/2)
p.circle(242.4, 0, 4.9/2)

p.circle(-293.84, -28.34, 4.9/2)
p.circle(0, -26.2, 4.9/2)
p.circle(345.28, 0, 4.9/2)
p.circle(0, 26.2, 4.9/2)

p.circle(-218.34, -6.2, 4.9/2)
p.circle(-58.6, 0, 4.9/2)
p.circle(0, -(360 + (heigh - 400)), 4.9/2)
p.circle(58.6, 0, 4.9/2)

p.circle(-75.5, -34.5, 4.9/2)
p.circle(242.4, 0, 4.9/2)

p.circle(51.44, 28.34, 4.9/2)
p.circle(0, 26.2, 4.9/2)
p.circle(-345.28, 0, 4.9/2)
p.circle(0, -26.2, 4.9/2)

p.circle(68.34, 6.2, 4.9/2)
p.circle(58.6, 0, 4.9/2)

doc.saveas(path+"test.dxf")
