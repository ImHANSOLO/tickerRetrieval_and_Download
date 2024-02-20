import requests
import re
from bs4 import BeautifulSoup


def get_etf_tickers(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    raw_data = []
    page = 1  # Start from the first page
    while True:
        url = f"{base_url}?r={page}"
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a', href=True)
            new_tickers_found = False
            for link in links:
                if 'ty=c&p=d&b=1' in link['href']:
                    ticker = link.text.strip().upper()
                    if ticker not in raw_data:
                        raw_data.append(ticker)
                        new_tickers_found = True
            if not new_tickers_found:
                break  # No new tickers found on this page, assume we are done
            page += 20  # Adjust the page number or offset as needed
        except requests.RequestException as e:
            print(f"Error fetching ETF tickers: {e}")
            break
    return raw_data


def extract_tickers(raw_data):
    ticker_pattern = re.compile(r'\b[A-Z]{1,4}\b')  # Suppose ticker has 1 to 4 capital letters
    tickers = []
    for item in raw_data:
        matches = ticker_pattern.findall(item)
        tickers.extend(matches)  # Add all matches found
    # Deduplication
    tickers = list(set(tickers))
    return tickers


base_url = "https://finviz.com/screener.ashx"
# rawData = get_etf_tickers(base_url)
tickers = extract_tickers(get_etf_tickers(base_url))
print(tickers)
