from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

import ad_forms
from user_window import Ui_MainWindow
from form import Ui_Form

ui_window = Ui_MainWindow()
app = QApplication()
window = QMainWindow()

ui_window.setupUi(window)

window.show()
app.exec()
