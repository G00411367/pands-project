# Pands Project
Author: Ioan Domsa

Programing and Scripting 2022

## Fisher's Iris data set, backgroud

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in 1936 as an example of linear discriminant analysis. 

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 

Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.


## The Project
This project will investigate the Fisher's Iris data set and performs analysis using a python script

The code will output:
1. A summary of each variable to a single text file 
2. Histogram of each variable saved to png files
3. Scatter plot of each pair of variables
4. Performs other appropriate analysis

## The Code: analysis.py

- Load data from cvs file which is specified with path & name
- Manipulation of data set  
    - After viewing the initial dataframe of the file, some data manipulation will be applied:
        - File doesn't have a header
        - Add names for columns & check dataframe shape. It is as expected 150 rows & 5 colums
        - Check the number of entries for each variety. Result shows same number for each specie, 50
    - We are checking this to understand if the data set is ballanced 
- Perform a statistical summary of the data set & output it to a file
    - Pandas describe() function shows counts, mean, standard deviation, min, max, etc
    - Check against missing values in data set by using isnull() function

    ```
    description = df.describe()
    summary = description.to_csv('./data/summary.csv', float_format='%.3f', sep='\t')

    ```
    Output 
	        sepallength	sepalwidth	petallength	petalwidth
        count	150.000	150.000	    150.000	    150.000
        mean	5.843	3.054	    3.759	    1.199
        std	    0.828	0.434	    1.764	    0.763
        min	    4.300	2.000	    1.000	    0.100
        25%	    5.100	2.800	    1.600	    0.300
        50%	    5.800	3.000	    4.350	    1.300
        75%	    6.400	3.300	    5.100	    1.800
        max	    7.900	4.400	    6.900	    2.500
    Analysis
        - Mean lenghts are greater then mean widths for both sepals & petals
        - Spread is largest in petal length
        - Max values for sepals are about 40% bigger than min & around double for petals

        
## Research
A CSV file of the Iris data set was downloaded from UCI Machine Learning repository

Data set contains 150 records under 5 atributes: Sepal Length, Sepal Width, Petal Length, Petal width and Species

Various analisys were performed and developed in order to distinquish between species


## ** References **

[Iris flower data set]

(https://en.wikipedia.org/wiki/Iris_flower_data_set)

[Exploratory Data Analysis on Iris Dataset]

(https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)

(https://medium.com/analytics-vidhya/exploratory-data-analysis-uni-variate-analysis-of-iris-data-set-690c87a5cd40)

(https://m.youtube.com/watch?v=02BFXhPQWHQ)

(https://m.youtube.com/watch?v=8yXpWGRBXjE)

()
