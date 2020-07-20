import alpaca_trade_api as tradeapi
from config import *
import json

APCA_API_BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, APCA_API_BASE_URL)
api.submit_order(symbol='SPY', qty='1', side='buy', type='market', time_in_force='day')