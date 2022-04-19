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

# sns.boxplot(x = "variety", y = "sepallength", data = df)
# plt.show()

# box plot matrix
# define a function to graph each of the 4 features
def graph(feature):
    sns.boxplot(x = 'variety', y=feature, data = df)
plt.figure(figsize = (10,10))

plt.subplot(221)
graph('sepallength')

plt.subplot(222)
graph('sepalwidth')

plt.subplot(223)
graph('petallength')

plt.subplot(224)
graph('petalwidth')
plt.savefig('./plots/boxplot.png')
plt.clf()
#plt.show()







# plt.clf()


