import cup
import plinth
import sidewall
import partition_wall
import partition_sidewall
import partition_sidewall_h
import profile_1
import profile_2
import supports
import support_of_axis
import edge
import os
import ring
import warm_vertical
import warm_vetical_with_hole
import warm_horizontal
import warm_angle
import box_of_actuator
import box_of_actuator_sidewall
import box_of_actuator_sidewall_2


message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи: '
g_path = ''


def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина клапана в мм: '))
    heigh = int(input('Высота клапана в мм: '))
    ms_inp = input('Модификация МС (Д/Н): ')
    ms = False
    if ms_inp in ('Д', 'д'):
        ms = True
    name = "/Противопожарный клапан ПДВ-1 (Пр) "
    if ms:
        name += "МС "
    quantity = int(input('Количество в резке(шт): '))
    path = g_path + name + str(
        width) + "x" + str(heigh) + "(Н) - " + str(quantity) + ' шт/'

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
        try:
            os.mkdir(path + "2мм/")
        except:
            print('Не удалось создать папку "2мм"')
        else:
            print('Все папки созданы успешно')
            nh = (((heigh - 16 - 23 * 2) // 120) // 2 + 1) * 2
            nw = ((width - 58 - 20 * 2) // 120) + 2
            if heigh <= 300 and heigh > 200:
                nh = 4

            sidewall.main(width, heigh, quantity, path + "0,8мм/")
            partition_wall.main(width, heigh, quantity,
                                nh, nw, path + "0,8мм/")
            plinth.main(width, heigh, quantity, ms, path + "0,8мм/")
            partition_sidewall.main(
                width, heigh, quantity, nh, path + "0,8мм/")
            partition_sidewall_h.main(
                width, heigh, quantity, nw, path + "0,8мм/")
            profile_1.main(width, heigh, quantity, ms, path + "0,8мм/")
            profile_2.main(width, heigh, quantity, path + "0,8мм/")
            supports.main(width, heigh, quantity, path + "0,8мм/")
            support_of_axis.main(width, heigh, quantity, path + "0,8мм/")
            ring.main(width, heigh, quantity, path + "2мм/")
            if not(width < 500 and heigh < 500 or heigh < 200):
                edge.main(width, heigh, quantity, path + "0,8мм/")
            if ms:
                warm_vertical.main(width, heigh, quantity, path + "0,8мм/")
                warm_vetical_with_hole.main(
                    width, heigh, quantity, path + "0,8мм/")
                warm_horizontal.main(width, heigh, quantity, path + "0,8мм/")
                warm_angle.main(width, heigh, quantity, path + "0,8мм/")
                box_of_actuator.main(width, heigh, quantity, path + "0,8мм/")
                box_of_actuator_sidewall.main(
                    width, heigh, quantity, path + "0,8мм/")
                box_of_actuator_sidewall_2.main(
                    width, heigh, quantity, path + "0,8мм/")
            else:
                cup.main(width, heigh, quantity, path + "0,8мм/")
    except:
        print("Ошибка сохранения файла! Сообщите о проблеме разработчику!")
    else:
        print("Работа завершена!")


print("Обратите внимание, что в папке не должно находиться несколько позиций с одинаоквыми названиями папок во избежание коллизии\nНе используйте данную программу для производства чертежей для клапанов хотя бы одним размером меньше 150")
ans = 'Д'
while ans in ('Д', 'д', 'L', 'l', ''):
    main()
    message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи\nПросто нажмите Enter, если путь не поменялся: '
    ans = input('Хотите сделать ещё одну позицию? (Д/Н)')
