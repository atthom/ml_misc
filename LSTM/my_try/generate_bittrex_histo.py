import urllib.request
import shutil
import os
import logging
from datetime import datetime
from datetime import timezone

#  https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName=BTC-WAVES&tickInterval=thirtyMin&_=1499100220008


DOWLOAD_MARKETS = ["BTC-ETH", "BTC-LTC", "BTC-SC", "BTC-DGB", "BTC-DASH", "BTC-STRAT", "BTC-BTS", "BTC-ETC"]


url = "https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName="

def fetch_market(market: str) -> None:
    get = url + market + "&tickInterval=fiveMin"
    print(get)
    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(get) as response:
        with open(market + ".history", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)


def gettimestamp(dd):
    do = datetime.strptime(dd, '%Y-%m-%dT%H:%M:%S')
    timestamp = do.replace(tzinfo=timezone.utc).timestamp()
    return timestamp

if __name__ == "__main__":
    for market in DOWLOAD_MARKETS:
        fetch_market(market)
    dd = "2017-10-21T22:35:00"
    dd1 = "2017-10-22T16:45:00"
    dd2 = "2017-11-11T16:30:00"

    print(gettimestamp(dd1))
    print(gettimestamp(dd2))
    