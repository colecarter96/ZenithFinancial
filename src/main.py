from scrape import Scrape
from trade import Trade

import requests 
from bs4 import BeautifulSoup 

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass 
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


def main():
    
    # Making a GET request 
    r = requests.get('https://www.capitoltrades.com/trades') 

    #resulting hashmap
    resultMap = {}
    
    # print request object 
    print(r.url) 
        
    # print status code 
    print(r.status_code)

    # Parsing the HTML 
    soup = BeautifulSoup(r.content, 'html.parser') 

    s = soup.find('main', class_="site-main")
    s1 = s.find('div', class_='container')
    yep = s1.find('tbody')
    trade = yep.find('tr', class_='q-tr')

    # while trade != None: #this works just testing something
        
    #     trade = trade.find_next('tr', class_='q-tr')
    
    

    s1 = Scrape(trade)
    output = s1.getTrades()
    # print(ou /tput.__len__())

    for i in output:
        print(" ")
        print(i.getTicker() + " " + i.getType()+ " " + i.getDays())
        print(" ")


if __name__=='__main__':
    main()