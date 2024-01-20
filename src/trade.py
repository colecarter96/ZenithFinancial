

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