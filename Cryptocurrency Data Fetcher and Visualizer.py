import threading
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API URL for fetching cryptocurrency data
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1,
    "sparkline": False
}

# Function to fetch data from the API
def fetch_crypto_data():
    try:
        response = requests.get(API_URL, params=PARAMS)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        print("Data fetched successfully!")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to process data into a DataFrame
def process_data(data):
    if not data:
        print("No data to process!")
        return None
    
    df = pd.DataFrame(data)
    df = df[["name", "symbol", "market_cap", "current_price", "price_change_percentage_24h"]]
    print("Data processed successfully!")
    return df

# Function to visualize the data
def visualize_data(df):
    if df is None or df.empty:
        print("No data to visualize!")
        return
    
    plt.figure(figsize=(10, 6))
    plt.bar(df["name"], df["market_cap"], color="skyblue")
    plt.title("Top 10 Cryptocurrencies by Market Cap")
    plt.xlabel("Cryptocurrency")
    plt.ylabel("Market Cap (USD)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

# Multithreading to fetch and process data simultaneously
def main():
    data = []
    fetch_thread = threading.Thread(target=lambda: data.append(fetch_crypto_data()))
    fetch_thread.start()
    fetch_thread.join()

    # Process and visualize the data
    df = process_data(data[0])
    visualize_data(df)

if __name__ == "__main__":
    main()
