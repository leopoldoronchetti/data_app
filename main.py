import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Title
st.title("Apple Stock Time Series")

# Fetch data for Apple (AAPL)
ticker = "AAPL"
data = yf.download(ticker, period="1y")

# Show raw data
st.subheader("Raw Data")
st.write(data.tail())

# Plot closing price
st.subheader("Closing Price Over Time")

fig, ax = plt.subplots()
ax.plot(data.index, data["Close"])
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")
ax.set_title("AAPL Closing Price")

st.pyplot(fig)
