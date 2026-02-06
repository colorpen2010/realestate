import json
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import ad_forms, os
from admin_window import Ui_MainWindow
from form import Ui_Form
import foundation


def add_ad(type, cost, address,descruption, rid=None):
    global id
    if rid != None:
        last_row = yoda(rid)
        # id=model.data()
    else:
        last_row = model.rowCount()
        model.insertRow(last_row)
        model.setData(model.index(last_row, 4), id)
        id += 1
    if last_row==-1:
        print("ia ne mogy rabotat v takix ysloviax")
        return
    model.setData(model.index(last_row, 0), type)
    model.setData(model.index(last_row, 1), cost)
    model.setData(model.index(last_row, 2), address)
    model.setData(model.index(last_row,3), descruption)


def yoda(id):
    winner=-1
    for o in range(model.rowCount()):
        id_candidate = model.data(model.index(o, 4))
        # print(id_candidate)
        if id_candidate == id:
            winner=o
    return winner





def edit_ad():
    tec_row = ui_window.tableView.currentRow()
    if tec_row == -1:
        return
    type = model.data(model.index(tec_row, 0))
    cost = model.data(model.index(tec_row, 1))
    address = model.data(model.index(tec_row, 2))
    desc= model.data(model.index(tec_row,3))
    rid = model.data(model.index(tec_row, 4))
    ad_form.ad_editor(cost, address, type,desc, rid)


# model=QStandardItemModel(0, 3)
ui_window = Ui_MainWindow()
app = QApplication()
window = QMainWindow()
ad_form = ad_forms.Ad_form(add_ad)
id = 0

ui_window.setupUi(window)
ui_window.addnew_form.clicked.connect(ad_form.ad_opener)
ui_window.tableView.doubleClicked.connect(lambda: print(model.data(ui_window.tableView.currentIndex())))
ui_window.editor_button.clicked.connect(edit_ad)


ui_window.tableView.setModel(foundation.AdsModel())
model:foundation.AdsModel = ui_window.tableView.model()
# timed_spisok,id=model.selling_loader()
# print(timed_slovar)

ui_window.tableView.hideColumn(3)
ui_window.tableView.hideColumn(4)

ui_window.tableView.setColumnWidth(0, 150)
ui_window.tableView.setColumnWidth(1, 150)
ui_window.tableView.setColumnWidth(2, 150)

# add_ad('Жилое', '9837.38', 'Planet_Core')
# add_ad('Коммерция', '87354.83', '1001 km from Earth')

window.show()
app.exec()
