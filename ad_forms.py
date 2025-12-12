from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl, QModelIndex, QTime, QDate
from mainwindow import Ui_MainWindow
from form import Ui_Form

class Ad_form():
    def __init__(self):
        # self.deff=add_ad
        self.ui_adform = Ui_Form()
        self.adform = QWidget()
        self.ui_adform.setupUi(self.adform)
        self.ui_adform.add_new.clicked.connect(self.adder)
        self.ui_adform.cancel.clicked.connect(self.adform.close)
    def ad_opener(self):

        self.adform.show()
    def adder(self):
        self.adform.close()
        print(1)