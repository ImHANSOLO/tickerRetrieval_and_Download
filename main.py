from tickerRetrieval import get_etf_tickers, extract_tickers
from priceDataDownloadScript import download_price_data


def main():
    # getting ETF tickers
    raw_data = get_etf_tickers()
    etf_tickers = extract_tickers(raw_data)

    # downloading the pricing data
    price_data = download_price_data(etf_tickers)

    # saving it as a csv file
    price_data.to_csv("etf_price_data.csv")
    print("Data has been successfully downloaded and saved.")


if __name__ == "__main__":
    main()
