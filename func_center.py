"""
Time    : 2020/12/9 上午12:28
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : func_center.py
Software: PyCharm
Desc    :
"""

import cv2
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QDesktopWidget, QDialog

import scale
from DLMainWindow import *
from Dip_func import add_noise, denoise, edge_detection, geometric_transformation
from Dip_func import gray_histogram, gray_scale, img_segment, show_img


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
        img:

    Returns:

    """
    shrink = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    dst_q_image = QtGui.QImage(shrink.data,
                               shrink.shape[1],
                               shrink.shape[0],
                               shrink.shape[1] * 3, QtGui.QImage.Format_RGB888)
    dst_qpixmap = QtGui.QPixmap.fromImage(dst_q_image)
    return dst_qpixmap


def exit_program():
    exit(0)


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

        self.a1 = QDialog()  # scale

        self.action_show_info.triggered.connect(self.show_image_info)
        self.action_O.triggered.connect(self.open_image)
        self.action_S.triggered.connect(self.save_image)
        self.action_E.triggered.connect(exit_program)
        self.SelectImgPushButton.clicked.connect(self.open_image)
        self.action_scale.triggered.connect(lambda: self.openscale())
        self.action_rotate.triggered.connect(lambda: self.image_rotate())
        self.action_mirror.triggered.connect(lambda: self.image_mirror())
        self.action_translation.triggered.connect(lambda: self.image_translation())
        self.action_grayscale.triggered.connect(lambda: self.image_grayscale(method="weighted_average"))
        self.action_hist.triggered.connect(lambda: self.image_draw_hist())
        self.action_balance.triggered.connect(lambda: self.image_hist_equal())
        self.action_gauss.triggered.connect(lambda: self.image_add_noise(method='gaussian'))
        self.action_sp.triggered.connect(lambda: self.image_add_noise(method='salt_pepper'))
        self.action_dn_mean.triggered.connect(lambda: self.image_de_noise(method='mean'))
        self.action_dn_median.triggered.connect(lambda: self.image_de_noise(method='median'))
        self.action_robert.triggered.connect(lambda: self.image_edge_detection(method='robert'))
        self.action_sobel.triggered.connect(lambda: self.image_edge_detection(method='sobel'))
        self.action_canny.triggered.connect(lambda: self.image_edge_detection(method='canny'))
        self.action_thresh_global.triggered.connect(lambda: self.image_segment(method='global'))
        self.action_thresh_adptive.triggered.connect(lambda: self.image_threshold_adaptive())

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

    def warning_no_file(self):
        if self.src_img_path == "":
            QMessageBox.warning(self, "注意", "未选择图片！\n请先选择图片")
            return 1

    def open_image(self):
        """
        Desc:
            选择要打开的图片，并将图片显示在窗口中的label中

        Returns:

        """
        self.src_img_path, file_type = QFileDialog.getOpenFileName(self, "选择图片", ".",
                                                                   "Image Files(*.jpeg *.jpeg *.jpg *.png *.bmp;;All "
                                                                   "Files(*)")
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

    def save_image(self):  # 保存图片到本地
        # screen = QApplication.primaryScreen()
        # pix = screen.grabWindow(self.label.winId())
        fd, type_1 = QFileDialog.getSaveFileName(self.centralwidget, "保存图片", "", "*.jpg;;*.png;;*.bmp;;All Files(*)")
        # pix.save(fd)
        cv2.imwrite(fd, self.dst_img)  # 保存图片

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
            image = self.dst_pix.scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(), Qt.KeepAspectRatio,
                                        Qt.SmoothTransformation)
            self.DstImgLabel.setPixmap(image)

    def show_image_info(self):
        """
        Desc:
            读取位图的头部数据并解码，将得到的位图信息显示在界面中的label_info中

        Returns:

        """
        if self.warning_no_file() == 1:
            return
        image_info_dict = show_img.bmp_info(self.src_img_path)
        image_info_list = ""
        for key in image_info_dict:
            list_item = str(key) + ': \t\t ' + str(image_info_dict[key]) + '\n'
            image_info_list += list_item
        self.label_info.setText(image_info_list)

    def openscale(self):
        a = scale.Ui_scale()
        a.setupUi(self.a1)
        self.a1.show()
        self.a1.accepted.connect(lambda: self.image_scale(a))

    def image_scale(self, a):
        """
        Desc:
            对图片执行缩放处理

        Returns:

        """
        multiples = a.lineEdit.text()
        if self.warning_no_file() == 1:
            return

        print(self.dst_img.shape)
        self.dst_img = geometric_transformation.img_scale(self.src_img, multiples=float(multiples))
        print(self.dst_img.shape)
        shrink = cv2.cvtColor(self.dst_img, cv2.COLOR_BGR2RGB)
        dst_q_image = QtGui.QImage(shrink.data,
                                   shrink.shape[1],
                                   shrink.shape[0],
                                   shrink.shape[1] * 3, QtGui.QImage.Format_RGB888)
        self.dst_pix = QtGui.QPixmap.fromImage(dst_q_image)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_rotate(self, angle=45):
        if self.warning_no_file() == 1:
            return

        self.dst_img = geometric_transformation.img_rotate(self.src_img, angle)
        print(self.dst_img.shape)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_mirror(self, axis=-1):
        if self.warning_no_file() == 1:
            return

        self.dst_img = geometric_transformation.image_mirror(self.src_img, axis)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_translation(self, dx=50, dy=100):
        if self.warning_no_file() == 1:
            return

        self.dst_img = geometric_transformation.img_translation(self.src_img, dx, dy)
        print(self.dst_img.dtype)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_grayscale(self, method="weighted_average", color="R"):
        if self.warning_no_file() == 1:
            return

        self.dst_img = gray_scale.method_choose(self.src_img, method, color)
        self.dst_img = self.dst_img.astype(np.uint8)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_draw_hist(self, method='hist_rgb'):
        if self.warning_no_file() == 1:
            return

        self.dst_img = gray_histogram.method_choose(self.src_img, method)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)
        # self.DstImgLabel.setScaledContents(True)

    def image_hist_equal(self, method='hist_equal_gray'):
        if self.warning_no_file() == 1:
            return

        self.dst_img = gray_histogram.method_choose(self.src_img, method)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_add_noise(self, method='gaussian', mean=0, var=20, prob=0.01):
        if self.warning_no_file() == 1:
            return

        self.dst_img = add_noise.method_choose(self.src_img, method, mean, var, prob)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_de_noise(self, method='mean', kernel_m=3, kernel_n=3):
        if self.warning_no_file() == 1:
            return

        self.dst_img = denoise.method_choose(self.src_img, method, kernel_m, kernel_n)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_edge_detection(self, method='robert'):
        if self.warning_no_file() == 1:
            return

        self.dst_img = edge_detection.method_choose(self.src_img, method)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_segment(self, method, thresh=111):
        if self.warning_no_file() == 1:
            return

        self.dst_img = img_segment.method_choose(self.src_img, method, thresh)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)

    def image_threshold_adaptive(self, ada_method=cv2.ADAPTIVE_THRESH_MEAN_C, block_size=5, c=2):
        if self.warning_no_file() == 1:
            return

        self.dst_img = img_segment.threshold_adaptive(self.src_img, ada_method, block_size, c)
        self.dst_pix = numpy_2_qpixmap(self.dst_img).scaled(self.SrcImgLabel.width(), self.SrcImgLabel.height(),
                                                            Qt.KeepAspectRatio,
                                                            Qt.SmoothTransformation)
        self.DstImgLabel.setPixmap(self.dst_pix)
