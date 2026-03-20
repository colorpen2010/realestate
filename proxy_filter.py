from PySide6.QtCore import QSortFilterProxyModel


class NumberFilter(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self.price = 0
        self.pattern = None
        self.adrs_pattern = None
        self.desc_pattern = None
        self.type_pattern = None

    def setFilterFixedint(self, price):
        self.price = price
        self.column = 1
        self.modelReset.emit()

    def setFilterFixedString(self, pattern, /, column):
        self.column = column
        if column == 3:
            self.desc_pattern = pattern
        elif self.column == 2:
            self.adrs_pattern = pattern
        elif self.column == 0:
            self.type_pattern = pattern
        self.modelReset.emit()

    def filterAcceptsRow(self, source_row, source_parent, /):
        price_filtr = False
        adrs_filtr = False
        desc_filtr = False
        type_filtr = False
        for o in range(0, 4):
            index = self.sourceModel().index(source_row, o)
            if o == 0:
                if self.type_pattern is None or self.type_pattern == 0:
                    type_filtr = True
                elif self.type_pattern == 2 and "жилое" in index.data().lower():
                    type_filtr = True
                elif self.type_pattern == 1 and "коммерция" in index.data().lower():
                    type_filtr = True
            elif o == 1 and index.data().isnumeric():
                if int(self.price) == 0:
                    price_filtr = True
                elif int(index.data()) <= int(self.price):
                    price_filtr = True
            elif o == 2:
                if self.adrs_pattern is None:
                    adrs_filtr = True
                elif self.adrs_pattern.lower() in index.data().lower():
                    adrs_filtr = True
            elif o == 3:
                if self.desc_pattern is None:
                    desc_filtr = True
                elif self.desc_pattern.lower() in index.data().lower():
                    desc_filtr = True

            if price_filtr == True and adrs_filtr == True and desc_filtr == True and type_filtr==True:
                return True
        return False
