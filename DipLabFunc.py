"""
Time    : 2020/12/9 上午12:28
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : DipLabFunc.py
Software: PyCharm
Desc    :
"""

import cv2
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QWidget, QDesktopWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from DLMainWindow import *
import Dip_func
from Dip_func import geometric_transformation, gray_histogram, gray_histogram_opencv, Grayscale, show_img


class DipLabFunc(QMainWindow, Ui_DLMainWindow):

    def __init__(self, parent=None):
        super(DipLabFunc, self).__init__(parent)
        self.setupUi(self)

        self.win_to_center()

        self.SrcImgLabel.clear()
        self.DstImgLabel.clear()

        self.src_img_path = ""
        self.src_img = QPixmap()
        self.dst_img = QPixmap()

        self.action_O.triggered.connect(self.open_image)
        self.SelectImgPushButton.clicked.connect(self.open_image)

    def win_to_center(self):
        """
        Desc：
            将窗口移动到屏幕的中央（窗口屏幕居中显示）

        Returns:

        """
        # 得到屏幕坐标
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标
        size = self.geometry()
        # 计算居中位置
        new_x = (screen.width() - size.width()) / 2
        new_y = (screen.height() - size.height()) / 2
        # 移动到居中位置
        self.move(new_x, new_y)

    def open_image(self):
        """
        Desc:
            选择要打开的图片，并将图片显示在窗口中的label中

        Returns:

        """
        self.src_img_path, file_type = QFileDialog.getOpenFileName(self, "选择图片", ".",
                                                                   "Image Files(*jpg *.jpeg *.png *.bmp;;All Files(*)")
        if len(self.src_img_path) == 0:
            return
        self.ExpImgLineEdit.setText(self.src_img_path)
        if self.src_img.load(self.src_img_path) is False:
            QMessageBox.warning(self, "打开图片失败", "请检查图片格式后重新打开")
            return
        else:
            self.dst_img = self.src_img.copy(self.src_img.rect())
            self.resizeEvent(None)
            # image = self.src_img.scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(), Qt.KeepAspectRatio,
            #                             Qt.SmoothTransformation)
            # self.SrcImgLabel.setPixmap(image)
            # self.DstImgLabel.setPixmap(image)

    def resizeEvent(self, QResizeEvent):
        """
        Desc:
            重写QWidget.resizeEvent()方法，这个方法在用户手动调整窗口大小时执行
            重写之后使得窗口中的内容可以自适应调节

        Args:
            QResizeEvent:

        Returns:

        """
        widget_width = self.ImgShowWidget.width()
        widget_height = self.ImgShowWidget.height()
        self.splitter.move(0, 0)
        self.splitter.resize(widget_width, widget_height)
        self.SrcImgLabel.resize(widget_width / 2, widget_height)
        self.SrcImgLabel.move(0, 0)
        self.DstImgLabel.resize(widget_width / 2, widget_height)
        self.DstImgLabel.move(widget_width / 2, 0)
        if len(self.src_img_path) != 0:
            image = self.src_img.scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(), Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
            self.SrcImgLabel.setPixmap(image)
            self.DstImgLabel.setPixmap(image)

    def show_image_info(self):
        return
    # s = show_img.bmp_info()
