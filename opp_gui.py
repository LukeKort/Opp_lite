# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opp_gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1350, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1350, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1350, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons_images/icons/opp.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Opp_title = QtWidgets.QLabel(self.centralwidget)
        self.Opp_title.setGeometry(QtCore.QRect(20, -20, 301, 211))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 255, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 227, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 133, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 227, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 255, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 227, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 133, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 227, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(135, 255, 55))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(110, 227, 31))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 133, 5))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(42, 100, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 200, 8))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.Opp_title.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(48)
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(50)
        self.Opp_title.setFont(font)
        self.Opp_title.setObjectName("Opp_title")
        self.help_button = QtWidgets.QPushButton(self.centralwidget)
        self.help_button.setGeometry(QtCore.QRect(1280, 10, 51, 51))
        self.help_button.setStyleSheet("border-image: url(:/icons_images/icons/help_button.png);")
        self.help_button.setText("")
        self.help_button.setObjectName("help_button")
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(960, 70, 361, 381))
        self.console.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.console.setObjectName("console")
        self.edit_function_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_function_button.setGeometry(QtCore.QRect(970, 510, 201, 91))
        self.edit_function_button.setAcceptDrops(False)
        self.edit_function_button.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-image: url(:/icons_images/icons/edit_function_icon.png);")
        self.edit_function_button.setText("")
        self.edit_function_button.setObjectName("edit_function_button")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setGeometry(QtCore.QRect(1200, 500, 111, 101))
        self.play_button.setMouseTracking(False)
        self.play_button.setStyleSheet("border-image: url(:/icons_images/icons/start_button.png);")
        self.play_button.setText("")
        self.play_button.setDefault(True)
        self.play_button.setObjectName("play_button")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(50, 180, 201, 431))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.verticalLayoutWidget_4.setFont(font)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.alcateia = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.alcateia.setFont(font)
        self.alcateia.setAcceptDrops(False)
        self.alcateia.setToolTip("")
        self.alcateia.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.alcateia.setAutoExclusive(False)
        self.alcateia.setObjectName("alcateia")
        self.verticalLayout_4.addWidget(self.alcateia)
        self.pso = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pso.setFont(font)
        self.pso.setAcceptDrops(False)
        self.pso.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pso.setAutoExclusive(False)
        self.pso.setObjectName("pso")
        self.verticalLayout_4.addWidget(self.pso)
        self.jaakola = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.jaakola.setFont(font)
        self.jaakola.setAcceptDrops(False)
        self.jaakola.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.jaakola.setAutoExclusive(False)
        self.jaakola.setObjectName("jaakola")
        self.verticalLayout_4.addWidget(self.jaakola)
        self.grad_desc_stoc = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.grad_desc_stoc.setFont(font)
        self.grad_desc_stoc.setAcceptDrops(False)
        self.grad_desc_stoc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.grad_desc_stoc.setAutoExclusive(False)
        self.grad_desc_stoc.setObjectName("grad_desc_stoc")
        self.verticalLayout_4.addWidget(self.grad_desc_stoc)
        self.pca = QtWidgets.QRadioButton(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pca.setFont(font)
        self.pca.setAcceptDrops(False)
        self.pca.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pca.setAutoExclusive(False)
        self.pca.setObjectName("pca")
        self.verticalLayout_4.addWidget(self.pca)
        self.export_results_cvs = QtWidgets.QCheckBox(self.centralwidget)
        self.export_results_cvs.setGeometry(QtCore.QRect(1020, 460, 241, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.export_results_cvs.setFont(font)
        self.export_results_cvs.setObjectName("export_results_cvs")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(730, 110, 151, 491))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.n_iterations = QtWidgets.QLineEdit(self.layoutWidget)
        self.n_iterations.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_iterations.setFont(font)
        self.n_iterations.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_iterations.setAlignment(QtCore.Qt.AlignCenter)
        self.n_iterations.setObjectName("n_iterations")
        self.verticalLayout_3.addWidget(self.n_iterations)
        self.n_particles = QtWidgets.QLineEdit(self.layoutWidget)
        self.n_particles.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_particles.setFont(font)
        self.n_particles.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_particles.setAlignment(QtCore.Qt.AlignCenter)
        self.n_particles.setObjectName("n_particles")
        self.verticalLayout_3.addWidget(self.n_particles)
        self.n_tolerance = QtWidgets.QLineEdit(self.layoutWidget)
        self.n_tolerance.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.n_tolerance.setFont(font)
        self.n_tolerance.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.n_tolerance.setAlignment(QtCore.Qt.AlignCenter)
        self.n_tolerance.setObjectName("n_tolerance")
        self.verticalLayout_3.addWidget(self.n_tolerance)
        self.vector_inf_limit = QtWidgets.QLineEdit(self.layoutWidget)
        self.vector_inf_limit.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_inf_limit.setFont(font)
        self.vector_inf_limit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_inf_limit.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_inf_limit.setObjectName("vector_inf_limit")
        self.verticalLayout_3.addWidget(self.vector_inf_limit)
        self.vector_sup_limit = QtWidgets.QLineEdit(self.layoutWidget)
        self.vector_sup_limit.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.vector_sup_limit.setFont(font)
        self.vector_sup_limit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.vector_sup_limit.setAlignment(QtCore.Qt.AlignCenter)
        self.vector_sup_limit.setObjectName("vector_sup_limit")
        self.verticalLayout_3.addWidget(self.vector_sup_limit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.alcateia_inner_circle = QtWidgets.QLineEdit(self.layoutWidget)
        self.alcateia_inner_circle.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.alcateia_inner_circle.setFont(font)
        self.alcateia_inner_circle.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.alcateia_inner_circle.setAlignment(QtCore.Qt.AlignCenter)
        self.alcateia_inner_circle.setObjectName("alcateia_inner_circle")
        self.horizontalLayout.addWidget(self.alcateia_inner_circle)
        self.alcatei_id = QtWidgets.QLineEdit(self.layoutWidget)
        self.alcatei_id.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.alcatei_id.setFont(font)
        self.alcatei_id.setAlignment(QtCore.Qt.AlignCenter)
        self.alcatei_id.setObjectName("alcatei_id")
        self.horizontalLayout.addWidget(self.alcatei_id)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.w_pso_only = QtWidgets.QLineEdit(self.layoutWidget)
        self.w_pso_only.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.w_pso_only.setFont(font)
        self.w_pso_only.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.w_pso_only.setAlignment(QtCore.Qt.AlignCenter)
        self.w_pso_only.setObjectName("w_pso_only")
        self.horizontalLayout_3.addWidget(self.w_pso_only)
        self.c1_pso_only = QtWidgets.QLineEdit(self.layoutWidget)
        self.c1_pso_only.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.c1_pso_only.setFont(font)
        self.c1_pso_only.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c1_pso_only.setAlignment(QtCore.Qt.AlignCenter)
        self.c1_pso_only.setObjectName("c1_pso_only")
        self.horizontalLayout_3.addWidget(self.c1_pso_only)
        self.c2_pso_only = QtWidgets.QLineEdit(self.layoutWidget)
        self.c2_pso_only.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.c2_pso_only.setFont(font)
        self.c2_pso_only.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.c2_pso_only.setAlignment(QtCore.Qt.AlignCenter)
        self.c2_pso_only.setObjectName("c2_pso_only")
        self.horizontalLayout_3.addWidget(self.c2_pso_only)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.inner_circle_lj_only = QtWidgets.QLineEdit(self.layoutWidget)
        self.inner_circle_lj_only.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.inner_circle_lj_only.setFont(font)
        self.inner_circle_lj_only.setAlignment(QtCore.Qt.AlignCenter)
        self.inner_circle_lj_only.setObjectName("inner_circle_lj_only")
        self.horizontalLayout_4.addWidget(self.inner_circle_lj_only)
        self.c_lj_only = QtWidgets.QLineEdit(self.layoutWidget)
        self.c_lj_only.setMinimumSize(QtCore.QSize(0, 49))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.c_lj_only.setFont(font)
        self.c_lj_only.setAlignment(QtCore.Qt.AlignCenter)
        self.c_lj_only.setObjectName("c_lj_only")
        self.horizontalLayout_4.addWidget(self.c_lj_only)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(360, 110, 361, 490))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.iterations_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.iterations_lb.setFont(font)
        self.iterations_lb.setObjectName("iterations_lb")
        self.verticalLayout_2.addWidget(self.iterations_lb)
        self.particles_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.particles_lb.setFont(font)
        self.particles_lb.setObjectName("particles_lb")
        self.verticalLayout_2.addWidget(self.particles_lb)
        self.tolerance_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.tolerance_lb.setFont(font)
        self.tolerance_lb.setObjectName("tolerance_lb")
        self.verticalLayout_2.addWidget(self.tolerance_lb)
        self.inf_limit_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.inf_limit_lb.setFont(font)
        self.inf_limit_lb.setObjectName("inf_limit_lb")
        self.verticalLayout_2.addWidget(self.inf_limit_lb)
        self.sup_limit_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.sup_limit_lb.setFont(font)
        self.sup_limit_lb.setObjectName("sup_limit_lb")
        self.verticalLayout_2.addWidget(self.sup_limit_lb)
        self.alcateia_only_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.alcateia_only_lb.setFont(font)
        self.alcateia_only_lb.setObjectName("alcateia_only_lb")
        self.verticalLayout_2.addWidget(self.alcateia_only_lb)
        self.pso_only_lb = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.pso_only_lb.setFont(font)
        self.pso_only_lb.setObjectName("pso_only_lb")
        self.verticalLayout_2.addWidget(self.pso_only_lb)
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Opp_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; font-weight:600; color:#92d050;\">Opp!</span></p></body></html>"))
        self.alcateia.setText(_translate("MainWindow", "Alcateia"))
        self.pso.setText(_translate("MainWindow", "PSO"))
        self.jaakola.setText(_translate("MainWindow", "Jaakola"))
        self.grad_desc_stoc.setText(_translate("MainWindow", "GDS"))
        self.pca.setText(_translate("MainWindow", "PCA"))
        self.export_results_cvs.setText(_translate("MainWindow", "Save results to a CSV file"))
        self.n_iterations.setText(_translate("MainWindow", "1"))
        self.n_particles.setText(_translate("MainWindow", "1"))
        self.n_tolerance.setText(_translate("MainWindow", "0"))
        self.vector_inf_limit.setText(_translate("MainWindow", "0"))
        self.vector_sup_limit.setText(_translate("MainWindow", "0"))
        self.alcateia_inner_circle.setText(_translate("MainWindow", "1"))
        self.alcatei_id.setText(_translate("MainWindow", "0"))
        self.w_pso_only.setText(_translate("MainWindow", "0"))
        self.c1_pso_only.setText(_translate("MainWindow", "0"))
        self.c2_pso_only.setText(_translate("MainWindow", "0"))
        self.inner_circle_lj_only.setText(_translate("MainWindow", "1"))
        self.c_lj_only.setText(_translate("MainWindow", "0"))
        self.iterations_lb.setText(_translate("MainWindow", "N° of iterations"))
        self.particles_lb.setText(_translate("MainWindow", "N° of particles"))
        self.tolerance_lb.setText(_translate("MainWindow", "Tolerance"))
        self.inf_limit_lb.setText(_translate("MainWindow", "Inf. limit - x,..,z"))
        self.sup_limit_lb.setText(_translate("MainWindow", "Sup. limit - x,...,z"))
        self.alcateia_only_lb.setText(_translate("MainWindow", "Alcateia - inner cicles, id"))
        self.pso_only_lb.setText(_translate("MainWindow", "PSO - w, c1, c2"))
        self.label.setText(_translate("MainWindow", "Jaakola - inner cicle, c"))

import icon_rc
