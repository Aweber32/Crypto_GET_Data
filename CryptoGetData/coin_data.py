import requests
from datetime import datetime
from zoneinfo import ZoneInfo


def run():
    url = "pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    url_FnG = "pro-api.coinmarketcap.com/v3/fear-and-greed/latest"
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'f64a2377-9da9-42dc-b1f1-8318478faced',
    }

    TARGET_SYMBOLS = {"BTC", "ETH", "XRP", "SOL"}

    est_hour = datetime.now(ZoneInfo("America/New_York")).replace(minute=0, second=0, microsecond=0)

    # Make a request to the CoinMarketCap API
    response = requests.get(f"https://{url}", headers=headers)
    response_FnG = requests.get(f"https://{url_FnG}", headers=headers)

    # Get Fear and Greed Index data
    FnG_data = response_FnG.json().get('data', {}).get('value')
    print(f"Fear and Greed Index: {FnG_data}")

    bulk_payload = []

    if response.status_code == 200:
        data = response.json()
        cryptocurrencies = data.get('data', [])

        for crypto in cryptocurrencies:
            symbol = crypto.get('symbol')
            if symbol in TARGET_SYMBOLS:
                id = str(datetime.now().strftime("%Y%m%d%H%M%S")) + symbol
                name = crypto.get('name')
                price = crypto.get('quote', {}).get('USD', {}).get('price')
                volume_24h = crypto.get('quote', {}).get('USD', {}).get('volume_24h')
                volume_change_24h = crypto.get('quote', {}).get('USD', {}).get('volume_change_24h')
                percent_change_1h = crypto.get('quote', {}).get('USD', {}).get('percent_change_1h')
                percent_change_24h = crypto.get('quote', {}).get('USD', {}).get('percent_change_24h')
                percent_change_7d = crypto.get('quote', {}).get('USD', {}).get('percent_change_7d')
                percent_change_30d = crypto.get('quote', {}).get('USD', {}).get('percent_change_30d')
                percent_change_60d = crypto.get('quote', {}).get('USD', {}).get('percent_change_60d')
                percent_change_90d = crypto.get('quote', {}).get('USD', {}).get('percent_change_90d')

                payload = {
                    "id": id,
                    "Symbol": symbol,
                    "TokenName": name,
                    "Date": est_hour.isoformat(),
                    "FearandGreed": FnG_data,
                    "Price": price,
                    "Volume24h": volume_24h,
                    "VolumeChange24h": volume_change_24h,
                    "PercentChange1h": percent_change_1h,
                    "PercentChange24h": percent_change_24h,
                    "PercentChange7d": percent_change_7d,
                    "PercentChange30d": percent_change_30d,
                    "PercentChange60d": percent_change_60d,
                    "PercentChange90d": percent_change_90d
                }

                bulk_payload.append(payload)

    # 🔁 Bulk post the collected data
    if bulk_payload:
        post_url = "https://cryptocurrency.azurewebsites.net/api/CoinData/bulk"
        post_headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(post_url, json=bulk_payload, headers=post_headers, timeout=10)
        print(f"Bulk CoinData POST Status: {response.status_code}")
    else:
        print("No coin data to send.")