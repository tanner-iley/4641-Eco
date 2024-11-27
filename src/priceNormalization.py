import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def normalize_prices(df):
    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    df['price'].fillna(df['price'].mean(), inplace=True)

    min_price = df['price'].min()
    max_price = df['price'].max()
    df['price'] = (df['price'] - min_price) / (max_price - min_price)
    
    return df

def save_normalized_data(df, output_file):
    df.to_csv(output_file, index=False)

def main():
    file_path = 'data/cleaned_energy_prices.csv'
    output_file = 'data/normalized_energy_prices.csv'
    
    df = load_data(file_path)
    df_normalized = normalize_prices(df)
    save_normalized_data(df_normalized, output_file)
    
    print("Normalization complete. Normalized data saved to:", output_file)

if __name__ == "__main__":
    main()
