import ezdxf as dxf
from point import *


def wall(width, heigh, quantity, path=str()):
    doc = dxf.new()
    doc.layers.add("FIGURE", color=2)
    msp = doc.modelspace()
    p = point()
    p.msp = msp
    p.go_line(97.52, 0)
    p.go_line(0, 23.8 - heigh)
    p.go_line(-64.48, 0)
    p.go_line(0, 1)
    p.go_line(-33.04, 0)
    p.go_arc(4, 2)
    p.go_arc(3, 2)
    p.go_line(0, -(28.8 - heigh))
    p.go_arc(2, 2)
    p.go_arc(1, 2)
    p.go_init()

    doc.saveas(path+"Боковина лопатки вертикальая"+str(width)+'x' +
               str(heigh)+' 0,8мм ' + str(quantity * 2)+'шт.dxf')


wall(900, 700, 1, 'D:/Рабочий стол/git projects/test/')
print('uspeh')
