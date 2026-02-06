from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import ad_forms, os, json
from PySide6.QtGui import QFont
from form import Ui_Form


class AdsModel(QAbstractTableModel):
    def __init__(self):
        QAbstractTableModel.__init__(self, None)
        self.spisok, self.id = self.selling_loader()
        print(self.spisok)
        self.colonki = {0: 'Type', 1: 'Cost', 2: 'Address', 3: 'Descruption', 4: 'ID'}
        print(self.spisok)

    def rowCount(self, /, parent=...):
        return len(self.spisok)

    def columnCount(self, /, parent=...):
        return 5

    def insertRow(self, row, /, parent=...):
        slovar = {"0": '', "1": '', "2": '', "3": '', "4": ''}
        self.spisok.append(slovar)
        self.modelReset.emit()

    def headerData(self, section, orientation, /, role=...):
        if role == Qt.ItemDataRole.DisplayRole and orientation == Qt.Orientation.Horizontal:
            return self.colonki[section]

    def data(self, index: QModelIndex, /, role=...):
        if role == Qt.ItemDataRole.FontRole:
            font = QFont()
            font.setPointSize(10)
            return font
        if role == Qt.ItemDataRole.DisplayRole and index.column() == 0:
            return self.spisok[index.row()]['0']
        if role == Qt.ItemDataRole.DisplayRole and index.column() == 1:
            return self.spisok[index.row()]['1']
        if role == Qt.ItemDataRole.DisplayRole and index.column() == 2:
            return self.spisok[index.row()]['2']
        return

    def setData(self, index, value, /, role=...):
        self.spisok[index.row()][str(index.column())] = value
        self.saver()
        return True

    def flags(self, index, /):
        return Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable

    @staticmethod
    def selling_loader():
        selling = open(os.path.dirname(__file__) + '\\selling.json', "r+")
        # print(json.load(selling))
        timed_spisok = json.load(selling)
        id = timed_spisok['next_ID']
        timed_spisok: list = timed_spisok['ADS']
        selling.close()
        return timed_spisok, id

    def saver(self):
        kenobi_file_manager = {}
        ads = []
        for a in range(self.rowCount()):
            slovar3 = {}
            for o in range(self.columnCount()):
                slovar3[o] = self.data(self.index(a, o), role=Qt.ItemDataRole.DisplayRole)
            ads.append(slovar3)

        kenobi_file_manager['next_ID'] = self.id
        kenobi_file_manager['ADS'] = ads
        selling = open(os.path.dirname(__file__) + '\\selling.json', "w+")
        json.dump(kenobi_file_manager, selling, indent=4)
        selling.close()
