'''
2019-09-12
PIL处理图片
'''

import matplotlib.image as mpimg
from PIL import Image
import numpy as np

img = Image.open('cert.png')
# 模式L”为灰色图像，它的每个像素用8个bit表示，0表示黑，255表示白，其他数字表示不同的灰度。
# Img = img.convert('L')

# 图片转为数组
im_array = np.array(img)
for i in im_array[210]:
    i[1]=i[2] = 0

new_im = Image.fromarray(im_array)
# 显示图片
new_im.show()



# # 图片二值化
# photo = Img.point(table, '1')
# photo.save("test1.jpg")





















