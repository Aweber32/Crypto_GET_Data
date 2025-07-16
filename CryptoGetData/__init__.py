import logging
import azure.functions as func
import requests
import time
import functools
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Retry decorator for transient network issues
def retry(max_retries=3, delay=2):
    def decorator_retry(func):
        @functools.wraps(func)
        def wrapper_retry(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.error(f"Attempt {attempt} failed: {e}")
                    if attempt == max_retries:
                        raise
                    time.sleep(delay)
        return wrapper_retry
    return decorator_retry

requests.get = retry(max_retries=3, delay=2)(requests.get)

# Import your crypto scripts
from .reddit import run as sentiment_run
from .investor_grades import run as investor_grade_run
from .coin_data import run as price_data_run

# Wake up the API
url = 'https://cryptocurrency.azurewebsites.net/api/sentiment'
max_attempts = 5

for attempt in range(1, max_attempts + 1):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Crypto API wakeup call successful.")
        break
    except requests.exceptions.RequestException as e:
        print(f"Wakeup attempt {attempt} failed: {e}")
        if attempt < max_attempts:
            time.sleep(5)
        else:
            print("Exceeded maximum wakeup attempts.")

time.sleep(5)

now_est = datetime.now(ZoneInfo("America/New_York"))
current_hour = now_est.hour

def main(myTimer: func.TimerRequest) -> None:
    logging.info("Crypto Azure Function started.")

    sentiment_result = sentiment_run()
    price_data_result = price_data_run()

    if current_hour == 6:
        investor_grade_result = investor_grade_run()
        logging.info(f"InvestorGrade ran: {investor_grade_result}")
    else:
        investor_grade_result = "Skipped (not 6 AM hour)"
        logging.info("InvestorGrade skipped.")

    logging.info(f"Results: Sentiment: {sentiment_result}, InvestorGrade: {investor_grade_result}, PriceData: {price_data_result}")

    try:
        start_container_job()
    except Exception as e:
        logging.error(f"Error starting container job: {e}")

from azure.identity import DefaultAzureCredential

def start_container_job():
    subscription_id = "24e9a834-c31f-4f9c-97c2-b069d8b256b3"
    resource_group = "Crypto"
    job_name = "crypto-engineering"
    api_version = "2023-05-01"

    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default").token

    url = (
        f"https://management.azure.com/subscriptions/{subscription_id}/"
        f"resourceGroups/{resource_group}/providers/Microsoft.App/jobs/{job_name}/start?api-version={api_version}"
    )

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, headers=headers)
    if response.status_code in [200, 202]:
        logging.info(f"Container App Job '{job_name}' started successfully.")
    else:
        logging.error(f"Failed to start job: {response.status_code} - {response.text}")
