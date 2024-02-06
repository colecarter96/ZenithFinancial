
import requests 
from bs4 import BeautifulSoup 
from trade import Trade
import json

class Scrape:
    def __init__(self):
        # self.r = requests.get('https://www.capitoltrades.com/trades') 
        self.r = requests.get('https://www.capitoltrades.com/trades?per_page=96')
        self.soup = BeautifulSoup(self.r.content, 'html.parser') 
        self.site = self.soup.find('main', class_="site-main")
        self.cont = self.site.find('div', class_='container')
        self.body = self.cont.find('tbody')
        self.trade = self.body.find('tr', class_='q-tr')

        self.lastTrade = ""
        self.politicians = {}
        self.txList = {}
        
        self.possNewList = {}

        
        
    def updateTxList(self, list):
        for t1 in list:
            if list[t1].getPolitician() not in self.politicians:
                self.politicians[list[t1].getPolitician()] = {}
            # key = i.getPolitician() + i.getTicker() + i.getDayPlaced() + i.getDaysSinceFiled() + i.getTradeType()
                
            if list[t1].getTicker() not in self.politicians[list[t1].getPolitician()]:
                self.politicians[list[t1].getPolitician()][list[t1].getTicker()] = list[t1].getQuantity()
            else:
                self.politicians[list[t1].getPolitician()][list[t1].getTicker()] += list[t1].getQuantity()

            # if self.politicians[list[t1].getPolitician()][list[t1].getTicker()] == None:
            #     self.politicians[list[t1].getPolitician()][list[t1].getTicker()] = list[t1].getQuantity()
            # else:
            #     self.politicians[list[t1].getPolitician()][list[t1].getTicker()] += list[t1].getQuantity()
        # self.txList |= list

    def calculateQuantity(self, quant):
        if quant == "1K–15K":
            return 1
        elif quant == "15K–50K":
            return 2
        elif quant == "50K–100K":
            return 3
        elif quant == "100K–250K":
            return 4
        elif quant == "250K–500K":
            return 5
        elif quant == "500K–1M":
            return 6
        else:
            return 0;

    def updateConnection (self):
        self.r = requests.get('https://www.capitoltrades.com/trades?per_page=96') 
        self.soup = BeautifulSoup(self.r.content, 'html.parser') 
        self.site = self.soup.find('main', class_="site-main")
        self.cont = self.site.find('div', class_='container')
        self.body = self.cont.find('tbody')

    def getNecessaryValues(self, trade):

        invalidTrade = False
        tradeObj = None

        # Get the name of the politician

        politician = trade.find('h3', class_='q-fieldset politician-name')


        # Get the ticker name

        ticker = trade.find('span', class_='q-field issuer-ticker')
            
        if(ticker.getText() == "N/A"):
                # trade = trade.find_next('tr', class_='q-tr')
                invalidTrade = True
                return (invalidTrade, tradeObj)
        
        
        # Get the day traded, ie the date that the politician placed the trade

        datePlaced = trade.find('td', class_='q-td q-column--txDate')
        datePlaced = datePlaced.find('div', class_='q-value')


        # Get the days filed after

        daysFiledSec = trade.find('td', class_='q-td q-column--reportingGap')

        daysFiled = daysFiledSec.find('span', class_='reporting-gap-tier--1')

        if daysFiled == None:
            daysFiled = daysFiledSec.find('span', class_='reporting-gap-tier--2')


        # Get the Trade Type, buying or Selling
        
        txType = trade.find('td', class_='q-td q-column--txType').find('div', class_='q-cell cell--tx-type')

        buyOrSell = ""

        print(txType.get_text())
            
        if txType.get_text().__contains__('buy'):
            buyOrSell = 'Buy'

        elif txType.get_text().__contains__('sell'):
            buyOrSell = 'Sell'

        
            

        # Get the quantity 
            
        amount = trade.find('td', class_='q-td q-column--value')
        amount = amount.find('span', class_='q-label')

        tradeAmount = self.calculateQuantity(amount.get_text())

        #  key = t1.getPolitician() + t1.getTicker() + t1.getDayPlaced() + t1.getDaysSinceFiled() + t1.getTradeType()

        if buyOrSell == 'Sell':
            # key = politician.get_text() + str(ticker.get_text().split(':')[0]) + datePlaced.get_text() + daysFiled.get_text() + buyOrSell
            if politician.get_text() not in self.politicians:
                self.politicians[politician.get_text()] = {}
                tradeAmount = 0
            elif str(ticker.get_text().split(':')[0]) not in self.politicians[politician.get_text()]:
                tradeAmount = 0
            elif self.politicians[politician.get_text()][str(ticker.get_text().split(':')[0])] > tradeAmount:
                self.politicians[politician.get_text()][str(ticker.get_text().split(':')[0])] -= tradeAmount
            elif self.politicians[politician.get_text()][str(ticker.get_text().split(':')[0])] <= tradeAmount:
                tradeAmount = self.politicians[politician.get_text()][str(ticker.get_text().split(':')[0])]
                self.politicians[politician.get_text()][str(ticker.get_text().split(':')[0])] = 0

        if tradeAmount == 0:
            invalidTrade = True
            return (invalidTrade, tradeObj)
                

        print(amount.get_text() + ": this is the quantity, this is the amount in shares: " + str(tradeAmount))
        # if txType.find('span', class_="q-field tx-type tx-type--buy") != None:
        #     buyOrSell = 'Buy'
        # elif txType.find('span', class_="q-field tx-type tx-type--sell") != None:
        #     buyOrSell = 'Sell'

        t1 = Trade(politician.get_text(), str(ticker.get_text().split(':')[0]), datePlaced.get_text(), daysFiled.get_text(), buyOrSell, tradeAmount)

        return (invalidTrade, t1)   



    def initalGetTrades(self):
        self.key = ""
        self.txList = {}
        counter = 0
        # print(self.trade)
        while self.trade != None:
            print(str(counter) + ", This is the current count.")
            tup = self.getNecessaryValues(self.trade)

            invalidTrade = tup[0]

            if invalidTrade:
                self.trade = self.trade.find_next('tr', class_='q-tr')
                # self.trade = self.body.find_next('tr', class_='q-tr')
                continue

            t1 = tup[1]

            key = t1.getPolitician() + t1.getTicker() + t1.getDayPlaced() + t1.getDaysSinceFiled() + t1.getTradeType()

            # key = txDayDate.get_text() + daysFiled.get_text() + ticker.get_text().split(':')[0] + buyOrSell + txDays.get_text() + politician
            
            # key = politician.get_text() + str(ticker.get_text().split(':')[0]) + txDayDate.get_text() + txDays.get_text() + buyOrSell

            

            # if self.politicians[t1.getPolitician()][t1.getTicker()] == None:
            #     self.politicians[t1.getPolitician()][t1.getTicker()] = t1
            # elif self.politicians[t1.getPolitician()][t1.getTicker()] != None:
            #     self.politicians[t1.getPolitician()][t1.getTicker()] = t1
            self.trade = self.trade.find_next('tr', class_='q-tr')
            # self.trade = self.body.find_next('tr', class_='q-tr')

            # print(self.trade)
            # print("             ")

            # if t1.getTradeType() == 'Buy':
            self.txList[key] = t1
            counter += 1
            
        
            # print("yeah")
            # print(self.trade)
            # print("yeah")
        
        self.lastTrade = key
        
        return self.txList
    
    def updateGetTrades(self):
        self.possNewList = {}
        self.trade = self.body.find('tr', class_='q-tr')
        foundNew = False;
        counter = 0
        tempLastNew = ""
        while self.trade != None:

            tup = self.getNecessaryValues(self.trade)

            invalidTrade = tup[0]

            if invalidTrade:
                self.trade = self.trade.find_next('tr', class_='q-tr')
                # self.trade = self.body.find_next('tr', class_='q-tr')
                continue

            t1 = tup[1]

            key = t1.getPolitician() + t1.getTicker() + t1.getDayPlaced() + t1.getDaysSinceFiled() + t1.getTradeType()

            if key == self.lastTrade:
                break
            
            if key != self.lastTrade:
                foundNew = True
                if counter == 0 & foundNew:
                    tempLastNew = key
                # self.possNewList[key] = t1
                
                print("found new trade")

            # key = txDayDate.get_text() + daysFiled.get_text() + ticker.get_text().split(':')[0] + buyOrSell + txDays.get_text() + politician
            
            # key = politician.get_text() + str(ticker.get_text().split(':')[0]) + txDayDate.get_text() + txDays.get_text() + buyOrSell

            print(key)

            if self.politicians[t1.getPolitician()][t1.getTicker()] == None:

                self.possNewList[key] = t1
                
            #     print("found new trade")
            
            

            # if self.txList[key] == None:
            #     self.possNewList[key] = t1
            #     print("found new trade")
           
            # if self.txList.get(key) == None:
            #     self.possNewList[key] = t1
            #     print("found new trade")
            

            # print(self.trade)
            counter += 1
            
            self.trade = self.trade.find_next('tr', class_='q-tr')
            # self.trade = self.body.find_next('tr', class_='q-tr')
            # print("yeah")
            # print(self.trade)
            # print("yeah")
        
        self.lastNew = tempLastNew

        return self.possNewList
    


    
        

