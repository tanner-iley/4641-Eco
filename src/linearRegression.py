import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# This function will plot all of our data
def plotModel(x, y, b, m, title, correlation):
    #plot the data as a scatterplot
    plt.scatter(x, y, color="m", marker="o", s=30)
    #will project the predicted line based on our data
    y1 = m*x + b
    plt.plot(x, y1, color="g") 
    plt.xlabel('Time Elapsed (hours)')
    plt.ylabel('Power Load (MW)')
    plt.title(title)
    #displaying the correlation coefficent (close to -1 indicates strong negative correlation, close to 1 indicates strong positive correlation)
    plt.text(0.95, 0.9, f'Correlation: {correlation:.2f}', fontsize=12, color='blue', ha='right', transform=plt.gca().transAxes)
    plt.show()

#This function reads the data from the CSV file (can alter based on how data preprocessing works)
def regression(csv, dependent):
    data = pd.read_csv(csv)
    # Converting data in csv to correct format
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    data['Time'] = (data['Datetime'] - data['Datetime'].min()).dt.total_seconds() / 3600.0
    #Removing unnecessary rows
    data = data[['Time', dependent]].dropna()
    #x and y are arrays that will store our data
    x = data[['Time']].values
    y = data[dependent].values
    #building a plotting the model
    rModel = LinearRegression()
    rModel.fit(x, y)
    correlation = np.corrcoef(data['Time'], y)[0, 1]
    m = rModel.coef_[0]
    b = rModel.intercept_
    plotModel(x, y, b, m, dependent, correlation)

#Make sure to change to correct path (location) of where the data is located on the computer if you try running it on your computer.
#The following line shows how to call the function.
regression('/Users/pranavjothi/Documents/linearRegression/normalized_AEP_hourly.csv', 'AEP_MW')

