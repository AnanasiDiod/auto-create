import openpyxl as xl
import os


def calculate_pdv_1_pr(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                       cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    # Расчёт длины реза. Каждая строка - отдельная деталь
    len_cut = height * (4 + 4 + 4 + 4) + \
        width * (4 + 4 + 4 + 4) + \
        (1076.346 + 37.699 +  # Крышка привода
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
    nh = (((height - 66) // 120) // 2 + 1) * 2
    nw = ((width - 98) // 120) + 2
    len_cut += (nh + nw) * 8 * 15.39
    # Расчёт длины гиба
    len_bend = ((height - 4) * 4 * 2 +  # Боковина
                # Боковина лопатки
                (height - 18) * 2 * 2 +
                # Боковина лопатки горизонтальная
                (width - 54.4) * 2 * 2 +
                # Крыщка привода
                494.8 +
                # Площадка
                864.8 +
                # Поддержка оси
                222.72 +
                # Профиль 1
                (312.4 * 2 + (height - 7.6) * 4) * 2 +
                # Профиль 2
                (width - 1) * 2 * 2 +
                # Уголок
                (width - 60) * 2)
    # Расчёт площади металла
    area_met_korp = (103 * 2 + 391 * 2) * height + (389 * 2 + 27.64 * 2) * width - \
        (4 * 103 * 2 - 55 * 391 * 2 - 56 * 389 * 2 +
         38 * 27.64) + 198 * 314 + 153 * 291
    area_met_lopatka = (height - 12) * (width - 54) * 2 + \
        (55.69 * 2 + 0) * height + (55.69 * 2 + 0) * width - \
        (18 * 55.69 * 2 + 54 * 55.69 * 2) + 50 * 55.68
    # Учёт наличия ребра
    if not(width < 500 and height < 500 or height < 200):
        len_cut += 548.58 + width * 2 - 84.4 * 2 + 15.39 * 9
        area_met_lopatka += (width - 84) * 198
        len_bend += (width - 84.4) * 4
    # Расчёт "голой" стоимости металла, стоимости реза и стоимости гиба
    val_bend = cost_bend * len_bend / 1000
    val_cut = len_cut * cost_cut / 1000
    area_met_lopatka /= 1000000
    area_met_korp /= 1000000
    val_met = (area_met_lopatka + area_met_korp) * cost_met

    res = {'width': width, 'height': height, 'quad': area_met_lopatka + area_met_korp, 'cost_met': cost_met,
           'val_met': val_met, 'val_cut': val_cut, 'val_bend': val_bend,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost + val_met) * \
        markup_box + val_cut + val_bend + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_1_kr(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                       cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    res = {'width': width, 'height': height, 'quad': 0, 'cost_met': cost_met,
           'val_met': 0, 'val_cut': 0, 'val_bend': 0,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost) * \
        markup_box + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_s_ei(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                         cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    # Расчёт длины реза
    nh = ((height - 18) // 120) + 1
    nw = ((width - 93) // 120) + 1
    len_cut = ((156.13 * 2 + 100.53 + 20.4 + 62.83 + 103.67) * 2 +  # Рычаг 1
               # Рычаг 2
               (109.5 * 2 + 2 * 2 + 62.83 + 40.84) * 2 +
               # Боковина для оси
               89.49 * 2 + 20 * 2 + 15.7 + 30.79 + 53.4 +
               # Боковина лопатки вертикальная
               ((22.1 * 4 + 23.25 + (height - 73)) * 2 + 35.5 + nh * 15.39) * 2 +
               # Боковиана лопатки горизонтальная
               ((20 * 2 + 27 + (width - 121)) * 2 + nw * 15.39) * 2 +
               # Половина лопатки зад
               ((height - 22) + (width - 97)) * \
               2 + 12.57 + (nh + nw) * 2 * 15.39 + 6 * 15.39 +
               # Половина лопатки перед
               ((height - 36) + (width - 97)) * 2 + \
               12.57 + (nh + nw) * 2 * 15.39 + 3 * 15.39 + (21 + 5.5) * 2 * 2 +
               # Профиль 1
               (163.79 + 18.44 + 5.42 + 43.8 + 24.13 + 10 + (height + 43.06) + 10 + 24.13 + 43.8 + \
                5.24 + 16.44 + 163.79 + 16.15 + 14.15 * 2 + (height - 29.81) + 14.15 * 2 + 12.57 + 15.7 + \
                8 * 15.4 + 28.27) * 2 + 30.78 + 30.63 +
               # Профиль 2
               188.08 + 55.43 + 2.22 + \
               (width - 143.14) + 2.22 + 55.43 + 188.08 + 23 + 24.13 + 10 + (width + 26.86) + 10 + 24.13 + 62.83 + 6 * 15.39 + 2 * 28.27 +
               # Профиль 3
               182.9 + (width - 15) + 182.9 + 23 + 24.13 + 10 + (width + 26.86) + 10 + 24.13 + 47.12 + 6 * 15.4 + 138.23 +
               # Ребро
               (198.29 + width - 123) * 2 + 9 * 15.39 + (29.1 * 2 + 20 + 31.4 + 15.39) * 2 +
               # Боковина
               (97.52 + (height - 23.8) + 64.48 + 1 + 33.04 +
                (height - 28.8) + 6.28 + 4 * 15.39 + 34.56) * 2 +
               # Поддержка оси
               89.5 * 2 + 20 * 2 + 15.7 + 30.79 + 53.4
               )
    # Расчёт длины гиба
    len_bend = ((width - 93) * 2 * 2 +  # боковина лопатки горизонтальная
                # боковина лопатки вертикальная
                (height - 43) * 2 * 2 +
                # Боковина
                (height - 23.8) * 3 * 2 +
                # Профиль 1
                (height - 25.8 + height - 30.4) * 2 +
                # Профиль 2 и 3
                (width - 5) * 2 * 2 +
                # Поддержка оси
                30 * 4 +
                # Ребро
                (width - 123) * 4 +
                # Рычаг 1
                32
                )
    # Расчёт площади металла
    area_met_korp = + 99.521 * (height - 23.8) * 2 + \
        (height + 167.2) * 230.38 * 2 + (width + 51) * (234.28 + 229.1) + \
        30 * 99.5 + 32 * 188 + 22 * 130
    area_met_lopatka = (width - 93) * (height - 18) * 2 + (width - 93) * \
        55.68 * 2 + (height - 43) * 55.68 * 2 + (width - 123) * 198.288
    # Расчёт "голой" стоимости металла, стоимости реза и стоимости гиба
    val_bend = cost_bend * len_bend / 1000
    val_cut = len_cut * cost_cut / 1000
    area_met_lopatka /= 1000000
    area_met_korp /= 1000000
    val_met = (area_met_lopatka + area_met_korp) * cost_met

    res = {'width': width, 'height': height, 'quad': area_met_lopatka + area_met_korp, 'cost_met': cost_met,
           'val_met': val_met, 'val_cut': val_cut, 'val_bend': val_bend,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost + val_met) * \
        markup_box + val_cut + val_bend + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_s(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                      cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    # Расчёт длины реза
    len_cut = ((156.13 * 2 + 100.53 + 20.4 + 62.83 + 103.67) * 2 +  # Рычаг 1
               # Рычаг 2
               (120 * 2 + 2 * 2 + 62.83 + 40.84) * 2 +
               # Боковина для оси
               89.5 * 2 + 20 * 2 + 15.7 + 30.79 + 53.4 +
               # Лопатка
               (width - 49.74) * 2 + 18.51 * 2 * 4 + (height - 93.67) * 2 + (14.14 + 20 + 14.14) * 2 + 17.93 * 2 + 30.79 + 34.56 +
               # Профиль 1
               (168.89 + 18.44 + 5.42 + 46.8 + 27.13 + 10 + (height + 42.86) + 10 + 27.13 + 46.8 + \
                5.24 + 18.44 + 168.89 + 16.15 + 14.15 * 2 + (height - 30.02) + 14.15 * 2 + 12.57 + 15.7 + \
                6 * 15.4 + 12.57 + 28.27) * 2 + 30.78 + 30.63 +
               # Профиль 2
               197.78 * 2 + (width - 9) + 23 + 24.13 + 10 + \
               width + 26.86 + 10 + 24.13 + 6.28 + 31.42 + 56.55 + 6 * 15.4 +
               # Профиль 3
               187.38 + (width - 9) + 187.38 + 23 + 24.13 + 10 + (width + 26.86) + 10 + 24.13 + 31.42 + 6.3 + 56.55 + 6 * 15.4 + 138.23 +
               # Ребро
               (100.29 + width - 98) * 2 + 30.79 + 40.84 + (25 + 22 + 25 + 6 + 25.13) * 2 +
               # Полоска горизонтальная
               (width - 93 + 32.5 + 6.28) * 2 +
               # Полоска вертикальная
               (height - 78 + 32.5 + 6.28) * 2 * 2
               )
    # Учёт отверстий в лопатке и полосках
    nh = int((270 + (height - 400))//120)
    nw = int((288.2 + (width - 400))//120)
    len_cut += (nh * 2 + nw) * 2 * 15.39
    # Расчёт длины гиба
    len_bend = ((width - 49.74) * 2 + (height - 35.74) * 2 +  # Лопатка
                # Профиль 1
                (168.89 * 2 + (height - 30.02) * 2) * 2 +
                # Профиль 2 и 3
                + (width - 5) * 2 * 2 +
                # Боковина для оси
                30 * 4 +
                # Ребро
                (width - 98) * 4 + 22 * 2 +
                # Рычаг 1
                32
                )
    # Расчёт площади металла
    area_met_korp = 231.48 * (height + 67) * 2 + \
        (width + 51) * 241 + (width + 51) * 230.6 + 99.5 * \
        30 + (height - 78) * 36.5 * 2 + (width - 93) * \
        36.5 + 100.29 * (width - 98) + 32 * 188.2 * 2 + 140 * 22 * 2
    area_met_lopatka = (height + 1.28) * (width + 7.28)
    # Расчёт "голой" стоимости металла, стоимости реза и стоимости гиба
    val_bend = cost_bend * len_bend / 1000
    val_cut = len_cut * cost_cut / 1000
    area_met_lopatka /= 1000000
    area_met_korp /= 1000000
    val_met = (area_met_lopatka + area_met_korp) * cost_met

    res = {'width': width, 'height': height, 'quad': area_met_lopatka + area_met_korp, 'cost_met': cost_met,
           'val_met': val_met, 'val_cut': val_cut, 'val_bend': val_bend,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost + val_met) * \
        markup_box + val_cut + val_bend + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_k(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                      cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    res = {'width': width, 'height': height, 'quad': 0, 'cost_met': cost_met,
           'val_met': 0, 'val_cut': 0, 'val_bend': 0,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost) * \
        markup_box + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_k_ei(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                         cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    res = {'width': width, 'height': height, 'quad': 0, 'cost_met': cost_met,
           'val_met': 0, 'val_cut': 0, 'val_bend': 0,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost) * \
        markup_box + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_ls(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                       cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    res = {'width': width, 'height': height, 'quad': 0, 'cost_met': cost_met,
           'val_met': 0, 'val_cut': 0, 'val_bend': 0,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost) * \
        markup_box + cost_work + cost_drive * markup_drive

    return res


def calculate_pdv_2_lk(width, height, cost_met, cost_cut, cost_bend, cost_vata, cost_axis,
                       cost_strip, cost_screw, extra_cost, markup_box, cost_work, cost_drive, markup_drive):
    markup_box = markup_box / 100 + 1
    markup_drive = markup_drive / 100 + 1
    res = {'width': width, 'height': height, 'quad': 0, 'cost_met': cost_met,
           'val_met': 0, 'val_cut': 0, 'val_bend': 0,
           'vata': cost_vata, 'axis': cost_axis, 'strip': cost_strip, 'screw': cost_screw,
           'extra': extra_cost, 'markup_metall': markup_box, 'work': cost_work, 'drive': cost_drive, 'markup_drive': markup_drive}
    res['total'] = (cost_vata + cost_axis + cost_strip + cost_screw + extra_cost) * \
        markup_box + cost_work + cost_drive * markup_drive

    return res


def extract_to_excel(res=dict(), n=int(), name=str(), path=str()):
    wb = xl.Workbook()
    ws = wb.active
    ws['A1'] = 'Сторона А'
    ws['A2'] = str(res['width'])
    ws['B1'] = 'Сторона B'
    ws['B2'] = str(res['height'])
    ws['C1'] = 'Квадратура клапана'
    ws['C2'] = str(res['quad'])
    ws['D1'] = 'Стоимость металла [м2]'
    ws['D2'] = str(res['cost_met'])
    ws['E1'] = 'Стоимость железа за коробку клапана'
    ws['E2'] = str(res['val_met'])
    ws['F1'] = 'Стоимость резки'
    ws['F2'] = str(res['val_cut'])
    ws['G1'] = 'Стоимость гиба'
    ws['G2'] = str(res['val_bend'])
    ws['H1'] = 'Стоимость ваты'
    ws['H2'] = str(res['vata'])
    ws['I1'] = 'Стоимость оси(-ей)'
    ws['I2'] = str(res['axis'])
    ws['J1'] = 'Стоимость ленты'
    ws['J2'] = str(res['strip'])
    ws['K1'] = 'Стоимость крепежа'
    ws['K2'] = str(res['screw'])
    ws['L1'] = 'Дополнительные расходы'
    ws['L2'] = str(res['extra'])
    ws['M1'] = 'Наценка на корпус клапана'
    ws['M2'] = str(round((res['markup_metall'] - 1) * 100, 2)) + '%'
    ws['N1'] = 'Стоимость работ'
    ws['N2'] = str(res['work'])
    ws['O1'] = 'Стоимость привода'
    ws['O2'] = str(res['drive'])
    ws['P1'] = 'Наценка на привод'
    ws['P2'] = str(round((res['markup_drive'] - 1) * 100, 2)) + '%'
    ws['Q1'] = 'Итоговая стоимость'
    ws['Q2'] = str(res['total'])
    print(path + '\\' + name + '.xlsx')
    wb.save(os.path.join(path, name + ".xlsx"))
    return name + '.xlsx'


# res = {'width': 0, 'height': 1, 'quad': 2, 'cost_met': 3,
#        'val_met': 4, 'val_cut': 5, 'val_bend': 6,
#        'vata': 7, 'axis': 8, 'strip': 9, 'screw': 10,
#        'extra': 11, 'markup_metall': 1.2, 'work': 13, 'drive': 14, 'markup_drive': 1.5}
# res['total'] = 16

# extract_to_excel(res, 1, 'jopa', 'D:\Загрузки\Telegram Desktop')
