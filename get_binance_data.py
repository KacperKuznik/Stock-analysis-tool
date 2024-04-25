import requests
import datetime

"""
example api response
[
  [
    1499040000000,      // Kline open time
    "0.01634790",       // Open price
    "0.80000000",       // High price
    "0.01575800",       // Low price
    "0.01577100",       // Close price
    "148976.11427815",  // Volume
    1499644799999,      // Kline Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "0"                 // Unused field, ignore.
  ]
]
"""

def get_data(start_time, symbol, interval):
  unix_start_time = int(start_time.strftime("%s")) * 1000 
  res = requests.get('https://www.binance.com/api/v3/klines', params={"symbol": symbol, "interval": interval, "startTime": unix_start_time})

  return res.json()

#usage
start_time = datetime.datetime(2024, 4, 10)
symbol = "BTCUSDT"
interval = "1d"

for kline in get_data(start_time, symbol, interval):
    print(kline)