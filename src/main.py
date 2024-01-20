from scrape import Scrape
from trade import Trade
from alpacaTrading import AlpacaTrading

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
    output = s1.getTrades()

    # print(output)

    for i in output:
        print(" ")
        
        print(output.get(i).getTicker() + " " + output.get(i).getType()+ " " + output.get(i).getDays())
        print(" ")

    # marketOrderData = alpaca.prepMarketOrderBuy(output[0].getTicker(), 1)
    # print(marketOrderData)
    # marketOrderBuy = alpaca.makeMarketOrder(marketOrderData)
    # print(marketOrderBuy)


if __name__=='__main__':
    main()