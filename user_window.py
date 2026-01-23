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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QHeaderView, QLineEdit,
    QMainWindow, QMenuBar, QRadioButton, QSizePolicy,
    QStatusBar, QTableView, QWidget)

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
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(320, 90, 113, 22))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(100, 90, 113, 22))
        self.doubleSpinBox = QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setGeometry(QRect(540, 90, 81, 22))
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setMaximum(10000000.000000000000000)
        self.doubleSpinBox.setSingleStep(10.000000000000000)
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(60, 120, 681, 401))
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
        self.both_types.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.commercial_type.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.living_type.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
    # retranslateUi

