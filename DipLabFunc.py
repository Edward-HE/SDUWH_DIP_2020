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
from Dip_func import geometric_transformation, gray_histogram, gray_histogram_opencv, gray_scale, show_img


def read_img_opencv(filename):
    """
    Desc:
        读取图像函数，使用 imdecode读取，避免OpenCV在Windows下不支持中文路径的问题

    Args:
        filename:

    Returns:

    """

    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    return img


def numpy_2_qpixmap(img):
    """
    Desc:
        将numpy数组表示的图片转化为QtGui.QPixmap格式，以显示在Qt的GUI界面中

    Args:
        shrink:

    Returns:

    """
    shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dst_q_image = QtGui.QImage(shrink.data,
                               shrink.shape[1],
                               shrink.shape[0],
                               shrink.shape[1] * 3, QtGui.QImage.Format_RGB888)
    dst_qpixmap = QtGui.QPixmap.fromImage(dst_q_image)
    return dst_qpixmap


class DipLabFunc(QMainWindow, Ui_DLMainWindow):

    def __init__(self, parent=None):
        super(DipLabFunc, self).__init__(parent)
        self.setupUi(self)

        self.win_to_center()

        self.SrcImgLabel.clear()
        self.DstImgLabel.clear()
        self.label_info.clear()

        self.src_img_path = ""
        self.src_img = None
        self.dst_img = None
        self.src_pix = QPixmap()
        self.dst_pix = QPixmap()

        self.action_show_info.triggered.connect(self.show_image_info)
        self.action_O.triggered.connect(self.open_image)
        self.SelectImgPushButton.clicked.connect(self.open_image)
        self.action_scale.triggered.connect(self.image_scale)
        self.action_rotate.triggered.connect(self.image_rotate)
        self.action_mirror.triggered.connect(self.image_mirror)
        self.action_translation.triggered.connect(self.image_translation)
        self.action_grayscale.triggered.connect(self.image_grayscale)

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
        self.src_img = read_img_opencv(self.src_img_path)
        self.dst_img = self.src_img
        if self.src_pix.load(self.src_img_path) is False:
            QMessageBox.warning(self, "打开图片失败", "请检查图片格式后重新打开")
            return
        else:
            self.dst_pix = self.src_pix.copy(self.src_pix.rect())
            self.resizeEvent(None)
            image = self.src_pix.scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(), Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
            self.SrcImgLabel.setPixmap(image)
            self.DstImgLabel.setPixmap(image)

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
            image = self.src_pix.scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(), Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
            self.SrcImgLabel.setPixmap(image)
            # self.DstImgLabel.setPixmap(image)

    def show_image_info(self):
        """
        Desc:
            读取位图的头部数据并解码，将得到的位图信息显示在界面中的label_info中

        Returns:

        """
        if self.src_img_path == "":
            print("no files!")
            QMessageBox.information(self, "提示", "未选择！")
            return
        image_info_dict = show_img.bmp_info(self.src_img_path)
        image_info_list = ""
        for key in image_info_dict:
            list_item = str(key) + ':' + str(image_info_dict[key]) + '\n'
            image_info_list += list_item
        self.label_info.setText(image_info_list)

    def image_scale(self, scale_multiples=2):
        """
        Desc:
            对图片执行缩放处理

        Returns:

        """
        print(self.dst_img.shape)

        self.dst_img = geometric_transformation.img_scale(self.src_img, multiples=5)
        print(self.dst_img.shape)
        shrink = cv2.cvtColor(self.dst_img, cv2.COLOR_BGR2RGB)
        dst_q_image = QtGui.QImage(shrink.data,
                                   shrink.shape[1],
                                   shrink.shape[0],
                                   shrink.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.dst_pix = QtGui.QPixmap.fromImage(dst_q_image)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_rotate(self, _angle):
        self.dst_img = geometric_transformation.img_rotate(self.src_img, angle=45)
        print(self.dst_img.shape)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_mirror(self, axis):
        self.dst_img = geometric_transformation.image_mirror(self.src_img, axis=-1)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_translation(self):
        self.dst_img = geometric_transformation.img_translation(self.src_img, dx=50, dy=100)
        print(self.dst_img.dtype)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_grayscale(self, method="weighted_average"):

        self.dst_img = gray_scale.method_choose(self.src_img, method="weighted_average", color="R")
        self.dst_img = self.dst_img.astype(np.uint8)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)
