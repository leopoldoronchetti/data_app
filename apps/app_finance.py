import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


def app_finance():
    # Title
    st.title("Stock Time Series")

    col1, col2, col3 = st.columns([5, 10, 10])

    tickers = col1.multiselect(
        "Select stock index",
        ("MSFT", "GOOGL", "AMZN", "TSLA"),
        accept_new_options=True
    )


    if  tickers:
        num_tickers = int(len(tickers))



        period = col1.selectbox("Period:", ["1mo", "3mo", "6mo", "1y"], index=3)

        data = []
        for ticker in tickers:


            data.append(yf.download(ticker, period=period))

        # Show raw data
        #st.subheader("Raw Data")
        #st.write(data.tail())

        # Plot closing price
        col2.subheader("Closing Price Over Time")

        fig, ax = plt.subplots(num_tickers, 2, figsize=(12, 6*num_tickers))
        ax = np.atleast_2d(ax)


        for i, ticker in zip(range(num_tickers), tickers):

            fig.suptitle("Stock Price Over Time")
            ax[i, 0].plot(data[i].index, data[i]["Close"])
            ax[i, 0].axvline(datetime(2026, 2, 28), color="red", linestyle = "dashed")
            ax[i, 0].axvline(datetime(2026, 1, 3), color="red", linestyle = "dashed")

            ax[i, 0].set_xlabel("Date")
            ax[i, 0].set_ylabel("Price (USD)")
            ax[i, 0].set_title(f"{ticker} Closing Price")

            ax[i, 1].hist(data[i]["Close"], bins = 50)
            ax[i, 1].set_xlabel("Price (USD)")
            ax[i, 1].set_ylabel("Count")
            ax[i, 1].set_title(f"{ticker} Closing Price")

        plt.tight_layout()


        col2.pyplot(fig)

        col3.subheader("View correlation")
        corr_tickers = col3.multiselect(
            "Select two indices to view correlation",
            ("MSFT", "GOOGL", "AMZN", "TSLA"),
            max_selections=2,
            accept_new_options=True

        )

        if corr_tickers and len(corr_tickers) == 2:
            corr_data = []
            for corr_ticker in corr_tickers:
                corr_data.append(yf.download(corr_ticker, period="1y"))

            fig,ax = plt.subplots( figsize=(10, 6))
            ax.scatter(corr_data[0]["Close"], corr_data[1]["Close"])
            ax.set_xlabel(f"{corr_tickers[0]} Closing Price")
            ax.set_ylabel(f"{corr_tickers[1]} Closing Price")
            col3.pyplot(fig)