'''
2019-09-07
机器学习：解析后台传入的证书模板，矩阵储存
'''


import cv2
# 转为灰度图

# 读取图像，并把图像转换为灰度图像并显示
img = cv2.imread("cert.png")  # 读取图片
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换了灰度化
cv2.imshow('gray', img_gray)  # 显示图片


# 二值化
# 将灰度图像二值化，设定阈值是150
img_thre = img_gray
cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV, img_thre)
cv2.imshow('threshold', img_thre)
cv2.waitKey(0)
# waitKey()函数的功能是不断刷新图像，频率时间为delay，单位为ms
# 如果使用waitKey(0)则只会显示第一帧视频
cv2.imwrite('thre_res.png', img_thre)

# 获取信息，生成证书


