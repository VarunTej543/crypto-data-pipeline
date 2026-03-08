from streamlit_autorefresh import st_autorefresh

import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("📊 Crypto Price Dashboard")

st_autorefresh(interval=10000, key="crypto_refresh")

conn = get_connection()

query = """
SELECT coin_name, price, market_cap, volume_24h, timestamp
FROM crypto_prices
ORDER BY timestamp DESC
LIMIT 20
"""

df = pd.read_sql(query, conn)

st.subheader("Latest Crypto Prices")
st.dataframe(df)

st.subheader("Price Chart")

chart_data = df.sort_values("timestamp")

st.line_chart(chart_data.set_index("timestamp")["price"])

st.subheader("Top 10 Cryptocurrencies by Market Cap")

top_query = """
SELECT coin_name, price, market_cap
FROM crypto_prices
ORDER BY market_cap DESC
LIMIT 10
"""

top_df = pd.read_sql(top_query, conn)

st.dataframe(top_df)

st.subheader("Market Cap Comparison")

chart_df = top_df.set_index("coin_name")

st.bar_chart(chart_df["market_cap"])