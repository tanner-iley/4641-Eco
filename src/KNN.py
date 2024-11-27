import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_weather_data(weather_data):
    weather_data['date'] = pd.to_datetime(weather_data['date'])
    weather_data['hour'] = weather_data.groupby('date').cumcount()
    weather_data['Datetime'] = weather_data.apply(lambda x: x['date'] + pd.Timedelta(hours=x['hour']), axis=1)
    return weather_data

def merge_data(weather_data, consumption_data):
    consumption_data['Datetime'] = pd.to_datetime(consumption_data['Datetime'])
    merged_data = pd.merge(consumption_data, weather_data, on='Datetime', how='inner')
    merged_data['Hour'] = merged_data['Datetime'].dt.hour
    merged_data['Day'] = merged_data['Datetime'].dt.day
    merged_data['Month'] = merged_data['Datetime'].dt.month
    return merged_data

def perform_knn_and_plot(data, output_folder, state):
    mean = data['AEP_MW'].mean()
    standard_deviation = data['AEP_MW'].std()
    data['Consumption'] = data['AEP_MW'].apply(lambda y: 0 if y < (mean - 1.5 * standard_deviation) else (1 if y <= (mean + 1.5 * standard_deviation) else 2))
    features = data[['Hour', 'Day', 'Month']]
    targets = data['Consumption']

    x_train, x_test, y_train, y_test = train_test_split(features, targets, test_size=0.3, random_state=42)
    
    best_accuracy = 0
    best_knn_model = None
    for neighbor_num in range(1, 30):
        temp_model = KNeighborsClassifier(n_neighbors=neighbor_num)
        temp_model.fit(x_train, y_train)
        temp_score = temp_model.score(x_test, y_test)
        if temp_score > best_accuracy:
            best_knn_model = temp_model
            best_accuracy = temp_score

    y_pred = best_knn_model.predict(x_test)
    display = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
    display.plot()
    plt.title(f"KNN Test Classification (Test Accuracy = {best_accuracy:.3f}) - {state}")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    plt.savefig(os.path.join(output_folder, f'knn_confusion_matrix_{state}.png'))
    plt.close()

def process_weather_files(weather_dir, consumption_csv):
    output_folder = 'graphs'
    consumption_data = load_data(consumption_csv)
    files = [f for f in os.listdir(weather_dir) if f.endswith('_weather_data_normalized.csv')]

    for file in files:
        state = file.split('_')[0]
        weather_data = load_data(os.path.join(weather_dir, file))
        weather_data = preprocess_weather_data(weather_data)
        weather_data.rename(columns={'value': 'Weather_Temp'}, inplace=True)
        merged_data = merge_data(weather_data, consumption_data)
        
        if not merged_data.empty:
            perform_knn_and_plot(merged_data, output_folder, state)

def main():
    weather_dir = 'src/data'
    consumption_csv = 'src/data/normalized_AEP_hourly.csv'
    process_weather_files(weather_dir, consumption_csv)

if __name__ == "__main__":
    main()
