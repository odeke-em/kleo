#!/usr/bin/python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

import sys
from hashlib import sha256
from PyQt5 import QtWidgets

try:
    from .FormUI import Tag, utils
    from .EKWindow import EKWindow
    from .DbLiason import ChatHandler, produceAndParse
except:
    from FormUI import Tag, utils
    from EKWindow import EKWindow
    from DbLiason import  ChatHandler, produceAndParse

class LoginUI:
    def __init__(self, dbHandler):
        self.initDBHandler(dbHandler)
        self.initUI()

    def initDBHandler(self, dbHandler, elemParent=None):
        self.__dbHandler = dbHandler
        self.__elemParent = elemParent

    def initUI(self):
        self.__tag = Tag(
            title='Login', size=utils.DynaItem(dict(x=300, y=300)), parent=self.__elemParent,
            location = utils.DynaItem(dict(x=600, y=200)), onSubmit=self.submitCredentials,
            entryList=[
                utils.DynaItem(dict(
                    title='Username', isMultiLine=False, isEditable=True, entryLocation=(1, 1,),
                    labelLocation=(1, 0,), entryText=None, regexStr='^([\w\d]{3,})$')
                ),
                utils.DynaItem(dict(
                    title='Password', isMultiLine=False,  isEditable=True, entryLocation=(3, 1,), labelLocation=(3, 0,),
                    entryText=None, regexStr='.{3,}', inputEchoMode=QtWidgets.QLineEdit.Password)
                )
            ]
        )

        self.__tag.initUI(saveText='Login', cancelText='Exit')

    def submitCredentials(self, content):
        if content:
            username = content.get('Username', {}).get('entryText', None)
            password = content.get('Password', {}).get('entryText', '')
            if not (username and password):
                print('\033[91mBoth username and password have to be non-NULL!\033[00m')
            else:
                encryptedPass = sha256(bytes(password, encoding='utf-8')).hexdigest()
                userQuery = produceAndParse(
                    self.__dbHandler.receipientHandler.getConn, dict(name=username, token=encryptedPass)
                )
                data = userQuery.get('response', {}).get('data', None)
                statusCode = userQuery.get('code', 404)
                if not data:
                    print('No such user exists', username)
                else:
                    print('User', username, 'Login successful')

def main():
    app = QtWidgets.QApplication(sys.argv)

    args, options = utils.cliParser()

    address = '{scheme}://{ip}:{port}'.format(
        scheme='https' if args.secure else 'http', ip=args.ip.strip('/'),
        port=args.port.strip('/')
    )
    ui = LoginUI(utils.makeDBHandler(address, ChatHandler))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
