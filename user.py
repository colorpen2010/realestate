from PySide6.QtWidgets import QApplication, QMainWindow, QButtonGroup
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
    filtr.setFilterFixedString(text,type)

def nmbrs(text,type):
    filtr.setFilterKeyColumn(type)
    filtr.setFilterFixedint(text)


group=QButtonGroup()
group.addButton(ui_window.both_types,0)
group.addButton(ui_window.commercial_type,1)
group.addButton(ui_window.living_type,2)

ads_fond=foundation.AdsModel()
filtr.setSourceModel(ads_fond)
filtr.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
ui_window.tableView.setModel(filtr)
ui_window.Price.textChanged.connect(lambda text: nmbrs(text,1))
ui_window.Address.textChanged.connect(lambda text: adrs(text,2))
ui_window.descruption.textChanged.connect(lambda text: adrs(text,3))
group.buttonClicked.connect(lambda: print(group.checkedId()))




# timed_spisok, id = foundation.Aselling_loader()

window.show()
app.exec()
