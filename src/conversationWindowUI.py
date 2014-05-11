# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/chatWindow.ui'
#
# Created: Sun May 11 00:55:23 2014
#      by: PyQt5 UI code generator 5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(19, 9, 581, 431))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.conversationScrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.conversationScrollArea.setWidgetResizable(True)
        self.conversationScrollArea.setObjectName("conversationScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 272, 427))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.messagesListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.messagesListWidget.setGeometry(QtCore.QRect(-5, 1, 281, 431))
        self.messagesListWidget.setObjectName("messagesListWidget")
        self.conversationScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.conversationScrollArea, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.contactScrollArea = QtWidgets.QScrollArea(self.gridLayoutWidget)
        self.contactScrollArea.setWidgetResizable(True)
        self.contactScrollArea.setObjectName("contactScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 271, 427))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.contactsListWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents_2)
        self.contactsListWidget.setGeometry(QtCore.QRect(0, 0, 271, 431))
        self.contactsListWidget.setObjectName("contactsListWidget")
        self.contactScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.contactScrollArea, 0, 2, 1, 1)
        self.conversationEntry = QtWidgets.QTextEdit(self.centralwidget)
        self.conversationEntry.setGeometry(QtCore.QRect(20, 450, 461, 71))
        self.conversationEntry.setObjectName("conversationEntry")
        self.sendButton = QtWidgets.QPushButton(self.centralwidget)
        self.sendButton.setGeometry(QtCore.QRect(500, 450, 99, 71))
        self.sendButton.setText("")
        self.sendButton.setObjectName("sendButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionToolBar = QtWidgets.QToolBar(MainWindow)
        self.actionToolBar.setObjectName("actionToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.actionToolBar)
        self.statusOptionsToolBar = QtWidgets.QToolBar(MainWindow)
        self.statusOptionsToolBar.setObjectName("statusOptionsToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.statusOptionsToolBar)
        self.actionToolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.actionToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.statusOptionsToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

