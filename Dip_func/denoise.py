"""
Time    : 2020/12/26 下午8:19
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : denoise.py
Software: PyCharm
Desc    : 
"""

import numpy as np
import cv2
import random


def method_choose(img, method='mean', kernel_m=3, kernel_n=3):
    result = None
    if method == 'mean':
        result = mean_filter(img, (kernel_m, kernel_n))
    elif method == 'median':
        result = median_filter(img, kernel_m)
    return result


def mean_filter(img, kernel):
    # 均值滤波
    result = cv2.blur(img, kernel)  # 可以更改核的大小
    return result


def median_filter(img, kernel):
    result = cv2.medianBlur(img, kernel)  # 可以更改核的大小
    return result


if __name__ == '__main__':
    img_input = cv2.imread('lena.BMP')
    # img_input = cv2.cvtColor(img_input, cv2.COLOR_BGR2RGB)

    cv2.imshow('src', img_input)

    result1 = method_choose(img_input, 'mean', 3, 3)
    cv2.imshow('mean', result1)
    result2 = method_choose(img_input, 'median', 3)
    cv2.imshow('median', result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
