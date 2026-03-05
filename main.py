from etl.extract import extract
from etl.transform import transform
from etl.load import load
from database.init_db import initialize_database

def run_pipeline():

    initialize_database()

    raw_data = extract()

    transformed_data = transform(raw_data)

    load(transformed_data)

    print("ETL Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()