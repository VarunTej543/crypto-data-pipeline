CREATE TABLE IF NOT EXISTS crypto_prices (
    id SERIAL PRIMARY KEY,
    coin_name VARCHAR(50),
    price FLOAT,
    market_cap FLOAT,
    volume_24h FLOAT,
    timestamp TIMESTAMP
);