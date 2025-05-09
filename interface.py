# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1352, 857)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fitButton = QtWidgets.QPushButton(self.centralwidget)
        self.fitButton.setGeometry(QtCore.QRect(20, 280, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.fitButton.setFont(font)
        self.fitButton.setObjectName("fitButton")
        self.loadTrainingSampleButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadTrainingSampleButton.setGeometry(QtCore.QRect(20, 240, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.loadTrainingSampleButton.setFont(font)
        self.loadTrainingSampleButton.setObjectName("loadTrainingSampleButton")
        self.trainingSampleTableView = QtWidgets.QTableView(self.centralwidget)
        self.trainingSampleTableView.setGeometry(QtCore.QRect(20, 350, 641, 351))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.trainingSampleTableView.setFont(font)
        self.trainingSampleTableView.setObjectName("trainingSampleTableView")
        self.virtualSampleModuleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.virtualSampleModuleGroupBox.setGeometry(QtCore.QRect(140, 130, 141, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.virtualSampleModuleGroupBox.setFont(font)
        self.virtualSampleModuleGroupBox.setObjectName("virtualSampleModuleGroupBox")
        self.layoutWidget_2 = QtWidgets.QWidget(self.virtualSampleModuleGroupBox)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 30, 91, 63))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.layoutWidget_2.setFont(font)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inputVirtualSampleRadioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.inputVirtualSampleRadioButton.setFont(font)
        self.inputVirtualSampleRadioButton.setObjectName("inputVirtualSampleRadioButton")
        self.verticalLayout_2.addWidget(self.inputVirtualSampleRadioButton)
        self.manualVirtualSampleRadioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.manualVirtualSampleRadioButton.setFont(font)
        self.manualVirtualSampleRadioButton.setObjectName("manualVirtualSampleRadioButton")
        self.verticalLayout_2.addWidget(self.manualVirtualSampleRadioButton)
        self.virtualSampleTableView = QtWidgets.QTableView(self.centralwidget)
        self.virtualSampleTableView.setGeometry(QtCore.QRect(690, 350, 641, 351))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.virtualSampleTableView.setFont(font)
        self.virtualSampleTableView.setObjectName("virtualSampleTableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 325, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 325, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.manualVirtualSampleWidget = QtWidgets.QWidget(self.centralwidget)
        self.manualVirtualSampleWidget.setGeometry(QtCore.QRect(690, 130, 641, 191))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.manualVirtualSampleWidget.setFont(font)
        self.manualVirtualSampleWidget.setObjectName("manualVirtualSampleWidget")
        self.label_3 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_4.setGeometry(QtCore.QRect(0, 40, 72, 15))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.nameComboBox = QtWidgets.QComboBox(self.manualVirtualSampleWidget)
        self.nameComboBox.setGeometry(QtCore.QRect(0, 60, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.nameComboBox.setFont(font)
        self.nameComboBox.setObjectName("nameComboBox")
        self.label_5 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_5.setGeometry(QtCore.QRect(0, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_7.setGeometry(QtCore.QRect(170, 90, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(self.manualVirtualSampleWidget)
        self.label_9.setGeometry(QtCore.QRect(0, 130, 72, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.stepDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.stepDoubleSpinBox.setGeometry(QtCore.QRect(0, 160, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.stepDoubleSpinBox.setFont(font)
        self.stepDoubleSpinBox.setDecimals(3)
        self.stepDoubleSpinBox.setMaximum(1000000.0)
        self.stepDoubleSpinBox.setObjectName("stepDoubleSpinBox")
        self.okButton = QtWidgets.QPushButton(self.manualVirtualSampleWidget)
        self.okButton.setGeometry(QtCore.QRect(180, 160, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.okButton.setFont(font)
        self.okButton.setObjectName("okButton")
        self.minimumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.minimumDoubleSpinBox.setGeometry(QtCore.QRect(0, 110, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.minimumDoubleSpinBox.setFont(font)
        self.minimumDoubleSpinBox.setDecimals(3)
        self.minimumDoubleSpinBox.setMinimum(-1000000.0)
        self.minimumDoubleSpinBox.setMaximum(1000000.0)
        self.minimumDoubleSpinBox.setObjectName("minimumDoubleSpinBox")
        self.maximumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.manualVirtualSampleWidget)
        self.maximumDoubleSpinBox.setGeometry(QtCore.QRect(170, 110, 91, 22))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.maximumDoubleSpinBox.setFont(font)
        self.maximumDoubleSpinBox.setDecimals(3)
        self.maximumDoubleSpinBox.setMinimum(-1000000.0)
        self.maximumDoubleSpinBox.setMaximum(1000000.0)
        self.maximumDoubleSpinBox.setObjectName("maximumDoubleSpinBox")
        self.downloadVirtualSampleButton = QtWidgets.QPushButton(self.manualVirtualSampleWidget)
        self.downloadVirtualSampleButton.setGeometry(QtCore.QRect(532, 160, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.downloadVirtualSampleButton.setFont(font)
        self.downloadVirtualSampleButton.setObjectName("downloadVirtualSampleButton")
        self.selectSamplesWidget = QtWidgets.QWidget(self.centralwidget)
        self.selectSamplesWidget.setGeometry(QtCore.QRect(300, 130, 361, 191))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.selectSamplesWidget.setFont(font)
        self.selectSamplesWidget.setObjectName("selectSamplesWidget")
        self.sampleScrollArea = QtWidgets.QScrollArea(self.selectSamplesWidget)
        self.sampleScrollArea.setGeometry(QtCore.QRect(0, 30, 361, 161))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.sampleScrollArea.setFont(font)
        self.sampleScrollArea.setWidgetResizable(True)
        self.sampleScrollArea.setObjectName("sampleScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 359, 159))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.sampleScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_6 = QtWidgets.QLabel(self.selectSamplesWidget)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 72, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.HKUSTGZLabel = QtWidgets.QLabel(self.centralwidget)
        self.HKUSTGZLabel.setGeometry(QtCore.QRect(20, 10, 77, 115))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.HKUSTGZLabel.setFont(font)
        self.HKUSTGZLabel.setText("")
        self.HKUSTGZLabel.setObjectName("HKUSTGZLabel")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 710, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 730, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.citation1Label = QtWidgets.QLabel(self.centralwidget)
        self.citation1Label.setGeometry(QtCore.QRect(190, 730, 511, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.citation1Label.setFont(font)
        self.citation1Label.setObjectName("citation1Label")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 750, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.citation2Label = QtWidgets.QLabel(self.centralwidget)
        self.citation2Label.setGeometry(QtCore.QRect(270, 750, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.citation2Label.setFont(font)
        self.citation2Label.setObjectName("citation2Label")
        self.resultButton = QtWidgets.QPushButton(self.centralwidget)
        self.resultButton.setGeometry(QtCore.QRect(160, 280, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.resultButton.setFont(font)
        self.resultButton.setObjectName("resultButton")
        self.plotButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotButton.setGeometry(QtCore.QRect(160, 240, 101, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.plotButton.setFont(font)
        self.plotButton.setObjectName("plotButton")
        self.BgoLearnLabel = QtWidgets.QLabel(self.centralwidget)
        self.BgoLearnLabel.setGeometry(QtCore.QRect(140, 10, 221, 115))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.BgoLearnLabel.setFont(font)
        self.BgoLearnLabel.setText("")
        self.BgoLearnLabel.setObjectName("BgoLearnLabel")
        self.objectModuleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.objectModuleGroupBox.setGeometry(QtCore.QRect(10, 130, 121, 101))
        self.objectModuleGroupBox.setObjectName("objectModuleGroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.objectModuleGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 101, 63))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.singleObjectRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.singleObjectRadioButton.setFont(font)
        self.singleObjectRadioButton.setObjectName("singleObjectRadioButton")
        self.verticalLayout.addWidget(self.singleObjectRadioButton)
        self.multipleObjectRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.multipleObjectRadioButton.setFont(font)
        self.multipleObjectRadioButton.setObjectName("multipleObjectRadioButton")
        self.verticalLayout.addWidget(self.multipleObjectRadioButton)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(21, 771, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.citation3Label = QtWidgets.QLabel(self.centralwidget)
        self.citation3Label.setGeometry(QtCore.QRect(129, 771, 231, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.citation3Label.setFont(font)
        self.citation3Label.setObjectName("citation3Label")
        self.BgoFaceLabel = QtWidgets.QLabel(self.centralwidget)
        self.BgoFaceLabel.setGeometry(QtCore.QRect(400, 10, 184, 115))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.BgoFaceLabel.setFont(font)
        self.BgoFaceLabel.setText("")
        self.BgoFaceLabel.setObjectName("BgoFaceLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1352, 29))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSingleObjectParameter = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.actionSingleObjectParameter.setFont(font)
        self.actionSingleObjectParameter.setObjectName("actionSingleObjectParameter")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionMultipleObjectParameter = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.actionMultipleObjectParameter.setFont(font)
        self.actionMultipleObjectParameter.setObjectName("actionMultipleObjectParameter")
        self.menuSetting.addAction(self.actionSingleObjectParameter)
        self.menuSetting.addAction(self.actionMultipleObjectParameter)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fitButton.setText(_translate("MainWindow", "Fit"))
        self.loadTrainingSampleButton.setText(_translate("MainWindow", "Load Data"))
        self.virtualSampleModuleGroupBox.setTitle(_translate("MainWindow", "Virtual Sample"))
        self.inputVirtualSampleRadioButton.setText(_translate("MainWindow", "Input"))
        self.manualVirtualSampleRadioButton.setText(_translate("MainWindow", "Manual"))
        self.label.setText(_translate("MainWindow", "Training Sample:"))
        self.label_2.setText(_translate("MainWindow", "Virtual Sample:"))
        self.label_3.setText(_translate("MainWindow", "Manual Virtual Sample:"))
        self.label_4.setText(_translate("MainWindow", "Name:"))
        self.label_5.setText(_translate("MainWindow", "Minimum:"))
        self.label_7.setText(_translate("MainWindow", "Maximum:"))
        self.label_9.setText(_translate("MainWindow", "Step:"))
        self.okButton.setText(_translate("MainWindow", "OK"))
        self.downloadVirtualSampleButton.setText(_translate("MainWindow", "Download"))
        self.label_6.setText(_translate("MainWindow", "Samples:"))
        self.label_8.setText(_translate("MainWindow", "Citation: "))
        self.label_10.setText(_translate("MainWindow", "Materials & Design : "))
        self.citation1Label.setText(_translate("MainWindow", "https://doi.org/10.1016/j.matdes.2024.112921"))
        self.label_12.setText(_translate("MainWindow", "NPJ Computational Materials :"))
        self.citation2Label.setText(_translate("MainWindow", "https://doi.org/10.1038/s41524-024-01243-4"))
        self.resultButton.setText(_translate("MainWindow", "Result"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))
        self.objectModuleGroupBox.setTitle(_translate("MainWindow", "Object"))
        self.singleObjectRadioButton.setText(_translate("MainWindow", "Single"))
        self.multipleObjectRadioButton.setText(_translate("MainWindow", "Multiple"))
        self.label_13.setText(_translate("MainWindow", "HomePage : "))
        self.citation3Label.setText(_translate("MainWindow", "http://bgolearn.caobin.asia"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))
        self.actionSingleObjectParameter.setText(_translate("MainWindow", "Single-Object"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionMultipleObjectParameter.setText(_translate("MainWindow", "Multiple-Object"))
