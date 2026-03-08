import time

from etl.extract import extract
from etl.transform import transform
from etl.load import load
from database.init_db import initialize_database


def run_pipeline():
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)

    print("ETL Pipeline completed successfully!")


if __name__ == "__main__":

    # create database tables once
    initialize_database()

    while True:
        try:
            run_pipeline()
        except Exception as e:
            print("Error:", e)

        print("Waiting 60 seconds for next run...\n")
        time.sleep(60)