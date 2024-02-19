import yfinance as yf
import pandas as pd
from tickerRetrieval import get_etf_tickers


def download_price_data(tickers):
    # 创建一个空的DataFrame来存储所有ETF的价格数据
    all_data = pd.DataFrame()

    for ticker in tickers:
        # 下载每个ETF的数据
        data = yf.download(ticker, start="2022-01-01", end="2022-12-31")  # 示例日期范围
        data['Ticker'] = ticker  # 添加一个新列以标识ETF的ticker
        all_data = all_data.append(data)

    # 返回包含所有ETF价格数据的DataFrame
    return all_data


# 从tickerRetrieval.py获取ETF tickers
base_url = "https://finviz.com/screener.ashx"
etf_tickers = get_etf_tickers(base_url)

# 下载ETF价格数据
etf_price_data = download_price_data(etf_tickers)

# 选择保存数据的方式，例如保存为CSV文件
etf_price_data.to_csv("etf_price_data.csv")
