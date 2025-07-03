import ccxt
import os

symbol = os.environ.get('symbol')

def get_bgb_price():
    """Fetches and prints the current BGB/USDT price from Bitget."""
    try:
        exchange = ccxt.bitget()
        ticker = exchange.fetch_ticker(symbol)
        print(f"The current price of {symbol} is: {ticker['last']}")
    except ccxt.NetworkError as e:
        print(f"Network error: {e}")
    except ccxt.ExchangeError as e:
        print(f"Exchange error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    get_bgb_price()
