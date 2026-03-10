import requests

def extract():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum,solana,binancecoin,cardano",
        "vs_currencies": "usd",
        "include_market_cap": "true",
        "include_24hr_vol": "true"
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data