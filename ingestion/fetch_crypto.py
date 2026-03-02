import requests
from datetime import datetime

def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true"
    }

    response = requests.get(url, params=params)

    data = response.json()

    crypto_data = {
        "coin": "bitcoin",
        "price": data["bitcoin"]["usd"],
        "market_cap": data["bitcoin"]["usd_market_cap"],
        "volume_24h": data["bitcoin"]["usd_24h_vol"],
        "timestamp": datetime.now()
    }

    return crypto_data


if __name__ == "__main__":
    result = fetch_crypto_data()
    print(result)