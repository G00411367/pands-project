# This program analyse Fisher's Iris data set and outputs:
# 1. A summary of each variable to a single text file 
# 2. Histogram of each variable saved to png files
# 3. Scatter plot of each pair of variables
# 4. Performs other appropriate analysis

# Author: Ioan Domsa

# import modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# specify file path
datapath = './data/'
irisfile = datapath + 'iris.data.csv'

# loading data set. The file doesn't have a headere
df = pd.read_csv(irisfile, header=None)
# add names for columns
df.columns = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'variety']
# test file loading
print (df.head()) 
# check file shape, number of rows and columns
print(df.shape) 
# counts number of each veriety 
print(df['variety'].value_counts())

# output summary of variables to a file
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

# histograms
plt.hist(df['sepallength'])
plt.title('Sepal Length')
plt.savefig('./plots/histSepallength.png')
# plt.show()

# histograms grouped in one file
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0,0].set_title('Sepal Length')
axes[0,0].hist(df['sepallength'], edgecolor="red", bins=7)

axes[0,1].set_title('Sepal Width')
axes[0,1].hist(df['sepalwidth'], edgecolor="red", bins=7)

axes[1,0].set_title('Petal Length')
axes[1,0].hist(df['petallength'], edgecolor="red", bins=7)

axes[1,1].set_title('Petal Width')
axes[1,1].hist(df['petalwidth'], edgecolor="red", bins=7)
plt.savefig('./plots/hist.png')
# plt.show()


