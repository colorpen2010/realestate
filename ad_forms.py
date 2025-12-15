from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QButtonGroup
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel, QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import QUrl, QModelIndex, QTime, QDate
from mainwindow import Ui_MainWindow
from form import Ui_Form
slovar2={}
slovar = {0: "Жилое", 1: "Коммерция"}
for i in slovar:
    slovar2[slovar[i]]=i

class Ad_form():
    def __init__(self, add_ad):
        self.group = QButtonGroup()

        self.deff = add_ad
        self.ui_adform = Ui_Form()
        self.adform = QWidget()
        self.ui_adform.setupUi(self.adform)
        self.ui_adform.add_new.clicked.connect(self.adder)
        self.ui_adform.cancel.clicked.connect(self.adform.close)
        self.group.addButton(self.ui_adform.rb_residence, 0)
        self.group.addButton(self.ui_adform.rb_commercial, 1)
        self.tec_row=None

    def ad_opener(self):
        self.ui_adform.add_new.setText('add new')
        self.adform.show()
        self.ui_adform.price_line.clear()
        self.ui_adform.address_line.clear()
        self.tec_row=None

    def ad_editor(self, price, address, type, tec_row):
        self.ui_adform.add_new.setText('save')
        self.adform.show()
        self.ui_adform.price_line.setText(price)
        self.ui_adform.address_line.setText(address)
        self.group.button(slovar2[type]).setChecked(True)
        self.tec_row=tec_row

    def adder(self):
        self.deff(slovar[self.group.checkedId()], self.ui_adform.price_line.text(), self.ui_adform.address_line.text(),self.tec_row)
        self.adform.close()