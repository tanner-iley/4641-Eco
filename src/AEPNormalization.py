import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_data(df, columns):
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

def save_data(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    input_file = 'data/cleaned_AEP_hourly.csv'
    output_file = 'data/normalized_AEP_hourly.csv'
    
    df = load_data(input_file)
    
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    
    df_normalized = normalize_data(df, numerical_cols)

    save_data(df_normalized, output_file)
    
    print("Normalization complete. Normalized data saved to:", output_file)

if __name__ == "__main__":
    main()