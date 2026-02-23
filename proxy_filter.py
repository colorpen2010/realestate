from PySide6.QtCore import QSortFilterProxyModel

class NumberFilter(QSortFilterProxyModel):

    def priceFilter(self,price, column):
        self.price=price


    def filterAcceptsRow(self, source_row, source_parent, /):
        index=self.sourceModel().index(source_row, 1)

        if index.data() <= self.price:
            return True
        return False