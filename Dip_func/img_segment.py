"""
Time    : 2020/12/27 上午3:49
Author  : Edward-du
Contact : duchenhe@outlook.com
Project : DIP
File    : img_segment.py
Software: PyCharm
Desc    : 
"""

import cv2


def method_choose(img, method):
    result = None

    return result


def threshold_global(img, thresh):
    thresh_1, result = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    return result


if __name__ == '__main__':
    img_input = cv2.imread('../lena.BMP')
    img_gray = cv2.cvtColor(img_input, cv2.COLOR_BGR2GRAY)

    cv2.imshow('src1', img_input)

    result_th_gl = threshold_global(img_gray, 111)
    cv2.imshow('th_gl', result_th_gl)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
