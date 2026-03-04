from database.db_connection import get_connection

def insert_crypto_data(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO crypto_prices
        (coin_name, price, market_cap, volume_24h, timestamp)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["coin"],
        data["price"],
        data["market_cap"],
        data["volume_24h"],
        data["timestamp"]
    ))

    conn.commit()
    cursor.close()
    conn.close()