from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem
from PyQt5.QtCore import QTimer
import sys
from main import *
import os
from datetime import datetime
import json
import pics


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.params_list = ['width', 'height', 'cost_met', 'cost_cut', 'cost_bend', 'cost_vata', 'cost_axis', 'num_axis',
                            'cost_strip', 'cost_screw', 'extra_cost', 'markup_box', 'cost_work', 'cost_drive', 'markup_drive', 'additional',
                            'cost_warm_cable', 'cost_warm_work', 'quantity']
        self.general_params_list = ['name_1', 'name_2', 'limit_fire_resistance', 'no_nz', 'actuator', 'additional_key']
        self.cost_screw_data = []
        self.positions = []
        self.setWindowTitle('Manager calculator')
        self.clear_params.clicked.connect(self.clear)
        self.calc_total.clicked.connect(self.make_total)
        self.make_excel.clicked.connect(self.save_project)
        self.add_position_btn.clicked.connect(self.add_position)
        self.calc_screw_btn.clicked.connect(self.open_secondary_window)
        self.extract_to_kp.clicked.connect(self.save_kp)
        self.secondary_window = None

        self.load_session()

        self.timer = QTimer()
        self.timer.timeout.connect(self.save_session_params)
        self.timer.start(10000)

        self.show()

    def save_project(self):
        dialog = QFileDialog(self)
        name = dialog.getSaveFileName(self, 'Save File')[0]
        path = os.path.split(name)
        extract_to_excel(res=self.positions, name=path[1], path=path[0])
        self.add_log(f'Сохранено в файл: "{name}"')
        self.positions = []
        self.add_log('Все позиции удалены')
        self.save_session_params()

    def save_kp(self):
        dialog = QFileDialog(self)
        name = dialog.getSaveFileName(self, 'Save KP')[0]
        path = os.path.split(name)
        extract_to_kp(res=self.positions, name=path[1], path=path[0])
        self.add_log(f'Сохранено в файл: "{name}"')
        self.positions = []
        self.add_log('Все позиции удалены')
        self.save_session_params()

    def choose_method(self):
        methods = {'calculate_pdv_1_pr': calculate_pdv_1_pr,
                   'calculate_pdv_1_kr': calculate_pdv_1_kr,
                   'calculate_pdv_2_s_ei': calculate_pdv_2_s_ei,
                   'calculate_pdv_2_s': calculate_pdv_2_s,
                   'calculate_pdv_2_k': calculate_pdv_2_k,
                   'calculate_pdv_2_ls': calculate_pdv_2_ls,
                   'calculate_pdv_2_lk': calculate_pdv_2_lk,
                   'calculate_pdv_2_k_ei': calculate_pdv_2_k_ei,
                   'calculate_pdv_1_kr_ei150': calculate_pdv_1_kr_ei150,
                   'calculate_pdv_1_pr_ei150': calculate_pdv_1_pr_ei150,
                   }
        name_2 = self.name_2.currentText()
        limit_fire_resistance = self.limit_fire_resistance.currentText()
        no_nz = self.no_nz.currentText()
        actuator = self.actuator.currentText()
        additional_key = self.additional_key.currentText()
        height = self.height.text()
        width = self.width.text()
        if additional_key:
            additional_key_name = ' ' + additional_key
        else:
            additional_key_name = ''
        if name_2 == 'ПДВ-1 (Пр)':
            if limit_fire_resistance == 'EI150':
                return methods['calculate_pdv_1_pr_ei150'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            else:
                return methods['calculate_pdv_1_pr'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-1 (Кр)':
            if height and not width:
                if limit_fire_resistance == 'EI150':
                    return methods['calculate_pdv_1_kr_ei150'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{height}-{actuator}{additional_key_name}'
                else:
                    return methods['calculate_pdv_1_kr'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{height}-{actuator}{additional_key_name}'
            elif not height and width:
                if limit_fire_resistance == 'EI150':
                    return methods['calculate_pdv_1_kr_ei150'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{width}-{actuator}{additional_key_name}'
                else:
                    return methods['calculate_pdv_1_kr'], f'Клапан противопожарный ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{width}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2-К':
            if (limit_fire_resistance == 'EI90') or (limit_fire_resistance == 'EI150'):
                return methods['calculate_pdv_2_k_ei'], f'Клапан противопожарный ПДВ-2-К ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            elif (limit_fire_resistance == 'E90') or (limit_fire_resistance == 'E150'):
                return methods['calculate_pdv_2_k'], f'Клапан противопожарный ПДВ-2-К ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2-С':
            if (limit_fire_resistance == 'EI90') or (limit_fire_resistance == 'EI150'):
                return methods['calculate_pdv_2_s_ei'], f'Клапан противопожарный ПДВ-2-С ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            elif (limit_fire_resistance == 'E90') or (limit_fire_resistance == 'E150'):
                return methods['calculate_pdv_2_s'], f'Клапан противопожарный ПДВ-2-С ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2-Л-К':
            return methods['calculate_pdv_2_lk'], f'Клапан противопожарный ПДВ-2-Л-К ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2-Л-С':
            return methods['calculate_pdv_2_ls'], f'Клапан противопожарный ПДВ-2-Л-С ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'

        self.add_log('Недопустимые параметры')
        return None, None

    def get_params(self):
        params_dict = {}
        for param in self.params_list:
            value = getattr(self, param).text()
            if value == '':
                params_dict[param] = 0
            else:
                try:
                    params_dict[param] = float(value.replace(',', '.'))
                except:
                    params_dict[param] = 0
        if self.additional_key.currentText() in ['МС', 'МС-К']:
            params_dict['ms'] = True
        else:
            params_dict['ms'] = False
        return params_dict

    def save_session_params(self):
        try:
            session_data = {}
            for param in self.params_list:
                session_data[param] = getattr(self, param).text()

            for param in self.general_params_list:
                session_data[param] = getattr(self, param).currentText()

            session_data['cost_screw_data'] = self.cost_screw_data

            with open('session.json', 'w') as file:
                json.dump(session_data, file, ensure_ascii=False)
        except:
            pass

    def load_session(self):
        try:
            with open('session.json', 'r') as file:
                data = json.load(file)
                for param in self.params_list:
                    obj = getattr(self, param)
                    obj.setText(data[param])

                for param in self.general_params_list:
                    obj = getattr(self, param)
                    obj.setCurrentText(data[param])

                self.cost_screw_data = data['cost_screw_data']
        except:
            pass

    def clear(self):
        for param in self.params_list:
            getattr(self, param).clear()

    def make_total(self):
        method, name = self.choose_method()
        if method:
            try:
                res = method(**self.get_params())
                self.total.setText(str(float('{:.2f}'.format(res['total']))))
                self.add_log('Расчёт произведён')
            except:
                self.add_log('Недопустимые параметры')
        self.save_session_params()

    def add_position(self):
        method, file_name = self.choose_method()
        if method:
            try:
                res = method(**self.get_params())
                res.update({'name': file_name})
                self.positions.append(res)
                self.add_log('Добавлено ' + f'"{file_name}"')
            except:
                self.add_log('Недопустимые параметры')
        self.save_session_params()

    def add_log(self, message):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.log_area.addItem(f'[{current_time}] ' + message)

    def open_secondary_window(self):
        if not self.secondary_window:
            self.secondary_window = SecondaryWindow(self)
        self.secondary_window.show()

    def set_cost_screw_data(self, cost_screw_data):
        self.cost_screw_data = cost_screw_data


class SecondaryWindow(QtWidgets.QWidget):
    def __init__(self, main_window):
        super(SecondaryWindow, self).__init__()
        uic.loadUi('cost_screw_window.ui', self)
        self.setWindowTitle('Расчёт стоимости крепежа')
        self.main_window = main_window

        try:
            self.array_to_table(self.main_window.cost_screw_data)
        except:
            pass

        self.add_row_btn.clicked.connect(self.add_row)
        self.del_row_btn.clicked.connect(self.delete_row)
        self.calc_btn.clicked.connect(self.calc_screw_cost)
        self.clear_btn.clicked.connect(self.clear_table)
        self.cost_screw_input = self.main_window.cost_screw

    def add_row(self):
        row_position = self.screw_table.rowCount()
        self.screw_table.insertRow(row_position)

    def delete_row(self):
        self.screw_table.removeRow(self.screw_table.rowCount()-1)

    def clear_table(self):
        row_count = self.screw_table.rowCount()
        for row in range(row_count):
            for i in range(3):
                if self.screw_table.item(row, i):
                    self.screw_table.item(row, i).setText('')

    def calc_screw_cost(self):
        row_count = self.screw_table.rowCount()
        cost = 0
        for row in range(row_count):
            if (self.screw_table.item(row, 2)) and (self.screw_table.item(row, 1)):
                if is_number(self.screw_table.item(row, 2).text()) and is_number(self.screw_table.item(row, 1).text()):
                    cost = cost + float(self.screw_table.item(row, 1).text().replace(
                        ',', '.'))*float(self.screw_table.item(row, 2).text().replace(',', '.'))
        self.cost_screw_input.setText(str(cost))
        self.main_window.set_cost_screw_data(self.table_to_array())
        self.main_window.save_session_params()

    def table_to_array(self):
        table_data = []
        for row in range(self.screw_table.rowCount()):
            row_data = []
            for column in range(self.screw_table.columnCount()):
                if self.screw_table.item(row, column):
                    row_data.append(self.screw_table.item(row, column).text())
                else:
                    row_data.append('')
            table_data.append(row_data)
        return table_data

    def array_to_table(self, table_data):
        self.screw_table.setColumnCount(len(table_data[0]))
        self.screw_table.setRowCount(len(table_data))
        for row in range(self.screw_table.rowCount()):
            for column in range(self.screw_table.columnCount()):
               self.screw_table.setItem(row, column,  QTableWidgetItem(str(table_data[row][column])))


def is_number(line: str):
    try:
        float(line.replace(',', '.'))
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.exec_()
