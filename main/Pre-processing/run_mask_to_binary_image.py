# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 12:18:09 2021

@author: Admin
"""
from image_utils import*
source_mask_folder = '../Training-Testing/DATA2/Test/masks/'
destination_mask_norm = '../Training-Testing/DATA2/Train/npymask/'
destination_binary = '../Training-Testing/DATA2/Test/npymask/'

# background_to_white(source_mask_folder, destination_mask_norm)
mask_to_binary_image(source_mask_folder, destination_binary)