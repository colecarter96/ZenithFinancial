from scrape import Scrape
from trade import Trade
from alpacaTrading import AlpacaTrading

import time

import requests 
from bs4 import BeautifulSoup 

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass 
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


def main():

    alpaca = AlpacaTrading()

    s1 = Scrape()
    # print(s1.soup)
    output = s1.initalGetTrades()
    marketOrderList = alpaca.prepMarketOrders(output)
    print(marketOrderList)
    alpaca.executeMarketOrders(marketOrderList)
    s1.updateTxList(output)

    print(s1.politicians)

    # print("start of initial")
    # print(lol)
    
    # make sure to get new link

    # comment for testing on Cole Branch

    while True:
        # update scrape
        s1.updateConnection()

        newOutput = s1.updateGetTrades()
        if(newOutput != None):
            newMarketOrderList = alpaca.prepMarketOrders(newOutput)
            alpaca.executeMarketOrders(newMarketOrderList)

            s1.updateTxList(newOutput)

        time.sleep(3600)

    



if __name__=='__main__':
    main()