import requests
from datetime import datetime

# This script fetches cryptocurrency data from CoinMarketCap API and prints relevant information.
url = "pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
url_FnG = "pro-api.coinmarketcap.com/v3/fear-and-greed/latest"
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f64a2377-9da9-42dc-b1f1-8318478faced',
}

# Make a request to the CoinMarketCap API
response = requests.get(f"https://{url}", headers=headers)
response_FnG = requests.get(f"https://{url_FnG}", headers=headers)

# Get Fear and Greed Index data
FnG_data = response_FnG.json().get('data', {}).get('value')
print(f"Fear and Greed Index: {FnG_data}")

if response.status_code == 200:
    data = response.json()
    # Extract the relevant information from the response
    cryptocurrencies = data.get('data', [])
    for crypto in cryptocurrencies:
        id = str(datetime.now().strftime("%Y%m%d%H%M%S")) + crypto.get('symbol') 
        name = crypto.get('name')
        symbol = crypto.get('symbol')
        price = crypto.get('quote', {}).get('USD', {}).get('price')
        volume_24h = crypto.get('quote', {}).get('USD', {}).get('volume_24h')
        volume_change_24h = crypto.get('quote', {}).get('USD', {}).get('volume_change_24h')
        percent_change_1h = crypto.get('quote', {}).get('USD', {}).get('percent_change_1h')
        percent_change_24h = crypto.get('quote', {}).get('USD', {}).get('percent_change_24h')
        percent_change_7d = crypto.get('quote', {}).get('USD', {}).get('percent_change_7d')
        percent_change_30d = crypto.get('quote', {}).get('USD', {}).get('percent_change_30d')
        percent_change_60d = crypto.get('quote', {}).get('USD', {}).get('percent_change_60d')
        percent_change_90d = crypto.get('quote', {}).get('USD', {}).get('percent_change_90d')
        print(f"{name} ({symbol}): ${price:.2f}" 
              f"ID : {id},"
              f"Volume Change (24h): {volume_change_24h:.2f}%, "
              f"1h Change: {percent_change_1h:.2f}%, "
              f"24h Change: {percent_change_24h:.2f}%, "
              f"7d Change: {percent_change_7d:.2f}%, "
              f"30d Change: {percent_change_30d:.2f}%, "
              f"60d Change: {percent_change_60d:.2f}%, "
              f"90d Change: {percent_change_90d:.2f}%")