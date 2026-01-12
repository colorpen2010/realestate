from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QButtonGroup
from form import Ui_Form
import json

slovar2 = {}
slovar = {0: "Жилое", 1: "Коммерция"}
for i in slovar:
    slovar2[slovar[i]] = i


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
        self.rid = None

    def ad_opener(self):
        self.ui_adform.add_new.setText('add new')
        self.adform.show()
        self.ui_adform.price_line.clear()
        self.ui_adform.address_line.clear()
        self.ui_adform.descruption.clear()
        self.rid = None

    def ad_editor(self, price, address, type, descruption, rid):
        self.ui_adform.add_new.setText('save')
        self.adform.show()
        self.ui_adform.price_line.setText(price)
        self.ui_adform.address_line.setText(address)
        self.ui_adform.descruption.setText(descruption)
        self.group.button(slovar2[type]).setChecked(True)
        self.rid = rid

    def adder(self):
        self.deff(slovar[self.group.checkedId()], self.ui_adform.price_line.text(), self.ui_adform.address_line.text(),self.ui_adform.descruption.toPlainText(),self.rid)

        self.adform.close()
