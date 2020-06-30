# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'get_text.ui'
#
# Created: Thu Oct 25 15:44:42 2018
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(431, 367)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 381, 141))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 221, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 70, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 70, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 270, 235, 80))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonGetText = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonGetText.setObjectName(_fromUtf8("pushButtonGetText"))
        self.horizontalLayout.addWidget(self.pushButtonGetText)
        self.pushButtonQuit = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonQuit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.pushButtonQuit.setObjectName(_fromUtf8("pushButtonQuit"))
        self.horizontalLayout.addWidget(self.pushButtonQuit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "File name", None))
        self.label_2.setText(_translate("Dialog", "Text", None))
        self.pushButtonGetText.setText(_translate("Dialog", "Get text", None))
        self.pushButtonQuit.setText(_translate("Dialog", "Quit", None))
        self.pushButtonGetText.clicked.connect(self.buttonGetTextPressed)
        self.pushButtonQuit.clicked.connect(self.buttonQuitPressed)

    def buttonGetTextPressed(self):
        fileName = self.lineEdit.text()
        with open(fileName) as doc:
                text=doc.read()
        self.lineEdit.setText('File is read')
        self.textEdit.setText(text)

    def buttonQuitPressed(self):
        app.quit()

app = QtGui.QApplication(sys.argv)
form = Ui_Dialog()
form.show()
app.exec_()
