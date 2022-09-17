import damper
import stripe_vert
import stripe_hor

import os


def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина клапана в мм: '))
    heigh = int(input('Высота клапана в мм: '))
    quantity = int(input('Количество в резке(шт): '))
    path = g_path + "/Клапан дымовой ПДВ-2(Стеновой) " + str(
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
        else:
            print('Все папки созданы успешно')
        nh = int((270 + (heigh - 400))//120)
        nw = int((288.2 + (width - 400))//120)
        stripe_vert.main(width, heigh, quantity, nh, path + "1мм/")
        stripe_hor.main(width, heigh, quantity, nw, path + "1мм/")
    except:
        print("Ошибка сохранения файла! Сообщите о проблеме разработчику!")
    else:
        print("Работа завершена!")


print("Обратите внимание, что в папке не должно находиться несколько позиций с одинаоквыми названиями папок во избежание коллизии\nНе используйте данную программу для производства чертежей для клапанов шириной меньше 350мм")
ans = 'Д'
while ans in ('Д', 'д', 'L', 'l'):
    main()
    message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи\nПросто нажмите Enter, если путь не поменялся: '
    ans = input('Хотите сделать ещё одну позицию? (Д/Н)')