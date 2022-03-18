#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 20:43:49 2022

@author: rbx
"""

from PyQt5.QtCore import QObject
from PyQt5 import QtWidgets, QtCore#, QtGui
from PyQt5.QtWidgets import QTableWidgetItem as WidgetItem
from ui_mapler import Ui_MainWindow  # importing our generated file 
import sys

class mywindow(QtWidgets.QMainWindow, QObject):
    def __init__(self, parent=None):
        super(mywindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #rows = self.ui.tableWidget.rowCount()
        for i in range(1,self.ui.tableWidget.rowCount()):
            self.ui.tableWidget.setItem(i,0,WidgetItem.setFlags(QtCore.Qt.ItemIsEnabled))

        
        
        
def main():        
    app = QtWidgets.QApplication([]) 
    application = mywindow() 
    application.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()