import io
import itertools
import os
import re
import sys
import numpy as np
import pandas as pd
import seaborn as sns
import Bgolearn.BGOsampling as BGOS
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QHeaderView, QCheckBox, QVBoxLayout, \
    QWidget, QRadioButton, QButtonGroup, QGraphicsScene
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QPixmap
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel, RBF, ConstantKernel
from sklearn.model_selection import LeaveOneOut

from interface import Ui_MainWindow
from load import Ui_LoadWindow
from download import Ui_DownloadWindow
from parameter import Ui_ParameterWindow
from result import Ui_ResultWindow
from show import Ui_ShowWindow
from export import Ui_ExportWindow



class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('BgoFace')

        # 子窗口
        self.loadWindow = LoadWindow()
        self.parameterWindow = ParameterWindow()
        self.downloadWindow = DownloadWindow()
        self.showWindow = ShowWindow()
        self.resultWindow = ResultWindow()

        # 函数
        self.load_image()
        self.citation1Label.setText('<a href="https://doi.org/10.1016/j.matdes.2024.112921">https://doi.org/10.1016/j.matdes.2024.112921</a>')
        self.citation2Label.setText('<a href="https://doi.org/10.1038/s41524-024-01243-4">https://doi.org/10.1038/s41524-024-01243-4</a>')
        self.loadTrainingSampleButton.clicked.connect(self.open_load_window)
        self.plotButton.clicked.connect(self.open_show_window)
        self.resultButton.clicked.connect(self.open_result_window)
        self.inputVirtualSampleRadioButton.clicked.connect(self.switch_virtual_sample_method)
        self.manualVirtualSampleRadioButton.clicked.connect(self.switch_virtual_sample_method)
        self.nameComboBox.currentIndexChanged.connect(self.change_virtual_sample)
        self.okButton.clicked.connect(self.ok_virtual_sample)
        self.actionParameter.triggered.connect(self.open_parameter_window)
        self.downloadVirtualSampleButton.clicked.connect(self.open_download_window)
        self.fitButton.clicked.connect(self.fit)

        # 变量
        self.inputVirtualSampleRadioButton.setChecked(True)
        self.selectSamplesWidget.setVisible(False)
        self.manualVirtualSampleWidget.setVisible(False)
        self.model = QStandardItemModel()
        self.training_sample = None
        self.virtual_sample = None

        self.sample_data = {}
        self.selected_sample_data = {}
        self.parameters_setting = {
            'module': 'regression',
            'function': 'EI',
            'opt_num': 1,
            'min_search': True,
            'Dynamic_W': False
        }
        self.elements = []
        self.checkboxes = []
        self.selected_elements = []


    def load_image(self):
        file_path = 'logo.jpg'
        pixmap = QPixmap(file_path)
        scaled_pixmap = pixmap.scaled(self.logoLabel.size(), aspectRatioMode=True)
        self.logoLabel.setPixmap(scaled_pixmap)
    def on_checkbox_state_changed(self, state):
        sender = self.sender()  # 获取发出信号的QCheckBox
        element = sender.text()
        if state == 2:  # 选中状态
            if element not in self.selected_elements:
                self.selected_elements.append(element)
                dataset = self.sample_data[element]
                self.selected_sample_data[element] = dataset

        else:  # 未选中状态
            if element in self.selected_elements:
                self.selected_elements.remove(element)
                self.selected_sample_data.pop(element)
        self.selected_elements = self.reorder_list_by_reference(self.elements, self.selected_elements)
        self.nameComboBox.clear()
        self.nameComboBox.addItems(self.selected_elements)

    def reorder_list_by_reference(self, ref_list, target_list):
        # 创建一个字典，存储 ref_list 中每个元素的索引
        ref_index_map = {value: idx for idx, value in enumerate(ref_list)}

        # 使用 ref_list 的顺序来对 target_list 进行排序
        sorted_target_list = sorted(target_list, key=lambda x: ref_index_map.get(x, float('inf')))

        return sorted_target_list

    def show_select_element(self):
        scroll_content = QWidget()
        layout = QVBoxLayout(scroll_content)

        # 定义元素列表
        self.elements = list(self.training_sample.columns)
        # 用于存储选中的QCheckBox
        self.selected_elements = self.elements.copy()
        self.selected_elements.pop()
        # 为每个元素创建一个QCheckBox，并添加到布局中

        for index, element in enumerate(self.elements):
            checkbox = QCheckBox(element)
            checkbox.setObjectName(f"checkbox_{index}")  # 设置对象名称，方便查找
            checkbox.setChecked(True)
            if index != (len(self.elements) - 1):
                checkbox.setChecked(True)
                self.nameComboBox.addItem(element)
            else:
                checkbox.setChecked(False)
            checkbox.stateChanged.connect(self.on_checkbox_state_changed)  # 连接信号和槽
            layout.addWidget(checkbox)
            # self.checkboxes.append(checkbox)

        # 设置QScrollArea的内容
        self.sampleScrollArea.setWidget(scroll_content)
        self.sampleScrollArea.setWidgetResizable(True)
    def open_show_window(self):
        self.showWindow.get_training_sample(self.training_sample)
        self.showWindow.show()
    def open_result_window(self):
        self.resultWindow.show()
    def open_load_window(self):
        self.loadWindow.files_uploaded.connect(self.process_uploaded_files)
        self.loadWindow.show()

    def open_download_window(self):
        if self.virtual_sample is None:
            QMessageBox.warning(self, "Warning", "Please generate Virtual Sample first！")
            return
        self.downloadWindow.get_virtual_sample(self.virtual_sample)
        self.downloadWindow.show()

    def open_parameter_window(self):
        self.parameterWindow.parameters_uploaded.connect(self.get_uploaded_parameters)
        self.parameterWindow.show()

    def switch_virtual_sample_method(self):
        if self.inputVirtualSampleRadioButton.isChecked():
            self.loadWindow.label_2.setVisible(True)
            self.loadWindow.virtualSampleFileName.setVisible(True)
            self.loadWindow.browseVirtualSampleButton.setVisible(True)
            self.selectSamplesWidget.setVisible(False)
            self.manualVirtualSampleWidget.setVisible(False)
        elif self.manualVirtualSampleRadioButton.isChecked():
            self.loadWindow.label_2.setVisible(False)
            self.loadWindow.virtualSampleFileName.setVisible(False)
            self.loadWindow.browseVirtualSampleButton.setVisible(False)
            self.selectSamplesWidget.setVisible(True)
            self.manualVirtualSampleWidget.setVisible(True)

    def process_uploaded_files(self, file_contents):
        if 'training_sample' in file_contents:
            self.training_sample = file_contents['training_sample']['training_sample_file']
            if file_contents['training_sample']['training_sample_file_extension'] in ['xls', 'xlsx']:
                self.display_excel_content(self.training_sample, self.trainingSampleTableView)
                self.get_training_sample_data(self.training_sample)

        if 'virtual_sample' in file_contents:
            self.virtual_sample = file_contents['virtual_sample']['virtual_sample_file']
            if file_contents['virtual_sample']['virtual_sample_file_extension'] in ['xls', 'xlsx']:
                self.display_excel_content(self.virtual_sample, self.virtualSampleTableView)
        else:
            self.virtual_sample = None
            self.nameComboBox.clear()
            # 创建新的空模型
            empty_model = QStandardItemModel()

            # 设置空模型给 QTableView
            self.virtualSampleTableView.setModel(empty_model)

            self.show_select_element()

    def get_uploaded_parameters(self, setting):
        self.parameters_setting = setting


    def display_excel_content(self, excel_file, table_view):
        model = QStandardItemModel()

        for column in excel_file.columns:
            model.setHorizontalHeaderItem(excel_file.columns.get_loc(column), QStandardItem(column))

        for row in excel_file.itertuples(index=False):
            items = [QStandardItem(str(cell)) for cell in row]
            model.appendRow(items)

        table_view.setModel(model)
        # table_view.resizeColumnsToContents()

        # 设置表头自适应填满水平空间
        header = table_view.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

    def get_training_sample_data(self, training_sample):
        self.sample_data = {}
        self.selected_sample_data = {}
        training_sample_dict = training_sample.to_dict(orient='list')
        for key, value in training_sample_dict.items():
            dataset = {'data': value, 'minimum': min(value), 'maximum': max(value), 'step': 0}
            self.sample_data[key] = dataset
        self.selected_sample_data = self.sample_data.copy()
        self.selected_sample_data.popitem()

    def get_virtual_sample_data(self):
        virtual_samples = [values['virtual_sample'] for key, values in self.selected_sample_data.items()]

        # 使用 itertools.product 生成所有可能的组合
        all_combinations = list(itertools.product(*virtual_samples))

        # 将组合转换为 DataFrame
        df_virtual_samples = pd.DataFrame(all_combinations, columns=[key for key in self.selected_sample_data.keys()])
        self.virtual_sample = df_virtual_samples
        self.display_excel_content(df_virtual_samples, self.virtualSampleTableView)

    def change_virtual_sample(self):
        item = str(self.nameComboBox.currentText())
        if item == '':
            return
        minimum = self.selected_sample_data[item]['minimum']
        maximum = self.selected_sample_data[item]['maximum']
        step = self.selected_sample_data[item]['step']
        self.minimumDoubleSpinBox.setValue(minimum)
        self.maximumDoubleSpinBox.setValue(maximum)
        self.stepDoubleSpinBox.setValue(step)


    def ok_virtual_sample(self):
        item = str(self.nameComboBox.currentText())
        step = self.stepDoubleSpinBox.value()
        minimum = self.minimumDoubleSpinBox.value()
        maximum = self.maximumDoubleSpinBox.value()
        if self.stepDoubleSpinBox.value() == 0:
            QMessageBox.warning(self, "Warning", "Please re-enter step！")
            return
        if minimum > maximum:
            QMessageBox.warning(self, "Warning", "Please re-enter minimum and maximum！")
            return
        self.selected_sample_data[item]['minimum'] = minimum
        self.selected_sample_data[item]['maximum'] = maximum
        self.selected_sample_data[item]['step'] = step
        self.selected_sample_data[item]['virtual_sample'] = np.arange(minimum, maximum+step, step)
        # 获取当前索引
        current_index = self.nameComboBox.currentIndex()
        # 计算下一个索引
        next_index = (current_index + 1) % self.nameComboBox.count()
        # 切换到下一个项目
        self.nameComboBox.setCurrentIndex(next_index)
        number = 0
        for key, value in self.selected_sample_data.items():
            if 'virtual_sample' in value:
                number += 1
        if number == len(self.selected_sample_data) and number > 0:
            self.get_virtual_sample_data()

    def fit(self):
        if self.training_sample is None or self.virtual_sample is None:
            QMessageBox.warning(self, "Warning", "Please enter suitable training sample and virtual sample！")
            return
        if self.inputVirtualSampleRadioButton.isChecked():
            x = self.training_sample.iloc[:, :-1]
        else:
            x = self.training_sample[self.selected_elements]
        y = self.training_sample.iloc[:, -1]

        # Capture the output
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        # Print the output to the console (this will be captured)
        Bgolearn = BGOS.Bgolearn()
        # Restore the original stdout
        sys.stdout = old_stdout
        captured_output = buffer.getvalue()
        buffer.close()
        self.resultWindow.resultTextEdit.append(captured_output)
        try:
            if self.parameters_setting['module'] == 'regression':
                opt_num = self.parameters_setting['opt_num']
                min_search = self.parameters_setting['min_search']
                Dynamic_W = self.parameters_setting['Dynamic_W']

                # Capture the output
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                # Print the output to the console (this will be captured)
                Mymodel = Bgolearn.fit(data_matrix=x, Measured_response=y, virtual_samples=self.virtual_sample, opt_num=opt_num, min_search=min_search, Dynamic_W=Dynamic_W)
                # Restore the original stdout
                sys.stdout = old_stdout
                captured_output = buffer.getvalue()
                buffer.close()
                self.resultWindow.resultTextEdit.append(captured_output)

                if self.parameters_setting['function'] == 'EI':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.EI()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'EI_plugin':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.EI_plugin()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'Augmented_EI':
                    self.resultWindow.show()
                    alpha = int(self.parameters_setting['parameter1'])
                    tao = float(self.parameters_setting['parameter2'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Augmented_EI(alpha=alpha, tao=tao)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'EQI':
                    self.resultWindow.show()
                    beta = float(self.parameters_setting['parameter1'])
                    tao_new = float(self.parameters_setting['parameter2'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.EQI(beta=beta, tao_new=tao_new)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'Reinterpolation_EI':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Reinterpolation_EI()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'UCB':
                    self.resultWindow.show()
                    alpha = int(self.parameters_setting['parameter1'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.UCB(alpha=alpha)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'PoI':
                    self.resultWindow.show()
                    tao = float(self.parameters_setting['parameter1'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.PoI(tao=tao)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'PES':
                    self.resultWindow.show()
                    sam_num = int(self.parameters_setting['parameter1'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.PES(sam_num=sam_num)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'Knowledge_G':
                    self.resultWindow.show()
                    MC_num = int(self.parameters_setting['parameter1'])
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Knowledge_G(MC_num=MC_num)
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
            else:
                opt_num = self.parameters_setting['opt_num']
                min_search = self.parameters_setting['min_search']
                classifier = self.parameters_setting['classifier']
                Dynamic_W = self.parameters_setting['Dynamic_W']

                # Capture the output
                old_stdout = sys.stdout
                sys.stdout = buffer = io.StringIO()
                # Print the output to the console (this will be captured)
                Mymodel = Bgolearn.fit(data_matrix=x, Measured_response=y, virtual_samples=self.virtual_sample, Mission='Classification', Classifier=classifier,opt_num=opt_num, min_search=min_search, Dynamic_W=Dynamic_W)
                # Restore the original stdout
                sys.stdout = old_stdout
                captured_output = buffer.getvalue()
                buffer.close()
                self.resultWindow.resultTextEdit.append(captured_output)

                if self.parameters_setting['function'] == 'Least_cfd':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Least_cfd()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'Margin_S':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Margin_S()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
                if self.parameters_setting['function'] == 'Entropy':
                    self.resultWindow.show()
                    # Capture the output
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    # Print the output to the console (this will be captured)
                    Mymodel.Entropy()
                    # Restore the original stdout
                    sys.stdout = old_stdout
                    captured_output = buffer.getvalue()
                    buffer.close()
                    self.resultWindow.resultTextEdit.append(captured_output)
        except Exception as e:
            self.show_error_message(str(e))

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText("An error occurred")
        msg_box.setInformativeText(message)
        msg_box.setWindowTitle("Error")
        msg_box.exec_()

class LoadWindow(QMainWindow, Ui_LoadWindow):
    files_uploaded = pyqtSignal(dict)

    def __init__(self):
        super(LoadWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Load')
        self.browseTrainingSampleButton.clicked.connect(self.upload_training_sample_file)
        self.browseVirtualSampleButton.clicked.connect(self.upload_virtual_sample_file)
        self.loadButton.clicked.connect(self.upload_file)
        self.cancelButton.clicked.connect(self.close)

        self.training_sample_file = None
        self.training_sample_file_extension = None
        self.virtual_sample_file = None
        self.virtual_sample_file_extension = None

    def upload_training_sample_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Text Files (*.txt);;Excel Files (*.xls *.xlsx)",
                                                   options=options)
        if file_path:
            # 显示文件路径
            self.trainingSampleFileName.setText(file_path)
            file_extension = file_path.rsplit('.', 1)[1].lower()
            self.training_sample_file_extension = file_extension
            try:
                if file_extension == 'txt':
                    with open(file_path, 'r') as file:
                        self.training_sample_file = file.read()
                elif file_extension in ['xls', 'xlsx']:
                    df = pd.read_excel(file_path)
                    self.training_sample_file = df
                # 上传成功后可以给用户提示
                self.statusBar().showMessage('File uploaded successfully！', 3000)
            except Exception as e:
                self.statusBar().showMessage(f'File processing failed: {e}', 3000)

    def upload_virtual_sample_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                   "All Files (*);;Text Files (*.txt);;Excel Files (*.xls *.xlsx)",
                                                   options=options)
        if file_path:
            # 显示文件路径
            self.virtualSampleFileName.setText(file_path)
            file_extension = file_path.rsplit('.', 1)[1].lower()
            self.virtual_sample_file_extension = file_extension
            try:
                if file_extension == 'txt':
                    with open(file_path, 'r') as file:
                        self.virtual_sample_file = file.read()
                elif file_extension in ['xls', 'xlsx']:
                    df = pd.read_excel(file_path)
                    self.virtual_sample_file = df
                # 上传成功后可以给用户提示
                self.statusBar().showMessage('File uploaded successfully！', 3000)
            except Exception as e:
                self.statusBar().showMessage(f'File processing failed: {e}', 3000)

    def upload_file(self):
        if self.label_2.isVisible():
            if self.training_sample_file is not None and self.virtual_sample_file is not None:
                file_contents = {
                    'training_sample': {
                        'training_sample_file': self.training_sample_file,
                        'training_sample_file_extension': self.training_sample_file_extension
                    },
                    'virtual_sample': {
                        'virtual_sample_file': self.virtual_sample_file,
                        'virtual_sample_file_extension': self.virtual_sample_file_extension
                    }
                }
                self.files_uploaded.emit(file_contents)
                self.close()
            else:
                self.statusBar().showMessage("Please upload two suitable files first！", 3000)
        else:
            if self.training_sample_file is not None:
                file_contents = {
                    'training_sample': {
                        'training_sample_file': self.training_sample_file,
                        'training_sample_file_extension': self.training_sample_file_extension
                    }
                }
                self.files_uploaded.emit(file_contents)
                self.close()
            else:
                self.statusBar().showMessage("Please upload suitable file first！", 3000)

class DownloadWindow(QMainWindow, Ui_DownloadWindow):
    def __init__(self):
        super(DownloadWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Download')

        self.browseDownloadVirtualSampleFileButton.clicked.connect(self.browse_download_path)
        self.okDownloadButton.clicked.connect(self.download_file)
        self.cancelDownloadButton.clicked.connect(self.close)

        self.download_virtual_sample_file_path = None
        self.virtual_sample = None

    def browse_download_path(self):
        options = QFileDialog.Options()
        # 获取文件夹路径
        self.download_virtual_sample_file_path = QFileDialog.getExistingDirectory(self, "选择保存 CSV 文件的文件夹", options=options)
        if self.download_virtual_sample_file_path:
            self.downloadVirtualSampleFilePath.setText(self.download_virtual_sample_file_path)
    def get_virtual_sample(self, virtual_sample):
        self.virtual_sample = virtual_sample

    def download_file(self):
        if self.download_virtual_sample_file_path:
            download_path = os.path.join(self.download_virtual_sample_file_path, 'virtual_sample.xlsx')
            self.virtual_sample.to_excel(download_path, index=False)
            self.statusBar().showMessage("Download file successfully！", 1000)
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the download path of the file！")
            return

class ShowWindow(QMainWindow, Ui_ShowWindow):
    def __init__(self):
        super(ShowWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Show')

        self.exportWindow = ExportWindow()

        # 创建QGraphicsScene
        self.scene_element = QGraphicsScene(self)
        self.exportButton.clicked.connect(self.open_export_window)
        self.trainingSampleGraphicsView.setScene(self.scene_element)


        self.buttonGroup = None
        self.training_sample = {}
        self.elements = []

    def get_training_sample(self, training_sample):
        self.training_sample = training_sample
        if self.training_sample is not None:
            self.show_training_sample()
            self.first_element_checked()

    def open_export_window(self):
        if self.training_sample is None:
            QMessageBox.warning(self, "Warning", "Please enter training sample first！")
            return
        self.exportWindow.get_training_sample(self.training_sample)
        self.exportWindow.show()

    def show_training_sample(self):
        scroll_content = QWidget()
        layout = QVBoxLayout(scroll_content)

        # 定义元素列表
        self.elements = list(self.training_sample.columns)
        self.elements.append('Numerical Features')
        self.elements.append('Pred v.s. Label (waiting)')

        self.buttonGroup = QButtonGroup(scroll_content)
        self.buttonGroup.buttonClicked[int].connect(self.on_radio_button_clicked)

        for index, element in enumerate(self.elements):
            radioButton = QRadioButton(element)
            layout.addWidget(radioButton)
            if index == 0:
                radioButton.setChecked(True)
            self.buttonGroup.addButton(radioButton, index)

        # 设置QScrollArea的内容
        self.showTrainingSampleScrollArea.setWidget(scroll_content)
        self.showTrainingSampleScrollArea.setWidgetResizable(True)

    def on_radio_button_clicked(self, idx):
        self.scene_element.clear()
        self.plot_data(idx)

    def plot_data(self, index):
        data_features = self.training_sample.iloc[:, :-1]
        labels = self.training_sample.iloc[:, -1]
        column = self.elements[index]
        # 设置绘图风格和字体
        sns.set(style="ticks", context="paper")
        # matplotlib.rcParams['font.family'] = ['Arial Unicode MS']  # 设置字体为支持中文
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        plt.rcParams['font.size'] = 12  # 设置全局字体大小
        plt.rcParams['axes.titlesize'] = 18  # 设置标题字体大小
        plt.rcParams['axes.labelsize'] = 15  # 设置轴标签字体大小
        plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度字体大小
        plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度字体大小

        # 创建一个matplotlib Figure
        fig, ax = plt.subplots(figsize=(7.5, 4.5))

        if 0 <= index <= len(self.elements) - 4:
            # 绘制柱状图或直方图
            if pd.api.types.is_numeric_dtype(data_features[column]):
                sns.histplot(data=data_features, x=column, kde=True, color='skyblue', bins=30, edgecolor='black', ax=ax)
                ax.set_title(f"{column} Distribution", fontsize=18)
                ax.set_xlabel(column, fontsize=15)
                ax.set_ylabel('Frequency', fontsize=15)
            else:
                sns.countplot(data=data_features, x=column, palette="viridis", ax=ax)
                ax.set_title(f"{column} Count", fontsize=18)
                ax.set_xlabel(column, fontsize=15)
                ax.set_ylabel('Count', fontsize=15)
            ax.tick_params(axis='x', rotation=45, labelsize=12)
            ax.tick_params(axis='y', labelsize=12)
            sns.despine(trim=True)
            plt.tight_layout()
        elif index == len(self.elements) - 3:
            # 标签列的统计分析
            sns.countplot(x=labels, hue=labels, palette="Set2", legend=False, ax=ax)
            ax.set_title('Distribution of label columns', fontsize=18)
            ax.set_xlabel('Label', fontsize=15)
            ax.set_ylabel('Count', fontsize=15)
            ax.tick_params(axis='x', rotation=45, labelsize=12)
            ax.tick_params(axis='y', labelsize=12)
            sns.despine(trim=True)
            plt.tight_layout()
        elif index == len(self.elements) - 2:
            # 绘制箱线图以展示数值列的分布情况
            numeric_columns = data_features.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_columns) > 0:
                sns.boxplot(data=data_features[numeric_columns], orient='h', palette="vlag", ax=ax)
                ax.set_title('Boxplots for numerical features', fontsize=18)
                ax.set_xlabel('Value', fontsize=15)
                ax.set_ylabel('Feature', fontsize=15)
                ax.tick_params(axis='x', labelsize=12)
                ax.tick_params(axis='y', labelsize=12)
                sns.despine(trim=True)
                plt.tight_layout()
        elif index == len(self.elements) - 1:
            fig = self.pre_scatter()

        # 将matplotlib Figure转换为FigureCanvas
        canvas = FigureCanvas(fig)
        self.scene_element.addWidget(canvas)

    def pre_scatter(self):
        data = self.training_sample
        X = data.iloc[:, :-1]
        Y = data.iloc[:, -1]

        X = np.array(X)
        Y = np.array(Y)

        loo = LeaveOneOut()
        loo.get_n_splits(X)

        ypre = []
        yvar = []

        KErnel = RBF() + WhiteKernel()
        for train_index, test_index in loo.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = Y[train_index], Y[test_index]
            model = GaussianProcessRegressor(kernel=KErnel, n_restarts_optimizer=10, alpha=0, normalize_y=True,
                                             random_state=0).fit(X_train, y_train)
            y_pre, y_var = model.predict(X_test, return_std=True)
            ypre.append(y_pre[0])
            yvar.append(y_var[0])
        y = Y
        ypre = np.array(ypre)
        plt.rcParams.update({
            'font.size': 16,
            'axes.labelsize': 20,
            'axes.titlesize': 24,
            'legend.fontsize': 16,
            'xtick.labelsize': 16,
            'ytick.labelsize': 16,
            'axes.linewidth': 2,
            'xtick.major.size': 8,
            'ytick.major.size': 8,
            'xtick.major.width': 2,
            'ytick.major.width': 2,
            'lines.linewidth': 2.5,
            'lines.markersize': 10,
            'axes.grid': True,
            'grid.alpha': 0.8,
            'grid.linestyle': '--',
            'grid.linewidth': 1,
            'figure.figsize': (12, 12)
        })
        fig, ax = plt.subplots(figsize=(4.7, 4.7))
        sns.set(style="whitegrid")

        ax.scatter(y, ypre, marker='o', s=150, edgecolor='k', color='#1f77b4', alpha=0.8)

        gap = (y.max() - y.min()) * 0.05
        ax.plot([y.min() - gap, y.max() + gap], [y.min() - gap, y.max() + gap], '--', color='k', linewidth=2.5)

        ax.set_title('Model Predictions vs True Values', fontsize=18)
        ax.set_xlabel('True Values', fontsize=14)
        ax.set_ylabel('Predicted Values', fontsize=14)

        ax.text(0.05, 0.95, 'Correlation Coefficient: {:.2f}'.format(np.corrcoef(y, ypre)[0, 1]), fontsize=12,
                color='black', transform=ax.transAxes)
        ax.text(0.05, 0.9, 'RMSE: {:.2f}'.format(np.sqrt(np.mean((y - ypre) ** 2))), fontsize=12, color='black',
                transform=ax.transAxes)

        ax.set_xlim(y.min() - gap, y.max() + gap)
        ax.set_ylim(y.min() - gap, y.max() + gap)
        ax.set_aspect('equal', adjustable='box')

        fig.tight_layout()
        return fig
    def first_element_checked(self):
        self.buttonGroup.button(0).setChecked(True)
        self.scene_element.clear()

        data_features = self.training_sample.iloc[:, :-1]
        column = self.elements[0]
        # 设置绘图风格和字体
        sns.set(style="ticks", context="paper")
        plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
        plt.rcParams['font.size'] = 12  # 设置全局字体大小
        plt.rcParams['axes.titlesize'] = 18  # 设置标题字体大小
        plt.rcParams['axes.labelsize'] = 15  # 设置轴标签字体大小
        plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度字体大小
        plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度字体大小

        # 创建一个matplotlib Figure
        fig, ax = plt.subplots(figsize=(7.5, 4.5))

        # 绘制柱状图或直方图
        if pd.api.types.is_numeric_dtype(data_features[column]):
            sns.histplot(data=data_features, x=column, kde=True, color='skyblue', bins=30, edgecolor='black', ax=ax)
            ax.set_title(f"{column} Distribution", fontsize=18)
            ax.set_xlabel(column, fontsize=15)
            ax.set_ylabel('Frequency', fontsize=15)
        else:
            sns.countplot(data=data_features, x=column, palette="viridis", ax=ax)
            ax.set_title(f"{column} Count", fontsize=18)
            ax.set_xlabel(column, fontsize=15)
            ax.set_ylabel('Count', fontsize=15)
        ax.tick_params(axis='x', rotation=45, labelsize=12)
        ax.tick_params(axis='y', labelsize=12)
        sns.despine(trim=True)
        plt.tight_layout()
        # 将matplotlib Figure转换为FigureCanvas
        canvas = FigureCanvas(fig)
        self.scene_element.addWidget(canvas)

class ExportWindow(QMainWindow, Ui_ExportWindow):
    def __init__(self):
        super(ExportWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Export')

        self.browseExportTrainingSampleFileButton.clicked.connect(self.browse_export_path)
        self.okExportButton.clicked.connect(self.export)
        self.cancelExportButton.clicked.connect(self.close)

        self.training_sample = None
        self.export_training_sample_path = None
    def browse_export_path(self):
        options = QFileDialog.Options()
        # 获取文件夹路径
        self.export_training_sample_path = QFileDialog.getExistingDirectory(self, "选择保存图片文件的文件夹", options=options)
        if self.export_training_sample_path:
            self.exportTrainingSamplePath.setText(self.export_training_sample_path)
    def get_training_sample(self, training_sample):
        self.training_sample = training_sample

    def pre_scatter(self):
        data = self.training_sample
        X = data.iloc[:, :-1]
        Y = data.iloc[:, -1]

        X = np.array(X)
        Y = np.array(Y)

        loo = LeaveOneOut()
        loo.get_n_splits(X)

        ypre = []
        yvar = []

        KErnel = RBF() + WhiteKernel()
        for train_index, test_index in loo.split(X):
            X_train, X_test = X[train_index], X[test_index]
            y_train, y_test = Y[train_index], Y[test_index]
            model = GaussianProcessRegressor(kernel=KErnel, n_restarts_optimizer=10, alpha=0, normalize_y=True,
                                             random_state=0).fit(X_train, y_train)
            y_pre, y_var = model.predict(X_test, return_std=True)
            ypre.append(y_pre[0])
            yvar.append(y_var[0])
        y = Y
        ypre = np.array(ypre)

        plt.rcParams.update({
            'font.size': 16,
            'axes.labelsize': 20,
            'axes.titlesize': 24,
            'legend.fontsize': 16,
            'xtick.labelsize': 16,
            'ytick.labelsize': 16,
            'axes.linewidth': 2,
            'xtick.major.size': 8,
            'ytick.major.size': 8,
            'xtick.major.width': 2,
            'ytick.major.width': 2,
            'lines.linewidth': 2.5,
            'lines.markersize': 10,
            'axes.grid': True,
            'grid.alpha': 0.8,
            'grid.linestyle': '--',
            'grid.linewidth': 1,
            'figure.figsize': (12, 12)
        })
        fig, ax = plt.subplots(figsize=(8, 8))


        sns.set(style="whitegrid")

        ax.scatter(y, ypre, marker='o', s=150, edgecolor='k', color='#1f77b4', alpha=0.8)

        gap = (y.max() - y.min()) * 0.05
        ax.plot([y.min() - gap, y.max() + gap], [y.min() - gap, y.max() + gap], '--', color='k', linewidth=2.5)

        ax.set_title('Model Predictions vs True Values', fontsize=24)
        ax.set_xlabel('True Values', fontsize=18)
        ax.set_ylabel('Predicted Values', fontsize=18)

        ax.text(0.05, 0.95, 'Correlation Coefficient: {:.2f}'.format(np.corrcoef(y, ypre)[0, 1]), fontsize=18,
                color='black', transform=ax.transAxes)
        ax.text(0.05, 0.9, 'RMSE: {:.2f}'.format(np.sqrt(np.mean((y - ypre) ** 2))), fontsize=18, color='black',
                transform=ax.transAxes)

        ax.set_xlim(y.min() - gap, y.max() + gap)
        ax.set_ylim(y.min() - gap, y.max() + gap)
        ax.set_aspect('equal', adjustable='box')

        fig.tight_layout()
        return fig

    def export(self):
        if self.export_training_sample_path is not None:
            if self.training_sample is None:
                QMessageBox.warning(self, "Warning", "Please enter the training sample file！")
                return
            # 得到数据
            data_features = self.training_sample.iloc[:, :-1]
            labels = self.training_sample.iloc[:, -1]
            save_dir = self.export_training_sample_path
            # 设置绘图风格和字体
            sns.set(style="ticks", context="paper")
            # matplotlib.rcParams['font.family'] = ['Arial Unicode MS']  # 设置字体为支持中文
            plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
            plt.rcParams['font.size'] = 12  # 设置全局字体大小
            plt.rcParams['axes.titlesize'] = 18  # 设置标题字体大小
            plt.rcParams['axes.labelsize'] = 15  # 设置轴标签字体大小
            plt.rcParams['xtick.labelsize'] = 12  # 设置x轴刻度字体大小
            plt.rcParams['ytick.labelsize'] = 12  # 设置y轴刻度字体大小

            # 对每一列进行统计分析并绘制图表
            name = 1
            for column in data_features.columns:
                fig, ax = plt.subplots(figsize=(10, 6))
                # 绘制柱状图或直方图
                if pd.api.types.is_numeric_dtype(data_features[column]):
                    sns.histplot(data=data_features, x=column, kde=True, color='skyblue', bins=30, edgecolor='black',
                                 ax=ax)
                    ax.set_title(f"{column} Distribution", fontsize=18)
                    ax.set_xlabel(column, fontsize=15)
                    ax.set_ylabel('Frequency', fontsize=15)
                else:
                    sns.countplot(data=data_features, x=column, palette="viridis", ax=ax)
                    ax.set_title(f"{column} Count", fontsize=18)
                    ax.set_xlabel(column, fontsize=15)
                    ax.set_ylabel('Count', fontsize=15)
                ax.tick_params(axis='x', rotation=45, labelsize=12)
                ax.tick_params(axis='y', labelsize=12)
                sns.despine(trim=True)
                plt.tight_layout()
                # 保存图表到文件
                try:
                    fig.savefig(os.path.join(save_dir, f"{column}_analysis.png"))
                except:
                    # 防止部分特征命名不规范导致保存错误，命名为备选数字
                    fig.savefig(os.path.join(save_dir, f"{name}_analysis.png"))
                    name += 1
                plt.close(fig)
            # 标签列的统计分析
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(x=labels, hue=labels, palette="Set2", legend=False, ax=ax)
            ax.set_title('Distribution of label columns', fontsize=18)
            ax.set_xlabel('Label', fontsize=15)
            ax.set_ylabel('Count', fontsize=15)
            ax.tick_params(axis='x', rotation=45, labelsize=12)
            ax.tick_params(axis='y', labelsize=12)
            sns.despine(trim=True)
            plt.tight_layout()
            fig.savefig(os.path.join(save_dir, "label_distribution.png"))
            plt.close(fig)
            # 绘制箱线图以展示数值列的分布情况
            numeric_columns = data_features.select_dtypes(include=['float64', 'int64']).columns
            if len(numeric_columns) > 0:
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.boxplot(data=data_features[numeric_columns], orient='h', palette="vlag", ax=ax)
                ax.set_title('Boxplots for numerical features', fontsize=18)
                ax.set_xlabel('Value', fontsize=15)
                ax.set_ylabel('Feature', fontsize=15)
                ax.tick_params(axis='x', labelsize=12)
                ax.tick_params(axis='y', labelsize=12)
                sns.despine(trim=True)
                plt.tight_layout()
                fig.savefig(os.path.join(save_dir, "label_distribution.png"))
                plt.close(fig)

            # contrast
            fig = self.pre_scatter()
            fig.savefig(os.path.join(save_dir, "contrast.png"), dpi=500, bbox_inches='tight')
            plt.close(fig)

            self.statusBar().showMessage("Export successfully！", 1000)
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Please enter the export path！")
            return

class ResultWindow(QMainWindow, Ui_ResultWindow):
    def __init__(self):
        super(ResultWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Result')


class ParameterWindow(QMainWindow, Ui_ParameterWindow):
    parameters_uploaded = pyqtSignal(dict)

    def __init__(self):
        super(ParameterWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Parameter")

        # 变量
        self.regression_default_setting = {
            'opt_num': 1,
            'min_search': True,
            'Dynamic_W': False,
            'function': {
                'EI': {
                    'name': 'Expected improvement method'
                },
                'EI_plugin': {
                    'name': 'Expected improvement with "plugin" method'
                },
                'Augmented_EI': {
                    'name': 'Augmented Expected Improvement method',
                    'alpha': 1,
                    'alpha_recommend': 'recommended [0,3]',
                    'tao': 0,
                    'tao_recommend': 'recommended [0,1]'
                },
                'EQI': {
                    'name': 'Expected Quantile Improvement method',
                    'beta': 0.5,
                    'beta_recommend': 'recommended [0.2,0.8]',
                    'tao_new': 0,
                    'tao_new_recommend': 'recommended [0,1]'
                },
                'Reinterpolation_EI': {
                    'name': 'Reinterpolation Expected Improvement method'
                },
                'UCB': {
                    'name': 'Upper confidence bound method',
                    'alpha': 1,
                    'alpha_recommend': 'recommended [0,3]'
                },
                'PoI': {
                    'name': 'Probability of Improvement method',
                    'tao': 0,
                    'tao_recommend': 'recommended [0,0.3]'
                },
                'PES': {
                    'name': 'Predictive Entropy Search method',
                    'sam_num': 500,
                    'sam_num_recommend': 'recommended [100,1000]'
                },
                'Knowledge_G': {
                    'name': 'Knowledge gradient method',
                    'MC_num': 50,
                    'MC_num_recommend': 'recommended [50,300]'
                }
            }
        }

        self.classification_default_setting = {
            'classifier': ['GaussianProcess', 'LogisticRegression', 'NaiveBayes', 'SVM', 'RandomForest'],
            'opt_num': 1,
            'min_search': True,
            'Dynamic_W': False,
            'function': {
                'Least_cfd': 'Least Confidence method',
                'Margin_S': 'Margin Sampling method',
                'Entropy': 'Entropy-based approach'
            }
        }

        self.setting = {}
        self.initialize()


        self.regressionRadioButton.clicked.connect(self.switch_tab_module)
        self.classificationRadioButton.clicked.connect(self.switch_tab_module)
        self.tabWidget.currentChanged.connect(self.switch_button_module)
        self.regressionFunctionComboBox.currentIndexChanged.connect(self.change_regression_function)
        self.setParametersButton.clicked.connect(self.set_parameters)
        self.resetParametersButton.clicked.connect(self.reset_parameters)
    # 初始化
    def initialize(self):

        self.regressionRadioButton.setChecked(True)
        self.tabWidget.setCurrentIndex(0)

        self.regressionFunctionComboBox.addItems(self.regression_default_setting['function'].keys())
        self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['EI']['name'])
        self.regression_opt_num_SpinBox.setValue(self.regression_default_setting['opt_num'])
        self.regression_min_search_TrueRadioButton.setChecked(self.regression_default_setting['min_search'])
        if self.regression_default_setting['Dynamic_W']:
            self.regression_Dynamic_W_TrueRadioButton.setChecked(True)
        else:
            self.regression_Dynamic_W_FalseRadioButton.setChecked(True)

        self.parameterLabel.setVisible(False)
        self.regressionParameter1Widget.setVisible(False)
        self.regressionParameter2Widget.setVisible(False)

        self.classificationClassifierComboBox.addItems(self.classification_default_setting['classifier'])
        self.classificationFunctionComboBox.addItems(self.classification_default_setting['function'].keys())
        self.classification_opt_num_SpinBox.setValue(self.classification_default_setting['opt_num'])
        self.classification_min_search_TrueRadioButton.setChecked(self.classification_default_setting['min_search'])
        if self.classification_default_setting['Dynamic_W']:
            self.classification_Dynamic_W_TrueRadioButton.setChecked(True)
        else:
            self.classification_Dynamic_W_FalseRadioButton.setChecked(True)

    def switch_tab_module(self):
        if self.regressionRadioButton.isChecked():
            self.tabWidget.setCurrentIndex(0)
        else:
            self.tabWidget.setCurrentIndex(1)
    def switch_button_module(self):
        if self.tabWidget.currentIndex() == 0:
            self.regressionRadioButton.setChecked(True)
        else:
            self.classificationRadioButton.setChecked(True)

    def change_regression_function(self):
        if self.regressionFunctionComboBox.currentText() == 'EI':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['EI']['name'])
            self.parameterLabel.setVisible(False)
            self.regressionParameter1Widget.setVisible(False)
            self.regressionParameter2Widget.setVisible(False)
        elif self.regressionFunctionComboBox.currentText() == 'EI_plugin':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['EI_plugin']['name'])
            self.parameterLabel.setVisible(False)
            self.regressionParameter1Widget.setVisible(False)
            self.regressionParameter2Widget.setVisible(False)
        elif self.regressionFunctionComboBox.currentText() == 'Augmented_EI':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['Augmented_EI']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(True)
            self.parameter1Label.setText('alpha')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['Augmented_EI']['alpha']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['Augmented_EI']['alpha_recommend'])
            self.parameter2Label.setText('tao')
            self.parameter2LineEdit.setText(str(self.regression_default_setting['function']['Augmented_EI']['tao']))
            self.parameter2RecommendLabel.setText(self.regression_default_setting['function']['Augmented_EI']['tao_recommend'])
        elif self.regressionFunctionComboBox.currentText() == 'EQI':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['EQI']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(True)
            self.parameter1Label.setText('beta')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['EQI']['beta']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['EQI']['beta_recommend'])
            self.parameter2Label.setText('tao_new')
            self.parameter2LineEdit.setText(str(self.regression_default_setting['function']['EQI']['tao_new']))
            self.parameter2RecommendLabel.setText(self.regression_default_setting['function']['EQI']['tao_new_recommend'])
        elif self.regressionFunctionComboBox.currentText() == 'Reinterpolation_EI':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['Reinterpolation_EI']['name'])
            self.parameterLabel.setVisible(False)
            self.regressionParameter1Widget.setVisible(False)
            self.regressionParameter2Widget.setVisible(False)
        elif self.regressionFunctionComboBox.currentText() == 'UCB':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['UCB']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(False)
            self.parameter1Label.setText('alpha')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['UCB']['alpha']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['UCB']['alpha_recommend'])
        elif self.regressionFunctionComboBox.currentText() == 'PoI':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['PoI']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(False)
            self.parameter1Label.setText('tao')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['PoI']['tao']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['PoI']['tao_recommend'])
        elif self.regressionFunctionComboBox.currentText() == 'PES':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['PES']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(False)
            self.parameter1Label.setText('sam_num')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['PES']['sam_num']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['PES']['sam_num_recommend'])
        elif self.regressionFunctionComboBox.currentText() == 'Knowledge_G':
            self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['Knowledge_G']['name'])
            self.parameterLabel.setVisible(True)
            self.regressionParameter1Widget.setVisible(True)
            self.regressionParameter2Widget.setVisible(False)
            self.parameter1Label.setText('MC_num')
            self.parameter1LineEdit.setText(str(self.regression_default_setting['function']['Knowledge_G']['MC_num']))
            self.parameter1RecommendLabel.setText(self.regression_default_setting['function']['Knowledge_G']['MC_num_recommend'])

    def set_parameters(self):
        if self.regressionRadioButton.isChecked():
            self.setting['module'] = 'regression'
            self.setting['opt_num'] = self.regression_opt_num_SpinBox.value()
            self.setting['min_search'] = self.regression_min_search_TrueRadioButton.isChecked()
            self.setting['Dynamic_W'] = self.regression_Dynamic_W_TrueRadioButton.isChecked()
            function = str(self.regressionFunctionComboBox.currentText())
            self.setting['function'] = function
            if function in ['UCB', 'PoI', 'PES', 'Knowledge_G']:
                parameter1 = str(self.parameter1LineEdit.text())
                if re.fullmatch(r'[+-]?(\d+(\.\d*)?|\.\d+)', parameter1):
                    self.setting['parameter1'] = parameter1
                else:
                    QMessageBox.warning(self, "Warning", "Please re-enter the parameter number！")
                    return
            if function in ['Augmented_EI', 'EQI']:
                parameter1 = str(self.parameter1LineEdit.text())
                parameter2 = str(self.parameter2LineEdit.text())
                if re.fullmatch(r'[+-]?(\d+(\.\d*)?|\.\d+)', parameter1) and re.fullmatch(r'[+-]?(\d+(\.\d*)?|\.\d+)', parameter2):
                    self.setting['parameter1'] = parameter1
                    self.setting['parameter2'] = parameter2
                else:
                    QMessageBox.warning(self, "Warning", "Please re-enter the parameter number！")
                    return
        else:
            self.setting['module'] = 'classification'
            self.setting['classifier'] = self.classificationClassifierComboBox.currentText()
            self.setting['opt_num'] = self.classification_opt_num_SpinBox.value()
            self.setting['min_search'] = self.classification_min_search_TrueRadioButton.isChecked()
            self.setting['Dynamic_W'] = self.classification_Dynamic_W_TrueRadioButton.isChecked()
            self.setting['function'] = self.classificationFunctionComboBox.currentText()
        self.parameters_uploaded.emit(self.setting)
        self.close()

    def reset_parameters(self):
        self.regressionFunctionComboBox.setCurrentIndex(0)
        self.regressionFunctionNameLabel.setText(self.regression_default_setting['function']['EI']['name'])
        self.regression_opt_num_SpinBox.setValue(self.regression_default_setting['opt_num'])
        self.regression_min_search_TrueRadioButton.setChecked(self.regression_default_setting['min_search'])
        if self.regression_default_setting['Dynamic_W']:
            self.regression_Dynamic_W_TrueRadioButton.setChecked(True)
        else:
            self.regression_Dynamic_W_FalseRadioButton.setChecked(True)
        self.parameterLabel.setVisible(False)
        self.regressionParameter1Widget.setVisible(False)
        self.regressionParameter2Widget.setVisible(False)

        self.classification_opt_num_SpinBox.setValue(self.classification_default_setting['opt_num'])
        self.classification_min_search_TrueRadioButton.setChecked(self.classification_default_setting['min_search'])
        if self.classification_default_setting['Dynamic_W']:
            self.classification_Dynamic_W_TrueRadioButton.setChecked(True)
        else:
            self.classification_Dynamic_W_FalseRadioButton.setChecked(True)
        self.classificationClassifierComboBox.setCurrentIndex(0)
        self.classificationFunctionComboBox.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())