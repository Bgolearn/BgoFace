# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'contrast.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContrastWindow(object):
    def setupUi(self, ContrastWindow):
        ContrastWindow.setObjectName("ContrastWindow")
        ContrastWindow.resize(605, 541)
        self.centralwidget = QtWidgets.QWidget(ContrastWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.regressionContrastGraphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.regressionContrastGraphicsView.setGeometry(QtCore.QRect(10, 10, 531, 481))
        self.regressionContrastGraphicsView.setObjectName("regressionContrastGraphicsView")
        self.saveRegressionContrastButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveRegressionContrastButton.setGeometry(QtCore.QRect(10, 500, 81, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.saveRegressionContrastButton.setFont(font)
        self.saveRegressionContrastButton.setObjectName("saveRegressionContrastButton")
        ContrastWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ContrastWindow)
        QtCore.QMetaObject.connectSlotsByName(ContrastWindow)

    def retranslateUi(self, ContrastWindow):
        _translate = QtCore.QCoreApplication.translate
        ContrastWindow.setWindowTitle(_translate("ContrastWindow", "MainWindow"))
        self.saveRegressionContrastButton.setText(_translate("ContrastWindow", "Save"))
