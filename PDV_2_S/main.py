import damper
import stripe_vert
import stripe_hor
import axle_support
import arm_1, arm_2
import rib
import profile_1
import os


message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи: '
g_path = ''

def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина клапана в мм: '))
    heigh = int(input('Высота клапана в мм: '))
    Bel = input('Если привод Китай, жмите Enter, если Белимо, введите любые символы: ')
    Belimo = False
    if Bel != '':
        Belimo = True
    quantity = int(input('Количество в резке(шт): '))
    path = g_path + "/Клапан дымовой ПДВ-2 стеновой " + str(
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
        nh = int((270 + (heigh - 400))//120)
        nw = int((288.2 + (width - 400))//120)
        arm_1.main(width, heigh, quantity, path + "2мм/")
        arm_2.main(width, heigh, quantity, path + "2мм/")
        stripe_vert.main(width, heigh, quantity, nh, path + "1мм/")
        stripe_hor.main(width, heigh, quantity, nw, path + "1мм/")
        axle_support.main(width, heigh, quantity, path + "1мм/")
        rib.main(width, heigh, quantity, path + "1мм/")
        damper.main(width, heigh, quantity, nh, nw, path + "0,8мм/")
        profile_1.main(width, heigh, quantity, path + "0,8мм/", Belimo)
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