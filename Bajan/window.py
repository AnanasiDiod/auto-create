from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QFileDialog
import sys
from main import *  # calculate_pdv_1_pr, calculate_pdv_1_kr, calculate_pdv_2_s_ei, calculate_pdv_2_s, calculate_pdv_2_k, calculate_pdv_2_ls, calculate_pdv_2_lk, extract_to_excel
import os


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main_window.ui', self)
        self.params_list = ['width', 'height', 'cost_met', 'cost_cut', 'cost_bend', 'cost_vata', 'cost_axis',
                            'cost_strip', 'cost_screw', 'extra_cost', 'markup_box', 'cost_work', 'cost_drive', 'markup_drive', 'additional']
        self.setWindowTitle('Manager calculator')
        self.clear_params.clicked.connect(self.clear)
        self.calc_total.clicked.connect(self.make_total)
        self.make_excel.clicked.connect(self.save_project)

        self.show()

    def save_project(self):
        method, file_name = self.choose_method()
        dialog = QFileDialog(self)
        name = dialog.getSaveFileName(self, 'Save File', file_name)[0]
        path = os.path.split(name)
        res = method(**self.get_params())
        extract_to_excel(res=res, name=path[1], path=path[0])

    def choose_method(self):
        methods = {'calculate_pdv_1_pr': calculate_pdv_1_pr,
                   'calculate_pdv_1_kr': calculate_pdv_1_kr,
                   'calculate_pdv_2_s_ei': calculate_pdv_2_s_ei,
                   'calculate_pdv_2_s': calculate_pdv_2_s,
                   'calculate_pdv_2_k': calculate_pdv_2_k,
                   'calculate_pdv_2_ls': calculate_pdv_2_ls,
                   'calculate_pdv_2_lk': calculate_pdv_2_lk,
                   'calculate_pdv_2_k_ei': calculate_pdv_2_k_ei,
                   }
        name_1 = self.name_1.currentText()
        name_2 = self.name_2.currentText()
        limit_fire_resistance = self.limit_fire_resistance.currentText()
        no_nz = self.no_nz.currentText()
        actuator = self.actuator.currentText()
        cut = self.cut.text()
        additional_key = self.additional_key.currentText()
        height = self.height.text()
        width = self.width.text()
        if additional_key:
            additional_key_name = ' ' + additional_key
        else:
            additional_key_name = ''
        if name_2 == 'ПДВ-1':
            if height and width:
                return methods['calculate_pdv_1_pr'], f'ПДВ-1 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            elif height and not width:
                return methods['calculate_pdv_1_kr'], f'ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{height}-{actuator}{additional_key_name}'
            elif not height and width:
                return methods['calculate_pdv_1_kr'], f'ПДВ-1 ({limit_fire_resistance})-{no_nz} ф{width}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2':
            if (limit_fire_resistance == 'EI90') or (limit_fire_resistance == 'EI150'):
                if additional_key == 'K':
                    return methods['calculate_pdv_2_k_ei'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
                elif additional_key == '':
                    return methods['calculate_pdv_2_s_ei'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            elif (limit_fire_resistance == 'E90') or (limit_fire_resistance == 'E150'):
                if additional_key == 'K':
                    return methods['calculate_pdv_2_k'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
                elif additional_key == '':
                    return methods['calculate_pdv_2_s'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
        elif name_2 == 'ПДВ-2-Л':
            if additional_key == 'K':
                return methods['calculate_pdv_2_lk'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
            elif additional_key == '':
                return methods['calculate_pdv_2_ls'], f'ПДВ-2 ({limit_fire_resistance})-{no_nz} {width}х{height}-{actuator}{additional_key_name}'
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
        return params_dict

    def clear(self):
        for param in self.params_list:
            getattr(self, param).clear()

    def make_total(self):
        method, name = self.choose_method()
        res = method(**self.get_params())
        self.total.setText(str(float('{:.2f}'.format(res['total']))))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    app.exec_()
