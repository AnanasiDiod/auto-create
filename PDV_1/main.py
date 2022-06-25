import cup, damper, profile_1, profile_2, plinth, stripes
import profile_1_2, profile_2_2, rib_1, rib_2
import side_support, ud_support, fixture


width, heigh, quantity = 700, 400, 2
path = "C:/Users/vip/Documents/Danila/scripts/test/"
ei150 = False
cup.main(width, heigh, quantity, path)
damper.main(width, heigh, quantity, path)
profile_1.main(width, heigh, quantity, ei150, path)
profile_2.main(width, heigh, quantity, ei150, path)
plinth.main(width, heigh, quantity, path)
stripes.main(width, heigh, quantity, path)
side_support.main(width, heigh, quantity, path)
ud_support.main(width, heigh, quantity, path)
fixture.main(width, heigh, quantity, ei150, path)
if  ei150:
    profile_1_2.main(width, heigh, quantity, path)
    profile_2_2.main(width, heigh, quantity, path)

if width >= 500:
    rib_1.main(width, heigh, quantity, path)
    rib_2.main(width, heigh, quantity, path)