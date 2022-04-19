# Pands Project - Fisher's Iris data set
Author: Ioan Domsa 

Date : April 2022

Programing and Scripting 2022

## Backgroud

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936 as an example of linear discriminant analysis. 

The data set consists of 50 samples from each of three species of Iris: Setosa, Virginica and Versicolor).

Following images are the flowering Iris Setosa, Iris Virginica and iris Versicolor:

<img src = "https://github.com/G00411367/pands-project/blob/main/images/Iris%20variety.png" width=50% height=50%>

The petals are the inner flower while the sepals protect the emerging flower on the outer part of the plant. 

Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters.

<img src = "https://github.com/G00411367/pands-project/blob/main/images/Iris.png" width=20% height=20%>

Based on the combination of these features, Fisher developed a linear discriminant model to distinguish the species from each other.

Fisher’s analysis investigated if petal / sepal measurements alone could predict which species of Iris the sample came from (Fisher, 1936). 

This project uses the version of the Iris data hosted at UCI machine learning repository.

The project will investigate Fisher's Iris data set and performs analysis using a python scripts.


## Objectives

The project will perform Exploratory Data Analysis and visual technique to investigate how measurements of petal or sepals can be used to predict Iris variety 

It starts with statistical summary analysis using python libraries. Is assesses the counts, mean, min, max, etc. 

Next, the project moves into data visualisation

The code will output:
1. A summary of each variable to a single text file 
2. Histograms of each variable saved to png files
3. Scatter plots of each pair of variables
4. Performs other appropriate analysis

## Project folders and files

1. data 	- contains the data file used for analysis. The folder also contains resuslts files after running the script, e.g. summary.csv
3. images 	- images of the Iris speies 
4. plots 	- plots results of the analysis 
5. test		- test code samples

   Readme.md

   analysis.py 
   
## Python Code : analysis.py

- Load data from cvs file, specified with path & name
- Manipulation of data set: added names for columns
- Check dataframe shape. It is expected 150 rows & 5 colums
	```
	# add names for columns
	df.columns = ['sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'variety']
	# check file shape, number of rows and columns
	print(df.shape) 
	```
   Output
	(150, 5)
	
- Check the number of entries for each variety. Result shows same number for each specie, 50
- to understand data is ballanced
	```
	# counts number of each veriety
	df['variety'].value_counts().to_csv('./data/counts.csv', sep ='\t')
	```
   Output
	variety
	
	Iris-setosa	50
	
	Iris-versicolor	50
	
	Iris-virginica	50

- Perform a statistical summary of the data set & output it to a file
    - Pandas describe() function shows counts, mean, standard deviation, min, max, etc
    - Check against missing values in data set by using isnull() function

    ```
    description = df.describe()
    summary = description.to_csv('./data/summary.csv', float_format='%.3f', sep='\t')

    ```
    Output 

![image](https://user-images.githubusercontent.com/98125831/164041934-0bc05dd9-d8f9-4e1e-a569-23c6bbd43761.png)
	
	
    Analysis
        - Mean lenghts are greater than mean widths for both sepals & petals
        - Spread is largest in petal length
        - Max values for sepals are about 40% bigger than min & around double for petals

- Hitograms for Sepal length, Sepal width, Petal length and Petal width were ploted individually and saved in the plot folder
- A matrix pf above histograms was ploted in one figure for an overall analysis
   ```
    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes[0,0].set_title('Sepal Length')
    axes[0,0].hist(df['sepallength'])
    axes[0,1].set_title('Sepal Width')
    axes[0,1].hist(df['sepalwidth'])
    axes[1,0].set_title('Petal Length')
    axes[1,0].hist(df['petallength'])
    axes[1,1].set_title('Petal Width')
    axes[1,1].hist(df['petalwidth'])
    plt.savefig('./plots/hist.png')
  ```
  Output 
  
  <
  
    Analysis
         - The highest frequency of the sepal length is between 30 and 35 which is between 5.5 and 6
        - The highest frequency of the sepal Width is around 70 which is between 3.0 and 3.5
        - The highest frequency of the petal length is around 50 which is between 1 and 2
        - The highest frequency of the petal width is between 40 and 50 which is between 0.0 and 0.5

## Research


## ** References **

[Iris flower data set]

(https://en.wikipedia.org/wiki/Iris_flower_data_set)

[Exploratory Data Analysis on Iris Dataset]

(https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)

(https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)

(https://m.youtube.com/watch?v=02BFXhPQWHQ)

(https://m.youtube.com/watch?v=8yXpWGRBXjE)

()
