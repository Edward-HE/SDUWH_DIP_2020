# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DLMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DLMainWindow(object):
    def setupUi(self, DLMainWindow):
        DLMainWindow.setObjectName("DLMainWindow")
        DLMainWindow.resize(1333, 579)
        self.centralwidget = QtWidgets.QWidget(DLMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.ImgShowWidget = QtWidgets.QWidget(self.centralwidget)
        self.ImgShowWidget.setObjectName("ImgShowWidget")
        self.splitter = QtWidgets.QSplitter(self.ImgShowWidget)
        self.splitter.setGeometry(QtCore.QRect(64, 134, 154, 17))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.SrcImgLabel = QtWidgets.QLabel(self.splitter)
        self.SrcImgLabel.setObjectName("SrcImgLabel")
        self.DstImgLabel = QtWidgets.QLabel(self.splitter)
        self.DstImgLabel.setObjectName("DstImgLabel")
        self.gridLayout.addWidget(self.ImgShowWidget, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)
        self.LabCtrlWidget = QtWidgets.QWidget(self.centralwidget)
        self.LabCtrlWidget.setMinimumSize(QtCore.QSize(350, 0))
        self.LabCtrlWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.LabCtrlWidget.setObjectName("LabCtrlWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.LabCtrlWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.LabCtrlWidget)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.ExpTypeComboBox = QtWidgets.QComboBox(self.LabCtrlWidget)
        self.ExpTypeComboBox.setObjectName("ExpTypeComboBox")
        self.horizontalLayout_2.addWidget(self.ExpTypeComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.LabCtrlWidget)
        self.label_3.setMinimumSize(QtCore.QSize(80, 0))
        self.label_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.ExpImgLineEdit = QtWidgets.QLineEdit(self.LabCtrlWidget)
        self.ExpImgLineEdit.setEnabled(True)
        self.ExpImgLineEdit.setObjectName("ExpImgLineEdit")
        self.horizontalLayout_3.addWidget(self.ExpImgLineEdit)
        self.SelectImgPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.SelectImgPushButton.setObjectName("SelectImgPushButton")
        self.horizontalLayout_3.addWidget(self.SelectImgPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_info = QtWidgets.QLabel(self.LabCtrlWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy)
        self.label_info.setObjectName("label_info")
        self.verticalLayout.addWidget(self.label_info)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LoadTestDataPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.LoadTestDataPushButton.setObjectName("LoadTestDataPushButton")
        self.horizontalLayout.addWidget(self.LoadTestDataPushButton)
        self.GoExpPushButton = QtWidgets.QPushButton(self.LabCtrlWidget)
        self.GoExpPushButton.setObjectName("GoExpPushButton")
        self.horizontalLayout.addWidget(self.GoExpPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.LabCtrlWidget, 0, 0, 1, 1)
        DLMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DLMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1333, 30))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_G = QtWidgets.QMenu(self.menubar)
        self.menu_G.setObjectName("menu_G")
        self.menu_H = QtWidgets.QMenu(self.menubar)
        self.menu_H.setObjectName("menu_H")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menubar)
        self.menu_5.setObjectName("menu_5")
        DLMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DLMainWindow)
        self.statusbar.setObjectName("statusbar")
        DLMainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(DLMainWindow)
        self.toolBar.setObjectName("toolBar")
        DLMainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_O = QtWidgets.QAction(DLMainWindow)
        self.action_O.setObjectName("action_O")
        self.action_S = QtWidgets.QAction(DLMainWindow)
        self.action_S.setObjectName("action_S")
        self.action_E = QtWidgets.QAction(DLMainWindow)
        self.action_E.setObjectName("action_E")
        self.action_scale = QtWidgets.QAction(DLMainWindow)
        self.action_scale.setObjectName("action_scale")
        self.action_rotate = QtWidgets.QAction(DLMainWindow)
        self.action_rotate.setObjectName("action_rotate")
        self.action_mirror = QtWidgets.QAction(DLMainWindow)
        self.action_mirror.setObjectName("action_mirror")
        self.action_show_info = QtWidgets.QAction(DLMainWindow)
        self.action_show_info.setObjectName("action_show_info")
        self.action_translation = QtWidgets.QAction(DLMainWindow)
        self.action_translation.setObjectName("action_translation")
        self.action_grayscale = QtWidgets.QAction(DLMainWindow)
        self.action_grayscale.setObjectName("action_grayscale")
        self.action_hist = QtWidgets.QAction(DLMainWindow)
        self.action_hist.setObjectName("action_hist")
        self.action_balance = QtWidgets.QAction(DLMainWindow)
        self.action_balance.setObjectName("action_balance")
        self.menu.addAction(self.action_O)
        self.menu.addAction(self.action_S)
        self.menu.addAction(self.action_E)
        self.menu.addAction(self.action_show_info)
        self.menu_G.addAction(self.action_scale)
        self.menu_G.addAction(self.action_rotate)
        self.menu_G.addAction(self.action_mirror)
        self.menu_G.addAction(self.action_translation)
        self.menu_H.addAction(self.action_grayscale)
        self.menu_H.addAction(self.action_hist)
        self.menu_H.addAction(self.action_balance)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_G.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())

        self.retranslateUi(DLMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DLMainWindow)

    def retranslateUi(self, DLMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DLMainWindow.setWindowTitle(_translate("DLMainWindow", "DIP_Lab"))
        self.SrcImgLabel.setText(_translate("DLMainWindow", "SrcImgLabel"))
        self.DstImgLabel.setText(_translate("DLMainWindow", "DstImgLabel"))
        self.label_2.setText(_translate("DLMainWindow", "实验类型："))
        self.label_3.setText(_translate("DLMainWindow", "实验图片："))
        self.SelectImgPushButton.setText(_translate("DLMainWindow", "选择"))
        self.label_info.setText(_translate("DLMainWindow", "TextLabel"))
        self.LoadTestDataPushButton.setText(_translate("DLMainWindow", "载入测试数据"))
        self.GoExpPushButton.setText(_translate("DLMainWindow", "进行实验"))
        self.menu.setTitle(_translate("DLMainWindow", "文件(F)"))
        self.menu_G.setTitle(_translate("DLMainWindow", "几何变换(G)"))
        self.menu_H.setTitle(_translate("DLMainWindow", "灰度变换(H)"))
        self.menu_3.setTitle(_translate("DLMainWindow", "噪声抑制"))
        self.menu_4.setTitle(_translate("DLMainWindow", "锐化与边缘检测"))
        self.menu_5.setTitle(_translate("DLMainWindow", "图像分割"))
        self.toolBar.setWindowTitle(_translate("DLMainWindow", "toolBar"))
        self.action_O.setText(_translate("DLMainWindow", "打开(&O)"))
        self.action_S.setText(_translate("DLMainWindow", "另存为(S)"))
        self.action_E.setText(_translate("DLMainWindow", "退出(Q)"))
        self.action_scale.setText(_translate("DLMainWindow", "缩放"))
        self.action_rotate.setText(_translate("DLMainWindow", "旋转"))
        self.action_mirror.setText(_translate("DLMainWindow", "镜像"))
        self.action_show_info.setText(_translate("DLMainWindow", "显示图像信息"))
        self.action_translation.setText(_translate("DLMainWindow", "平移"))
        self.action_grayscale.setText(_translate("DLMainWindow", "灰度化"))
        self.action_hist.setText(_translate("DLMainWindow", "绘制灰度直方图"))
        self.action_balance.setText(_translate("DLMainWindow", "直方图均衡化"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DLMainWindow = QtWidgets.QMainWindow()
    ui = Ui_DLMainWindow()
    ui.setupUi(DLMainWindow)
    DLMainWindow.show()
    sys.exit(app.exec_())
