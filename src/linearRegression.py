import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_weather_data(weather_data):
    weather_data['date'] = pd.to_datetime(weather_data['date'])
    weather_data['hour'] = weather_data.groupby('date').cumcount()
    weather_data['Datetime'] = weather_data.apply(lambda x: x['date'] + pd.Timedelta(hours=x['hour']), axis=1)
    return weather_data

def merge_data(weather_data, consumption_data):
    consumption_data['Datetime'] = pd.to_datetime(consumption_data['Datetime'])
    return pd.merge(consumption_data, weather_data, on='Datetime', how='inner')

def perform_regression_and_plot(data, dependent_var, independent_vars, state, output_folder):
    model = LinearRegression()
    x = data[independent_vars]
    y = data[dependent_var]
    model.fit(x, y)
    predictions = model.predict(x)

    plt.figure(figsize=(10, 5))
    plt.scatter(data['Datetime'], y, color='m', label='Actual')
    plt.plot(data['Datetime'], predictions, color='g', label='Predicted')
    plt.title(f'Regression Model for {dependent_var} in {state}')
    plt.xlabel('Datetime')
    plt.ylabel(dependent_var)
    plt.legend()

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    filename = f'linearRegression_{state}.png'
    plt.savefig(os.path.join(output_folder, filename))
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
            perform_regression_and_plot(merged_data, 'AEP_MW', ['Weather_Temp'], state, output_folder)

def main():
    weather_dir = 'src/data'
    consumption_csv = 'src/data/normalized_AEP_hourly.csv'
    process_weather_files(weather_dir, consumption_csv)

if __name__ == "__main__":
    main()
