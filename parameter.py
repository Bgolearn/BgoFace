# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'parameter.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ParameterWindow(object):
    def setupUi(self, ParameterWindow):
        ParameterWindow.setObjectName("ParameterWindow")
        ParameterWindow.resize(905, 603)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        ParameterWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ParameterWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.moduleGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.moduleGroupBox.setGeometry(QtCore.QRect(20, 10, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.moduleGroupBox.setFont(font)
        self.moduleGroupBox.setObjectName("moduleGroupBox")
        self.layoutWidget = QtWidgets.QWidget(self.moduleGroupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 141, 63))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.regressionRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.regressionRadioButton.setObjectName("regressionRadioButton")
        self.verticalLayout.addWidget(self.regressionRadioButton)
        self.classificationRadioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.classificationRadioButton.setObjectName("classificationRadioButton")
        self.verticalLayout.addWidget(self.classificationRadioButton)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 130, 871, 371))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label.setObjectName("label")
        self.regressionFunctionComboBox = QtWidgets.QComboBox(self.tab)
        self.regressionFunctionComboBox.setGeometry(QtCore.QRect(10, 120, 201, 27))
        self.regressionFunctionComboBox.setObjectName("regressionFunctionComboBox")
        self.parameterLabel = QtWidgets.QLabel(self.tab)
        self.parameterLabel.setGeometry(QtCore.QRect(10, 150, 101, 21))
        self.parameterLabel.setObjectName("parameterLabel")
        self.regressionFunctionNameLabel = QtWidgets.QLabel(self.tab)
        self.regressionFunctionNameLabel.setGeometry(QtCore.QRect(220, 120, 511, 21))
        self.regressionFunctionNameLabel.setText("")
        self.regressionFunctionNameLabel.setObjectName("regressionFunctionNameLabel")
        self.regressionParameter1Widget = QtWidgets.QWidget(self.tab)
        self.regressionParameter1Widget.setGeometry(QtCore.QRect(10, 170, 561, 61))
        self.regressionParameter1Widget.setObjectName("regressionParameter1Widget")
        self.parameter1Label = QtWidgets.QLabel(self.regressionParameter1Widget)
        self.parameter1Label.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.parameter1Label.setText("")
        self.parameter1Label.setObjectName("parameter1Label")
        self.parameter1LineEdit = QtWidgets.QLineEdit(self.regressionParameter1Widget)
        self.parameter1LineEdit.setGeometry(QtCore.QRect(0, 30, 91, 27))
        self.parameter1LineEdit.setText("")
        self.parameter1LineEdit.setObjectName("parameter1LineEdit")
        self.parameter1RecommendLabel = QtWidgets.QLabel(self.regressionParameter1Widget)
        self.parameter1RecommendLabel.setGeometry(QtCore.QRect(100, 30, 461, 21))
        self.parameter1RecommendLabel.setText("")
        self.parameter1RecommendLabel.setObjectName("parameter1RecommendLabel")
        self.regressionParameter2Widget = QtWidgets.QWidget(self.tab)
        self.regressionParameter2Widget.setGeometry(QtCore.QRect(10, 230, 561, 61))
        self.regressionParameter2Widget.setObjectName("regressionParameter2Widget")
        self.parameter2Label = QtWidgets.QLabel(self.regressionParameter2Widget)
        self.parameter2Label.setGeometry(QtCore.QRect(0, 0, 561, 21))
        self.parameter2Label.setText("")
        self.parameter2Label.setObjectName("parameter2Label")
        self.parameter2LineEdit = QtWidgets.QLineEdit(self.regressionParameter2Widget)
        self.parameter2LineEdit.setGeometry(QtCore.QRect(0, 30, 91, 27))
        self.parameter2LineEdit.setObjectName("parameter2LineEdit")
        self.parameter2RecommendLabel = QtWidgets.QLabel(self.regressionParameter2Widget)
        self.parameter2RecommendLabel.setGeometry(QtCore.QRect(100, 30, 461, 21))
        self.parameter2RecommendLabel.setText("")
        self.parameter2RecommendLabel.setObjectName("parameter2RecommendLabel")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(11, 32, 76, 23))
        self.label_4.setObjectName("label_4")
        self.regression_opt_num_SpinBox = QtWidgets.QSpinBox(self.tab)
        self.regression_opt_num_SpinBox.setGeometry(QtCore.QRect(10, 60, 75, 27))
        self.regression_opt_num_SpinBox.setMinimum(1)
        self.regression_opt_num_SpinBox.setMaximum(1000000)
        self.regression_opt_num_SpinBox.setObjectName("regression_opt_num_SpinBox")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(110, 32, 56, 23))
        self.label_5.setObjectName("label_5")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 60, 140, 29))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.regression_Dynamic_W_TrueRadioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.regression_Dynamic_W_TrueRadioButton.setObjectName("regression_Dynamic_W_TrueRadioButton")
        self.horizontalLayout.addWidget(self.regression_Dynamic_W_TrueRadioButton)
        self.regression_Dynamic_W_FalseRadioButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.regression_Dynamic_W_FalseRadioButton.setObjectName("regression_Dynamic_W_FalseRadioButton")
        self.horizontalLayout.addWidget(self.regression_Dynamic_W_FalseRadioButton)
        self.layoutWidget2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(110, 60, 222, 29))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.regression_min_search_TrueRadioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        self.regression_min_search_TrueRadioButton.setObjectName("regression_min_search_TrueRadioButton")
        self.horizontalLayout_2.addWidget(self.regression_min_search_TrueRadioButton)
        self.regression_min_search_FalseRadioButton = QtWidgets.QRadioButton(self.layoutWidget2)
        self.regression_min_search_FalseRadioButton.setObjectName("regression_min_search_FalseRadioButton")
        self.horizontalLayout_2.addWidget(self.regression_min_search_FalseRadioButton)
        self.layoutWidget3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget3.setGeometry(QtCore.QRect(530, 60, 325, 29))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.regression_Kriging_model_Random_Forest_RadioButton = QtWidgets.QRadioButton(self.layoutWidget3)
        self.regression_Kriging_model_Random_Forest_RadioButton.setObjectName("regression_Kriging_model_Random_Forest_RadioButton")
        self.horizontalLayout_3.addWidget(self.regression_Kriging_model_Random_Forest_RadioButton)
        self.regression_Kriging_model_Gaussian_Process_RadioButton = QtWidgets.QRadioButton(self.layoutWidget3)
        self.regression_Kriging_model_Gaussian_Process_RadioButton.setObjectName("regression_Kriging_model_Gaussian_Process_RadioButton")
        self.horizontalLayout_3.addWidget(self.regression_Kriging_model_Gaussian_Process_RadioButton)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 300, 701, 34))
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.showRegressionContrastButton = QtWidgets.QPushButton(self.widget)
        self.showRegressionContrastButton.setObjectName("showRegressionContrastButton")
        self.horizontalLayout_6.addWidget(self.showRegressionContrastButton)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(359, 32, 100, 23))
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(530, 32, 124, 23))
        self.label_12.setObjectName("label_12")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 231, 16))
        self.label_7.setObjectName("label_7")
        self.classificationClassifierComboBox = QtWidgets.QComboBox(self.tab_2)
        self.classificationClassifierComboBox.setGeometry(QtCore.QRect(10, 60, 181, 27))
        self.classificationClassifierComboBox.setObjectName("classificationClassifierComboBox")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(10, 35, 91, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(250, 30, 81, 31))
        self.label_9.setObjectName("label_9")
        self.classification_opt_num_SpinBox = QtWidgets.QSpinBox(self.tab_2)
        self.classification_opt_num_SpinBox.setGeometry(QtCore.QRect(250, 60, 75, 27))
        self.classification_opt_num_SpinBox.setMinimum(1)
        self.classification_opt_num_SpinBox.setMaximum(100000)
        self.classification_opt_num_SpinBox.setObjectName("classification_opt_num_SpinBox")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_11.setObjectName("label_11")
        self.classificationFunctionComboBox = QtWidgets.QComboBox(self.tab_2)
        self.classificationFunctionComboBox.setGeometry(QtCore.QRect(10, 140, 181, 27))
        self.classificationFunctionComboBox.setObjectName("classificationFunctionComboBox")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(390, 30, 111, 31))
        self.label_2.setObjectName("label_2")
        self.layoutWidget4 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(390, 60, 141, 29))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.classification_Dynamic_W_TrueRadioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        self.classification_Dynamic_W_TrueRadioButton.setObjectName("classification_Dynamic_W_TrueRadioButton")
        self.horizontalLayout_4.addWidget(self.classification_Dynamic_W_TrueRadioButton)
        self.classification_Dynamic_W_FalseRadioButton = QtWidgets.QRadioButton(self.layoutWidget4)
        self.classification_Dynamic_W_FalseRadioButton.setObjectName("classification_Dynamic_W_FalseRadioButton")
        self.horizontalLayout_4.addWidget(self.classification_Dynamic_W_FalseRadioButton)
        self.tabWidget.addTab(self.tab_2, "")
        self.setParametersButton = QtWidgets.QPushButton(self.centralwidget)
        self.setParametersButton.setGeometry(QtCore.QRect(760, 510, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.setParametersButton.setFont(font)
        self.setParametersButton.setObjectName("setParametersButton")
        self.resetParametersButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetParametersButton.setGeometry(QtCore.QRect(620, 510, 91, 28))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.resetParametersButton.setFont(font)
        self.resetParametersButton.setObjectName("resetParametersButton")
        ParameterWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ParameterWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 29))
        self.menubar.setObjectName("menubar")
        ParameterWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ParameterWindow)
        self.statusbar.setObjectName("statusbar")
        ParameterWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ParameterWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ParameterWindow)

    def retranslateUi(self, ParameterWindow):
        _translate = QtCore.QCoreApplication.translate
        ParameterWindow.setWindowTitle(_translate("ParameterWindow", "MainWindow"))
        self.moduleGroupBox.setTitle(_translate("ParameterWindow", "Module"))
        self.regressionRadioButton.setText(_translate("ParameterWindow", "Regression"))
        self.classificationRadioButton.setText(_translate("ParameterWindow", "Classification"))
        self.label.setText(_translate("ParameterWindow", "Function:"))
        self.parameterLabel.setText(_translate("ParameterWindow", "Parameter:"))
        self.label_3.setText(_translate("ParameterWindow", "Parameters in function fit():"))
        self.label_4.setText(_translate("ParameterWindow", "opt_num:"))
        self.label_5.setText(_translate("ParameterWindow", "search:"))
        self.regression_Dynamic_W_TrueRadioButton.setText(_translate("ParameterWindow", "True"))
        self.regression_Dynamic_W_FalseRadioButton.setText(_translate("ParameterWindow", "False"))
        self.regression_min_search_TrueRadioButton.setText(_translate("ParameterWindow", "minimum"))
        self.regression_min_search_FalseRadioButton.setText(_translate("ParameterWindow", "maximum"))
        self.regression_Kriging_model_Random_Forest_RadioButton.setText(_translate("ParameterWindow", "Random Forest"))
        self.regression_Kriging_model_Gaussian_Process_RadioButton.setText(_translate("ParameterWindow", "Gaussian Process"))
        self.showRegressionContrastButton.setText(_translate("ParameterWindow", "Pred v.s. Label"))
        self.label_10.setText(_translate("ParameterWindow", "Loading this image involves some calculations, please wait patiently."))
        self.label_6.setText(_translate("ParameterWindow", "Dynamic_W:"))
        self.label_12.setText(_translate("ParameterWindow", "Kriging_model:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("ParameterWindow", "Regression"))
        self.label_7.setText(_translate("ParameterWindow", "Parameters in function fit():"))
        self.label_8.setText(_translate("ParameterWindow", "Classifier:"))
        self.label_9.setText(_translate("ParameterWindow", "opt_num:"))
        self.label_11.setText(_translate("ParameterWindow", "Function:"))
        self.label_2.setText(_translate("ParameterWindow", "Dynamic_W:"))
        self.classification_Dynamic_W_TrueRadioButton.setText(_translate("ParameterWindow", "True"))
        self.classification_Dynamic_W_FalseRadioButton.setText(_translate("ParameterWindow", "False"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("ParameterWindow", "Classification"))
        self.setParametersButton.setText(_translate("ParameterWindow", "OK"))
        self.resetParametersButton.setText(_translate("ParameterWindow", "Reset"))
