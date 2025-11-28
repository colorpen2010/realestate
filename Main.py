from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtGui import QPixmap, QPen, QStandardItemModel,QStandardItem
from PySide6.QtMultimedia import QSoundEffect, QMediaPlayer
from PySide6.QtCore import  QUrl, QModelIndex, QTime, QDate
from mainwindow import Ui_MainWindow
from form import Ui_Form


model=QStandardItemModel(0, 3)
ui_window=Ui_MainWindow()
ui_adform=Ui_Form()
app=QApplication()
window=QMainWindow()
adform=QWidget()


ui_window.setupUi(window)
ui_adform.setupUi(adform)
ui_window.addnew_form.clicked.connect(adform.show)

window.show()
app.exec()