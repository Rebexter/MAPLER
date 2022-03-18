# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mapler.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem as WidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 893)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        ###
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(60, 40, 631, 211))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setRowCount(7)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(80)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0,140)
        self.tableWidget.setColumnWidth(1,320)
        self.tableWidget.setItem(0, 0, WidgetItem("Name"))
        self.tableWidget.setItem(1, 0, WidgetItem("Vorname"))
        self.tableWidget.setItem(2, 0, WidgetItem("Matr. Nummer"))
        self.tableWidget.setItem(3, 0, WidgetItem("Tel. (Optional)"))
        self.tableWidget.setItem(4, 0, WidgetItem("Mail"))
        self.tableWidget.setItem(5, 0, WidgetItem("Straße, Hausnummer"))
        self.tableWidget.setItem(6, 0, WidgetItem("PLZ, Ort"))
        ###
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(60, 260, 631, 211))
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(True)
        self.tableWidget_2.verticalHeader().setMinimumSectionSize(29)
        ###
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1099, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
