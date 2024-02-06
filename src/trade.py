

class Trade:
    def __init__(self, poli,  ticker, datePlaced, daysFiled, tipo, quant):
        self.datePlaced = datePlaced
        self.ticker = ticker
        self.tipo = tipo
        self.daysFiled = daysFiled
        self.politician = poli
        self.quantity = quant
        

    def getTicker(self):
         return self.ticker
    
    def getTradeType(self):
        return self.tipo
    
    def getDaysSinceFiled(self):
        return self.daysFiled
    
    def getDayPlaced(self):
        return self.datePlaced
    
    def getPolitician(self):
        return self.politician
    
    def getQuantity(self):
        return self.quantity
