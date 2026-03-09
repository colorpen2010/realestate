from PySide6.QtCore import QSortFilterProxyModel

class NumberFilter(QSortFilterProxyModel):
    def __init__(self):
        QSortFilterProxyModel.__init__(self)
        self.price=0
        self.pattern=None


    def setFilterFixedint(self,price):
        self.price = price
        self.column=1
        self.modelReset.emit()


    def setFilterFixedString(self, pattern, /,column):
        self.column=column
        self.pattern=pattern
        self.modelReset.emit()


    def filterAcceptsRow(self, source_row, source_parent, /):
        price_filtr=False
        adrs_filtr=False
        for o in range(1,4):
            index = self.sourceModel().index(source_row, o)
            if o == 1 and index.data().isnumeric():
                if int(self.price)==0:
                    price_filtr=True
                elif int(index.data()) <= int(self.price):
                    price_filtr= True
            elif o == 2:
                if self.pattern==None:
                    adrs_filtr=True
                elif self.pattern.lower() in index.data().lower():
                    adrs_filtr=True

            if price_filtr==True and adrs_filtr == True:
                return True
        return False