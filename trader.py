import alpaca_trade_api as tradeapi
from config import *
import json

BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(KEY_ID, SECRET_KEY, BASE_URL)