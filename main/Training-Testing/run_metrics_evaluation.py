# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:52:06 2021

@author: Admin
"""
from model_plus import createDeepLabv3Plus
from tqdm import tqdm
import torch
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import f1_score, jaccard_score, confusion_matrix
from metric_evaluation import plot_confusion_matrix, iterate_data

# './Test/Test_LCW/Test/'
# './Test/LCW_cracked/'
data_dir = './DATA/Test/'
batchsize = 2

model = torch.load(f'./Checkpoints/weights_20.pt', map_location=torch.device('cuda'))
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(device)
model.to(device)
model.eval() 
##############################################################################

iOU, f1, confm_sum = iterate_data(model, data_dir)
print('iOU: ' + str(iOU))
print('f1 score: ' + str(f1))
plot_confusion_matrix(confm_sum, target_names=['Background', 'Crack'], normalize=True, 
                      title='Confusion Matrix')
