import pandas as pd

def transform(data):

    print("Transforming data...")

    df = pd.DataFrame([data])

    # Data Cleaning
    df["coin"] = df["coin"].str.lower()
    df["price"] = df["price"].astype(float)

    # Add processing timestamp
    df["processed_at"] = pd.Timestamp.now()

    return df