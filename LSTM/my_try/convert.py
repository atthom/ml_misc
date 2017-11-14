import json
from pprint import pprint

def get_new_response(old_response, last_close, new_close):
    if last_new_response == 'response' or last_new_response == 1:
        new_response = 0
    

with open('BTC-ETH.history') as data_file:    
    data = json.load(data_file)

new_data = [['response','O', 'H', 'L', 'C', 'V', 'T', 'BV']]

for tick in data["result"]:
    last_new_tick = data[-1]
    last_new_response = last_new_tick[0]
    last_close = int(last_new_tick[4])
    new_close = int(tick['C'])

    if last_new_response == 'response':
        new_response = 0
    elif last_new_response == 1:
        
        

    new_tick = [new_response, tick['O'], tick['H'], tick['L'], tick['C'], tick['V'], tick['T'], tick['BV']]


