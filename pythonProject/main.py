import requests
from key import apikey


response = requests.get(apikey)

print("conversion_rates")
data = response.json()
time = response.json()
USD = data['conversion_rates']['USD']
TZS = data['conversion_rates']['TZS']
GBP = data['conversion_rates']['GBP']
KES = data['conversion_rates']['KES']
EUR = data['conversion_rates']['EUR']
ZAR = data['conversion_rates']['ZAR']
date = time['time_last_update_utc']
print(f'1 TZS = {USD}USD')
print(f'1 TZS = {TZS}TZS')
print(f'1 TZS = {GBP}GBP')
print(f'1 TZS = {KES}KES')
print(f'1 TZS = {EUR}EUR')
print(f'1 TZS = {ZAR}ZAR')