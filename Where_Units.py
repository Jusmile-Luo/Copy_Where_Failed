# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Where_Units.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Where_Units(object):
    def setupUi(self, Where_Units):
        Where_Units.setObjectName("Where_Units")
        Where_Units.resize(751, 556)
        self.label = QtWidgets.QLabel(Where_Units)
        self.label.setGeometry(QtCore.QRect(30, 20, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dataTable = QtWidgets.QTableView(Where_Units)
        self.dataTable.setGeometry(QtCore.QRect(30, 130, 701, 411))
        self.dataTable.setObjectName("dataTable")
        self.PNlable = QtWidgets.QLabel(Where_Units)
        self.PNlable.setGeometry(QtCore.QRect(330, 30, 47, 13))
        self.PNlable.setText("")
        self.PNlable.setObjectName("PNlable")
        self.PNedit = QtWidgets.QLineEdit(Where_Units)
        self.PNedit.setGeometry(QtCore.QRect(60, 60, 471, 31))
        self.PNedit.setObjectName("PNedit")
        self.getBtn = QtWidgets.QPushButton(Where_Units)
        self.getBtn.setGeometry(QtCore.QRect(570, 60, 101, 31))
        self.getBtn.setObjectName("getBtn")
        self.line = QtWidgets.QFrame(Where_Units)
        self.line.setGeometry(QtCore.QRect(20, 100, 721, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Where_Units)
        QtCore.QMetaObject.connectSlotsByName(Where_Units)

    def retranslateUi(self, Where_Units):
        _translate = QtCore.QCoreApplication.translate
        Where_Units.setWindowTitle(_translate("Where_Units", "Where_Failed_Component"))
        self.label.setText(_translate("Where_Units", "Please Input Component Part Number:"))
        self.getBtn.setText(_translate("Where_Units", "Get Data"))
