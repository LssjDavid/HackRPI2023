# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 16:12:30 2023

@author: carmos
"""


import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

#For some reason this is glitchy, in where when we run this it will save it forever so we can't run it again
#Because of that we have to rerun the last cell for it to work. Just something to keep in mind

temp_var = pd.get_dummies(newData,columns=['gender', 'major', 'class_status', 'marital_status', 'have_depression', 'have_anxiety', 'have_panicattacks'])
newData = temp_var
newData.head(100)

#This is the Principle Data Analysis

Second_data_frame = newData.copy(deep=True)
Second_data_frame['seeked_treatment'] = Second_data_frame['seeked_treatment'].mask(Second_data_frame['seeked_treatment'] == 'No', 0)
Second_data_frame['seeked_treatment'] = Second_data_frame['seeked_treatment'].mask(Second_data_frame['seeked_treatment'] == 'Yes', 1)
Second_data_frame.head()


