import requests
from bs4 import BeautifulSoup

def get_etf_tickers(base_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    tickers = []
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
                    if ticker not in tickers:
                        tickers.append(ticker)
                        new_tickers_found = True
            if not new_tickers_found:
                break  # No new tickers found on this page, assume we are done
            page += 20  # Adjust the page number or offset as needed
        except requests.RequestException as e:
            print(f"Error fetching ETF tickers: {e}")
            break
    return tickers

base_url = "https://finviz.com/screener.ashx"
etf_tickers = get_etf_tickers(base_url)
print(etf_tickers)
