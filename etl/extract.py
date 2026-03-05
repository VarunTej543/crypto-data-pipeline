from ingestion.fetch_crypto import fetch_crypto_data

def extract():
    print("Extracting data from API...")
    data = fetch_crypto_data()
    return data