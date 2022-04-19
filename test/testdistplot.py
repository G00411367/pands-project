# This program analyse Fisher's Iris data set and outputs:
# 1. A summary of each variable to a single text file 
# 2. Histogram of each variable saved to png files
# 3. Scatter plot of each pair of variables
# 4. Performs other appropriate analysis

# Author: Ioan Domsa

# import modules
from matplotlib import axes
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

# Dist plot with histograms  

plt.figure(figsize = (10,10))

plot=sns.FacetGrid(df, hue = 'variety')
plot.map(sns.distplot, 'sepallength').add_legend()
plt.savefig('./plots/distsepallength.png')

plot=sns.FacetGrid(df, hue = 'variety')
plot.map(sns.distplot, 'sepalwidth').add_legend()
plt.savefig('./plots/distsepalwidth.png')

plot=sns.FacetGrid(df, hue = 'variety')
plot.map(sns.distplot, 'petallength').add_legend()
plt.savefig('./plots/distpetallength.png')

plot=sns.FacetGrid(df, hue = 'variety')
plot.map(sns.distplot, 'petalwidth').add_legend()
plt.savefig('./plots/distpetalwidth.png')

plt.clf()
#plt.show()




