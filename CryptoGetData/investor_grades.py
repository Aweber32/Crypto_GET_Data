import requests
from datetime import datetime
from zoneinfo import ZoneInfo

def run():
    HEADERS = {
        "accept": "application/json",
        "x-api-key": "tm-2670d02e-7da2-444f-9762-5897fa08be20",
    }

    TOKENS = {
        '3375',  # BTC
        '3306',  # ETH
        '3369',  # XRP
        '3988',  # SOL
    }

    est_hour = datetime.now(ZoneInfo("America/New_York")).replace(minute=0, second=0, microsecond=0)

    bulk_payload = []

    for token in TOKENS:
        URL_SIGNALS = f"https://api.tokenmetrics.com/v2/trading-signals?token_id={token}&limit=1"
        URL_GRADES = f"https://api.tokenmetrics.com/v2/trader-grades?token_id={token}&limit=1"
        
        try:
            response_signals = requests.get(URL_SIGNALS, headers=HEADERS)
            response_grades = requests.get(URL_GRADES, headers=HEADERS)

            data_signals = response_signals.json().get('data', [])
            data_grades = response_grades.json().get('data', [])

            if data_signals and data_grades:
                signal = data_signals[0]
                grade = data_grades[0]

                id = datetime.now().strftime("%Y%m%d%H%M%S") + signal["TOKEN_SYMBOL"]

                payload = {
                    "id": id,
                    "Symbol": signal["TOKEN_SYMBOL"],
                    "Date": est_hour.isoformat(),
                    "TokenName": signal.get("TOKEN_NAME"),
                    "TradingSignal": signal.get("TRADING_SIGNAL"),
                    "TokenTrend": signal.get("TOKEN_TREND"),
                    "TradingSignalsReturns": signal.get("TRADING_SIGNALS_RETURNS"),
                    "HoldingReturns": signal.get("HOLDING_RETURNS"),
                    "TMTraderGrade": signal.get("TM_TRADER_GRADE"),
                    "TMInvestorGrade": signal.get("TM_INVESTOR_GRADE"),
                    "TAGrade": grade.get("TA_GRADE"),
                    "QuantGrade": grade.get("QUANT_GRADE"),
                    "TMTraderGrade24hPctChange": grade.get("TM_TRADER_GRADE_24H_PCT_CHANGE")
                }

                bulk_payload.append(payload)

        except Exception as e:
            print(f"Error retrieving data for token {token}: {e}")

    if bulk_payload:
        post_url = "https://cryptocurrency.azurewebsites.net/api/InvestorGrade/bulk"
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(post_url, json=bulk_payload, headers=headers, timeout=10)
        print(f"Bulk InvestorGrades POST Status: {response.status_code}")
    else:
        print("No investor grades to send.")
