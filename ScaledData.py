# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:16:52 2023

@author: bhagab
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

#creating a newer transformed data
transformed_data = pca.transform(Scaled_info)
Scaled_info.shape

#comparing both data frames
transformed_data.shape

plt.figure(figsize=(6,4))
plt.scatter(transformed_data[:,0], transformed_data[:,1], c=Second_data_frame['seeked_treatment'], cmap='plasma')
plt.xlabel('First Transformed Data')
plt.ylabel('Second Transformed Data')