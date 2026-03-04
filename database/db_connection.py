import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="crypto_db",
        user="postgres",
        password="Earthly009#"
    )
    return conn