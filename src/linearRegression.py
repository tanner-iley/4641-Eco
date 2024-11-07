import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# This function will plot all of our data
def plotModel(x, y, b, m, title, correlation):
    plt.scatter(x, y, color="m", marker="o", s=30)
    y1 = m*x + b
    plt.plot(x, y1, color="g") 
    plt.xlabel('Time Elapsed (hours)')
    plt.ylabel('Power Load (MW)')
    plt.title(title)
    plt.text(0.95, 0.9, f'Correlation: {correlation:.2f}', fontsize=12, color='blue', ha='right', transform=plt.gca().transAxes)
    plt.show()

#This function reads the data from the CSV file (can alter based on how data preprocessing works)
def regression(csv, dependent):
    data = pd.read_csv(csv)
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    data['Time'] = (data['Datetime'] - data['Datetime'].min()).dt.total_seconds() / 3600.0
    data = data[['Time', dependent]].dropna()
    x = data[['Time']].values
    y = data[dependent].values
    rModel = LinearRegression()
    rModel.fit(x, y)
    correlation = np.corrcoef(data['Time'], y)[0, 1]
    m = rModel.coef_[0]
    b = rModel.intercept_
    plotModel(x, y, b, m, dependent, correlation)


regression('/Users/pranavjothi/Documents/linearRegression/normalized_AEP_hourly.csv', 'AEP_MW')

