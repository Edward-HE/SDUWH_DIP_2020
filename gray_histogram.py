import cv2
import matplotlib.pyplot as plt

src = cv2.imread('lena.BMP')
cv2.imshow("src", src)
cv2.waitKey(0)
cv2.destroyAllWindows()

# hist(数据源, 像素级)
# 参数：
# 数据源必须是一维数组，通常需要通过函数ravel()拉直图像
# 像素级一般是256，表示[0, 255]
plt.hist(src.ravel(), 256)
plt.show()
