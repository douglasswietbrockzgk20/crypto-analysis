import ccxt
import requests # Adding requests for direct HTTP calls if ccxt doesn't support the v2 endpoint easily

def get_open_interest(product_type: str) -> dict[str, str]:
    """
    Fetches the open interest for all symbols of a given product type from Bitget
    and returns it as a dictionary.
    Open interest is represented by the 'holdingAmount' field in the API response.
    Returns an empty dictionary if data fetching fails or no data is found.
    """
    url = "https://api.bitget.com/api/v2/mix/market/tickers"
    params = {"productType": product_type}
    open_interest_data = {}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)

        data = response.json()

        if data.get("code") == "00000" and "data" in data:
            if not data["data"]:
                # print(f"No open interest data found for product type: {product_type}") # Silenced for library use
                return open_interest_data # Return empty dict

            for ticker_data in data["data"]:
                symbol = ticker_data.get("symbol")
                holding_amount = ticker_data.get("holdingAmount")
                if symbol and holding_amount is not None:
                    open_interest_data[symbol] = holding_amount
                # else:
                    # print(f"  Incomplete data for one ticker: {ticker_data}") # Silenced for library use
        else:
            print(f"API error when fetching open interest for {product_type}: {data.get('msg', 'Unknown error')}")
            return open_interest_data # Return empty dict on API error message

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error fetching open interest for {product_type}: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Network error fetching open interest for {product_type}: {e}")
    except ValueError as e: # For JSON decoding errors
        print(f"Error decoding JSON response for {product_type}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while fetching for {product_type}: {e}")

    return open_interest_data

if __name__ == "__main__":
    # Example usage:
    print("Fetching open interest for USDT-FUTURES...")
    usdt_oi = get_open_interest("USDT-FUTURES")
    if usdt_oi:
        print(f"USDT-FUTURES Open Interest Data ({len(usdt_oi)} symbols):")
        for symbol, oi in list(usdt_oi.items())[:5]: # Print first 5 for brevity
            print(f"  Symbol: {symbol}, Open Interest: {oi}")
    else:
        print("No USDT-FUTURES open interest data returned or an error occurred.")

    print("\nFetching open interest for COIN-FUTURES...")
    coin_oi = get_open_interest("COIN-FUTURES")
    if coin_oi:
        print(f"COIN-FUTURES Open Interest Data ({len(coin_oi)} symbols):")
        for symbol, oi in list(coin_oi.items())[:5]: # Print first 5 for brevity
            print(f"  Symbol: {symbol}, Open Interest: {oi}")
    else:
        print("No COIN-FUTURES open interest data returned or an error occurred.")

    print("\nFetching open interest for INVALID-FUTURES (expected empty or error)...")
    invalid_oi = get_open_interest("INVALID-FUTURES")
    if not invalid_oi:
        print("Correctly received no data or an error for INVALID-FUTURES.")
    else:
        print(f"Unexpectedly received data for INVALID-FUTURES: {invalid_oi}")
