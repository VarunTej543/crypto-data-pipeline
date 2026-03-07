import streamlit as st
import pandas as pd
from database.db_connection import get_connection

st.title("📊 Crypto Price Dashboard")

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