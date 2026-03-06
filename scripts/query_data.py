import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from database.db_connection import get_connection


def get_crypto_prices():
    conn = get_connection()
    query = "SELECT * FROM crypto_prices"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


if __name__ == "__main__":
    data = get_crypto_prices()
    print(data)
    print("\nAverage Price:")
    print(data['price'].mean())