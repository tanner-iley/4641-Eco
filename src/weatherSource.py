import requests
import pandas as pd
import time
from datetime import datetime, timedelta

def fetch_data(state_fips, api_key, start_date, end_date):
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
    headers = {'token': api_key}
    
    # Prepare to hold all data
    all_data = []
    
    # Generate date ranges for each year within the start and end date
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    date_ranges = [(max(start, datetime(year, 1, 1)), min(end, datetime(year, 12, 31))) for year in range(start.year, end.year + 1)]

    for start_dt, end_dt in date_ranges:
        params = {
            'datasetid': 'GHCND',
            'locationid': f'FIPS:{state_fips}',
            'startdate': start_dt.strftime("%Y-%m-%d"),
            'enddate': end_dt.strftime("%Y-%m-%d"),
            'units': 'metric',
            'limit': 1000,
            'datatypeid': 'TAVG',  # Adjust this as necessary for other data types
            'offset': 1
        }

        while True:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code != 200:
                print(f"Failed to fetch data: {response.status_code} - {response.text}")
                break  # Exiting the loop on failure to avoid infinite loops
            try:
                data = response.json()
                if 'results' not in data:
                    print("No more data available.")
                    break
                all_data.extend(data['results'])
                if 'metadata' in data and 'resultset' in data['metadata']:
                    total_count = data['metadata']['resultset']['count']
                    params['offset'] += params['limit']
                    if params['offset'] > total_count:
                        break
            except ValueError as e:
                print("Failed to decode JSON:", e)
                break
            time.sleep(1)  # Respect the API's rate limit

    return pd.DataFrame(all_data)

api_key = 'GJchkdITnLUESJMHMVzxwpJQUAiOeNjo'  # Replace with your actual API key
start_date = '2004-01-01'
end_date = '2019-01-01'
state_fips = '11'  # FIPS code for the District of Columbia

print("Fetching data for the District of Columbia")
df = fetch_data(state_fips, api_key, start_date, end_date)
if not df.empty:
    df.to_csv('District_of_Columbia_weather_data.csv', index=False)
    print("Data for the District of Columbia written to CSV file.")
else:
    print("No data retrieved for the District of Columbia.")
