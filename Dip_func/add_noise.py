"""
Time    : 2020/12/26 下午7:11
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : add_noise.py
Software: PyCharm
Desc    : 
"""
import numpy as np
import cv2
import random
from joblib import Parallel, delayed


def method_choose(img, method, mean, var, prob):
    result = None
    if method == 'gaussian':
        result = add_gaussian(img, mean, var)
    elif method == 'salt_pepper':
        result = add_salt_pepper(img, prob)
    return result


def clamp(pv):
    if pv > 255:
        return 255
    elif pv < 0:
        return 0
    else:
        return pv


def add_gaussian(img, mean=0, var=20):
    h, w, c = img.shape

    for row in range(h):
        for col in range(w):
            # 获取三个高斯随机数
            # 第一个参数：概率分布的均值，对应着整个分布的中心
            # 第二个参数：概率分布的标准差，对应于分布的宽度
            # 第三个参数：生成高斯随机数数量
            s = np.random.normal(loc=mean, scale=var, size=3)
            # 获取每个像素点的bgr值
            b = img[row, col, 0]  # blue
            g = img[row, col, 1]  # green
            r = img[row, col, 2]  # red
            # 给每个像素值设置新的bgr值
            img[row, col, 0] = clamp(b + s[0])
            img[row, col, 1] = clamp(g + s[1])
            img[row, col, 2] = clamp(r + s[2])
        if row % 10 == 0:
            print("{:%}".format(row / h))
    return img


def add_salt_pepper(img, prob):
    output = np.zeros(img.shape, np.uint8)
    thres = 1 - prob
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = img[i][j]
    return output


if __name__ == '__main__':
    img_input = cv2.imread('../lena.BMP')
    result1 = add_gaussian(img_input)
    result2 = add_salt_pepper(img_input, 0.01)
    cv2.imshow('gui', result1)
    cv2.imshow('gui2', result2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
