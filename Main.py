from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl, QModelIndex, QTime, QDate

import ad_forms
from mainwindow import Ui_MainWindow
from form import Ui_Form

def add_ad(type,cost,address):
    last_row=model.rowCount()
    model.insertRow(last_row)
    model.setData(model.index(last_row,0),type)
    model.setData(model.index(last_row,1),cost)
    model.setData(model.index(last_row,2),address)
    # model.removeRow()
# model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
app=QApplication()
window=QMainWindow()
ad_form=ad_forms.Ad_form()

ui_window.setupUi(window)
ui_window.addnew_form.clicked.connect(ad_form.ad_opener)

model=ui_window.tableWidget.model()

ui_window.tableWidget.setColumnWidth(0, 150)
ui_window.tableWidget.setColumnWidth(1, 150)
ui_window.tableWidget.setColumnWidth(2, 150)


add_ad('Жилой','9837.38','Planet_Core')
add_ad('Коммерция','87354.83','1001 km from Earth')

window.show()
app.exec()