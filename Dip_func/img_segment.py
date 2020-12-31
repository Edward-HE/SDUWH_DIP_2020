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


def method_choose(img, method, thresh):
    thresh_final = 0
    result = None
    if method == 'global':
        thresh_final, result = threshold_global(img, thresh)

    return result


def threshold_global(img, thresh):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh_1, result = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)
    return thresh_1, result


def threshold_adaptive(img, ada_method, block_size, c):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 第一个参数为原始图像矩阵，第二个参数为像素值上限，第三个是自适应方法（adaptive method）：
    #                   -----cv2.ADAPTIVE_THRESH_MEAN_C:领域内均值
    #                   -----cv2.ADAPTIVE_THRESH_GAUSSIAN_C:领域内像素点加权和，权重为一个高斯窗口
    # 第四个值的赋值方法：只有cv2.THRESH_BINARY和cv2.THRESH_BINARY_INV
    # 第五个Block size：设定领域大小（一个正方形的领域）
    # 第六个参数C，阈值等于均值或者加权值减去这个常数（为0相当于阈值，就是求得领域内均值或者加权值）
    #
    result = cv2.adaptiveThreshold(img_gray, 255, ada_method, cv2.THRESH_BINARY, block_size, c)
    return result


if __name__ == '__main__':
    img_input = cv2.imread('../lena.BMP')

    cv2.waitKey(0)
    cv2.destroyAllWindows()
