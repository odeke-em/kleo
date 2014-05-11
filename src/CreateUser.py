#!/usr/bin/python3
# Author: Emmanuel Odeke <odeke@ualberta.ca>

import sys
from hashlib import sha256
from PyQt5 import QtWidgets

try:
    from .FormUI import Tag, utils
    from .DbLiason import ChatHandler, produceAndParse
except:
    from FormUI import Tag, utils
    from DbLiason import  ChatHandler, produceAndParse

class UserUI:
    def __init__(self, dbHandler, elemParent=None):
        self.__dbHandler = dbHandler
        self.__elemParent = elemParent

        self.initDBHandler(dbHandler)
        self.initUI()
        self.initFileDialog()


    def initFileDialog(self):
        self.fileDialog = QtWidgets.QFileDialog(caption='Add profile picture')
        self.fileDialog.filesSelected.connect(self.pictureDropped)

    def pictureDropped(self, pathList):
        print(pathList)

    def initUI(self):
        self.__tag = Tag(
            title='Register User', size=utils.DynaItem(dict(x=300, y=300)), parent=self.__elemParent,
            location = utils.DynaItem(dict(x=600, y=200)), onSubmit=self.submitCredentials,
            entryList = [
                utils.DynaItem(dict(
                    title='Username', isMultiLine=False, isEditable=True, entryLocation=(1, 1,),
                    labelLocation=(1, 0,), entryText=None, regexStr='^([\w\d]{3,})$')
                ),
                utils.DynaItem(dict(
                    title='Alias', isMultiLine=False, isEditable=True, entryLocation=(2, 1,), labelLocation=(2, 0,),
                    entryText=None, regexStr='^([\w\d]{3,})$')
                ),
                utils.DynaItem(dict(
                    title='Password', isMultiLine=False,  isEditable=True, entryLocation=(3, 1,), labelLocation=(3, 0,),
                    entryText=None, regexStr='.{3,}', inputEchoMode=QtWidgets.QLineEdit.Password)
                )
            ]
        )
        self.__tag.initUI(saveText='Create User', cancelText='Exit')

    def submitCredentials(self, content):
        if content:
            username = content.get('Username', {}).get('entryText', None)

            userQuery = produceAndParse(self.__dbHandler.receipientHandler.getConn, dict(name=username))
            data = userQuery.get('response', {}).('data', None)
            if not data:
                alias = content.get('Alias', {}).get('entryText', None)
                password = content.get('Password', {}).get('entryText', '')
                encryptedPass = sha256(bytes(password, encoding='utf-8')).hexdigest()
                print('in here', password, encryptedPass)
                createResponse = produceAndParse(self.__dbHandler.receipientHandler.postConn, dict(
                    name=username, token=encryptedPass, alias=alias
                ))
                print('createResponse', createResponse)

                # Perform the redirect
                self.__tag.close()
                
                
            else:
                print('User', username, 'already exists')
                delResponse = produceAndParse(self.__dbHandler.receipientHandler.deleteConn, dict(name=username))
                print('DelResponse', delResponse)

def main():
    app = QtWidgets.QApplication(sys.argv)

    args, options = utils.cliParser()

    address = '{scheme}://{ip}:{port}'.format(
        scheme='https' if args.secure else 'http', ip=args.ip.strip('/'),
        port=args.port.strip('/')
    )

    ui = UserUI(utils.makeDBHandler(address, ChatHandler))

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
