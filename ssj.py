# 要用到三个包
import numpy as np
import struct
import matplotlib.pyplot as plt

f = open('彩色lena图像256色.BMP',
         'rb')  # python要加两个\\
# rb:以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。

# read有一个指针
f_type = str(f.read(2))  # 读取两个字节--文件类型
file_size_byte = f.read(4)  # 读取四个字节--文件大小
f.seek(f.tell() + 4)  # 跳过中间四个无用字节
file_ofset_byte = f.read(4)  # 读取位图数据的偏移量
f.seek(f.tell() + 4)  # 跳过中间两个无用字节
file_wide_byte = f.read(4)  # 读取宽度
file_height_byte = f.read(4)  # 读取高度
f.seek(f.tell() + 2)  # 跳过中间两个无用字节
file_bitcount_byte = f.read(4)  # 每个像素所占的位数--可知图片类型

# 字节转换
# l是长整型，i是整型
f_size, = struct.unpack('l', file_size_byte)
f_ofset, = struct.unpack('l', file_ofset_byte)
f_wide, = struct.unpack('l', file_wide_byte)
f_height, = struct.unpack('l', file_height_byte)
f_bitcount, = struct.unpack('i', file_bitcount_byte)

# 读取颜色表
color_table = np.empty(shape=[256, 4], dtype=int)  # 创建的矩阵
# 颜色表：四个字节为一行:R G B 预留
f.seek(54)  # 跳过文件信息头和位图信息头

for i in range(0, 256):  # 256行
    b = struct.unpack('B', f.read(1))[0]  # 蓝色
    g = struct.unpack('B', f.read(1))[0]  # 绿色
    r = struct.unpack('B', f.read(1))[0]  # 红色
    alpha = struct.unpack('B', f.read(1))[0]  # 预留
    color_table[i][0] = r
    color_table[i][1] = g
    color_table[i][2] = b
    color_table[i][3] = 255

# '下面部分用来读取BMP位图数据区域,将数据存入numpy数组'
# 首先对文件指针进行偏移
print(f_ofset)
f.seek(f_ofset)
# 因为图像是8位伪彩色图像，所以一个像素点占一个字节，即8位

img = np.empty(shape=[f_height, f_wide, 4], dtype=int)  # 建一个矩阵
cout = 0
for y in range(0, f_height):  # 0~图片高度
    for x in range(0, f_wide):  # 0~图片宽度
        cout = cout + 1
        index = struct.unpack('B', f.read(1))[0]
        img[f_height - y - 1, x] = color_table[index]
    while cout % 4 != 0:  # 一行是不是4的整数倍
        f.read(1)
        cout = cout + 1

# 图像显示
plt.imshow(img)
plt.show()
f.close()
