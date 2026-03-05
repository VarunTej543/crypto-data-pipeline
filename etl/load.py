from database.db_connection import get_connection

def load(df):

    print("Loading data into database...")

    conn = get_connection()
    cursor = conn.cursor()

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO crypto_prices
            (coin_name, price, market_cap, volume_24h, timestamp)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                row["coin"],
                row["price"],
                row["market_cap"],
                row["volume_24h"],
                row["timestamp"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()