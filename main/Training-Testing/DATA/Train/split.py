import os
import random
import shutil

# 定义源文件夹和目标文件夹的路径
src_folder1 = './masks'
src_folder2 = './images'
dst_folder1 = './masks_new'
dst_folder2 = './images_new'

# 如果目标文件夹不存在，就创建它
if not os.path.exists(dst_folder1):
    os.makedirs(dst_folder1)
if not os.path.exists(dst_folder2):
    os.makedirs(dst_folder2)

# 遍历第一个源文件夹中的所有图片，随机选择其中的20%复制到目标文件夹1
for filename in os.listdir(src_folder1):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        src_path = os.path.join(src_folder1, filename)
        if random.random() < 0.2:
            dst_filename = filename
            dst_path = os.path.join(dst_folder1, dst_filename)
            shutil.copyfile(src_path, dst_path)
            print(f"Copy {filename} to {dst_filename}")

# 遍历第二个源文件夹中的所有图片，如果文件名与目标文件夹1中的图片不包括后缀的文件名相同，就复制到目标文件夹2中
for filename in os.listdir(src_folder2):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        src_path = os.path.join(src_folder2, filename)
        filename_without_ext = os.path.splitext(filename)[0]  # 不包括后缀的文件名
        for dst_filename in os.listdir(dst_folder1):
            if os.path.splitext(dst_filename)[0] == filename_without_ext:
                dst_path = os.path.join(dst_folder2, dst_filename)
                shutil.copyfile(src_path, dst_path)
                print(f"Copy {filename} to {dst_filename}")
                break
