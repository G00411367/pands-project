# This program analyse Fisher's Iris data set and outputs:
# 1. A summary of each variable to a single text file 
# 2. Histogram of each variable saved to png files
# 3. Scatter plot of each pair of variables
# 4. Performs other appropriate analysis

# Author: Ioan Domsa

# import necessary modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import numpy as np

# specify file path
datapath = './data/'
irisfile = datapath + 'iris.data.csv'
# dataframe, loading data.The file doesn't have a header, so header=None
df = pd.read_csv(irisfile, header=None)
# add names for columns
df.columns = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'variety']
# test file loading
print (df.head()) 
# check file shape, number of rows and columns
print(df.shape) 
# counts number of each veriety 
print(df['variety'].value_counts())

# output a summary of the variables to a file
# use flot format to show only 3 decimals
description = df.describe()
summary = description.to_csv('./data/summary.csv', float_format='%.3f', sep='\t')

# check for missing values on the dataset
print(df.isnull().sum())

# create dadaframes for each of variety and print to check resluts
setosa = df.loc[df['variety'] == 'Iris-setosa']
# print(setosa)
versicolor = df.loc[df['variety'] == 'Iris-versicolor']
# print(versicolor)
virginica = df.loc[df['variety'] == 'Iris-virginica']
# print(virginica)



