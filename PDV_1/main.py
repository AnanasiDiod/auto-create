import cup, damper, profile_1, profile_2, plinth, stripes
import profile_1_2, profile_2_2, rib_1, rib_2
import side_support, ud_support, fixture
import os


width, heigh, quantity = 700, 400, 2
path = "C:/Users/vip/Documents/Danila/scripts/test/Клапан противопожарный ПДВ-1(Пр) " + str(width) + "x" + str(heigh) + '/'
ei150 = False

try:
    try:
        os.mkdir(path)
    except:
        pass
    else:
        print("Directory for DXFs created successfully")
    try:
        os.mkdir(path + "/резка/")
    except:
        pass
    path += '/резка/'
    try:
        os.mkdir(path + "0,8мм/")
    except:
        pass
    try:
        os.mkdir(path + "1мм/")
    except:
        pass
    print('All directories were created successfully')
    cup.main(width, heigh, quantity, path + "0,8мм/")
    damper.main(width, heigh, quantity, path + "0,8мм/")
    profile_1.main(width, heigh, quantity, ei150, path + "0,8мм/")
    profile_2.main(width, heigh, quantity, ei150, path + "0,8мм/")
    plinth.main(width, heigh, quantity, path + "0,8мм/")
    stripes.main(width, heigh, quantity, path + "0,8мм/")
    side_support.main(width, heigh, quantity, path + "0,8мм/")
    ud_support.main(width, heigh, quantity, path + "0,8мм/")
    fixture.main(width, heigh, quantity, ei150, path + "1мм/")
    if  ei150:
        profile_1_2.main(width, heigh, quantity, path + "0,8мм/")
        profile_2_2.main(width, heigh, quantity, path + "0,8мм/")

    if width >= 500:
        rib_1.main(width, heigh, quantity, path + "0,8мм/")
        rib_2.main(width, heigh, quantity, path + "0,8мм/")
except:
    print("Error creating directory or saving file")
else:
    print("All directories and files created successfully")