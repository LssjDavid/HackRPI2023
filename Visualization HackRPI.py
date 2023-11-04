"""
Created on Sat Nov  4 16:07:08 2023

@author: Felip
"""

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

#reading the csv file
df = pd.read_csv(r"C:\Users\Felip\OneDrive\Documentos\HACKATON\student_mental_health_dataset.csv")

#getting the title
print(df.head())

#how to make scatterplot using matplot in python

#gets rid of the missing values from the data set to clean it up
newData = df.dropna(axis =0, how ='any')


#finds the median and standard deviation of the new data set to make sure there are no outliers
medianAge = np.median(newData['age'])
medianGPA = np.median(newData['gpa'])
STD = newData[['age','gpa']].std()

newData.head() 

z = newData['class_status']
p= newData['age']

myFreq = newData['major'].value_counts()

myFreq.plot(kind='pie')
plt.show()


#fig = plt.figure(figsize = (10,7))
#num = np.array([len(df[df.major==x]),len(df[df.major==y]),plt.pie(num,labels=df['major'].unique()))
#print(df.head())







#print(df.plot(kind='scatter', x='x', y = 'y'))

#how to make pie chart using matplot in python

