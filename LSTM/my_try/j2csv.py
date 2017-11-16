import json
import csv

x = json.load(open("./datasets/BTC_ETH.history"))

f = csv.writer(open("./datasets/BTC_ETH.csv", "w", newline=''))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["date", "high", "low", "open", "close", "volume", "quoteVolume", "weightedAverage"])

# {"date":1439010600,"high":50,"low":0.00900005,"open":50,"close":0.00900005,"volume":10.65496054,"quoteVolume":1033.26076055,"weightedAverage":0.01031197}

i =0

print(len(open("BTC_ETH.history", "r").readline()))

print(len(x))
for row in x:
    #print(row["date"], row["high"], row["low"], row["open"], row["close"], row["volume"], row["quoteVolume"], row["weightedAverage"])
    f.writerow([row["date"], row["high"], row["low"], row["open"], row["close"], row["volume"], row["quoteVolume"], row["weightedAverage"]])

