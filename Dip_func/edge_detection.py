"""
Time    : 2020/12/26 下午11:36
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : edge_detection.py
Software: PyCharm
Desc    : 
"""
import cv2
import numpy as np


def method_choose(img, method):
    result = None
    if method == 'robert':
        result = robert_operators(img)
    elif method == 'sobel':
        result = sobel_operators(img)
    elif method == 'canny':
        result = canny_operators(img, False)
    return result


def robert_operators(img):
    result = np.copy(img)
    h, w, _ = result.shape
    rob = [[-1, -1], [1, 1]]
    for x in range(h):
        for y in range(w):
            if (y + 2 <= w) and (x + 2 <= h):
                img_child = result[x:x + 2, y:y + 2, 1]
                list_robert = rob * img_child
                result[x, y] = abs(list_robert.sum())  # 求和加绝对值
    return result


def sobel_operators(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    x = cv2.Sobel(img_gray, cv2.CV_16S, 1, 0)
    y = cv2.Sobel(img_gray, cv2.CV_16S, 0, 1)
    # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
    # 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
    scale_abs_x = cv2.convertScaleAbs(x)
    scale_abs_y = cv2.convertScaleAbs(y)
    result = cv2.addWeighted(scale_abs_x, 0.5, scale_abs_y, 0.5, 0)
    return result


def canny_operators(img, l2):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(img_gray, (3, 3), 0)  # 用高斯滤波处理原图像降噪
    canny = cv2.Canny(image=blur, threshold1=50, threshold2=150, L2gradient=l2)  # 50是最小阈值,150是最大阈值
    return canny


if __name__ == '__main__':
    img_input = cv2.imread('../lena.BMP')
    cv2.imshow('src1', img_input)

    result_robert = method_choose(img_input, 'robert')
    cv2.imshow('robert', result_robert)

    result_sobel = method_choose(img_input, 'sobel')
    cv2.imshow('sobel', result_sobel)

    result_canny = method_choose(img_input, 'canny')
    cv2.imshow('canny', result_canny)

    result_canny2 = canny_operators(img_input, True)
    cv2.imshow('canny2', result_canny2)
    cv2.imshow('src2', img_input)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
