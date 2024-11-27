import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_energy_prices(df):
    df['period'] = pd.to_datetime(df['period'], format='%Y-%m')
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    df['price'].fillna(df['price'].mean(), inplace=True)

    df.drop_duplicates(inplace=True)

    df.dropna(inplace=True)

    return df

def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    file_path = 'data/energy_prices.csv'
    output_file = 'data/cleaned_energy_prices.csv'
    
    df = load_data(file_path)
    df_cleaned = clean_energy_prices(df)
    save_cleaned_data(df_cleaned, output_file)
    
    print("Data cleaning complete. Cleaned data saved to:", output_file)

if __name__ == "__main__":
    main()
