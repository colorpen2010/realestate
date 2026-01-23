from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import ad_forms, os, json
import foundation
from user_window import Ui_MainWindow
from form import Ui_Form

ui_window = Ui_MainWindow()
app = QApplication()
window = QMainWindow()

ui_window.setupUi(window)

ads_fond=foundation.AdsModel()
ui_window.tableView.setModel(ads_fond)
# timed_spisok, id = foundation.Aselling_loader()

window.show()
app.exec()
