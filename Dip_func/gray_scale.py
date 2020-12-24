import numpy as np


# 读取 img 图，并显示
def get_rgb(img):
    r, g, b = [img[:, :, i] for i in range(3)]
    alpha = np.ones((256, 256, 1)) * 255
    return r, g, b


def method_choose(img, method, color):
    """
    Desc:
        选择需要调用的具体灰度化方法，并返回处理后得到的图片

    Args:
        img:
        method:
        color:

    Returns:

    """
    img_dst = img
    if method == "weight":
        img_dst = weight(img, color)
    elif method == "max":
        img_dst = max_rgb(img)
    elif method == "average":
        img_dst = average_rgb(img)
    elif method == "weighted_average":
        img_dst = weighted_average(img)
    return img_dst


def weight(img, color):
    """
    Desc:
        分量法
        该方法最为简单，即在R、G、B三种颜色分量中，任意选取一种颜色作为灰度值

    Args:
        img:
        color:

    Returns:

    """
    r, g, b = get_rgb(img)
    if color == 'R':
        rgb = np.reshape(r, (256, 256, 1))
    elif color == 'G':
        rgb = np.reshape(g, (256, 256, 1))
    elif color == 'B':
        rgb = np.reshape(b, (256, 256, 1))
    else:
        print("分量选择错误，请输入R,G,B中的一个")
        exit()
    img_gray_w = np.concatenate([rgb, rgb, rgb], axis=2)
    return img_gray_w


def max_rgb(img):
    """
    Desc:
        最大值法
        该方法是先找出每个像素R、G、B三种颜色分量的值，然后找到值最大的那个颜色，然后以此最大值作为灰度值

    Args:
        img:

    Returns:

    """
    r, g, b = get_rgb(img)
    rgb = np.max(img[:, :, :3], axis=2)
    rgb = np.reshape(rgb, (256, 256, 1))
    img_gray_max = np.concatenate([rgb, rgb, rgb], axis=2).astype(int)
    return img_gray_max


def average_rgb(img):
    """
    Desc:
        平均值法

    Args:
        img:

    Returns:

    """
    r, g, b = get_rgb(img)
    rgb = np.average(img[:, :, :3], axis=2)
    rgb = np.reshape(rgb, (256, 256, 1))
    img_gray_average = np.concatenate([rgb, rgb, rgb], axis=2).astype(int)
    return img_gray_average


def weighted_average(img):
    """
    Desc:
        加权平均值法
        因为人眼对每种颜色的敏感度不同，其中人眼对绿色敏感度最高，蓝色敏感度最低，
        所以我们可以使用加权平均的方法来求灰度值，公式如下

    Args:
        img:

    Returns:

    """
    r, g, b = get_rgb(img)
    rgb = r * 0.299 + g * 0.587 + b * 0.114
    rgb = np.reshape(rgb, (256, 256, 1))
    img_gray_wa = np.concatenate([rgb, rgb, rgb], axis=2)
    # img_gray_wa /= 255
    return img_gray_wa

# # img_gray = weight('R')
# img_gray = average_rgb()
# # img_gray = weighted_average()
# # print(img_gray.shape)
# # print(img_gray)
# plt.imshow(img_gray)
# plt.axis('off')
# plt.show()
