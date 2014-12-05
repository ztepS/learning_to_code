# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'group.ui'
#
# Created: Fri Nov 28 12:37:37 2014
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(406, 301)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(300, 250, 71, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.searchType = QtGui.QComboBox(Dialog)
        self.searchType.setGeometry(QtCore.QRect(50, 10, 141, 22))
        self.searchType.setObjectName(_fromUtf8("searchType"))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.searchType.addItem(_fromUtf8(""))
        self.progressBar1 = QtGui.QProgressBar(Dialog)
        self.progressBar1.setGeometry(QtCore.QRect(20, 220, 261, 23))
        self.progressBar1.setProperty("value", 0)
        self.progressBar1.setObjectName(_fromUtf8("progressBar1"))
        self.searchButton = QtGui.QPushButton(Dialog)
        self.searchButton.setGeometry(QtCore.QRect(300, 220, 71, 23))
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 341, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.FlatcomboBox = QtGui.QComboBox(self.groupBox)
        self.FlatcomboBox.setGeometry(QtCore.QRect(20, 20, 301, 22))
        self.FlatcomboBox.setObjectName(_fromUtf8("FlatcomboBox"))
        self.PiezocomboBox = QtGui.QComboBox(self.groupBox)
        self.PiezocomboBox.setGeometry(QtCore.QRect(20, 50, 301, 22))
        self.PiezocomboBox.setObjectName(_fromUtf8("PiezocomboBox"))
        self.SpherecomboBox = QtGui.QComboBox(self.groupBox)
        self.SpherecomboBox.setGeometry(QtCore.QRect(20, 80, 301, 22))
        self.SpherecomboBox.setObjectName(_fromUtf8("SpherecomboBox"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 50, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 91, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.timer1 = QtGui.QLabel(Dialog)
        self.timer1.setGeometry(QtCore.QRect(130, 250, 46, 13))
        self.timer1.setText(_fromUtf8(""))
        self.timer1.setObjectName(_fromUtf8("timer1"))
        self.checkBox = QtGui.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(270, 50, 121, 18))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.searchType.setItemText(0, _translate("Dialog", "ЭК-104 и К-5", None))
        self.searchType.setItemText(1, _translate("Dialog", "ЭК-104", None))
        self.searchType.setItemText(2, _translate("Dialog", "К-5", None))
        self.searchType.setItemText(3, _translate("Dialog", "Комплекты с любым L0", None))
        self.searchButton.setText(_translate("Dialog", "Поиск", None))
        self.groupBox.setTitle(_translate("Dialog", "для К-5", None))
        self.lineEdit.setText(_translate("Dialog", "0.001", None))
        self.label.setText(_translate("Dialog", "Дельта не более", None))
        self.checkBox.setText(_translate("Dialog", "Использовать \"тт\"", None))

