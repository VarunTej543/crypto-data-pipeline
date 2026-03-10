import pandas as pd
from datetime import datetime

def transform(data):

    rows = []

    for coin_name, values in data.items():

        rows.append({
            "coin_name": coin_name,
            "price": values["usd"],
            "market_cap": values["usd_market_cap"],
            "volume_24h": values["usd_24h_vol"],
            "timestamp": datetime.now()
        })

    df = pd.DataFrame(rows)

    return df