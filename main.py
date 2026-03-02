from ingestion.fetch_crypto import fetch_crypto_data

def run_pipeline():
    data = fetch_crypto_data()
    print("Pipeline Running...")
    print(data)

if __name__ == "__main__":
    run_pipeline()