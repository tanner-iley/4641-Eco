import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix



def createPlot(model, y_test, y_pred, data, x_test):
    matrix = confusion_matrix(y_test, y_pred, labels=model.classes_)
    display = ConfusionMatrixDisplay(confusion_matrix=matrix, display_labels=model.classes_)
    display.plot()
    plt.title("KNN Test Classification (Test Accuracy = " + str(round(model.score(x_test, y_test), 3)) + ")")
    plt.show()

    mean = data['AEP_MW'].mean()
    standard_deviation = data['AEP_MW'].std()

    plt.scatter(data['AEP_MW'], data['Hour'], c=data['Consumption'])
    plt.title("Consumption by Hour")
    plt.xlabel(f'Low, Normal, and High Consumption Based on 1 1/2 standard deviations from mean')
    plt.show()

    plt.scatter(data['AEP_MW'], data['Day'], c=data['Consumption'])
    plt.title("Consumption by Day")
    plt.xlabel(f'Low, Normal, and High Consumption Based on 1 1/2 standard deviations from mean')
    plt.show()

    plt.scatter(data['AEP_MW'], data['Month'], c=data['Consumption'])
    plt.title("Consumption by Month")
    plt.xlabel(f'Low, Normal, and High Consumption Based on 1 1/2 standard deviations from mean')
    plt.show()


def KNN(csv):
    data = pd.read_csv(csv)
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    mean = data['AEP_MW'].mean()
    standard_deviation = data['AEP_MW'].std()
    data['Consumption'] = data['AEP_MW'].apply(lambda y: 0 if y < (mean - (standard_deviation * 1.5)) else (1 if ((y >= mean - (standard_deviation * 1.5)) and (y <= mean + (standard_deviation * 1.5))) else 2))
    data['Hour'] = data['Datetime'].dt.hour
    data['Day'] = data['Datetime'].dt.day
    data['Month'] = data['Datetime'].dt.month
    features = data[['Hour', 'Day', 'Month']]
    targets = data[['Consumption']]

    x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.3, random_state=42)

    best_accuracy = 0

    knn_model = KNeighborsClassifier()
    for neighbor_num in np.arange(1,30):
        temp_model = KNeighborsClassifier(n_neighbors=neighbor_num)
        temp_model.fit(x_train, y_train)
        temp_score = temp_model.score(x_test, y_test)
        if (temp_score > best_accuracy):
            knn_model = temp_model
            best_accuracy = temp_score
    
    createPlot(knn_model, y_test, knn_model.predict(x_test), data, x_test)

KNN("C:/Users/hillg/OneDrive/GATech/5th Year/Fall 2024/CS 4641/Project/4641-Eco/src/data/normalized_AEP_hourly.csv")