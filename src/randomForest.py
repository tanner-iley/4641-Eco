import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
data = pd.read_csv("C:/Users/hillg/OneDrive/GATech/5th Year/Fall 2024/CS 4641/Project/4641-Eco/src/data/normalized_AEP_hourly.csv") 

def random_forest_classification(df):
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    median_value = df['AEP_MW'].median()
    df['High_Consumption'] = (df['AEP_MW'] > median_value).astype(int)
    df['Hour'] = df['Datetime'].dt.hour
    df['Day'] = df['Datetime'].dt.day
    df['Month'] = df['Datetime'].dt.month
    features = ['Hour', 'Day', 'Month']
    target = 'High_Consumption'
    X_train, X_test, y_train, y_test = train_test_split(df[features], df[target], test_size=0.2, random_state=42)
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    y_pred = rf_model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    plt.figure(figsize=(8, 6))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()
    feature_importance = pd.DataFrame({
        'feature': features,
        'importance': rf_model.feature_importances_
    })
    feature_importance = feature_importance.sort_values('importance', ascending=False)
    plt.figure(figsize=(8, 6))
    sns.barplot(x='importance', y='feature', data=feature_importance)
    plt.title('Feature Importance')
    plt.show()

    return feature_importance
feature_importance = random_forest_classification(data)