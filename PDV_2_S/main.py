import damper
import stripe_vert
import stripe_hor
import os


width, heigh, quantity = 700, 400, 2
# path = "C:/Users/vip/Documents/Danila/scripts/test/Клапан дымовой ПДВ-2(Стеновой) " + str(width) + "x" + str(heigh) + '/'
path = "D:/Рабочий стол/git projects/test/Клапан дымовой ПДВ-2(Стеновой) " + str(
    width) + "x" + str(heigh) + '/'

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
    try:
        os.mkdir(path + "2мм/")
    except:
        pass
    print('All directories were created successfully')
    damper.main(width, heigh, quantity, path + "0,8мм/")
    stripe_vert.main(width, heigh, quantity, path + "1мм/")
    stripe_hor.main(width, heigh, quantity, path + "1мм/")
except:
    print("Error creating directory or saving file")
else:
    print("All files were created successfully")
