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

#creating bar chart on the seeked_treatment portion
seek = newData['seeked_treatment'].value_counts()
plt.bar(x=seek.index,height=seek.values,width = 0.5)
plt.title("Number of Students that Sought Treatment")


#Uncomment to see data separately
#creating pie chart 
#plt.pie(newData['seeked_treatment'].value_counts(),labels=['Yes',' No'],startangle=90,autopct='%.1f%%', explode=[0.1, 0]);
#plt.title("Percentage of Students that Sought Treatment")


plt.show()


