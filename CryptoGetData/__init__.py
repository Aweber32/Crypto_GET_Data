import logging
import azure.functions as func
import requests
import time
import functools
import os

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

def main(myTimer: func.TimerRequest) -> None:
    logging.info("Crypto Azure Function started.")

    sentiment_result = sentiment_run()
    investor_grade_result = investor_grade_run()
    price_data_result = price_data_run()

    logging.info(f"Results: Sentiment: {sentiment_result}, InvestorGrade: {investor_grade_result}, PriceData: {price_data_result}")