# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:48:39 2020

@author: Eric Bianchi
"""

import os 
from show_results__ import*
from tqdm import tqdm   
import torch

# Load the trained model, you could possibly change the device from cpu to gpu if 
# you have your gpu configured.
model = torch.load(f'../Training-Testing/3-8-2/weights.pt', map_location=torch.device('cuda'))

# Set the model to evaluate mode
model.eval()

source_image_dir = './Test/Images/'
destination_mask = './output20+1/masks/'
destination_overlays = './output20+1/overlays/'

for image_name in tqdm(os.listdir(source_image_dir)):
    print(image_name)
    image_path = source_image_dir + image_name
    generate_images(model, image_path, image_name, destination_mask, destination_overlays)