from turtle import width
import ezdxf as dxf
from point import *
import os

heigh, width, quantity = 700, 700, 1
ver, side = False, False
axle, Belimo = False, True
nh = int((270 + (heigh - 400))//120)
nw = int((288.2 + (width - 400))//120)
doc = dxf.new()
path = "C:/Users/vip/Documents/Danila/scripts/test/"
doc.layers.add("FIGURE", color=2) 
msp = doc.modelspace()
p = point()
p.msp = msp

p.go_line(168.89, 0)
p.go_line(0, -18.44)
p.go_line(5.24, 0)
p.go_line(0, 46.8)
p.go_arc(2, 2)
p.go_arc(1, 2)
p.go_line(27.13, 0)
p.go_arc(8, 5)
p.go_angle(-45, 10)
p.go_arc(7, 5)
p.go_line(0, -(442.86 + (heigh - 400)))
p.go_arc(6, 5)
p.go_angle(-135, 10)
p.go_arc(5, 5)
p.go_line(-27.13, 0)
p.go_arc(4, 2)
p.go_arc(3, 2)
p.go_line(0, 46.8)
p.go_line(-5.24, 0)
p.go_line(0, -18.44)
p.go_line(-168.89, 0)
p.go_line(0, 16.15)
p.go_line(-14.15, 0)
p.go_arc(4, 2)
p.go_arc(3, 2)
p.go_line(0, 369.98 + (heigh - 400))
p.go_arc(2, 2)
p.go_arc(1, 2)
p.go_line(14.15, 0)
p.go_init()
#Отверстия для крепления
for i in range(3):
    p.set_xy(25 + i * 59.45, -6.6)
    p.circle(0, 0, 4.9/2)
    p.circle(0, -(393.08 + (heigh - 400)), 4.9/2)
#Отверстие под привод
p.set_xy(17.49, -(347.84 + (heigh - 400)))
p.circle(0, 0, 4)
#Отверстия для крепления в ушах
p.set_xy(200.33, 15.36)
p.circle(0, 0, 4.5)
p.circle(0, -(437 + (heigh - 400)), 4.5)

if axle:
    if Belimo:
        p.set_xy(92.69, -(259.64 + (heigh - 400)))
        p.circle(0, 0, 3.25)
        p.circle(60, 0 , 3.25)
        doc.saveas(path+"Профиль 1 под привод Belimo"+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
    else:
        p.set_xy(82.69, -(271.64 + (heigh - 400)))
        p.circle(0, 0, 3.25)
        p.circle(80, 0, 3.25)
        p.circle(-40, 93, 3.25)
        doc.saveas(path+"Профиль 1 под привод Китай"+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')
else:
    p.set_xy(122.69, -(262.64 + (heigh - 400)))
    p.circle(0, 0, 4.9/2)
    p.circle(0, -54, 4.9/2)

    doc.saveas(path+"Профиль 1 "+str(width)+'x'+str(heigh)+' 0,8мм '+ str(quantity)+'шт.dxf')

doc.saveas(path+"test.dxf")