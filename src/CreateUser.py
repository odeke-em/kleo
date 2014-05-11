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
    def __init__(self, dbHandler, elemParent=None, onSubmitCallback=None):
        self.__dbHandler = dbHandler
        self.__elemParent = elemParent
        self.__onSubmitCallback = onSubmitCallback

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
                    title='Password', isMultiLine=False,  isEditable=True,
                    entryLocation=(3, 1,), labelLocation=(3, 0,), entryText=None, 
                    regexStr='.{3,}', inputEchoMode=QtWidgets.QLineEdit.Password)
                )
            ]
        )
        self.__tag.initUI(saveText='Create User', cancelText='Exit')

    def submitCredentials(self, content):
        if content:
            username = content.get('Username', {}).get('entryText', None)

            userQuery = produceAndParse(self.__dbHandler.receipientHandler.getConn, dict(name=username))
            data = userQuery.get('response', {}).get('data', None)
            if userQuery.get('code', 400) != 200:
                print('\033[91m', userQuery, '\033[00m')
            elif not data:
                alias = content.get('Alias', {}).get('entryText', None)
                password = content.get('Password', {}).get('entryText', '')
                encryptedPass = sha256(bytes(password, encoding='utf-8')).hexdigest()
                print('in here', password, encryptedPass)
                creationVars = dict(name=username, token=encryptedPass, alias=alias)
                cResp = produceAndParse(
                    self.__dbHandler.receipientHandler.postConn, creationVars
                )
                print('createdResponse', cResp)
                code = cResp.get('code', 400)
                data = cResp.get('response', {}).get('data', None)
                if code == 200 and data:
                    # Perform the redirect
                    self.__onSubmitCallback(creationVars, self.__tag)
                else:
                    print('err\033[91m', code, cResp, '\033[00m') 
                
            else:
                print('User', username, 'already exists')

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
