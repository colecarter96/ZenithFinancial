
import requests 
from bs4 import BeautifulSoup 

class Trade:
    def __init__(self, ticker, tipo, days):
        self.ticker = ticker
        self.tipo = tipo
        self.days = days

    def getTicker(self):
         return self.ticker
    def getType(self):
        return self.tipo
    def getDays(self):
        return self.days

  
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

# while trade != None: --this works just testing something
#     print(trade)
#     print(" ")
#     trade = trade.find_next('tr', class_='q-tr')


    
txList = []
while trade != None:
    ticType = trade.find('span', class_='q-field issuer-ticker')
    # print(ticType.get_text())

    txType = trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')
    # print(" ")
    if txType.find('span', class_="q-field tx-type tx-type--buy") != None:
        tipo = 'Buy'
    elif txType.find('span', class_="q-field tx-type tx-type--sell") != None:
        tipo = 'Sell'

    # print(' ')
    txDays = trade.find('span', class_='reporting-gap-tier--2')
    # print(txDays.get_text())
    # trades[counter] = trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')
    # print(" ")
    # print(' ')

    t1 = Trade(ticType.get_text(), tipo, txDays.get_text())

    txList.append(t1)

    trade = trade.find_next('tr', class_='q-tr')
    



for i in txList:
    print(" ")
    print(i.getTicker() + " " + i.getType()+ " " + i.getDays())
    print(" ")

