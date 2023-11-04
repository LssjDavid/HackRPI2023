# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 17:07:12 2023

@author: bhagab
"""

import pandas as pd
import numpy as np
#reads in the data set
df = pd.read_csv(r"C:\Users\bhagab\Desktop\HACKRPI\student_mental_health_dataset.csv")

#gets rid of the missing values from the data set to clean it up
newData = df.dropna(axis =0, how ='any')


#finds the median and standard deviation of the new data set to make sure there are no outliers
medianAge = np.median(newData['age'])
medianGPA = np.median(newData['gpa'])
STD = newData[['age','gpa']].std()

#prints the new data set along with the median and standard deviation of the GPA and age 
newData.head()
print("Median:")
print("age\t", medianAge)
print("gpa\t", medianGPA)
print("Standard Deviation:")
print(STD)


