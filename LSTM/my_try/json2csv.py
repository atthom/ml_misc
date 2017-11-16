import json
import csv
from datetime import datetime
from datetime import timezone


def gettimestamp(dd):
    do = datetime.strptime(dd, '%Y-%m-%dT%H:%M:%S')
    timestamp = do.replace(tzinfo=timezone.utc).timestamp()
    return timestamp


x = json.load(open("./datasets/BTC-ETH.history"))

f = csv.writer(open("./datasets/BTC-ETH.csv", "w", newline=''))

f.writerow(["time", "high", "low", "open", "close", "V", "BV"])

for row in x["result"]:
    f.writerow([gettimestamp(row["T"]), row["H"], row["L"], row["O"], row["C"], row["V"], row["BV"]])
