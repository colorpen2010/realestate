# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client_window.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QRadioButton,
    QSizePolicy, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.both_types = QRadioButton(self.centralwidget)
        self.both_types.setObjectName(u"both_types")
        self.both_types.setGeometry(QRect(630, 90, 89, 20))
        self.commercial_type = QRadioButton(self.centralwidget)
        self.commercial_type.setObjectName(u"commercial_type")
        self.commercial_type.setGeometry(QRect(630, 60, 89, 20))
        self.living_type = QRadioButton(self.centralwidget)
        self.living_type.setObjectName(u"living_type")
        self.living_type.setGeometry(QRect(630, 30, 89, 20))
        self.descruption = QLineEdit(self.centralwidget)
        self.descruption.setObjectName(u"descruption")
        self.descruption.setGeometry(QRect(320, 90, 113, 22))
        self.Address = QLineEdit(self.centralwidget)
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(100, 90, 113, 22))
        self.Price = QDoubleSpinBox(self.centralwidget)
        self.Price.setObjectName(u"Price")
        self.Price.setGeometry(QRect(540, 90, 81, 22))
        self.Price.setDecimals(0)
        self.Price.setMaximum(10000000.000000000000000)
        self.Price.setSingleStep(10.000000000000000)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(60, 120, 681, 401))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 70, 49, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 70, 71, 20))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 70, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.both_types.setText(QCoreApplication.translate("MainWindow", u"Both types", None))
        self.commercial_type.setText(QCoreApplication.translate("MainWindow", u"Commercial", None))
        self.living_type.setText(QCoreApplication.translate("MainWindow", u"Living", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Price", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Descruption", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Address", None))
    # retranslateUi

