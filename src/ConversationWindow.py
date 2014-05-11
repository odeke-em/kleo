import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore

import conversationWindowUI

try:
    from .utils import makeDBHandler, cliParser
    from .DbLiason import ChatHandler, produceAndParse
except:
    from utils import makeDBHandler, cliParser
    from DbLiason import  ChatHandler, produceAndParse

class ConversationWindow(QtWidgets.QMainWindow):
    __iconCache = dict()
    def __init__(self, parent=None, dbHandler=None, credentials=dict()):
        super(ConversationWindow, self).__init__(parent)

        self.__dbHandler = dbHandler

        self.ui_window = conversationWindowUI.Ui_MainWindow()
        self.ui_window.setupUi(self)

        self.initUI()
        self.initActions()
        self.initToolBars()

        self.initRefreshTimers()

        self.__contactsCache = dict()
        self.__credentials = credentials
        print('credentials', credentials)

        self.__crossProfileMessages = dict()
        self.__selectedUser = None
        self.refreshContacts()

    def initRefreshTimers(self):
        self.__contactsRefreshTimer = QtCore.QTimer(self)
        self.__contactsRefreshTimer.timeout.connect(self.refreshContacts)
        self.__contactsRefreshTimer.start(15000)

    def refreshContacts(self):
        self.__syncStatusAction.setIcon(
            QtGui.QIcon('icons/iconmonstr-cloud-syncing.png')
        )

        queryDict =dict(select='name,alias,id', format='short')
        queryForAllContacts = produceAndParse(
            self.__dbHandler.receipientHandler.getConn, queryDict
        )

        code = queryForAllContacts.get('code', 400)

        if code != 200:
            self.__syncStatusAction.setIcon(
                QtGui.QIcon('icons/iconmonstr-cloud-unsynced.png')
            )
        else:
            self.__syncStatusAction.setIcon(
                QtGui.QIcon('icons/iconmonstr-cloud-syncd.png')
            )
            data = queryForAllContacts.get('response', {}).get('data', [])
            if data:
                for entry in data:
                    name = entry.get('name', 'Anonymous')  or 'Anonymous'
                    memContent = self.__contactsCache.get(name, None)
                    if memContent is None:
                        self.__contactsCache[name] = entry

                        icon = QtGui.QIcon(self.memoizeIcon(
                            'icons/iconmonstr-checkbox.png')
                        )
                        freshItem = QtWidgets.QListWidgetItem(name, self.ui_window.contactsListWidget)
                        freshItem.setIcon(icon)
                        freshItem.setStatusTip(name)

    def memoizeIcon(self, path):
        memPixMap, memIcon = self.__iconCache.get(path, (None, None,))
        NEEDS_MEMOIZE = False
        if memPixMap is None:
            NEEDS_MEMOIZE = True
            memPixMap = QtGui.QPixmap(path)

        if memIcon is None:
            NEEDS_MEMOIZE = True
            memIcon = QtGui.QIcon(memPixMap)

        if NEEDS_MEMOIZE:
            self.__iconCache[path] = (memPixMap, memIcon,)

        return memIcon

    def initUI(self):
        self.__warningQBox = QtWidgets.QMessageBox(parent=self)
        self.ui_window.contactsListWidget.clicked.connect(self.selectReceipient)
        self.initSendButton()

    def initSendButton(self):
        memIcon = self.memoizeIcon('icons/iconmonstr-paper-plane-icon.png')
        self.ui_window.sendButton.setIcon(memIcon)
        self.ui_window.sendButton.clicked.connect(self.sendMessage)

    def selectReceipient(self, e):
        curItem = self.ui_window.contactsListWidget.currentItem()
        if curItem:
            self.__selectedUser = curItem.statusTip()
            print('selectedUser', self.__selectedUser)

            # Query for this user's information
            memInfo = self.__contactsCache.get(self.__selectedUser, None)
            if memInfo is None:
                print('cannot find info for user', memInfo)
            else:
                print('Cache hit for user', memInfo)
                self.ui_window.messagesListWidget.clear()
                self.loadMessagesIntoListWidget(self.__selectedUser)

    def loadMessagesIntoListWidget(self, username):
        # msgQueryResponse = produceAndParse(self.__dbHandler.messageHandler
        entres = self.__crossProfileMessages.get(username, [])
        # pass

    def sendMessage(self):
        prevMsg = self.ui_window.conversationEntry.toPlainText()
        if not self.__selectedUser:
            self.__warningQBox.setText('Select a user first')
            self.__warningQBox.show()
        elif prevMsg:
            ownCredentials = self.__credentials.get('name', 'Anonymous')
            ownInfo=self.__contactsCache.get(ownCredentials, None)
            auxUserInfo = self.__contactsCache.get(self.__selectedUser, None)
            print('auxUserInfo', auxUserInfo, 'ownInfo', ownInfo)
            if not auxUserInfo:
                self.__warningQBox.setText(
                    'Could not find contact information for user %s'%(self.__selectedUser)
                )
                self.__warningQBox.show()
            elif not ownInfo:
                self.__warningQBox.setText(
                    'Could not find your contact information. Try again'
                )
                self.__warningQBox.show()
            else:
                auxUserId, senderId = auxUserInfo.get('id', -1), ownInfo.get('id', -1)
                messagePod = dict(receipient_id=auxUserId, sender_id=senderId, body=prevMsg)

                msgSendResponse = produceAndParse(
                    self.__dbHandler.messageHandler.postConn, messagePod
                )
                statusCode = msgSendResponse.get('code', 400)
                v = QtWidgets.QListWidgetItem(prevMsg, self.ui_window.messagesListWidget)
                msgIcon = None
                if statusCode != 200:
                    msgIcon = QtGui.QIcon(self.memoizeIcon('icons/iconmonstr-xbox.png'))
                else:
                    msgIcon = QtGui.QIcon(self.memoizeIcon('icons/iconmonstr-checkbox.png'))
                    dataIn = msgSendResponse.get('response', {}).get('data', [])
                    msgId = dataIn.get('id', -1)
                    if dataIn:
                        v.setStatusTip(str(msgId))

                    inorderListing = self.__crossProfileMessages.get(auxUserId, [])
                    inorderListing.append(dataIn)

                    self.__crossProfileMessages[auxUserId] = inorderListing

                v.setIcon(msgIcon)
                self.ui_window.conversationEntry.setText('')

    def deleteMessage(self, event):
        pass

    def initActions(self):
        self.__exitAction = QtWidgets.QAction(
            QtGui.QIcon('icons/iconmonstr-exit.png'), '&Exit', self
        )
        self.__exitAction.triggered.connect(self.close)
        self.__syncStatusAction = QtWidgets.QAction('&Sync Status', self)

    def initToolBars(self):
        self.__actionToolBar = self.ui_window.actionToolBar
        self.__statusToolBar = self.ui_window.statusOptionsToolBar

        self.__actionToolBar.addAction(self.__exitAction)
        self.__actionToolBar.addAction(self.__syncStatusAction)

    def close(self):
        print('\033[94mClosing\033[00m')
        self.__warningQBox.close()
        self.__contactsRefreshTimer.stop()
        super().close()

def main():
    app = QtWidgets.QApplication(sys.argv)

    args, options = cliParser()

    address = '{scheme}://{ip}:{port}'.format(
        scheme='https' if args.secure else 'http', ip=args.ip.strip('/'),
        port=args.port.strip('/')
    )

    conversationWindow = ConversationWindow(
        dbHandler=makeDBHandler(address, ChatHandler)
    )

    conversationWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
