from tkinter import *
from tkinter import messagebox


def calculate_pdv_1_pr():
    # Забираем значения из ячеек заполнения
    width = int(width_tf.get())
    heigh = int(heigh_tf.get())
    cost_met = float(cost_tf.get())
    add_cost_met = float(add_cost_tf.get())/100
    cost_cut = float(cut_tf.get())
    # Считаем длину реза. Каждая строка - отдельная деталь
    len_cut = heigh * (8) + width * (8) + (1114.035 +
                                           687.124 +
                                           (134.959 - 48 * 2)*2 + 35.5 + 49.2 +
                                           (134.172 - 82.4 * 2) * 2 +
                                           (-16 * 2 - 58.4 * 2 + 12.566)*2)
    nh = (((heigh - 66) // 120) // 2 + 1) * 2
    nw = ((width - 98) // 120) + 2
    len_cut += (nh + nw) * 8 * 15.39

    area_met = 1*heigh + 1*width + 1

    if not(width < 500 and heigh < 500 or heigh < 200):
        len_cut += width * 2 - 84.4 * 2
        area_met += 1
    val_cut = len_cut * cost_cut
    val_met = area_met * cost_met

    messagebox.showinfo(
        'Результаты подсчётов', 'Длина реза: %s м\nЦена резки: %s руб\nПлощадь металла: %s м2\nСтоимость металла: %s руб\nСтоимость металла после наценки: %s руб' % (len_cut, val_cut, area_met, val_met, val_met*(1 + add_cost_met)))


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
    pady=10  # Задаём отступ по вертикали.
)
frame.pack(expand=True)
# НАДПИСИ
width_lb = Label(frame,    text="Введите ширину клапана (мм)  ")
width_lb.grid(row=1, column=3)

heigh_lb = Label(frame, text="Введите ширину клапана (мм)  ")
heigh_lb.grid(row=2, column=3)

cost_lb = Label(frame, text="Введите цену за квадратный метр металла (руб)  ")
cost_lb.grid(row=3, column=3)

add_cost_lb = Label(frame, text="Введите наценку на металл (%)  ")
add_cost_lb.grid(row=4, column=3)

cut_lb = Label(frame, text="Введите цену за метр реза (руб)  ")
cut_lb.grid(row=5, column=3)

# ПОЛЯ ДЛЯ ЗАПОЛНЕНИЯ
width_tf = Entry(frame)
width_tf.grid(row=1, column=4)

heigh_tf = Entry(frame)
heigh_tf.grid(row=2, column=4)

cost_tf = Entry(frame)
cost_tf.grid(row=3, column=4)

add_cost_tf = Entry(frame)
add_cost_tf.grid(row=4, column=4)

cut_tf = Entry(frame)
cut_tf.grid(row=5, column=4)

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
