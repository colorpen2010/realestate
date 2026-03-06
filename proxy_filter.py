from PySide6.QtCore import QSortFilterProxyModel

class NumberFilter(QSortFilterProxyModel):

    def setFilterFixedint(self,price):
        self.price = price
        self.column=1
        self.modelReset.emit()


    def setFilterFixedString(self, pattern, /,column):
        self.column=column
        self.pattern=pattern
        self.modelReset.emit()


    def filterAcceptsRow(self, source_row, source_parent, /):
        index=self.sourceModel().index(source_row, self.column)
        if self.column == 1:
            if int(self.price)==0:
                return True
            elif int(index.data()) <= int(self.price):
                return True
        else:
            return self.pattern in index.data()
        return False