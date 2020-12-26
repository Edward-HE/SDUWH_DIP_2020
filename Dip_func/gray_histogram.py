import cv2
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np
import PIL


def method_choose(img, method):
    hist = None
    if method == 'hist_gray':
        hist = draw_hist_gray(img)
    elif method == 'hist_rgb':
        hist = draw_hist_rgb(img)
    elif method == 'hist_equal_gray':
        hist = hist_equalize_gray(img)
    elif method == 'hist_equal_rgb':
        hist = hist_equalize_rgb(img)
    return hist


def plt2cv():
    buffer_ = BytesIO()
    # 保存在内存中，而不是在本地磁盘
    plt.savefig(buffer_, format='png', dpi=100)
    buffer_.seek(0)
    # 用PIL或CV2从内存中读取
    data_pil = PIL.Image.open(buffer_)
    # 转换为nparrary，PIL转换就非常快了,data即为所需
    data = np.asarray(data_pil)
    buffer_.close()
    return data


def draw_hist_rgb(img):
    hist_b = cv2.calcHist([img], [0], None, [256], [0, 255])
    hist_g = cv2.calcHist([img], [1], None, [256], [0, 255])
    hist_r = cv2.calcHist([img], [2], None, [256], [0, 255])

    plt.plot(hist_b, color='b')
    plt.plot(hist_g, color='g')
    plt.plot(hist_r, color='r')

    # plt.show()
    data = plt2cv()
    plt.close()
    return data


def draw_hist_gray(img):
    """
    Desc:
        hist(数据源, 像素级)
        参数：
        数据源必须是一维数组，通常需要通过函数ravel()拉直图像
        像素级一般是256，表示[0, 255]

    Args:
        img:

    Returns:

    """

    plt.hist(img.ravel(), 256, [0, 256])
    # plt.show()
    data = plt2cv()
    plt.close()
    return data


def hist_equalize_gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.equalizeHist(gray)
    return result


def hist_equalize_rgb(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.equalizeHist(gray)
    return result


if __name__ == '__main__':
    img_input = cv2.imread('../lena.BMP')
    hist_rgb = draw_hist_rgb(img_input)
    hist_gray = draw_hist_gray(img_input)
    print(hist_gray.shape)
    cv2.imshow('gray', hist_gray)
    cv2.imshow('rgb', hist_rgb)
    cv2.waitKey(0)
