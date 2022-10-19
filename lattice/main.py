import lattice
import os


message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи: '
g_path = ''

def main():
    global g_path
    t_path = input(message_1).replace('\\', "/")
    if t_path != '':
        g_path = t_path
    width = int(input('Ширина решётки в мм: '))
    heigh = int(input('Высота решётки в мм: '))
    ans_rib = input('Введите ширину отгибов, если хотите измерить параметр по умлчанию (30.0 мм): ')
    rib = 30.0
    if ans_rib != '':
        rib = float(ans_rib)
    circles = input('Сделать отверстия? (Д/Н) ') in ('Д', 'д', 'L', 'l')
    quantity = int(input('Количество в резке(шт): '))
    path = g_path + "/Решётка оц " + str(
        width) + "x" + str(heigh) + "(Н) - " + str(quantity) + ' шт/'
    try:
        try:
            os.mkdir(path)
        except:
            print('Не удалось создать папку с названием позиции')

        else:
            print("Папка с названием позиции создана успешно")
        try:
            os.mkdir(path + "/резка/")
        except:
            print('Не удалось создать папку "резка"')
        path += '/резка/'
        try:
            os.mkdir(path + "0,7мм/")
        except:
            print('Не удалось создать папку "0,7мм"')
        else:
            print('Все папки созданы успешно')
        
        lattice.main(width, heigh, quantity, rib, circles, path + "0,7мм/")
        
    except:
        print("Ошибка сохранения файла! Сообщите о проблеме разработчику!")
    else:
        print("Работа завершена!")


print("Обратите внимание, что в папке не должно находиться несколько позиций с одинаоквыми названиями папок во избежание коллизии\n")
ans = 'Д'
while ans in ('Д', 'д', 'L', 'l'):
    main()
    message_1 = 'Скопируйте сюда путь к папке, в которой необходимо сделать чертежи\nПросто нажмите Enter, если путь не поменялся: '
    ans = input('Хотите сделать ещё одну позицию? (Д/Н) ')