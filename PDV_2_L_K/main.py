import os
import area
import axis_support
import corner_top_bottom
import cover_of_actuator
import edge
import half_of_spacula_with_fold_new
import half_of_spacula_new
import profile_1
import profile_2
import sidewall
import washer
from math import ceil

message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи: '
g_path = ''


def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина клапана в мм: '))
    heigh = int(input('Высота клапана в мм: '))
    quantity = int(input('Количество в резке(шт): '))
    path = g_path + "/Клапан противопожарный ПДВ-2 канальный лифтовый " + str(
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
        # количество горизонтальных отверстий в лопатках
        nw = ceil((width - 114.4)/125) + 1
        # количество лопаток
        np = int(heigh / 220) + 1
        # высота лопатки
        hp = (heigh - 7.5 * (np + 1)) / np
        # шаг лопаток
        sp = hp + 7.5

        area.main(width, heigh, quantity, path + "/0,8мм/")
        axis_support.main(width, heigh, quantity, path + "/2мм/")
        corner_top_bottom.main(width, heigh, quantity, path + "/0,8мм/")
        cover_of_actuator.main(width, heigh, quantity, path + "/0,8мм/")
        edge.main(width, heigh, quantity, np, sp, path + "/2мм/")
        half_of_spacula_with_fold_new.main(
            width, heigh, quantity, np, hp, nw, path + "/0,8мм/")
        half_of_spacula_new.main(width, heigh, quantity, np,
                             hp, nw, path + "/0,8мм/")
        profile_1.main(width, heigh, quantity, np, sp, path + "/0,8мм/")
        profile_2.main(width, heigh, quantity, path + "/0,8мм/")
        # sidewall_of_spacula_hor.main(
        #     width, heigh, quantity, nw, np, path + "/0,8мм/")
        # sidewall_of_spacula.main(
        #     width, heigh, quantity, np, hp, path + "/0,8мм/")
        sidewall.main(width, heigh, quantity, np, sp, path + "/0,8мм/")
        washer.main(width, heigh, quantity, np, path + "/2мм/")

    except:
        print("Ошибка сохранения файла! Сообщите о проблеме разработчику!")
    else:
        print("Работа завершена!")


print("Обратите внимание, что в папке не должно находиться несколько позиций с одинаоквыми названиями папок во избежание коллизии")
ans = 'Д'
while ans in ('Д', 'д', 'L', 'l'):
    main()
    message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи\nПросто нажмите Enter, если путь не поменялся: '
    ans = input('Хотите сделать ещё одну позицию? (Д/Н) ')
