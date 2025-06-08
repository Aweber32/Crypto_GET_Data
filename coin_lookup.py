import requests

url = "https://api.tokenmetrics.com/v2/tokens?token_name=XRP"

headers = {
    "accept": "application/json",
    "x-api-key": "tm-2670d02e-7da2-444f-9762-5897fa08be20"
}

response = requests.get(url, headers=headers)

print(response.text)