# -*- coding: utf-8 -*-

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt


def calcGrayHist(img):
    rows = img.shape[0]
    cols = img.shape[1]
    grayHist = np.zeros([256], np.uint64)
    for r in range(rows):
        for c in range(cols):
            grayHist[img[r][c]] += 1
    return grayHist


if __name__ == "__main__":
    img = cv2.imread('lena.BMP', cv2.IMREAD_ANYCOLOR)
    # 计算灰度直方图
    grayHist = calcGrayHist(img)
    # 画出灰度直方图
    x_range = range(256)
    plt.plot(x_range, grayHist, 'r', linewidth=2, c='black')
    # 设置坐标轴的范围
    y_maxValue = np.max(grayHist)
    plt.axis([0, 255, 0, y_maxValue])
    # 设置坐标轴的标签
    plt.xlabel("gray Level")
    plt.ylabel("number of pixels")
    # 显示灰度直方图
    plt.show()
