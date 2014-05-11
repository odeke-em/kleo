#!/usr/bin/python3

# Author: Emmanuel Odeke <odeke@ualberta.ca>

import sys
import time
from PyQt5 import QtWidgets, QtGui, QtCore

import utils # Local module

def labelEntryPairFromSource(srcDict):
    lbPair = LabelEntryPair(**srcDict)
    return lbPair

def tagFromSource(srcDict):
    entryList = srcDict.get('entryList', [])
    srcDict['entryList'] = [utils.DynaItem(initArgs) for initArgs in entryList]
    return Tag(**srcDict)

class LabelEntryPair:
    def __init__(
      self, labelText, isEditable=False, isMultiLine=True, title=None, parent=None,
      labelLocation=(), entryText=None, entryLocation=(), regexStr=None, inputEchoMode=0
    ):
        self.__title = title
        self.__labelWidget = QtWidgets.QLabel(labelText, parent=parent)
        self.isMultiLine = isMultiLine

        __widget = QtWidgets.QLabel
        if isEditable:
            __widget = QtWidgets.QTextEdit if isMultiLine else QtWidgets.QLineEdit

        self.__textGetter = 'toPlainText' if isMultiLine else 'text'
        self.__entryWidget = __widget(parent)

        self.__colorPalette = QtGui.QPalette()
        self.setCleanText()

        self.__entryWidget.setText(entryText)
        self.__entryWidget.setEchoMode(inputEchoMode)
        self.entryLocation = entryLocation
        self.labelLocation = labelLocation

        self.__validator = None
        if regexStr:
            regExp = QtCore.QRegExp(regexStr)
            self.__validator = QtGui.QRegExpValidator(regExp)

    def setError(self):
        self.__entryWidget.setFocus()
        self.setColorPalette(QtCore.Qt.red)

    def setCleanText(self):
        self.__entryWidget.setFocus()
        self.setColorPalette(QtCore.Qt.gray)

    def setColorPalette(self, color):
        self.__colorPalette.setColor(self.__entryWidget.foregroundRole(), color)
        self.__entryWidget.setPalette(self.__colorPalette)

    def getContent(self):
        entryText = getattr(self.__entryWidget, self.__textGetter)()
        validity = True 
        if self.__validator:
            state, inText, position = self.__validator.validate(entryText, 0)
            # print('state', state, 'inText', inText, QtGui.QValidator.Acceptable)
            if state != QtGui.QValidator.Acceptable:
                validity = False
                self.setError()
            else:
                self.setCleanText()

        return validity, dict(labelText=self.__labelWidget.text(),entryText=entryText)

    def serialize(self):
        return dict(
          isMultiLine = self.isMultiLine,
          labelLocation = self.labelLocation,
          entryLocation = self.entryLocation, title = self.__title,
          labelText = self.__labelWidget.text(),
          entryText = getattr(self.__entryWidget, self.__textGetter)()
        )

    @property
    def title(self): return self.__title

    @property
    def entryWidget(self): return self.__entryWidget

    @property
    def labelWidget(self): return self.__labelWidget

    @property
    def getId(self): return self.__id

    def __str__(self):
        return self.__dict__.__str__()

class Tag(QtWidgets.QWidget):
    def __init__(
      self, parent=None, spacing=5, entryList=[], size=None,
      title='Tag', onSubmit=None, location=None, metaData=None
    ):
        super(Tag, self).__init__(parent)
        self.entryList = entryList
        self.spacing   = spacing
        self.location    = location
        self.size        = size
        self.title       = title
        self.metaData    = metaData
        self.parent      = parent
        self.onSubmit    = onSubmit if onSubmit else lambda c: print(c)

    def initUI(self, saveText='&Save', cancelText='&Exit'):
        self.entries = []
        for entry in self.entryList:
            validator = entry.regexStr if 'regexStr' in entry else None
            inputEchoMode = entry.inputEchoMode if 'inputEchoMode' in entry else 0
            isEditable = entry.isEditable if 'isEditable' in entry else True
            labelEntryItem = LabelEntryPair(
                entry.title, title=entry.title,isMultiLine=entry.isMultiLine,
                labelLocation=entry.labelLocation, isEditable=isEditable, inputEchoMode=inputEchoMode,
                entryLocation=entry.entryLocation, entryText=entry.entryText, regexStr=validator
            )
            self.entries.append(labelEntryItem)

        self.__errLabel = QtWidgets.QLabel('', parent=self)
        self.__errLabel.show()

        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(self.spacing)
        
        # self.grid.addWidget(self.__logoLabel)

        for e in self.entries:
            self.grid.addWidget(e.labelWidget, *e.labelLocation)
            self.grid.addWidget(e.entryWidget, *e.entryLocation)

        saveButton = QtWidgets.QPushButton()
        saveButton.setText(saveText)
        saveButton.clicked.connect(self.submit)

        cancelButton = QtWidgets.QPushButton()
        cancelButton.setText(cancelText)
        cancelButton.clicked.connect(lambda: self.close())

        lastRow = self.grid.rowCount() + 1
        self.grid.addWidget(saveButton, lastRow, 0)
        self.grid.addWidget(cancelButton, lastRow, 1)
        
        self.setLayout(self.grid)
        self.setGeometry(
          self.location.x, self.location.y,
          self.size.x, self.size.y
        )
        self.setWindowTitle(self.title)
        self.show()

    def submit(self):
        self.onSubmit(self.getContent())
        # self.close()

        # serialized = self.serialize()
        # self.onSubmit(serialized)
        # Uncomment to test the serialization
        # t = tagFromSource(serialized)

    def serialize(self):
        return dict(
            location = self.location, 
            size = self.size, title = self.title,
            metaData = self.metaData, spacing = self.spacing, entryList = [
              item.serialize() for item in self.entries
            ]
        )

    def getContent(self):
        dataOut = dict()
        for entry in self.entries:
            validity, content = entry.getContent()
            if validity:
                dataOut[entry.title] = content
            else:
                print('isTinted', validity)
                self.__errLabel.setText('Error for ' + entry.title)

        return dataOut

def main():
    pass
    
if __name__ == '__main__':
    main()
