from math import *

import cv2
import numpy as np


def read_img(filename):
    """读取图像函数，使用 imdecode读取，避免OpenCV在Windows下不支持中文路径的问题"""
    img = cv2.imdecode(np.fromfile(filename, dtype=np.uint8), -1)
    return img


def img_scale(img, multiples):
    """图像缩放函数"""
    # INTER_NEAREST	最近邻插值
    # INTER_LINEAR	双线性插值（默认设置）
    # INTER_AREA	使用像素区域关系进行重采样。 它可能是图像抽取的首选方法，因为它会产生无云纹理的结果。 但是当图像缩放时，它类似于INTER_NEAREST方法。
    # INTER_CUBIC	4x4像素邻域的双三次插值
    # INTER_LANCZOS4	8x8像素邻域的Lanczos插值
    # 一是通过设置图像缩放比例，即缩放因子，来对图像进行放大或缩小
    # res1 = cv2.resize(img, None, fx=multiples, fy=multiples, interpolation=cv2.INTER_LINEAR)
    height, width = img.shape[:2]
    # 二是直接设置图像的大小，不需要缩放因子
    res = cv2.resize(img, (int(multiples * width), int(multiples * height)), interpolation=cv2.INTER_CUBIC)
    return res


def img_translation(img, angle):
    height, width = img.shape[:2]
    height_new = int(width * fabs(sin(radians(angle))) + height * fabs(cos(radians(angle))))  # 这个公式参考之前内容
    width_new = int(height * fabs(sin(radians(angle))) + width * fabs(cos(radians(angle))))
    # 获取旋转矩阵，这个函数可以自动求出旋转矩阵
    # 第一个参数是旋转中心，第二个参数是旋转角度，第三个参数是缩放比例
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    print(matrix.shape)
    print(matrix)

    matrix[0, 2] += (width_new - width) / 2  # 因为旋转之后,坐标系原点是新图像的左上角,所以需要根据原图做转化
    print(matrix)
    matrix[1, 2] += (height_new - height) / 2
    print(matrix)
    res = cv2.warpAffine(img, matrix, (width_new, height_new))
    return res


lena = read_img('彩色lena图像256色.BMP')

lena_res = img_scale(lena, 0.2)
# lena_res = img_translation(lena, 30)  # 逆时针旋转
cv2.imshow('lena_origin', lena)
cv2.imshow('lena_res', lena_res)
cv2.waitKey(0)
