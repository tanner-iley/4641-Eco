import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_data(df):
    scaler = MinMaxScaler()
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    return df

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

def process_files(directory):
    for filename in os.listdir(directory):
        if 'weather_data_cleaned.csv' in filename:
            file_path = os.path.join(directory, filename)
            output_file = os.path.join(directory, filename.replace('_cleaned.csv', '_normalized.csv'))
            
            df = load_data(file_path)
            df_normalized = normalize_data(df)
            save_data(df_normalized, output_file)
            
            print(f"Normalization complete. Normalized data saved to: {output_file}")

if __name__ == "__main__":
    directory = 'src/data'
    process_files(directory)
