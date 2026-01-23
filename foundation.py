from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import ad_forms, os, json
from PySide6.QtGui import QFont
from form import Ui_Form


class AdsModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self,None)
        self.spisok=[8,9,7,5,2,3,6,8,4,2,7,1]
    def rowCount(self, /, parent=...):
        return len(self.spisok)

    def columnCount(self, /, parent=...):
        return 2

    def headerData(self, section, orientation, /, role=...):
        if role != Qt.ItemDataRole.DisplayRole:
            return
        return 'E'

    def data(self, index:QModelIndex, /, role=...):
        if role == Qt.ItemDataRole.FontRole:
            font = QFont()
            font.setPointSize(20)
            return font
        if role == Qt.ItemDataRole.DisplayRole and index.column()==0:
            return self.spisok[index.row()]
        if role == Qt.ItemDataRole.DisplayRole and index.column() == 1:
            spsk=self.spisok[index.row()]
            return spsk*spsk
        return


    def selling_loader():
        selling = open(os.path.dirname(__file__) + '\\selling.json', "r+")
        # print(json.load(selling))
        timed_spisok = json.load(selling)
        id = timed_spisok['next_ID']
        timed_spisok = timed_spisok['ADS']
        selling.close()
        return timed_spisok, id


def selling_unloader():
    for i in timed_spisok:
        last_row = model.rowCount()
        model.insertRow(last_row)
        for o in i:
            model.setData(model.index(last_row, int(o)), i[o])
