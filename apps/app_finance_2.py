import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def app_finance_2():
    # Title
    st.title("Stock Time Series")

    col1, col2, col3 = st.columns([7, 10, 10])

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

        fig = make_subplots(rows=num_tickers, cols=2)

        for i, ticker in zip(range(num_tickers), tickers):
            df = data[i].sort_index().dropna()

            fig.add_trace(
                go.Scatter(x=df.index, y=df["Close"], mode="lines"),
                row=i + 1, col=1
            )

            fig.add_trace(
                go.Scatter(x=df.index, y=df["Close"], mode="lines"),
                row=i + 1, col=2
            )

        fig.update_layout(height=600, width=800, title_text="Side By Side Subplots")

        col2.plotly_chart(fig, use_container_width=True)

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