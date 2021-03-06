# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(401, 348)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/3.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(150, 260, 97, 33))
        self.closeButton.setObjectName("closeButton")
        self.textEdit1 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textEdit1.setGeometry(QtCore.QRect(0, 0, 401, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit1.sizePolicy().hasHeightForWidth())
        self.textEdit1.setSizePolicy(sizePolicy)
        self.textEdit1.setReadOnly(True)
        self.textEdit1.setCenterOnScroll(False)
        self.textEdit1.setObjectName("textEdit1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 401, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mouse locker"))
        self.closeButton.setText(_translate("MainWindow", "Close"))
        self.textEdit1.setPlainText(_translate("MainWindow", "Thank you for using this program!\n"
"\n"
"In tray icon enable program and press:\n"
"\"/\" - For lock mouse\n"
"\"*\" - For unlock mouse\n"
"\n"
"Please Donate:\n"
"https://blog.bayrell.org/ru/donate\n"
"\n"
"Source code:\n"
"https://github.com/bayrell-os/mouselocker"))
