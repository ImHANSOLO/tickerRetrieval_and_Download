import yfinance as yf
import pandas as pd
from tickerRetrieval import get_etf_tickers, extract_tickers



def download_price_data(tickers):
    # Creating an empty DataFrame to store the price data of all ETFs
    all_data = pd.DataFrame()

    for ticker in tickers:
        # Downloading data for each ETF
        try:
            data = yf.download(ticker, start="2024-02-17", end="2024-02-17")  # here you can customise the start and end date
            data['Ticker'] = ticker  # Add a new column to identify the ticker for ETF
            all_data = pd.concat([all_data, data], ignore_index=True)
        except KeyError:
            print(f"Data for ticker {ticker} not found within the specified date range.")
        except Exception as e:
            print(f"An error occurred for ticker {ticker}: {e}")
        print(all_data)
    # Returns a DataFrame containing all ETF price data
    return all_data


# getting ETF tickers from tickerRetrieval.py
base_url = "https://finviz.com/screener.ashx"
etf_tickers = extract_tickers(get_etf_tickers(base_url))

# Download ETF price data
etf_price_data = download_price_data(etf_tickers)

# save the data as a CSV file
etf_price_data.to_csv("etf_price_data.csv")
