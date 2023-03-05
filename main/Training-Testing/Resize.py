from PIL import Image
import os


def resize_images(folder_path, width=512, height=512):
    """
    将指定文件夹下的所有图片调整为指定大小，忽略已经是该大小的图片
    :param folder_path: 文件夹路径
    :param width: 图片宽度
    :param height: 图片高度
    :return: None
    """
    for filename in os.listdir(folder_path):
        if not filename.endswith('.jpg') and not filename.endswith('.png'):
            continue  # 忽略非图片文件

        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as image:
            # 如果图片已经是指定大小，则跳过
            if image.width == width and image.height == height:
                continue

            resized_image = image.resize((width, height))
            resized_image.save(image_path)


# 调用示例
folder_path = './DATA/Test/images'
resize_images(folder_path)
