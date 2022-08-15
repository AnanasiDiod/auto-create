import cup, plinth, sidewall, partition_wall, partition_sidewall, partition_sidewall_h
import profile_1, profile_2, supports, support_of_axis, edge
import os

width, heigh, quantity = 500, 600, 1
# path = input().replace('\\', "/")
path = "C:/Users/vip/Documents/Danila/scripts/test/Клапан противопожарный ПДВ-1(Пр) " + str(width) + "x" + str(heigh) +" - " + str(quantity) + ' шт'+ '/'
# path = "D:/Рабочий стол/git projects/test/Клапан дымовой ПДВ-2(Стеновой) " + str(width) + "x" + str(heigh) + '/'

ei150 = False

try:
    try:
        os.mkdir(path)
    except:
        print('Не удалось создать папку с названием клапана')
        
    else:
        print("Папка с названием клапана создана успешно")
    try:
        os.mkdir(path + "/резка/")
    except:
        print('Не удалось создать папку "резка"')
    path += '/резка/'
    try:
        os.mkdir(path + "0,8мм/")
    except:
        print('Не удалось создать папку "0,8мм"')
    else:
        print('Все папки созданы успешно')
        nh = (((384 + (heigh - 400) - 23 * 2) // 140) // 2 + 1) * 2
        nw = ((int(341.6) + 1 + (width - 400) - 20 * 2) // 140) + 2
        cup.main(width, heigh, quantity, path + "0,8мм/")
        sidewall.main(width, heigh, quantity, path + "0,8мм/")
        partition_wall.main(width, heigh, quantity, nh, nw, path + "0,8мм/")
        plinth.main(width, heigh, quantity, path + "0,8мм/")
        partition_sidewall.main(width, heigh, quantity, nh, path + "0,8мм/")
        partition_sidewall_h.main(width, heigh, quantity, nw, path + "0,8мм/")
        profile_1.main(width, heigh, quantity, path + "0,8мм/")
        profile_2.main(width, heigh, quantity, path + "0,8мм/")
        supports.main(width, heigh, quantity, path + "0,8мм/")
        support_of_axis.main(width, heigh, quantity, path + "0,8мм/")
        if (width >= 400 or heigh >= 400) and heigh >= 200:
            edge.main(width, heigh, quantity, path + "0,8мм/")
except:
    print("Ошибка сохранения файла!")
else:
    print("Работа завершена!")