from tkinter import *
from tkinter import messagebox


def calculate_pdv_1_pr():
    # Забираем значения из ячеек заполнения
    width = int(width_tf.get())
    heigh = int(heigh_tf.get())
    cost_met = float(cost_tf.get())
    add_cost_met = float(add_cost_tf.get())/100
    cost_cut = float(cut_tf.get())
    cost_vata = float(vata_tf.get())
    cost_ogneza = float(ogneza_tf.get())
    cost_krep = float(krep_tf.get())
    cost_drive = float(drive_tf.get())
    cost_etc = float(etc_tf.get())
    cost_axis = float(axis_tf.get())

    # Расчёт длины реза. Каждая строка - отдельная деталь
    len_cut = heigh * (4 + 4 + 4 + 4) + width * (4 + 4 + 4 + 4) + (1076.346 + 37.699 +  # Крышка привода
                                                                   # Боковина лопатки вертикаль
                                                                   (134.959 - 48 * 2)*2 + 35.5 + 49.2 +
                                                                   # Боковина лопатки горизонт
                                                                   (134.172 - 82.4 * 2) * 2 +
                                                                   # Половина лопатки
                                                                   (-16 * 2 - 58.4 * 2 + 12.566 + 15.39*2)*2 +
                                                                   # Площадка
                                                                   869.712 + 21.99 * 4 + 56.549 +
                                                                   # Профиль 1
                                                                   (918.296 - 17.6 * 2 + 15.39 * 16)*2 + 20.42 * 4 + 56.549 +
                                                                   # Профиль 2
                                                                   (1278.676 + 46 * 2 + 15.39 * 15 + 48.274 * 4) * 2 + 70.324 +
                                                                   # Боковина
                                                                   (205.92 - 4 * 2 + 15.39 * 4) * 2 + 34.558 + 56.549 +
                                                                   # Поддержка оси
                                                                   211.36 + 15.39 * 4 + 12.3 * 4 +
                                                                   # Уголок
                                                                   (77.27 - 98 + 15.39 * 3) * 2 +
                                                                   # Шайбы 2мм
                                                                   95.819 * 4)
    # Учёт отверстий в половине лопатки и в боковинах
    nh = (((heigh - 66) // 120) // 2 + 1) * 2
    nw = ((width - 98) // 120) + 2
    len_cut += (nh + nw) * 8 * 15.39
    # Расчёт площади металла
    area_met_korp = (103 * 2 + 391 * 2) * heigh + (389 * 2 + 27.64 * 2) * width - \
        (4 * 103 * 2 - 55 * 391 * 2 - 56 * 389 * 2 +
         38 * 27.64) + 198 * 314 + 153 * 291
    area_met_lopatka = (heigh - 12) * (width - 54) * 2 + \
        (55.69 * 2 + 0) * heigh + (55.69 * 2 + 0) * width - \
        (18 * 55.69 * 2 + 54 * 55.69 * 2) + 50 * 55.68
    # Расчёт площади утеплителя
    area_vata = (heigh - 18) * (width - 54) / 1000000
    # Длина огнезы
    len_ogneza = ((heigh - 4 + width - 54) * 2 + 40)/1000
    # Учёт наличия ребра
    if not(width < 500 and heigh < 500 or heigh < 200):
        len_cut += 548.58 + width * 2 - 84.4 * 2 + 15.39 * 9
        area_met_lopatka += (width - 84) * 198
    # Расчёт "голой" стоимости металла и реза
    val_cut = len_cut * cost_cut / 1000
    area_met_lopatka /= 1000000
    area_met_korp /= 1000000
    val_met = (area_met_lopatka + area_met_korp) * cost_met
    print(cost_met)

    messagebox.showinfo(
        'Результаты подсчётов',
        '''Длина реза: %s м
Цена резки: %s руб
Площадь металла корпус: %s м2
Площадь металла лопатка: %s м2
Стоимость металла: %s руб
Площадь утеплителя: %s м2
Стоимость утеплителя: %s руб
Стоимость привода (-ов): %s руб
Стоимость крепежа: %s руб
Длина Огнезы: %s м
Стоиость Огнезы: %s руб
Стоимость осей: %s руб
Стоимость прочих материалов: %s руб
----------------------------------------------------
Общая сумма: %s руб
            ''' % (len_cut / 1000, val_cut, area_met_korp, area_met_lopatka, val_met, area_vata, area_vata * cost_vata,
                   cost_drive, cost_krep, len_ogneza, len_ogneza * cost_ogneza, cost_axis, cost_etc, (val_cut + val_met + area_vata * cost_vata + cost_drive + cost_krep + len_ogneza * cost_ogneza + cost_axis + cost_etc)*(add_cost_met + 1)))


def calculate_pdv_1_kr():
    messagebox.showinfo('win')


def calculate_pdv_2_s():
    messagebox.showinfo('win')


def calculate_pdv_2_k():
    messagebox.showinfo('win')


def calculate_pdv_2_ls():
    messagebox.showinfo('win')


def calculate_pdv_2_lk():
    messagebox.showinfo('win')


window = Tk()
window.title('Bajan-calculator')


frame = Frame(
    # Обязательный параметр, который указывает окно для размещения Frame.
    window,
    padx=10,  # Задаём отступ по горизонтали.
    pady=10,  # Задаём отступ по вертикали.
)
frame.pack(expand=True)
# НАДПИСИ
width_lb = Label(frame,    text="Введите ширину клапана (мм)  ")
width_lb.grid(row=1, column=3)

heigh_lb = Label(frame, text="Введите ширину клапана (мм)  ")
heigh_lb.grid(row=2, column=3)

cost_lb = Label(frame, text="Введите цену за квадратный метр металла (руб)  ")
cost_lb.grid(row=4, column=3)

add_cost_lb = Label(frame, text="Введите наценку (%)  ")
add_cost_lb.grid(row=3, column=3)

cut_lb = Label(frame, text="Введите цену за метр реза (руб)  ")
cut_lb.grid(row=5, column=3)

vata_lb = Label(
    frame, text="Введите цену за квадратный метр утеплителя (руб)  ")
vata_lb.grid(row=6, column=3)

axis_lb = Label(frame, text="Введите стоимость оси (руб)  ")
axis_lb.grid(row=7, column=3)

krep_lb = Label(frame, text="Введите стоимость всего крепежа (руб)  ")
krep_lb.grid(row=8, column=3)

drive_lb = Label(frame, text="Введите стоимость приводов (руб)  ")
drive_lb.grid(row=9, column=3)

ogneza_lb = Label(frame, text="Введите цену за метр огнезы (руб)  ")
ogneza_lb.grid(row=10, column=3)

etc_lb = Label(
    frame, text="Введите стоимость всех остальных материалов (руб)  ")
etc_lb.grid(row=11, column=3)

# ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
width_tf = Entry(frame)
width_tf.grid(row=1, column=4)

heigh_tf = Entry(frame)
heigh_tf.grid(row=2, column=4)

cost_tf = Entry(frame)
cost_tf.grid(row=4, column=4)

add_cost_tf = Entry(frame)
add_cost_tf.grid(row=3, column=4)

cut_tf = Entry(frame)
cut_tf.grid(row=5, column=4)

vata_tf = Entry(frame)
vata_tf.grid(row=6, column=4)

axis_tf = Entry(frame)
axis_tf.grid(row=7, column=4)

krep_tf = Entry(frame)
krep_tf.grid(row=8, column=4)

drive_tf = Entry(frame)
drive_tf.grid(row=9, column=4)

ogneza_tf = Entry(frame)
ogneza_tf.grid(row=10, column=4)

etc_tf = Entry(frame)
etc_tf.grid(row=11, column=4)

# КНОПКИ
pdv_1_pr_btn = Button(frame, text='ПДВ-1 (Пр)', command=calculate_pdv_1_pr)
pdv_1_pr_btn.grid(row=1, column=1)

pdv_1_kr_btn = Button(frame, text='ПДВ-1 (Кр)', command=calculate_pdv_1_kr)
pdv_1_kr_btn.grid(row=1, column=2)

pdv_2_s_btn = Button(frame, text='ПДВ-2-С', command=calculate_pdv_2_s)
pdv_2_s_btn.grid(row=2, column=1)

pdv_2_k_btn = Button(frame, text='ПДВ-2-К', command=calculate_pdv_2_k)
pdv_2_k_btn.grid(row=2, column=2)

pdv_2_ls_btn = Button(frame, text='ПДВ-2-Л-С', command=calculate_pdv_2_ls)
pdv_2_ls_btn.grid(row=3, column=1)

pdv_2_lk_btn = Button(frame, text='ПДВ-2-Л-К', command=calculate_pdv_2_lk)
pdv_2_lk_btn.grid(row=3, column=2)

window.mainloop()
