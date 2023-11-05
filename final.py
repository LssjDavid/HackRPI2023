#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 01:43:46 2023

@author: david
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv("/Users/david/Desktop/Data Science/student_mental_health_dataset.csv")


#gets rid of the missing values from the data set to clean it up
newData = df.dropna(axis =0, how ='any')


#finds the median and standard deviation of the new data set to make sure there are no outliers
medianAge = np.median(newData['age'])
medianGPA = np.median(newData['gpa'])
STD = newData[['age','gpa']].std()


z = newData['class_status']
p= newData['age']

myFreq = newData['major'].value_counts()

myFreq.plot(kind='pie')
plt.show()

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

#Now that we got the PCA its time to transform the Data to something the ML can understand
Scale = StandardScaler()
Scale.fit(Second_data_frame)
Scaled_info = Scale.transform(Second_data_frame)

#5 rows so we wanna makesure the components stay in bounds
#The PCA library comes with N_components built in for the number of components in the data set
pca = PCA(n_components=5)
pca.fit(Scaled_info)

#creating a newer transformed data
transformed_data = pca.transform(Scaled_info)
Scaled_info.shape

#comparing both data frames 
transformed_data.shape

plt.figure(figsize=(6,4))
plt.scatter(transformed_data[:,0], transformed_data[:,1], c=Second_data_frame['seeked_treatment'], cmap='plasma')
plt.xlabel('First Transformed Data')
plt.ylabel('Second Transformed Data')

type(transformed_data)

print(transformed_data)

third_data_frame = pd.DataFrame(transformed_data, columns = ['A', 'B', 'C', 'D', 'E'])
third_data_frame.head()

x = third_data_frame
y = newData['seeked_treatment']
x_train, x_test, y_train, y_test = train_test_split(x , y, test_size=0.30, random_state=101) 


rfc = RandomForestClassifier(n_estimators = 600)

rfc.fit(x_train, y_train)

prediction = rfc.predict(x_test)

print(classification_report(y_test, prediction))
















