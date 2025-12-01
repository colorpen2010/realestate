# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.add_new = QPushButton(Form)
        self.add_new.setObjectName(u"add_new")
        self.add_new.setGeometry(QRect(0, 270, 75, 24))
        self.cancel = QPushButton(Form)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(100, 270, 75, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(280, 100, 113, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 80, 49, 16))
        self.radioButton = QRadioButton(Form)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(300, 10, 89, 20))
        self.radioButton_2 = QRadioButton(Form)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(300, 40, 89, 20))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 120, 49, 16))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(280, 140, 113, 22))
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 256, 192))
        self.textBrowser.setReadOnly(False)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 0, 61, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_new.setText(QCoreApplication.translate("Form", u"add new", None))
        self.cancel.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0410\u0434\u0440\u0435\u0441", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u0416\u0438\u043b\u043e\u0435", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u043c\u0435\u0440\u0446\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
    # retranslateUi

