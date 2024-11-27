import pandas as pd
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    if 'Datetime' in df.columns:
        df['Datetime'] = pd.to_datetime(df['Datetime'])

    df.replace([-9999, -999], pd.NA, inplace=True)

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    return df

def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)

def process_files(directory):
    full_directory = os.path.join(os.getcwd(), directory)
    
    for filename in os.listdir(full_directory):
        if 'weather_data' in filename and filename.endswith('.csv'):
            file_path = os.path.join(full_directory, filename)
            output_file = os.path.join(full_directory, filename.replace('.csv', '_cleaned.csv'))

            df = load_data(file_path)
            df_cleaned = clean_data(df)
            save_cleaned_data(df_cleaned, output_file)

            print(f"Data cleaning complete. Cleaned data saved to: {output_file}")

if __name__ == "__main__":
    directory = 'src/data'
    process_files(directory)
