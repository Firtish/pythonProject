from typing import List
import os
from pydantic import BaseModel

import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/B/AOA/'
response = re.get(url)
data = response.json()
print(data)
print(data['rates'][0]['mid'])


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class CurrencyInfo(BaseModel):
    table: str
    code: str
    rates: List[Rate]


currency_info = CurrencyInfo(**data)
print(currency_info)
print("Kurs kwanza:", currency_info.rates[0].mid)
os.system('cls')
print("\033[H\033[J", end="")
os.system('cmd /c "cls"')
