from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel, QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import QUrl, QModelIndex, QTime, QDate

import ad_forms
from mainwindow import Ui_MainWindow
from form import Ui_Form


def add_ad(type, cost, address,tec_row=None):
    global id
    if tec_row!=None:
        last_row=tec_row
    else:
        last_row = model.rowCount()
        model.insertRow(last_row)
        model.setData(model.index(last_row, 4), id)
        id+=1
    print(last_row)
    model.setData(model.index(last_row, 0), type)
    model.setData(model.index(last_row, 1), cost)
    model.setData(model.index(last_row, 2), address)


def edit_ad():
    tec_row = ui_window.tableWidget.currentRow()
    if tec_row == -1:
        return
    type = model.data(model.index(tec_row, 0))
    cost = model.data(model.index(tec_row, 1))
    address = model.data(model.index(tec_row, 2))
    ad_form.ad_editor(cost, address, type, tec_row)


# model=QStandardItemModel(0, 3)
ui_window = Ui_MainWindow()
app = QApplication()
window = QMainWindow()
ad_form = ad_forms.Ad_form(add_ad)
id=0

ui_window.setupUi(window)
ui_window.addnew_form.clicked.connect(ad_form.ad_opener)
ui_window.tableWidget.doubleClicked.connect(lambda: print(model.data(ui_window.tableWidget.currentIndex())))
ui_window.editor_button.clicked.connect(edit_ad)

ui_window.tableWidget.hideColumn(3)
# ui_window.tableWidget.hideColumn(4)

model = ui_window.tableWidget.model()

ui_window.tableWidget.setColumnWidth(0, 150)
ui_window.tableWidget.setColumnWidth(1, 150)
ui_window.tableWidget.setColumnWidth(2, 150)

add_ad('Жилое', '9837.38', 'Planet_Core')
add_ad('Коммерция', '87354.83', '1001 km from Earth')

window.show()
app.exec()
