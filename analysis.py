# This program analyse Fisher's Iris data set and outputs:
# 1. A summary of each variable to a single text file 
# 2. Histogram of each variable saved to png files
# 3. Scatter plot of each pair of variables
# 4. Performs other appropriate analysis

# Author: Ioan Domsa

# import all necessary modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load the data set
df = pd.read_csv("irisdata.csv")
df.head()
# print (df.head()) test the file


