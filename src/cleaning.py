import pandas as pd
import numpy as np

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df['Datetime'] = pd.to_datetime(df['Datetime'])
    
    df.drop_duplicates(inplace=True)
    
    return df

def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    file_path = 'data/AEP_hourly.csv'
    output_file = 'data/cleaned_AEP_hourly.csv'
    
    df = load_data(file_path)
    
    df_cleaned = clean_data(df)
    
    save_cleaned_data(df_cleaned, output_file)

    print("Data cleaning complete. Cleaned data saved to:", output_file)

if __name__ == "__main__":
    main()