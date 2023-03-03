"""
图片灰度处理functions
"""
from PIL import Image


def converter(image):
    # 创建一个pillow image 实例
    img = Image.open(image)
    # 将pillow image 转为 grayscale
    gray_img = img.convert('L')
    return gray_img
