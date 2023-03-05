import os

from PIL import Image

path = r'./Test/masks'
newpath = r'./Test/masks1'


def picture(path):
    files = os.listdir(path)
    for i in files:
        files = os.path.join(path, i)
        img = Image.open(files).convert('1')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(i)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.png')
        img.save(dst)


picture(path)
