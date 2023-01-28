import ezdxf as dxf
from point import *


def back(width, heigh, quantity, nh, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    # perimeter
    p.go_line(heigh - 22, 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, - width + 97)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-heigh + 22, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, width - 97)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    dh = (-83 + heigh) / (nh - 1)
    p.set_xy(40, -6.1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(0, -width + 105.2, 4.9/2)
        p.set_xy(40 + (i + 1) * dh, -6.1)

    p.set_xy(28.9, -30)
    dw = (-153 + width) / (nw - 1)
    for i in range(nw):
        p.circle(0, 0, 4.9 / 2)
        p.circle(-60.8 + heigh, 0, 4.9/2)
        p.set_xy(28.9, -(30 + (i + 1) * dw))

    # crew back
    p.set_xy(0, 0)
    p.circle(-216.8 + heigh, -35, 2.45)
    p.circle(128, 0, 2.45)
    p.circle(-128, 81.5 - width/2, 2.45)
    p.circle(128, 0, 2.45)
    p.circle(-128, 81.5 - width/2, 2.45)
    p.circle(128, 0, 2.45)
    doc.saveas(path+"Половина лопатки задняя "+str(width) +
               'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')

# Is not complited


def front(width, heigh, quantity, nh, nw, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    # perimeter
    p.go_line(heigh - 36, 0)
    p.go_arc(8, 2)
    p.go_arc(7, 2)
    p.go_line(0, - width + 97)
    p.go_arc(6, 2)
    p.go_arc(5, 2)
    p.go_line(-heigh + 36, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, width - 97)
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    dh = (-83 + heigh) / (nh - 1)
    p.set_xy(26, -6.1)
    for i in range(nh):
        p.circle(0, 0, 4.9 / 2)
        p.circle(0, -width + 105.2, 4.9/2)
        p.set_xy(26 + (i + 1) * dh, -6.1)

    p.set_xy(14.9, -30)
    dw = (-153 + width) / (nw - 1)
    for i in range(nw):
        p.circle(0, 0, 4.9 / 2)
        p.circle(-60.8 + heigh, 0, 4.9/2)
        p.set_xy(14.9, -(30 + (i + 1) * dw))

    # crew back
    p.set_xy(0, 0)
    p.circle(135.8, -35, 2.45)
    p.circle(0, 81.5 - width/2, 2.45)
    p.circle(0, 81.5 - width/2, 2.45)
    # screw for arms
    if width > 500:
        p.set_xy(159.3, -160.5)
        p.go_line(21, 0)
        p.go_line(0, -5.5)
        p.go_line(-21, 0)
        p.go_line(0, 5.5)

        p.set_xy(159.3, 259 - width)
        p.go_line(21, 0)
        p.go_line(0, -5.5)
        p.go_line(-21, 0)
        p.go_line(0, 5.5)
    else:
        p.set_xy(159.3, - (width - 97)/2 + 0.75)
        p.go_line(21, 0)
        p.go_line(0, -5.5)
        p.go_line(-21, 0)
        p.go_line(0, 5.5)
    doc.saveas(path+"Половина лопатки передняя "+str(width) +
               'x'+str(heigh)+' 0,8мм ' + str(quantity)+'шт.dxf')
