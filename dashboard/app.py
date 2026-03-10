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

# Dropdown selector
coin = st.selectbox(
    "Select Cryptocurrency",
    df["coin_name"].unique()
)

# Filter data for selected coin
filtered_df = df[df["coin_name"] == coin]

st.subheader("Latest Crypto Prices")
st.dataframe(filtered_df)

st.subheader("Price Chart")

chart_data = filtered_df.sort_values("timestamp")

st.line_chart(filtered_df.set_index("timestamp")["price"])

latest = filtered_df.iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Price", f"${latest['price']:,.2f}")
col2.metric("Market Cap", f"${latest['market_cap']:,.0f}")
col3.metric("24h Volume", f"${latest['volume_24h']:,.0f}")

st.subheader("Top 10 Cryptocurrencies by Market Cap")

top_query = """
SELECT DISTINCT ON (coin_name)
coin_name, price, market_cap, timestamp
FROM crypto_prices
ORDER BY coin_name, timestamp DESC;
"""

top_df = pd.read_sql(top_query, conn)

st.dataframe(top_df)

st.subheader("Market Cap Comparison")

chart_df = top_df.set_index("coin_name")

st.bar_chart(chart_df["market_cap"])