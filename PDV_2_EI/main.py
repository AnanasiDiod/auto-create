import os
import arm_1
import arm_2
import rib
import support_of_axis
import sidewall
import partition_wall
import partition_sidewall
import profile_1
import profile_2
import profile_3


message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи: '
g_path = ''


def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина клапана в мм: '))
    heigh = int(input('Высота клапана в мм: '))
    Bel = input(
        'Если привод Китай, жмите Enter, если Белимо, введите любые символы: ')
    Belimo = False
    if Bel != '':
        Belimo = True
    quantity = int(input('Количество в резке(шт): '))
    if Belimo:
        path = g_path + "/Клапан дымовой ПДВ-2 стеновой утеплённый Белимо" + str(
            width) + "x" + str(heigh) + "(Н) - " + str(quantity) + ' шт/'
    else:
        path = g_path + "/Клапан дымовой ПДВ-2 стеновой утеплённый Китай" + str(
            width) + "x" + str(heigh) + "(Н) - " + str(quantity) + ' шт/'
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
        try:
            os.mkdir(path + "2мм/")
        except:
            print('Не удалось создать папку "2мм"')
        try:
            os.mkdir(path + "1мм/")
        except:
            print('Не удалось создать папку "1мм"')
        else:
            print('Все папки созданы успешно')
        nh = ((heigh - 18) // 120) + 1
        nw = ((width - 93) // 120) + 1

        arm_1.main(width, heigh, quantity, path + "2мм/")
        arm_2.main(width, heigh, quantity, path + "2мм/")
        rib.main(width, heigh, quantity, path + "1мм/")
        support_of_axis.main(width, heigh, quantity, path + "1мм/")
        partition_wall.back(width, heigh, quantity, nh, nw, path + "0,8мм/")
        partition_wall.front(width, heigh, quantity, nh, nw, path + "0,8мм/")
        partition_sidewall.vertical(
            width, heigh, quantity, nh, path + "0,8мм/")
        partition_sidewall.horisontal(
            width, heigh, quantity, nw, path + "0,8мм/")
        sidewall.main(width, heigh, quantity, path + "0,8мм/")
        profile_1.main(width, heigh, quantity, path + "0,8мм/", Belimo)
        profile_2.main(width, heigh, quantity, path + "0,8мм/")
        profile_3.main(width, heigh, quantity, path + "0,8мм/")
    except:
        print("Ошибка сохранения файла! Сообщите о проблеме разработчику!")
    else:
        print("Работа завершена!")


print("Обратите внимание, что в папке не должно находиться несколько позиций с одинаоквыми названиями папок во избежание коллизии\nНе используйте данную программу для производства чертежей для клапанов шириной меньше 350мм")
ans = 'Д'
while ans in ('Д', 'д', 'L', 'l'):
    main()
    message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи\nПросто нажмите Enter, если путь не поменялся: '
    ans = input('Хотите сделать ещё одну позицию? (Д/Н) ')
