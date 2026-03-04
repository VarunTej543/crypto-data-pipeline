from database.init_db import initialize_database
from ingestion.fetch_crypto import fetch_crypto_data
from database.insert_data import insert_crypto_data

def run_pipeline():
    print("Fetching crypto data...")
    data = fetch_crypto_data()

    print("Inserting into database...")
    insert_crypto_data(data)

    print("Pipeline completed successfully!")

if __name__ == "__main__":
    initialize_database()
    run_pipeline()