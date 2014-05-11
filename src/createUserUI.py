# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../CreateUserUI.ui'
#
# Created: Mon May  5 01:50:03 2014
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(1247, 736)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(200, 200))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formWidget = QtWidgets.QWidget(self.centralwidget)
        self.formWidget.setGeometry(QtCore.QRect(240, 90, 431, 261))
        self.formWidget.setObjectName("formWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formWidget)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.FieldsStayAtSizeHint)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.aliasLabel = QtWidgets.QLabel(self.formWidget)
        self.aliasLabel.setObjectName("aliasLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.aliasLabel)
        self.aliasLineEdit = QtWidgets.QLineEdit(self.formWidget)
        self.aliasLineEdit.setObjectName("aliasLineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.aliasLineEdit)
        self.reTypePasswordLineEdit = QtWidgets.QLineEdit(self.formWidget)
        self.reTypePasswordLineEdit.setObjectName("reTypePasswordLineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reTypePasswordLineEdit)
        self.reTypePasswordLabel = QtWidgets.QLabel(self.formWidget)
        self.reTypePasswordLabel.setObjectName("reTypePasswordLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.reTypePasswordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.formWidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwordLineEdit)
        self.passwordLabel = QtWidgets.QLabel(self.formWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.passwordLabel)
        self.usernameLineEdit = QtWidgets.QLineEdit(self.formWidget)
        self.usernameLineEdit.setObjectName("usernameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.usernameLineEdit)
        self.usernameLabel = QtWidgets.QLabel(self.formWidget)
        self.usernameLabel.setObjectName("usernameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.usernameLabel)
        self.pushButton = QtWidgets.QPushButton(self.formWidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.lineEdit = QtWidgets.QLineEdit(self.formWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.createUserButton = QtWidgets.QPushButton(self.formWidget)
        self.createUserButton.setObjectName("createUserButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.createUserButton)
        self.exitButton = QtWidgets.QPushButton(self.formWidget)
        self.exitButton.setObjectName("exitButton")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.exitButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1247, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.topToolBar = QtWidgets.QToolBar(MainWindow)
        self.topToolBar.setObjectName("topToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.topToolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.aliasLabel.setText(_translate("MainWindow", "Alias"))
        self.reTypePasswordLabel.setText(_translate("MainWindow", "ReType Password"))
        self.passwordLabel.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">Password</p></body></html>"))
        self.usernameLabel.setText(_translate("MainWindow", "Username"))
        self.pushButton.setText(_translate("MainWindow", "Profile Photo"))
        self.createUserButton.setText(_translate("MainWindow", "Create User"))
        self.exitButton.setText(_translate("MainWindow", "      Exit       "))
        self.topToolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

