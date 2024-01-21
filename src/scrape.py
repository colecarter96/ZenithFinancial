
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
        self.txList = {}
        self.possNewList = {}
        
    def updateTxList(self, list):
        self.txList |= list

    def updateConnection (self):
        self.r = requests.get('https://www.capitoltrades.com/trades') 
        self.soup = BeautifulSoup(self.r.content, 'html.parser') 
        self.site = self.soup.find('main', class_="site-main")
        self.cont = self.site.find('div', class_='container')
        self.body = self.cont.find('tbody')
        

    def initalGetTrades(self):
        self.txList = {}
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
            
            self.txList[txDayDate.get_text() + daysFiled.get_text() + ticType.get_text().split(':')[0], tipo, txDays.get_text()] = t1

            # print(self.trade)

            self.trade = self.trade.find_next('tr', class_='q-tr')
            # print("yeah")
            # print(self.trade)
            # print("yeah")
        
        return self.txList
    
    def updateGetTrades(self):
        self.possNewList = {}
        self.trade = self.body.find('tr', class_='q-tr')
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
            # txDate = datePlaced.find('div', class_='q-label')
            # print(txDate.get_text())

            txDayDate = datePlaced.find('div', class_='q-value')
            # print(txDayDate.get_text())

            t1 = Trade(str(ticType.get_text().split(':')[0]), tipo, txDays.get_text())
            # print(t1.getDays() + "this printing")
            # print(t1)

            key = txDayDate.get_text() + daysFiled.get_text() + ticType.get_text().split(':')[0], tipo, txDays.get_text()
            
            if self.txList.get(key) == None:
                self.possNewList[key] = t1
                print("found new trade")
            

            # print(self.trade)

            self.trade = self.trade.find_next('tr', class_='q-tr')
            # print("yeah")
            # print(self.trade)
            # print("yeah")
        
        return self.possNewList

