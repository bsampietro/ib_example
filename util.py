""" Separate module for methods that are not completely related with the IBExample class """

import sys
sys.path.append('/home/bruno/ib_api/9_73/IBJts/source/pythonclient')

from ibapi.contract import *

def get_stock_contract(symbol):
    contract = Contract()
    contract.currency = "USD"
    contract.exchange = "SMART"
    contract.secType = "STK"
    contract.symbol = symbol
    #### Certain stocks/etfs tickers needs the exchange specified in the contract
    if symbol in ("GLD", "GDX", "GDXJ"):
        contract.exchange = "ARCA"
    elif symbol in ("MSFT", "INTC", "CSCO"):
        contract.exchange = "ISLAND"
    ############################################################################
    return contract


