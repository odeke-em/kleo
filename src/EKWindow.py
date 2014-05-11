#!/usr/bin/env python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

from PyQt5 import QtWidgets, QtGui, QtCore

class EKWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(EKWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1034, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(self)
        self.toolBar.setObjectName("toolBar")
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

    def close(self):
        print(self, 'closing')
        super().close()
