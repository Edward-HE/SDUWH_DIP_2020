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


def method_choose(img, method, mean, var, prob):
    result = None
    if method == 'gaussian':
        result = add_gaussian(img, mean, var)
    elif method == 'salt_pepper':
        result = add_salt_pepper(img, prob)
    return result


def add_gaussian(img, mean=0, var=0.001):
    img = np.array(img / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    out = img + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    return out


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
