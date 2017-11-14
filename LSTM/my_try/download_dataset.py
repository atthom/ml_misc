
"""Download Poloniex market data."""

import urllib.request
import shutil
import os
import logging


DOWLOAD_MARKETS = ["BTC_ETH", "BTC_LTC", "BTC_SC", "BTC_DGB", "BTC_DASH", "BTC_STRAT", "BTC_BTS", "BTC_ETC"]

def fetch_market(market: str, logger: logging, force_update: bool = True) -> None:
    """
    Fetch automatically the latest market data on poloniex.

    It can force_update to fetch newly created data, even if the
    market file is already downloaded.
    """
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    logger.addHandler(ch)

    if os.path.exists(market + ".history"):
        if force_update:
            logger.info("Market %s already downloaded, updating...", market)
        else:
            logger.info("Market already downloaded, not updated.")
            return
    else:
        logger.info("Downloading market %s", market)
    url = "https://poloniex.com/public?command=returnChartData&currencyPair=" + \
        market + "&start=1388534400&end=9999999999&period=300"

    # Download the file from `url` and save it locally under `file_name`:
    with urllib.request.urlopen(url) as response:
        with open(market + ".history", 'wb') as out_file:
            shutil.copyfileobj(response, out_file)


if __name__ == "__main__":
    log = logging.Logger("Log")

    for market in DOWLOAD_MARKETS:
        fetch_market(market, log)
