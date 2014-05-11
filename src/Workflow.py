#!/usr/bin/python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

import sys
from PyQt5 import QtWidgets, QtGui, QtCore

from CreateUser import UserUI
from LoginUser import LoginUI
from ConversationWindow import ConversationWindow
from DbLiason import  ChatHandler, produceAndParse


import utils

class WorkFlow(QtWidgets.QMainWindow):
    def __init__(self, parent=None, dbHandler=None):
        super(WorkFlow, self).__init__(parent)

        self.__dbHandler = dbHandler
        self.initActions()
        self.initToolBars()

    def initActions(self):
        self.__createNewUserAction = QtWidgets.QAction(
            QtGui.QIcon('icons/iconmonstr-newuser.png'), '&New User', self
        )
        self.__createNewUserAction.triggered.connect(self.createNewUser)

        self.__loginAction = QtWidgets.QAction(
            QtGui.QIcon('icons/iconmonstr-key.png'), '&Login', self
        )
        self.__loginAction.triggered.connect(self.login)

        self.__exitAction = QtWidgets.QAction(
            QtGui.QIcon('icons/iconmonstr-exit.png'), '&Exit', self
        )
        self.__exitAction.triggered.connect(self.close)
 
    def initToolBars(self):
        self.statusToolBar = QtWidgets.QToolBar(self)
        self.statusToolBar.addAction(self.__loginAction)
        self.statusToolBar.addAction(self.__createNewUserAction)
        self.statusToolBar.addAction(self.__exitAction)
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.statusToolBar)
       
    def login(self):
        self.__loginUI = LoginUI(
            self.__dbHandler, self.receiveLoggedInCredentials
        )

    def createNewUser(self):
        self.__newUserUI = UserUI(
            self.__dbHandler, None, self.receiveCreatedUser
        )

    def receiveCreatedUser(self, createdUser, srcWidget):
        print('createdUser', createdUser, srcWidget)
        return self.receiveLoggedInCredentials(createdUser, srcWidget)

    def receiveLoggedInCredentials(self, credDict, srcWidget):
        if credDict:
            if hasattr(srcWidget, 'hide') and hasattr(srcWidget.hide, '__call__'):
                srcWidget.hide()

            convoWindow = ConversationWindow(
                parent=self, dbHandler=self.__dbHandler, credentials=credDict
            )
            convoWindow.show()
            print('credentials', credDict)

    def close(self):
        print('closing', self)
        super().close()

def main():
    app = QtWidgets.QApplication(sys.argv)

    args, options = utils.cliParser()

    address = '{scheme}://{ip}:{port}'.format(
        scheme='https' if args.secure else 'http', ip=args.ip.strip('/'),
        port=args.port.strip('/')
    )

    ui = WorkFlow(dbHandler=utils.makeDBHandler(address, ChatHandler))
    ui.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
