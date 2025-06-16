import requests
from datetime import datetime, timedelta

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

for token in TOKENS:
    URL_SIGNALS = f"https://api.tokenmetrics.com/v2/trading-signals?token_id={token}&limit=1"
    URL_GRADES = f"https://api.tokenmetrics.com/v2/trader-grades?token_id={token}&limit=1"
    
    response_signals = requests.get(URL_SIGNALS, headers=HEADERS)
    response_grades = requests.get(URL_GRADES, headers=HEADERS)

    data_signals = response_signals.json()
    data_grades = response_grades.json()

    for signal in data_signals.get('data', []):
        id = str(datetime.now().strftime("%Y%m%d%H%M%S")) + signal["TOKEN_SYMBOL"]
        token_name = signal["TOKEN_NAME"]
        symbol = signal["TOKEN_SYMBOL"]
        date = signal["DATE"]
        trading_signal = signal["TRADING_SIGNAL"]
        token_trend = signal["TOKEN_TREND"]
        trading_signals_returns = signal["TRADING_SIGNALS_RETURNS"]
        holding_returns = signal["HOLDING_RETURNS"]
        tm_trader_grade = signal["TM_TRADER_GRADE"]
        tm_investor_grade = signal["TM_INVESTOR_GRADE"]
    for grade in data_grades.get('data', []):
        ta_grade = grade["TA_GRADE"]
        quant_grade = grade["QUANT_GRADE"]
        tm_trader_grade_24h_pct_change = grade["TM_TRADER_GRADE_24H_PCT_CHANGE"]
    url = "https://cryptocurrency.azurewebsites.net/api/InvestorGrade"

    payload = {      
        "id": id,
        "Symbol": symbol,
        "Date": date, 
        "TokenName": token_name,
        "TradingSignal": trading_signal,
        "TokenTrend": token_trend,
        "TradingSignalsReturns": trading_signals_returns,
        "HoldingReturns": holding_returns,
        "TMTraderGrade": tm_trader_grade,
        "TMInvestorGrade": tm_investor_grade,
        "TAGrade": ta_grade,
        "QuantGrade": quant_grade,
        "TMTraderGrade24hPctChange": tm_trader_grade_24h_pct_change
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, timeout=5)
    print(f"Response Status: {response.status_code}")

                
       

      


