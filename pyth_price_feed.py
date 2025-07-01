# https://hermes.pyth.network/docs/#/
# https://docs.pyth.network/price-feeds/price-feeds
url = "https://hermes.pyth.network/v2/price_feeds?"
import requests
def get_price_feed():
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching price feed: {e}")
        return None

if __name__ == "__main__":
    price_feed = get_price_feed()
    if price_feed:
        print(f"Total price feeds: {len(price_feed)}")
        #   {
#     "id": "c415de8d2eba7db216527dff4b60e8f3a5311c740dadb233e13e12547e226750",
#     "attributes": {
#       "asset_type": "Crypto",
#       "base": "NEAR",
#       "description": "NEAR PROTOCOL / US DOLLAR",
#       "display_symbol": "NEAR/USD",
#       "generic_symbol": "NEARUSD",
#       "quote_currency": "USD",
#       "schedule": "America/New_York;O,O,O,O,O,O,O;",
#       "symbol": "Crypto.NEAR/USD"
#     }
#   }
        for i in price_feed[0:10]:
            print(i['id'])
            print(i['attributes']['description'])