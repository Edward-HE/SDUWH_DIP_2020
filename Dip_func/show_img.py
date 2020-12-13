import struct

import matplotlib.pyplot as plt


# # 读取 lena 图，并显示
# lena = plt.imread('彩色lena图像256色.BMP')
# plt.imshow(lena)  # 调用图片显示函数
# plt.axis('off')  # 不显示坐标轴
# plt.show()
#
# with open('../彩色lena图像256色.BMP', 'rb') as f:
#     s = f.read(30)
#
# print(s)


# bytes 字节串，以字节为单位，和字符串类似
# unpack 可以把 bytes（字节串）变成相应的类型
# c是变成char类型，I是变成unsignedint，H是变成unsignedshort
# bmp位图采用小端模式，所以写 <
# 小端模式是指数据的低位保存在内存的低地址中，而数据的高位保存在内存的高地址中
# x86是小端
def bmp_info(filename):
    with open(filename, 'rb') as f:
        s = f.read(30)
    unpackbuf = struct.unpack('<ccIIIIIIHH', s)
    # print(unpackbuf)
    if unpackbuf[0] != b'B' or unpackbuf[1] != b'M':
        return None
    else:
        return {
            'bfType1': unpackbuf[0],
            'bfType2': unpackbuf[1],
            'bfSize': unpackbuf[2],
            'bfReserved': unpackbuf[3],
            'bfOffBits': unpackbuf[4],
            'biSize': unpackbuf[5],
            'biWidth': unpackbuf[6],
            'biHeight': unpackbuf[7],
            'biBitCount': unpackbuf[9]
        }

#
# bi = bmp_info()
# print(bi)
# print(bi['biWidth'], bi['biHeight'], bi['biBitCount'])
