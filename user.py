from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSortFilterProxyModel, Qt
import ad_forms, os, json
import foundation, proxy_filter
from user_window import Ui_MainWindow
from form import Ui_Form

filtr=proxy_filter.NumberFilter()
ui_window = Ui_MainWindow()
app = QApplication()
window = QMainWindow()

ui_window.setupUi(window)

def adrs(text,type):
    filtr.setFilterKeyColumn(type)
    filtr.setFilterFixedString(text)

ads_fond=foundation.AdsModel()
filtr.setSourceModel(ads_fond)
filtr.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
ui_window.tableView.setModel(filtr)
ui_window.Price.textChanged.connect(lambda text: adrs(text,1))
# ui_window.Address.textChanged.connect(lambda text: adrs(text,2))
# ui_window.descruption.textChanged.connect(lambda text: adrs(text,3))



# timed_spisok, id = foundation.Aselling_loader()

window.show()
app.exec()
