
import requests 
from bs4 import BeautifulSoup 
from trade import Trade

class Scrape:
    def __init__(self):
        self.r = requests.get('https://www.capitoltrades.com/trades') 
        self.soup = BeautifulSoup(self.r.content, 'html.parser') 
        self.site = self.soup.find('main', class_="site-main")
        self.cont = self.site.find('div', class_='container')
        self.body = self.cont.find('tbody')
        self.trade = self.body.find('tr', class_='q-tr')
        
        # print("hi")

    def getTrades(self):
        txList = {}
        # print(self.trade)
        while self.trade != None:

            ticType = self.trade.find('span', class_='q-field issuer-ticker')
            

            txType = self.trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')
            
            if txType.find('span', class_="q-field tx-type tx-type--buy") != None:
                tipo = 'Buy'
            elif txType.find('span', class_="q-field tx-type tx-type--sell") != None:
                tipo = 'Sell'

            
            txDays = self.trade.find('span', class_='reporting-gap-tier--2')

                      
            datePlaced = self.trade.find('td', class_='q-td q-column--txDate')
            daysFiledSec = self.trade.find('td', class_='q-td q-column--reportingGap')

            daysFiled = daysFiledSec.find('span', class_='reporting-gap-tier--2')
            # print(daysFiled.get_text())
            txDate = datePlaced.find('div', class_='q-label')
            # print(txDate.get_text())

            txDayDate = datePlaced.find('div', class_='q-value')
            # print(txDayDate.get_text())

            t1 = Trade(str(ticType.get_text().split(':')[0]), tipo, txDays.get_text())
            # print(t1.getDays() + "this printing")
            # print(t1)

            txList[txDayDate.get_text() + daysFiled.get_text() + ticType.get_text().split(':')[0], tipo, txDays.get_text()] = t1

            # print(self.trade)

            self.trade = self.trade.find_next('tr', class_='q-tr')
            # print("yeah")
            # print(self.trade)
            # print("yeah")
        
        return txList



# going to rework this into a thing

# # Making a GET request 
# r = requests.get('https://www.capitoltrades.com/trades') 

# #resulting hashmap
# resultMap = {}
  
# # print request object 
# print(r.url) 
    
# # print status code 
# print(r.status_code)

# # Parsing the HTML 
# soup = BeautifulSoup(r.content, 'html.parser') 

# s = soup.find('main', class_="site-main")
# s1 = s.find('div', class_='container')
# yep = s1.find('tbody')
# trade = yep.find('tr', class_='q-tr')

# # while trade != None: --this works just testing something
# #     print(trade)
# #     print(" ")
# #     trade = trade.find_next('tr', class_='q-tr')


    
# txList = []
# while trade != None:
#     ticType = trade.find('span', class_='q-field issuer-ticker')
#     # print(ticType.get_text())

#     txType = trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')
#     # print(" ")
#     if txType.find('span', class_="q-field tx-type tx-type--buy") != None:
#         tipo = 'Buy'
#     elif txType.find('span', class_="q-field tx-type tx-type--sell") != None:
#         tipo = 'Sell'

#     # print(' ')
#     txDays = trade.find('span', class_='reporting-gap-tier--2')
#     # print(txDays.get_text())
#     # trades[counter] = trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')
#     # print(" ")
#     # print(' ')

#     t1 = Trade(ticType.get_text(), tipo, txDays.get_text())

#     txList.append(t1)

#     trade = trade.find_next('tr', class_='q-tr')
    



# for i in txList:
#     print(" ")
#     print(i.getTicker() + " " + i.getType()+ " " + i.getDays())
#     print(" ")

