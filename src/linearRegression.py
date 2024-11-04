import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from cleaning import load_data, clean_data
from normalization import normalize_data  

# Will change implementation based on logistic regression function in HW3, as of now its based on tutorials
#This function will give us our slope and intercept
def getCoefficient(x, y):
    #we take the number of data points
    n = np.size(x) 
    #we take the number of data points
    mx = np.mean(x)
    my = np.mean(y)
    SSxy = np.sum(x*y) - n*my*mx
    SSxx = np.sum(x*x) - n*mx*mx
    #We calculate the slope and intercept
    b1 = SSxy/SSxx
    b0 = my - b1*mx
    return (b0, b1)

# This function will plot all of our data
def plotModel(x, y, b, title, correlation):
    #plot the data as a scatterplot
    plt.scatter(x, y, color="m", marker="o", s=30)
    #will project the predicted line based on our data
    y1 = b[0] + b[1] * x
    plt.plot(x, y1, color="g") 
    plt.xlabel('Time Elapsed (hours)')
    plt.ylabel('Power Load (MW)')
    plt.title(title)
    #displaying the correlation coefficent (close to -1 indicates strong negative correlation, close to 1 indicates strong positive correlation)
    plt.text(0.95, 0.9, f'Correlation: {correlation:.2f}', fontsize=12, color='blue', ha='right', transform=plt.gca().transAxes)
    plt.show()

#This function calculates the correlation coefficient
def calculateCorrelation(x, y):
    correlation_matrix = np.corrcoef(x, y)
    return correlation_matrix[0, 1]

#This function reads the data from the CSV file (can alter based on how data preprocessing works)
def regression(csv, dependent):
    data = load_data(csv)
    data = clean_data(data)
    numerical_cols = data.select_dtypes(include=['int64', 'float64']).columns
    data = normalize_data(data, numerical_cols)
    # Converting data in csv to correct format
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    data['Time'] = (data['Datetime'] - data['Datetime'].min()).dt.total_seconds() / 3600.0
    #Removing unecessary rows
    data = data[['Time', dependent]].apply(pd.to_numeric, errors='coerce').dropna()
    #x and y are arrays that will store our data
    x = data['Time'].values
    y = data[dependent].values
    b = getCoefficient(x, y)
    correlation = calculateCorrelation(x, y)
    plotModel(x, y, b, dependent, correlation)

#Make sure to change to correct path (location) of where the data is located on the computer if you try running it on your computer.
#The following line shows how to call the function.
regression('/Users/pranavjothi/Documents/linearRegression/AEP_hourly.csv', 'AEP_MW')

