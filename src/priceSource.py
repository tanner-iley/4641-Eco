import requests
import pandas as pd
import os

def fetch_energy_data():
    # URL for the API endpoint
    url = "https://api.eia.gov/v2/electricity/retail-sales/data/"
    
    # Parameters for the API request
    params = {
        "api_key": "EIRhBVmPt1KiCVz628SQIS00jTD1gfBUjku54cGI",  # Your actual API key
        "frequency": "monthly",
        "data[0]": "price",
        "facets[stateid][]": ["DC", "DE", "IL", "IN", "KY", "MD", "MI", "NC", "NJ", "OH", "PA", "TN", "VA", "WV"],
        "start": "2004-01",
        "end": "2018-12",
        "sort[0][column]": "period",
        "sort[0][direction]": "desc",
        "offset": 0,
        "length": 5000
    }
    
    # Make the GET request
    response = requests.get(url, params=params)
    
    # Convert the response to JSON
    data = response.json()
    
    # Check and create the 'data' directory if it doesn't exist
    directory = "data"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Extract the relevant part of the JSON into a DataFrame
    if 'response' in data and 'data' in data['response']:
        df = pd.json_normalize(data['response']['data'])
        
        # Save the DataFrame to a CSV file in the 'data' directory
        file_path = os.path.join(directory, "energy_prices.csv")
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    else:
        print("No data found in the response")

if __name__ == "__main__":
    fetch_energy_data()
