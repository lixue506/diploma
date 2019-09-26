'''
2019-09-12
PIL处理图片
PIL模块里的Image和ImageDraw
先读入图片，添加文字到指定位置
'''


import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# 读取证书模板图片
cert = Image.open('cert.png')

# 读取文件内容
rtext = '17121202036'


#初始化参数
word_size = 50
word_css = 'arial.ttf'

# 设置字体
font = ImageFont.truetype(word_css, word_size)

# cert.show() # 图片显示
# print(cert.mode) # 输出图片类型
draw = ImageDraw.Draw(cert)
draw.text((290, 400), rtext, fill=(255, 0, 0), font=font) # 添加文字（未知，内容，颜色，字体）
cert.show()
# cert.save(rtext+'.pdf')



















