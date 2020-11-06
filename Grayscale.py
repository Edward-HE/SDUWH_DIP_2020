import matplotlib.pyplot as plt
import numpy as np

# 读取 lena 图，并显示
lena = plt.imread('彩色lena图像256色.BMP')
plt.imshow(lena)  # 调用图片显示函数
plt.axis('off')  # 不显示坐标轴
# plt.show()
print(lena)
r, g, b = [lena[:, :, i] for i in range(3)]
alpha = np.ones((256, 256, 1)) * 255


# 1.分量法
# 该方法最为简单，即在R、G、B三种颜色分量中，任意选取一种颜色作为灰度值
def weight(color):
    if color == 'R':
        rgb = np.reshape(r, (256, 256, 1))
    elif color == 'G':
        rgb = np.reshape(g, (256, 256, 1))
    elif color == 'B':
        rgb = np.reshape(b, (256, 256, 1))
    else:
        print("分量选择错误，请输入R,G,B中的一个")
        exit()
    lena_gray_w = np.concatenate([rgb, rgb, rgb, alpha], axis=2)
    return lena_gray_w


# 2.最大值法
# 该方法是先找出每个像素R、G、B三种颜色分量的值，然后找到值最大的那个颜色，然后以此最大值作为灰度值
def max_rgb():
    rgb = np.max(lena[:, :, :3], axis=2)
    rgb = np.reshape(rgb, (256, 256, 1))
    lena_gray_max = np.concatenate([rgb, rgb, rgb, alpha], axis=2).astype(int)
    return lena_gray_max


# 3. 平均值法
def average_rgb():
    rgb = np.average(lena[:, :, :3], axis=2)
    rgb = np.reshape(rgb, (256, 256, 1))
    lena_gray_average = np.concatenate([rgb, rgb, rgb, alpha], axis=2).astype(int)
    return lena_gray_average


# 4. 加权平均值法
# 因为人眼对每种颜色的敏感度不同，其中人眼对绿色敏感度最高，蓝色敏感度最低，
# 所以我们可以使用加权平均的方法来求灰度值，公式如下
def weighted_average():
    rgb = r * 0.299 + g * 0.587 + b * 0.114
    rgb = np.reshape(rgb, (256, 256, 1))
    lena_gray_wa = np.concatenate([rgb, rgb, rgb, alpha], axis=2)
    lena_gray_wa /= 255
    return lena_gray_wa


# lena_gray = weight('R')
lena_gray = average_rgb()
# lena_gray = weighted_average()
# print(lena_gray.shape)
# print(lena_gray)
plt.imshow(lena_gray)
plt.axis('off')
plt.show()
