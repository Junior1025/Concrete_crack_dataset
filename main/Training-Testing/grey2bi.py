import os
import numpy as np
import cv2


# 定义函数将图片转换为可读取的格式并保存
def save_image_from_npy(npy_path, save_path):
    # 读取npy文件
    img = np.load(npy_path)

    # 转换为8位无符号整型
    img = img.astype(np.uint8)

    # 保存为图片
    cv2.imwrite(save_path, img)


# 定义函数将图片转换为0-1二值图并保存为npy文件
def img_to_binary_npy(source_image_folder, destination):
    if not os.path.exists(destination):  # 如果文件夹不存在则创建
        os.makedirs(destination)

    for filename in os.listdir(source_image_folder):
        # 读取图片
        img = cv2.imread(source_image_folder + '/' + filename)

        # 转换为灰度图
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 二值化
        ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # 保存为npy文件
        filename, ext = os.path.splitext(filename)
        np.save(destination + '/' + filename + '.npy', img)

        # 转换为可读取的格式并保存
        save_image_from_npy(destination + '/' + filename + '.npy', destination + '/' + filename + '.png')

img_to_binary_npy('E:/PaddleSeg/data/con_web/labels','E:/PaddleSeg/data/con_web/npy')
save_image_from_npy('E:/PaddleSeg/data/con_web/npy','E:/PaddleSeg/data/con_web/labels')