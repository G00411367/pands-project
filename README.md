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

<img src = "https://github.com/G00411367/pands-project/blob/main/plots/Summary.png" width=50% height=50%>
	
	
    Analysis
        - Mean lenghts are greater than mean widths for both sepals & petals
        - Spread is largest in petal length
        - Max values for sepals are about 40% bigger than min & around double for petals

- Hitograms for Sepal length, Sepal width, Petal length and Petal width were ploted individually and saved in the plot folder
- A matrix of above histograms was ploted in one figure for an overall analysis
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

  <img src = "https://github.com/G00411367/pands-project/blob/main/plots/hist.png" width=50% height=50%>
  
    Analysis: the following shows how sepal and petal measurements are distributed
          
         - The highest frequency of the sepal length is between 20 and 30 which is between 5.5 and 6
         - The highest frequency of the sepal width is around 35 which is between 3.0 and 3.5
         - The highest frequency of the petal length is around 40 which is between 1 and 2
         - The highest frequency of the petal width is around 40 which is between 0.0 and 0.5
      
- Scatter plots for sepal and petal length vs width are saved in the plot folder
  ```
 	 # scatter plot Sepal length vs width
	sns.scatterplot(x='sepallength', y='sepalwidth', hue ='variety', data=df )
	plt.savefig('./plots/scattersepal.png')
	plt.clf()

	# scatter plot Pepal length vs widt
	sns.scatterplot(x='petallength', y='petalwidth', hue ='variety', data=df )
	plt.savefig('./plots/scatterpetal.png')
	plt.clf()
  ```
	
	Outpout
<img src = "https://github.com/G00411367/pands-project/blob/main/plots/scattersepal.png" width=35% height=35%> <img src = "https://github.com/G00411367/pands-project/blob/main/plots/scatterpetal.png" width=35% height=35%>
  
- A pair plot matrix of scatter plots with density along diagonal was ploted for comparison analysis

  ```
	# pair plot of dataset with density along diagonal
	sns.pairplot(df, hue = 'variety', height=2)
	plt.savefig('./plots/scatterplot.png')
	plt.clf()
   ```

	Output
<img src = "https://github.com/G00411367/pands-project/blob/main/plots/scatterplot.png" width=75% height=75%>

    Analysis
    
        - One can see many tipes of relationships
	- Three clusters wihh Petal dimension
        - Setosa has the smallest Petal width and no overlap with other species. It also has the smallest sepal length
        - There is some overlap on Petal dimensiomn between Versicolor and Virginica
	
- Heat map, data corelation

   ```
  	# data corelation & heat map
	print(df.corr())
	fig, axes = plt.subplots(figsize = (6,6))
	sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
	plt.savefig('./plots/heatmap.png')
	plt.clf()
   ```
    	Output
	
<img src = "https://github.com/G00411367/pands-project/blob/main/plots/heatmap.png" width=50% height=50%>

	Analysis
    
        - Petal width and Petal length have high correlations
	- Petal width and Sepal length have high correlations
	- Petal length and Sepal length have high correlations
       

- Box plot, matrix

   ```
  	# box plot. Matrix
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
   ```
    	
	Output

<img src = "https://github.com/G00411367/pands-project/blob/main/plots/boxplot.png" width=75% height=75%>
	
	
	Analysis
    
        - Setosa has the smallest Petals but the widest Sepals
	- Versicolor has average features
	- Virginica has the highest Petals and average Sepals
	
	
- Dist plot wth histograms
    ```
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
	
    ```	
	
<img src = "https://github.com/G00411367/pands-project/blob/main/plots/distpetallength.png" width=25% height=25%> <img src = "https://github.com/G00411367/pands-project/blob/main/plots/distpetalwidth.png" width=25% height=25%>

<img src = "https://github.com/G00411367/pands-project/blob/main/plots/distsepallength.png" width=25% height=25%> <img src = "https://github.com/G00411367/pands-project/blob/main/plots/distsepalwidth.png" width=25% height=25%>
	
	
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
